#!/usr/bin/env python3

"""Script to validate self-description in JSON-LD format
   against its schema is turtle format.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
(c) Roman Hros <roman.hros@dnation.cloud>, 5/2023
(c) Matej Feder <matej.feder@dnation.cloud>, 5/2023
(c) Anja Strunk <anja.sturnk@cloudandheat.com>, 1/2024
SPDX-License-Identifier: EPL-2.0
"""

import functools
import json
import logging
import os
from datetime import datetime, timezone
from typing import List

import click
import openstack as o_stack
import yaml
from openstack.connection import Connection

import generator.common.const as const
import generator.common.json_ld as json_ld
from generator.common import credentials, crypto
from generator.common.config import Config
from generator.discovery.csp_generator import CspGenerator
from generator.discovery.gxdch_services import (ComplianceService,
                                                RegistryService)
from generator.discovery.openstack.openstack_discovery import \
    OpenstackDiscovery

SHAPES_FILE_FORMAT = "turtle"
DATA_FILE_FORMAT = "json-ld"

VC_NAME_LOOKUP = {
    "legal_person": "Legal Person",
    "lrn": "Legal Registration Number",
    "tandc": "Gaia-X Terms and Conditions",
    "csp_compliance": "GXDCH Compliance Service",
    "so_compliance": "GXDCH Compliance Service",
    "so": "Service Offering",
    "vmso": "Virtual Machine Service Offering",
}


def add_logging_options(func):
    """Python Click decorator to include common logging options

    Offers an alternative to adding logging options directly to a
    @click.group() in order to circumvent group option limitations that
    would require any such options to be specified before the command name
    by the user on the command line.

    Any @click.command() function can be decorated with this decorator to
    include logging initialization based on common logging options that
    can be specified alongside with the respective command's individual
    options, e.g.,

        mycommand --log-file local.log --debug --option1 --option2
    """
    @click.option(
        "--log-file",
        default="-",
        help="Specify path to log file. If not specified, log messages will be printed to stdout"
    )
    @click.option(
        "--debug/--no-debug",
        default=False,
        help="Enable debug log level"
    )
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # consume the common logging options from kwargs directly
        # (so that they are not passed to the wrapped function down below)
        debug = kwargs.pop("debug")
        log_file = kwargs.pop("log_file")
        # initialize logging
        log_file = None if log_file == "-" else log_file
        logging.basicConfig(
            format="%(levelname)s: %(message)s",
            level=logging.DEBUG if debug else logging.INFO,
            filename=log_file
        )
        # call wrapped function
        return func(*args, **kwargs)
    return wrapper


@click.group()
def cli_commands():
    pass


