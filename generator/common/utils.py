from hashlib import sha256

import jcs
from jwcrypto import jws
from jwcrypto.common import json_encode
from pyld import jsonld


def compact_token(token):
    parts = token.split(".")
    return parts[0] + ".." + parts[2]


def normalize(doc):
    return jsonld.normalize(doc, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})


def sha256_normalized_vc(normalized_vc):
    return sha256(normalized_vc.encode('utf-8'))


def sha256_string(canonized_vc):
    return sha256(canonized_vc).hexdigest()

def canonicalize(doc):
    return jcs.canonicalize(doc)


def sign_doc(doc, private_key, issuer_verification_method):
    # URDNA normalize
    normalized = normalize(doc)
    # sha256 the RDF
    normalized_hash = sha256_normalized_vc(normalized)
    # Sign using JWS
    jws_token = jws.JWS(normalized_hash.hexdigest())
    jws_token.add_signature(private_key, None,
                            json_encode({"alg": "PS256", "b64": False, "crit": ["b64"]}),
                            json_encode({"kid": private_key.thumbprint()}))
    signed = jws_token.serialize(compact=True)
    doc['proof'] = {
        "type": "JsonWebSignature2020",
        "proofPurpose": "assertionMethod",
        "verificationMethod": issuer_verification_method,
        "jws": compact_token(signed)
    }
    return doc
