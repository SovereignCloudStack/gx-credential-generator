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

import click
import openstack as os
import yaml

import generator.common.const as const
import generator.common.json_ld as json_ld
from generator.common.config import Config
from generator.discovery.openstack.openstack_discovery import \
    OpenstackDiscovery
from generator.discovery.vc_discovery import CredentialDiscovery
from generator.discovery.gxdch_services import NotaryService, ComplianceService
from generator.discovery.csp_generator import CspGenerator

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

    # init Openstack Connections
    conn = os.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
    try:
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

    # generate Gaia-X Credentials
    with open(config, "r") as config_file:
        # init everything
        config = Config(yaml.safe_load(config_file))
        os_cloud = OpenstackDiscovery(conn, config)
        vc_discovery = CredentialDiscovery()
        csp = config.get_value([const.CONFIG_CSP])
        cred_settings = config.get_value([const.CONFIG_CRED])

        # create mandatory Gaia-X Credentials
        cred_settings['cred_id'] = cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/tandc.json"
        tandc_vc = vc_discovery.create_gaia_x_terms_and_conditions_vc(
            csp=csp,
            cred_settings=cred_settings,
            cred_id=cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/tandc.json")
        #print(json.dumps(tandc_vc, indent=4))
        lrn_vc = vc_discovery.request_vat_id_vc(
            csp=csp,
            cred_id=config.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/lrn.json")
        print("=============== LRN ==================")
        print(json.dumps(lrn_vc, indent=4))
        lp_vc = vc_discovery.create_and_sign_legal_person_vc(
            cred_settings=cred_settings,
            csp=csp,
            cred_id=cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/legal_person.json",
            lrn_cred_id=config.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/lrn.json")
        print("=============== LP ==================")
        print(json.dumps(lp_vc, indent=4))
        vp_id = config.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/compliance.json"
        vp = vc_discovery.create_verifiable_presentation(vcs=[lrn_vc, tandc_vc, lp_vc], cred_settings=cred_settings)
        print("=============== VP ==================")
        print(vp)
        import requests
        response = requests.post(
            "https://compliance.lab.gaia-x.eu/v1-staging/api/credential-offers?vcid=http://bakeup.io/compliance.json",
            vp)
        print("=============== Compliance ==================")
        print(json.dumps(json.loads(response.text), indent=4))
        #comp_vc = vc_discovery.request_compliance_vc(vp=vp, vp_id=vp_id)

        # run discovery
        vm_offering = os_cloud.discover()

        # print results
        #props = json_ld.get_json_ld_context()
        #props["@graph"] = [lrn_vc, tandc_vc, lp_vc, comp_vc, vm_offering]
        #print(json.dumps(props, indent=4, default=json_ld.to_json_ld))


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
    """Generates Gaia-X Credential for CPS"""

    # load config file
    with open(config, "r") as config_file:
        config = Config(yaml.safe_load(config_file))
        csp_gen = CspGenerator(config)
        csp_gen.generate()

cli_commands.add_command(openstack)
cli_commands.add_command(kubernetes)
cli_commands.add_command(csp)


if __name__ == "__main__":
    cli_commands()
