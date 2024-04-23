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
import openstack as open_stack
import yaml
import generator.common.const as const

import generator.common.json_ld as json_ld
from generator.common.config import Config

from generator.discovery.openstack.openstack_discovery import OsCloud
import os
from generator.wallet.filesystem_wallet import FileSystemWallet

SHAPES_FILE_FORMAT = "turtle"
DATA_FILE_FORMAT = "json-ld"

DEFAULT_CONFIG_1 = "config.yaml"
DEFAULT_CONFIG_2 = "~/.config/scs-gax-gen/config.yaml"
DEFAULT_CONFIG_3 = "etc/scs-gax-gen/config.yaml"


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
    conn = open_stack.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
    try:
        conn.authorize()
    except Exception:
        print("INFO: Retry connection with 'default' domain", file=sys.stderr)
        conn = open_stack.connect(
            cloud=cloud,
            timeout=timeout,
            api_timeout=timeout * 1.5 + 4,
            default_domain="default",
            project_domain_id="default",
        )
        conn.authorize()

    # load config
    if not config:
        if os.path.exists(DEFAULT_CONFIG_1):
            config = DEFAULT_CONFIG_1
        elif os.path.exists(DEFAULT_CONFIG_2):
            config = DEFAULT_CONFIG_2
        else:
            config = DEFAULT_CONFIG_3

    # generate Gaia-X Credentials
    with open(config, "r") as config_file:
        # init everything
        config_dict = yaml.safe_load(config_file)
        os_cloud = OsCloud(conn, Config(config_dict))

        # init wallet
        if config_dict["wallet"] == const.CONFIG_WALLETS:
            wallet = FileSystemWallet(config_dict["wallet"])

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
