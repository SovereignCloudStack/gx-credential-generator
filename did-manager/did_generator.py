import json
import os
from datetime import datetime, timezone
from typing import Optional

import requests
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from jwcrypto import jwk

#from utils import sign_doc, canonicalize, sha256_string

OID2ALG = {
    "1.2.840.113549.2.9": "HS256",
    "1.2.840.113549.2.10": "HS384",
    "1.2.840.113549.2.11": "HS512",
    "1.2.840.113549.1.1.11": "RS256",
    "1.2.840.113549.1.1.12": "RS384",
    "1.2.840.113549.1.1.13": "RS512",
    "1.2.840.10045.4.3.2": "ES256",
    "1.2.840.10045.4.3.3": "ES384",
    "1.2.840.10045.4.3.4": "ES512",
    "1.2.840.113549.1.1.10": "PS256"
}

load_dotenv()  # Load from variables .env file
jinja_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)
issuer = os.getenv("issuer")
verification_method = os.getenv("verificationMethod")
certs_var = os.getenv("X509_CERTIFICATE")
private_key = jwk.JWK.from_pem(os.getenv("privateKey").encode("UTF-8"))

if __name__ == "__main__":
    print ("Generate DID")