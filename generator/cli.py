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

import generator.common.json_ld as json_ld
from generator.common.config import Config
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
    """Generates Gaia-X Credentials for openstack cloud CLOUD.
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
        config_dict = yaml.safe_load(config_file)
        os_cloud = OpenstackDiscovery(conn, Config(config_dict))

        # run discovery
        creds = os_cloud.discover()

        props = json_ld.get_json_ld_context()
        props["@graph"] = creds
        print(json.dumps(props, indent=4, default=json_ld.to_json_ld))


@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for kubernetes."""
    pass


# def load_file(filepath, file_format=DATA_FILE_FORMAT):
#    """Load file in a given format"""
#    graph = rdflib.Graph()
#    graph.parse(filepath, format=file_format)
#    return graph

cli_commands.add_command(openstack)
cli_commands.add_command(kubernetes)

if __name__ == "__main__":
    cli_commands()
