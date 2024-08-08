from hashlib import sha256
from jwcrypto.jws import JWS, JWK
from jwcrypto.common import json_encode
from pyld import jsonld
from datetime import timezone, datetime

"""
Methods to handle cryptography. Most source code is taken from Gaia-X Example 
in https://gitlab.com/gaia-x/lab/workshops/gaia-x-101/-/tree/master
"""


def hash_str(text: str) -> str:
    """
    Hash given sting.
    @param text: string to hash
    @return: hash in hexadecimal format
    """
    return sha256(text.encode("utf-8")).hexdigest()


def compact_sig(sig) -> str:
    """
    Compact Json Web Signature according to JWS Compact Serialization in RFC 7519.
    @param sig: JSON Web Signature value to be compacted
    @return: compacted signature as string
    """
    parts = sig.split(".")
    return parts[0] + ".." + parts[2]


def sign_cred(cred: dict, key: JWK, verification_method: str) -> dict:
    """
    Sign given credential with the given key and the given verification method.
    @param cred: credential to be signed
    @param key: private kes to sign
    @param verification_method: verification method to verifiy signature
    @return: Verificable Credential as dict
    """
    # canonicalize credential to produce a unique representation
    # According to JSON Web Signature 2020 Spec, use https://w3id.org/security#URDNA2015 for canonicalization
    cannon_cred = jsonld.normalize(cred, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})

    # hash document to insure integrity, see https://w3c.github.io/vc-data-integrity/#how-it-works
    # use SHA-256 for JSON Web Signature 2020, see https://w3c-ccg.github.io/lds-jws2020/#suite-definition
    # hash acts as JSON Web Signature's payload
    payload = hash_str(cannon_cred)

    # create JSON Web Signature for credential's hash
    jwstoken = JWS(payload)
    jwstoken.add_signature(key, None,
                            json_encode({"alg": "PS256", "b64": False, "crit": ["b64"]}),
                            json_encode({"kid": key.thumbprint()}))
    sig = jwstoken.serialize(compact=True)

    # add proof to credential as JsonWebSiganture2020, see https://w3c-ccg.github.io/lds-jws2020/
    cred['proof'] = {
        "type": "JsonWebSignature2020",
        # ISO_8601 formated date string.
        "created": datetime.now(tz=timezone.utc).isoformat(),
        # SHOULD match assertion method expressed in DID document.
        "proofPurpose": "assertionMethod",
        # resolvable link to verification method. Dereferencing SHOULD result in an object of type JsonWebKey2020.
        "verificationMethod": verification_method,
        "jws": compact_sig(sig)
    }
    return cred


def load_jwk_from_file(path: str) -> JWK:
    """
    Load Json Web Key from file
    @param path: path to key file
    @return: loaded Json Web Key
    """
    with open(path, "rb") as key_file:
        bytes = key_file.read()
        return JWK.from_pem(bytes, password=None)

