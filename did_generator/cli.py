#!/usr/bin/env python3

"""Script to generate DID documents fort did:web method.

(c) Anja Strunk <anja.sturnk@cloudandheat.com>, 4/2024
SPDX-License-Identifier: EPL-2.0
"""
import json

import click
import yaml
from jwcrypto.jwt import JWK
from cryptography.hazmat.primitives import serialization
from did_gen import DidGenerator
from cryptography.hazmat.primitives.serialization import load_pem_public_key

DEFAULT_CONFIG_FILE = "/etc/scs-did-gen/config.yaml"

@click.command()
@click.option("--config", help="Configuration file for DID generator")
@click.option("--output-file", help="Output file - default stdout")
def did_creator(output_file, config):
    """Generates DID document for given DID and private keys."""
    did_crea = DidGenerator("templates")

    if not config:
        config = DEFAULT_CONFIG_FILE

    with open(config, "r") as config_file:
        config_dict = yaml.safe_load(config_file)
        keys = []
        for key in config_dict['pub_key']:
            with open(key, "rb") as key_file:
                jwk = JWK.from_pem(load_pem_public_key(key_file.read()).public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
                keys.append(jwk)

        did_content = did_crea.generate_did_document(issuer=config_dict['issuer'], verification_methods=keys)
        if output_file:
            with open(output_file, "w") as did_doc:
                did_doc.write(json.dumps(did_content, indent=4))
        else:
            print(json.dumps(did_content, indent=4))


if __name__ == "__main__":
    did_creator()
