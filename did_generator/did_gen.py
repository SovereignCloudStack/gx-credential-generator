import json
import os
from datetime import datetime, timezone
from typing import Optional, List, Set

import requests
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jwcrypto import jwk

# from utils import sign_doc, canonicalize, sha256_string


class DidGenerator:

    def __init__(self, jinja_templates: str):
        self.jinja_env = Environment(
            loader=FileSystemLoader(jinja_templates),
            autoescape=select_autoescape()
        )

    def generate_did_document(self, issuer: str, verification_methods: List) -> dict:
        vfy_methods = []
        keys = []
        key_number = 0
        for jw_key in verification_methods:
            jwk_content = jw_key.export(as_dict=True)
            if jwk_content['kty'] == "RSA":
                jwk_tmpl = self.jinja_env.get_template("rsa_jwk.j2")
                keys.append("JWK2020-RSA-key#" + str(key_number))
            elif jwk_content['kty'] == "EC":
                jwk_tmpl = self.jinja_env.get_template("ec_jwk.j2")
                keys.append("JWK2020-EC-key#" + str(key_number))
            else:
                raise ValueError(jwk_content['kty'] + " no supported key type.")

            vfy_methods.append((jwk_tmpl.render(issuer=issuer, number=key_number, jwk=jwk_content)))
            key_number += 1

        did_doc_tmpl = self.jinja_env.get_template("did.j2")
        did_doc = did_doc_tmpl.render(issuer=issuer, verification_method=vfy_methods, keys=keys)
        return json.loads(did_doc)
