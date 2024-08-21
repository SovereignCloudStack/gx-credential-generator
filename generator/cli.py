#!/usr/bin/env python3

"""Script to validate self-description in JSON-LD format
   against its schema is turtle format.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
(c) Roman Hros <roman.hros@dnation.cloud>, 5/2023
(c) Matej Feder <matej.feder@dnation.cloud>, 5/2023
(c) Anja Strunk <anja.sturnk@cloudandheat.com>, 1/2024
SPDX-License-Identifier: EPL-2.0
"""

import json
import os
import sys
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
from generator.discovery.gxdch_services import ComplianceService
from generator.discovery.openstack.openstack_discovery import \
    OpenstackDiscovery

SHAPES_FILE_FORMAT = "turtle"
DATA_FILE_FORMAT = "json-ld"

VC_NAME_LOOKUP = {
    "lp": "Legal Person",
    "lrn": "Legal Registration Number",
    "tandc": "Gaia-X Terms and Conditions",
    "cs": "GXDCH Compliance Service",
    "so": "Service Offering",
    "vmso": "Virtual Machine Service Offering",
}


@click.group()
def cli_commands():
    pass


@click.command()
@click.option(
    "--out-dir",
    help="Path to output directory.",
)
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.",
)
@click.option("--timeout", default=24, help="Timeout for API calls in seconds")
@click.argument("cloud")
def openstack(cloud, timeout, config, out_dir):
    """Generates Gaia-X Credentials for CSP And OpenStack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""
    with open(config, "r") as config_file:
        conf = Config(yaml.safe_load(config_file))

    # create Gaia-X Credentials for CSP
    csp_gen = CspGenerator(conf=conf)
    csp_vcs = csp_gen.generate(auto_sign=True)

    # create Gaia-X Credentials for OpenStack
    so_vcs = create_vmso_vcs(
        conf=conf,
        cloud=cloud,
        csp_vcs=csp_vcs,
        timeout=timeout,
    )

    vcs = {**csp_vcs, **so_vcs}
    _print_vcs(vcs, out_dir)


@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for CPS and kubernetes."""
    pass


# def load_file(filepath, file_format=DATA_FILE_FORMAT):
#    """Load file in a given format"""
#    graph = rdflib.Graph()
#    graph.parse(filepath, format=file_format)
#    return graph

@click.command()
@click.option(
    "--out-dir",
    help="Path to output directory.",
)
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.")
def csp(config, out_dir):
    """Generate Gaia-X Credential for CPS."""
    # load config file
    with open(config, "r") as config_file:
        config = Config(yaml.safe_load(config_file))

    vcs = CspGenerator(config).generate()
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
        print("INFO: Retry connection with 'default' domain", file=sys.stderr)
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
    print('Create VC of type "gx:VirtualMachineServiceOffering"...', end='')
    vm_offering = discovery.discover()
    vmso_vc = {
        '@context': [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT],
        'type': "VerifiableCredential",
        'id': cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/vmo.json",
        'issuer': csp['did'],
        'issuanceDate': str(datetime.now(tz=timezone.utc).isoformat()),
        'credentialSubject': json.loads(json.dumps(vm_offering, default=json_ld.to_json_ld)),
    }
    vmso_vc_signed = crypto.sign_cred(cred=vmso_vc,
                                      key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                                      verification_method=cred_settings[const.CONFIG_CRED_VER_METH])
    print('ok')

    # build Gaia-X Credential for Service Offering
    print('Create VC of type "gx:ServiceOffering"...', end='')
    so_vc = {
        '@context': [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT],
        'type': "VerifiableCredential",
        'id': cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so.json",
        'issuer': csp['did'],
        'issuanceDate': str(datetime.now(tz=timezone.utc).isoformat()),
        'credentialSubject': {
            "type": "gx:ServiceOffering",
            "id": cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so_cs.json",  # iaas['did'],
            "gx:providedBy": {
                'id': csp_vcs['lp']['credentialSubject']['id']
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
    print('ok')

    # Request Gaia-X Compliance Credential for Service Offering
    print('Request VC of type "gx:compliance" for Service Offering at GXDCH Compliance Service...', end='')
    vp = credentials.convert_to_vp(creds=[csp_vcs['tandc'], csp_vcs['lrn'], csp_vcs['lp'], so_vc_signed])
    comp_vc = compliance.request_compliance_vc(vp,
                                               cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so_compliance.json")

    print('ok')
    return {'so': so_vc, 'cs': json.loads(comp_vc), 'vmso': vmso_vc_signed, 'vp_so': vp}


def _get_timestamp():
    dt = datetime.now()  # for date and time
    # ts_1 = datetime.timestamp(dt)  # for timestamp
    return dt.strftime('%Y-%m-%d_%H-%M-%S')


def _print_vcs(vcs: dict, out_dir: str):
    if not out_dir:
        out_dir = os.getcwd()

    if not os.path.isdir(out_dir):
        raise NotADirectoryError(out_dir + " is not a directory or does not exit!")

    ts = _get_timestamp()
    for key in vcs:
        vc_path = os.path.join(out_dir, key + "_" + ts + ".json")
        with open(vc_path, "w") as vc_file:
            if key == 'vp_csp':
                print(
                    "Write Verifiable Presentation of Cloud Service Provider to be verified at GXDCH Compliance Service to " + str(
                        vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))
            elif key == 'vp_so':
                print(
                    "Write Verifiable Presentation of Service Offering to be verified at GXDCH Compliance Service to " + str(
                        vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))
            else:
                print("Write Gaia-X Credential for " + VC_NAME_LOOKUP[key] + " to " + str(vc_path))
                vc_file.write(json.dumps(vcs[key], indent=2))


cli_commands.add_command(openstack)
cli_commands.add_command(kubernetes)
cli_commands.add_command(csp)

if __name__ == "__main__":
    cli_commands()
