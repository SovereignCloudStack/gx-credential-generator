import unittest

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from did_generator.did_gen import DidGenerator
from jwcrypto.jwt import JWK


class DidGenTestCase(unittest.TestCase):

    def setUp(self):
        self.did_gen = DidGenerator("../../did_generator/templates")

    def test_did_gen(self):
        # create rsa key pair
        private_rsa_key = rsa.generate_private_key(
            public_exponent=3,
            key_size=2048
        )
        public_rsa_key = JWK.from_pem(private_rsa_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

        # create elliptic key pair
        private_ec_key = ec.generate_private_key(ec.SECP256R1())
        public_ec_key = JWK.from_pem(private_ec_key.public_key().public_bytes(encoding=serialization.Encoding.PEM,
                                                                              format=serialization.PublicFormat.SubjectPublicKeyInfo))

        did_doc = self.did_gen.generate_did_document(issuer="did:web:example.com",
                                                     verification_methods={public_rsa_key, public_ec_key})

        self.assertEqual(["https://www.w3.org/ns/did/v1", "https://w3id.org/security/suites/jws-2020/v1"],
                         did_doc['@context'])
        self.assertEqual("did:web:example.com#JWK2020-RSA-key#0", did_doc['verificationMethod'][0]["id"])
        self.assertEqual("JsonWebKey2020", did_doc['verificationMethod'][0]["type"])
        self.assertEqual("did:web:example.com", did_doc['verificationMethod'][0]["controller"])
        self.assertEqual("RSA", did_doc['verificationMethod'][0]["publicKeyJwk"]["kty"])
        self.assertEqual("Aw", did_doc['verificationMethod'][0]["publicKeyJwk"]["e"])

        self.assertEqual("did:web:example.com#JWK2020-EC-key#1", did_doc['verificationMethod'][1]["id"])
        self.assertEqual("JsonWebKey2020", did_doc['verificationMethod'][1]["type"])
        self.assertEqual("did:web:example.com", did_doc['verificationMethod'][1]["controller"])
        self.assertEqual("EC", did_doc['verificationMethod'][1]["publicKeyJwk"]["kty"])
        self.assertEqual("P-256", did_doc['verificationMethod'][1]["publicKeyJwk"]["crv"])


if __name__ == '__main__':
    unittest.main()
