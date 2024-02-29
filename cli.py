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
import warnings


from typing import List

import click
import openstack as os
import yaml

import generator.common.const as const
import generator.common.json_ld as json_ld

from pyshacl import validate

from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.opentack_discovery import OsCloud
from generator.wallet.file_wallet import FileSystemWallet
from generator.wallet.wallet import WalletConnector
from generator.wallet.xfsc_wallet import XFSCWallet

import rdflib

SHAPES_FILE_FORMAT = "turtle"
DATA_FILE_FORMAT = "json-ld"


@click.group()
def cli():
    pass


@click.command()
#@click.option(
#    "--wallet",
#    is_flag=True,
#    help="Use '--wallet' to store generated credentials in all wallets. Wallets can be configured in configuration file.",
#)
#@click.option(
#    "--no-print",
#    is_flag=True,
#    help="Use '--no-print' to omit json-ld print on screen.",
#)
@click.option(
    "--config",
    default="config/config.yaml",
    help="Path to Configuration file for SCS GX Credential Generator.",
)
@click.option("--timeout", default=12, help="Timeout for API calls in seconds")
@click.argument("cloud")
def openstack(cloud, timeout, config):
#def openstack(cloud, timeout, config, no_print, wallet):
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
        os_cloud = OsCloud(conn, config_dict)

        # run discovery
        creds = os_cloud.discover_properties()

        # store creds in wallets
        #if wallet:
        #    wallets = init_wallets(config_dict)
        #    store_creds_in_wallet(wallets, creds)

        # print on screen
        #if not no_print:
        props = json_ld.get_json_ld_context()
        props["@graph"] = creds
        print(json.dumps(props, indent=4, default=json_ld.to_json_ld))

        #if not wallet and no_print:
        #    warnings.warn("--no-print is set, but not --wallet. Generated credential(s) will be stored/printed nowhere.")


@click.command()
def kubernetes():
    """Generates Gaia-X Credentials for kubernetes."""
    pass


def init_wallets(config: dict) -> List[WalletConnector]:
    wallets = list()
    try:
        for wallet in config[const.CONFIG_WALLETS]:
            if wallet == const.CONFIG_FILESYSTEM_WALLET:
                wallets.append(
                    FileSystemWallet(
                        config[const.CONFIG_WALLETS][const.CONFIG_FILESYSTEM_WALLET]["path"]
                    )
                )
            elif wallet == const.CONFIG_XFSC_WALLET:
                wallets.append(XFSCWallet())
    except KeyError:
        pass
    return wallets


def store_creds_in_wallet(
        wallets: List[WalletConnector], creds: List[JsonLdObject]
) -> None:
    for w in wallets:
        for c in creds:
            w.store_credential(c)


def load_file(filepath, file_format=DATA_FILE_FORMAT):
    """Load file in a given format"""
    graph = rdflib.Graph()
    graph.parse(filepath, format=file_format)
    return graph


#@click.command()
#@click.argument("credential", help=f"Filepath of GX Credential to validate. Should have {DATA_FILE_FORMAT} format", )
#@click.argument("shapes",
#                help=f"Filepath of shacl schema to be used for validation. Should have {SHAPES_FILE_FORMAT} format", )
#def validate(credential, shapes):
#    """Validate SD in jsonld format against given schema in turtle format"""
#    conforms, results_graph, results_text = validate(
#        load_file(credential),
#        shacl_graph=load_file(shapes, file_format=SHAPES_FILE_FORMAT),
#        data_graph_format=DATA_FILE_FORMAT,
#        shacl_graph_format=SHAPES_FILE_FORMAT,
#        inference="rdfs",
#        debug=False,
#        serialize_report_graph=True,
#    )
#    print(results_text)


cli.add_command(openstack)
cli.add_command(kubernetes)
#cli.add_command(validate)


if __name__ == "__main__":
    cli()