@cli_commands.command()
@add_logging_options
@click.option(
    "--auto-sign/--no-auto-sign",
    default=False,
    help="Sign Gaia-X Terms and Conditions, automatically, without asking for permission on screen.",
)
@click.option(
    "--out-dir",
    default=".",
    help="Path to output directory.",
)
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.",
)
@click.option("--timeout", default=24, help="Timeout for API calls in seconds")
@click.argument("cloud")
def openstack(cloud, timeout, config, out_dir, auto_sign):
    """Generates Gaia-X Credentials for CSP And OpenStack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""
    with open(config, "r") as config_file:
        conf = Config(yaml.safe_load(config_file))

    if not auto_sign and not _are_gaiax_tandc_signed(conf):
        # user did not agree Gaia-X terms and conditions, we have to abort here
        logging.error(
            "Gaia-X Terms and Conditions were not signed - process aborted!"
        )
        return
    elif auto_sign:
        logging.info(
            "Gaia-X Terms and Conditions accepted non-interactively via "
            "auto-sign option"
        )

    # create Gaia-X Credentials for CSP
    csp_gen = CspGenerator(conf=conf)
    csp_vcs = csp_gen.generate()

    # create Gaia-X Credentials for OpenStack
    so_vcs = create_vmso_vcs(
        conf=conf,
        cloud=cloud,
        csp_vcs=csp_vcs,
        timeout=timeout,
    )

    vcs = {**csp_vcs, **so_vcs}
    _print_vcs(vcs, out_dir)


@cli_commands.command()
@add_logging_options
def kubernetes():
    """Generates Gaia-X Credentials for CSP and Kubernetes."""
    pass


# def load_file(filepath, file_format=DATA_FILE_FORMAT):
#    """Load file in a given format"""
#    graph = rdflib.Graph()
#    graph.parse(filepath, format=file_format)
#    return graph

@cli_commands.command()
@add_logging_options
@click.option(
    "--auto-sign/--no-auto-sign",
    default=False,
    help="Sign Gaia-X Terms and Conditions, automatically, without asking for permission on screen.",
)
@click.option(
    "--out-dir",
    default=".",
    help="Path to output directory.",
)
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.")
def csp(config, out_dir, auto_sign):
    """Generate Gaia-X Credential for CSP."""
    # load config file
    with open(config, "r") as config_file:
        conf = Config(yaml.safe_load(config_file))

    if not auto_sign and not _are_gaiax_tandc_signed(conf):
        # user did not agree Gaia-X terms and conditions, we have to abort here
        logging.error(
            "Gaia-X Terms and Conditions were not signed - process aborted!"
        )
        return
    elif auto_sign:
        logging.info(
            "Gaia-X Terms and Conditions accepted non-interactively via "
            "auto-sign option"
        )
    vcs = CspGenerator(conf).generate()
    _print_vcs(vcs, out_dir)


def init_openstack_connection(cloud: str, timeout: int = 12) -> Connection:
    """
    Init connection to OpenStack cloud.
    @param cloud: name of OpenStack cloud to be connected.
    @param timeout: time, after connection is initiated a second time.
    @return: OpenStacl connection.
    """
    try:
        conn = o_stack.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
        conn.authorize()
    except Exception:
        logging.error("Retry connection with 'default' domain")
        conn = o_stack.connect(
            cloud=cloud,
            timeout=timeout,
            api_timeout=timeout * 1.5 + 4,
            default_domain="default",
            project_domain_id="default",
        )
        conn.authorize()
    return conn


def create_vmso_vcs(conf: Config, cloud: str, csp_vcs: List[dict], timeout: int = 12) -> dict[dict]:
    """
    Create Gaia-X Credentials  for Virtual Machine Service Offering. This means
      - Gaia-X Credential of OpenStack Cloud as ServiceOffering with mandatory attributes
      - Gaia-X Credential of OpenStack Cloud as VirtualMachineServiceOffering
      - Gaia-X Credential of GXDCH Compliance Service, attesting complaince of OpenStack cloud description with Gaia-X rules.
    @param conf: configuration settings for creation process.
    @param cloud: OpenStack ncloud name.
    @param csp_vcs: Gaia-X Credentials of Cloud Service Provider.
    @param timeout: timeout for connection to OpenStack cloud. If timeout expires, connection is initialed a second time.
    @return: A list of Gaia-X Credentials describing given OpenStack cloud.
    """

    csp = conf.get_value([const.CONFIG_CSP])
    # iaas = conf.get_value([const.CONFIG_IAAS]) not yet used, as Gaia-X "abuses" id attribute of Verifiable Credentials
    cred_settings = conf.get_value([const.CONFIG_CRED])

    # init services
    conn = init_openstack_connection(cloud=cloud, timeout=timeout)
    compliance = ComplianceService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_COMP]))
    discovery = OpenstackDiscovery(conn=conn, config=conf)

    # run openstack discovery and build Gaia-X Credential for Virtual Machine Service Offering
    logging.info('Create VC of type "gx:VirtualMachineServiceOffering"...')
    vm_offering = discovery.discover()
    vmso_vc = {
        '@context': [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT],
        'type': "VerifiableCredential",
        'id': cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/vmso.json",
        'issuer': csp['did'],
        'issuanceDate': str(datetime.now(tz=timezone.utc).isoformat()),
        'credentialSubject': json.loads(json.dumps(vm_offering, default=json_ld.to_json_ld)),
    }
    vmso_vc_signed = crypto.sign_cred(cred=vmso_vc,
                                      key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                                      verification_method=cred_settings[const.CONFIG_CRED_VER_METH])
    logging.info('ok')

    # build Gaia-X Credential for Service Offering
    logging.info('Create VC of type "gx:ServiceOffering"...')
    so_vc = {
        '@context': [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT],
        'type': "VerifiableCredential",
        'id': cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so.json",
        'issuer': csp['did'],
        'issuanceDate': str(datetime.now(tz=timezone.utc).isoformat()),
        'credentialSubject': {
            "type": "gx:ServiceOffering",
            "id": cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so.json#subject",  # iaas['did'],
            "gx:providedBy": {
                'id': csp_vcs['legal_person']['credentialSubject']['id']
            },
            "gx:termsAndConditions": [
                {'gx:URL': s_tac.url, 'gx:hash': s_tac.hash}
                for s_tac in vm_offering.serviceOfferingTermsAndConditions],
            "gx:policy": vm_offering.servicePolicy,
            "gx:dataAccountExport": {
                "gx:requestType": vm_offering.dataAccountExport.requestType.code.text,
                "gx:accessType": vm_offering.dataAccountExport.accessType.code.text,
                "gx:formatType": "application/" + vm_offering.dataAccountExport.formatType.code.text
            }
        }
    }

    # sign service offering credential
    so_vc_signed = crypto.sign_cred(cred=so_vc,
                                    key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                                    verification_method=cred_settings[const.CONFIG_CRED_VER_METH])
    logging.info('ok')

    # Request Gaia-X Compliance Credential for Service Offering
    logging.info('Request VC of type "gx:compliance" for Service Offering at GXDCH Compliance Service...')
    vp = credentials.convert_to_vp(creds=[csp_vcs['tandc'], csp_vcs['lrn'], csp_vcs['legal_person'], so_vc_signed])
    comp_vc = compliance.request_compliance_vc(vp,
                                               cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so_compliance.json")

    logging.info('ok')
    return {'so': so_vc, 'so_compliance': json.loads(comp_vc), 'vmso': vmso_vc_signed, 'vp_so': vp}


def _get_timestamp():
    dt = datetime.now()  # for date and time
    # ts_1 = datetime.timestamp(dt)  # for timestamp
    return dt.strftime('%Y-%m-%d_%H-%M-%S')


def _print_vcs(vcs: dict, out_dir: str = "."):
    if not os.path.isdir(out_dir):
        raise NotADirectoryError(out_dir + " is not a directory or does not exit!")

    ts = _get_timestamp()
    for key in vcs:
        vc_path = os.path.join(out_dir, key + "_" + ts + ".json")
        with open(vc_path, "w") as vc_file:
            if key == 'vp_csp':
                logging.info(
                    "Writing Verifiable Presentation of Cloud Service Provider to be verified at GXDCH Compliance Service to " + str(
                        vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))
            elif key == 'vp_so':
                logging.info(
                    "Writing Verifiable Presentation of Service Offering to be verified at GXDCH Compliance Service to " + str(
                        vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))
            else:
                logging.info("Writing Gaia-X Credential for " + VC_NAME_LOOKUP[key] + " to " + str(vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))


def _are_gaiax_tandc_signed(conf: Config) -> bool:
    reg = RegistryService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_REG]))
    tand = reg.get_gx_tandc()

    print("Do you agree Gaia-X Terms and Conditions version " + tand['version'] + "?")
    print()
    print("-------------------------- Gaia-X Terms and Conditions --------------------------------------------")
    print(tand['text'])
    print("-------------------------- ------------------------------------------------------------------------")
    print()
    print("Please type 'y' for 'I do agree' and 'n' for 'I do not agree': ")

    resp = input()
    while resp.lower() not in ['y', 'n']:
        print("Please type 'y' for 'I do agree' and 'n' for 'I do not agree: '")
        resp = input()

    if resp.lower() == 'y':
        logging.info(
            "Gaia-X Terms and Conditions accepted via interactive input"
        )
        return True
    logging.info(
        "Gaia-X Terms and Conditions declined via interactive input"
    )
    return False


if __name__ == "__main__":
    cli_commands()
