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
import sys
from datetime import datetime, timezone
from typing import List

import click
import openstack as os
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


@click.group()
def cli_commands():
    pass


@click.command()
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.",
)
@click.option("--timeout", default=12, help="Timeout for API calls in seconds")
@click.argument("cloud")
def openstack(cloud, timeout, config):
    """Generates Gaia-X Credentials for CSP And OpenStack cloud CLOUD.
    CLOUD MUST refer to a name defined in Openstack's configuration file clouds.yaml."""
    with open(config, "r") as config_file:
        conf = Config(yaml.safe_load(config_file))

        # create Gaia-X Credentials for CSP
        csp_gen = CspGenerator(conf=conf)
        csp_vcs = csp_gen.generate(auto_sign=True)
        for vc in csp_vcs:
            print(json.dumps(vc, indent=2))

        # create Gaia-X Credentials for OopenStack
        for vc in create_vmso_vcs(
                conf=conf,
                cloud=cloud,
                csp_vcs=csp_vcs,
                timeout=timeout):
            print(json.dumps(vc, indent=2))


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
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.")
def csp(config):
    """Generate Gaia-X Credential for CPS."""
    # load config file
    with open(config, "r") as config_file:
        config = Config(yaml.safe_load(config_file))

        vcs = CspGenerator(config).generate()
        if vcs is not None:
            for vc in vcs.values():
                print(json.dumps(vc, indent=4))


def init_openstack_connection(cloud: str, timeout: int = 12) -> Connection:
    """
    Init connection to OpenStack cloud.
    @param cloud: name of OpenStack cloud to be connected.
    @param timeout: time, after connection is initiated a second time.
    @return: OpenStacl connection.
    """
    try:
        conn = os.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
        conn.authorize()
    except Exception:
        print("INFO: Retry connection with 'default' domain", file=sys.stderr)
        conn = os.connect(
            cloud=cloud,
            timeout=timeout,
            api_timeout=timeout * 1.5 + 4,
            default_domain="default",
            project_domain_id="default",
        )
        conn.authorize()
    return conn


def create_vmso_vcs(conf: Config, cloud: str, csp_vcs: List[dict], timeout: int = 12) -> List[dict]:
    """
    Create Gaia-X Credentials  for Virtual Machine Service Offering. This means
      - Gaia-X Credential of OpenStack Cloud as ServiceOffering with mandatory attributes
      - Gaia-X Credential of OpenStack Cloud as VirtualMachineServiceOffering
      - Gaia-X Credential of GXDCH Compliance Service, attesting complaince of OpenStack cloud description with Gaia-X rules.
    @param conf: configuration settings for creation process.
    @param cloud: OpenStack ncloud name.
    @param csp_vc: Gaia-X Credentials of Cloud Service Provider.
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
    vm_offering = discovery.discover()
    vmso_vc = dict()
    vmso_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
    vmso_vc['type'] = "VerifiableCredential"
    vmso_vc['id'] = cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/vmo.json"
    vmso_vc['issuer'] = csp['did']
    vmso_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
    vmso_vc['credentialSubject'] = json.loads(json.dumps(vm_offering, default=json_ld.to_json_ld))
    vmso_vc_signed = crypto.sign_cred(cred=vmso_vc,
                                      key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                                      verification_method=cred_settings[const.CONFIG_CRED_VER_METH])

    # build Gaia-X Credential for Service Offering
    so_vc = dict()
    so_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
    so_vc['type'] = "VerifiableCredential"
    so_vc['id'] = cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so.json"
    so_vc['issuer'] = csp['did']
    so_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
    so_vc['credentialSubject'] = {
        "type": "gx:ServiceOffering",
        "id": cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so_cs.json",  # iaas['did'],
        "gx:providedBy": {
            'id': csp_vcs['lp']['credentialSubject']['id']
        },
        "gx:termsAndConditions": list(),
        "gx:policy": vm_offering.servicePolicy,
        "gx:dataAccountExport": {
            "gx:requestType": vm_offering.dataAccountExport.requestType.code.text,
            "gx:accessType": vm_offering.dataAccountExport.accessType.code.text,
            "gx:formatType": "application/" + vm_offering.dataAccountExport.formatType.code.text
        }
    }

    for s_tac in vm_offering.serviceOfferingTermsAndConditions:
        so_vc['credentialSubject']["gx:termsAndConditions"].append({
            'gx:URL': s_tac.url,
            'gx:hash': s_tac.hash})

    # sign service offering credential
    so_vc_signed = crypto.sign_cred(cred=so_vc,
                                    key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                                    verification_method=cred_settings[const.CONFIG_CRED_VER_METH])

    # Request Gaia-X Compliance Credential for Service Offering
    vp = credentials.convert_to_vp(creds=[csp_vcs['tandc'], csp_vcs['lrn'], csp_vcs['lp'], so_vc_signed])
    comp_vc = compliance.request_compliance_vc(vp,
                                               cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/so_compliance.json")

    return [so_vc, json.loads(comp_vc), vmso_vc_signed]


cli_commands.add_command(openstack)
cli_commands.add_command(kubernetes)
cli_commands.add_command(csp)

if __name__ == "__main__":
    cli_commands()
