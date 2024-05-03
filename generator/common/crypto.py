import json
from hashlib import sha256
from jwcrypto.jws import JWS, JWK
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat, NoEncryption
from jwcrypto.common import json_encode
from pyld import jsonld


def get_sha256(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def sign_cred(cred: dict, private_key: JWK, verification_method: str) -> dict:
    # canonicalize credential to produce a unique representation
    cannon_cred = jsonld.normalize(cred, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})

    # calculate hash of canonicalize credential
    cannon_cred_hash = get_sha256(cannon_cred)

    # create JWS for credential
    signature = JWS(cannon_cred_hash)
    signature.add_signature(private_key, None,
                            json_encode({"alg": "PS256", "b64": False, "crit": ["b64"]}),
                            json_encode({"kid": private_key.thumbprint()}))
    signed = signature.serialize(compact=True)

    # add proof to credential
    cred['proof'] = {
        "type": "JsonWebSignature2020",
        "proofPurpose": "assertionMethod",
        "verificationMethod": verification_method,
        "jws": signed
    }

    return cred


def load_JWK_from_file(path: str) -> JWK:
    with open(path, "rb") as key_file:
        private_bytes = key_file.read()
        private_key = load_pem_private_key(private_bytes, password=None)

        return JWK.from_pem(private_bytes, password=None)
