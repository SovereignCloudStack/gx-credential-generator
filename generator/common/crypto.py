import base64
import json
import requests
from hashlib import sha256
from jwcrypto.jws import JWS, JWK
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat, NoEncryption
from jwcrypto.common import json_encode
from pyld import jsonld
from generator.common.did_resolver import DidResolver
import datetime


def hash_str(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def compact_token(token):
    parts = token.split(".")
    return parts[0] + ".." + parts[2]


def sign_cred(cred: dict, private_key: JWK, verification_method: str) -> dict:
    # canonicalize credential to produce a unique representation
    # According to JSON Web Signature 2020 Spec, use https://w3id.org/security#URDNA2015 for canonicalization
    cannon_cred = jsonld.normalize(cred, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})

    # hash document to insure integrity, see https://w3c.github.io/vc-data-integrity/#how-it-works
    # use SHA-256 for JSON Web Signature 2020, see https://w3c-ccg.github.io/lds-jws2020/#suite-definition
    # hash acts as JSON Web Signature's payload
    # TODO: Clarify why we need an additional hash here, as JWS already hash document prior to signing
    #payload = hash_str(cannon_cred)

    # create JSON Web Signature for credential's hash
    jwstoken = JWS(cannon_cred)
    # TODO: Support all JWS key types here and check if Gaia-X does the same
    jwstoken.add_signature(private_key, alg=None,
                           protected=json_encode({"alg": "PS256"}),
                           header=json_encode({"kid": private_key.thumbprint()}))
    #jwstoken.add_signature(private_key, alg=None,
    #                       protected=json_encode({"alg": "PS256", "b64": False, "crit": ["b64"]}),
    #                       header=json_encode({"kid": private_key.thumbprint()}))
    # Compact signature cause verification to fail, so we have to do a workaround here
    sig = jwstoken.serialize(compact=True)
    #sig = jwstoken.serialize()

    #data = sig_c.split(".")
    #sig_new = dict()
    #sig_new['payload'] = data[1]
    #sig_new['protected'] = data[0]
    #sig_new['signature'] = data[2]
    #sig_new_str = str(sig_new).replace('\'', '\"')

    pub_key = load_jwk_from_file("/home/anja-strunk/.gaia-x/gaia-x_vc.key.public.pem")

    jwstoken_sig= JWS()
    jwstoken_sig.deserialize(sig, key=pub_key)

    #try:
    #    jwstoken3_c = JWS()
    #    jwstoken3_c.deserialize(sig_c, key=pub_key)
    #except Exception:
    #    pass

    #jwstoken_new = JWS()
    #jwstoken_new.deserialize(sig_new_str, key=pub_key)

    # add proof to credential as JsonWebSiganture2020, see https://w3c-ccg.github.io/lds-jws2020/
    cred['proof'] = {
        "type": "JsonWebSignature2020",

        "created": datetime.datetime.today().isoformat(),  # ISO_8601 formated date string.
        "proofPurpose": "assertionMethod",  # SHOULD match assertion method expressed in DID document.
        "verificationMethod": verification_method,  # resolvable link to verification method. Dereferencing SHOULD
        # result in an object of type JsonWebKey2020.
        "jws": sig
    }

    # double-check if cred could be verified with given values
    verify_cred(cred)

def load_jwk_from_file(path: str) -> JWK:
    with open(path, "rb") as key_file:
        bytes = key_file.read()
        return JWK.from_pem(bytes, password=None)


def verify_cred(cred: dict) -> None:
    cred_copy = cred.copy()
    proof = cred_copy['proof']
    doc = cred_copy.pop('proof')
    # Accocring to https://www.w3.org/TR/vc-data-model/#proofs-signatures one or more proof elements are allowed, so we have to count proof elements here
    if isinstance(proof, list):
        for p in proof:
            _verify_signature(doc, p)
    else:
        _verify_signature(doc, proof)


def _verify_signature(cred: dict, proof: dict):
    """
    Support JWS as proof only!!! And did only
    @param cred:
    @param proof:
    @return:
    """
    if proof['proofPurpose'] == 'assertionMethod':
        if proof['type'] == 'JsonWebSignature2020':
            # extract verification key
            veri_meth = proof['verificationMethod']
            if str(veri_meth).startswith("did:web"):
                # verification method is
                key = _get_verification_key(proof, "https://uniresolver.io/1.0/identifiers")
                jwstoken = JWS()
                try:
                    djws = json.loads(proof['jws'])
                except json.JSONDecoderError as e:
                    # we may have a compact signature here
                    data = proof['jws'].split(".")

                    pass

                jwstoken.deserialize(proof['jws'], key=key)
                #jwstoken.verify(key<)
            else:
                # TODO: Which verification methods do exist in JWT?
                raise TypeError("Verification method not support: ...")
        else:
            print("Unsupported type '" + proof['type'] + "' for assertion method found")


def _get_verification_key(proof, did_resolver_url: str) -> str:
    verif_method = proof['verificationMethod']
    did = str(verif_method).split("#")[0]
    # c = ClientWebResolver(did_resolver_url)
    # c2 = ClientWebResolver2("https://uniresolver.io/1.0/identifiers")
    # r = c.resolve(did)
    if not did_resolver_url.endswith("/"):
        did_resolver_url += "/"
    # url = did_resolver_url + did
    resp = requests.get(did_resolver_url + did)
    if resp.ok:
        did_doc = resp.json()['didDocument']
        for vm in did_doc['verificationMethod']:
            if vm['id'] == verif_method:
                return JWK.from_json(json.dumps(vm['publicKeyJwk']))
    else:
        raise TypeError(
            "Could not retrieve DID document for '" + did + "' from reolver '" + did_resolver_url + "\n(Status Code: " + resp.status_code + ". " + resp.text + ".)")
