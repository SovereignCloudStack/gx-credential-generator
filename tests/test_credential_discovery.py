import unittest

from jinja2 import Environment, FileSystemLoader, select_autoescape
from unittest.mock import patch
from cryptography.hazmat.primitives.asymmetric import rsa
from jwcrypto.jwt import JWK


class CredentialDiscoveryTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.discovery = CredentialDiscovery(Environment(
            loader=FileSystemLoader("../templates"),
            autoescape=select_autoescape()
        ))
        cls.cred_settings = {
            "verification-method": "did:web:example.com#JWK2020-RSA-key0",
            "base_credential_url": "www.example.com",
            "key": "path/to/key"
        }
        cls.csp = {
            "did": "did:web:example.com",
            "legal-name": "Acme",
            "legal-address-country-code": "DE-SN",
            "headquarter-address-country-code": "DE-SN",
            "vat-id": "DE123456789"
        }
        rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        cls.key = JWK.generate(kty='RSA', size=2048)

    @patch("generator.common.crypto.load_jwk_from_file")
    def test_create_gaia_x_terms_and_conditions_vc(self, load_jwk_mock):
        # set return value of mocked methods
        load_jwk_mock.return_value = self.key

        # run test
        vc = self.discovery.create_gaia_x_terms_and_conditions_vc(csp=self.csp, cred_settings=self.cred_settings)

        # check results
        self.assertEqual(['https://www.w3.org/2018/credentials/v1',
                          'https://w3id.org/security/suites/jws-2020/v1',
                          'https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#'],
                         vc['@context'])
        self.assertEqual('did:web:example.com', vc['credentialSubject']['id'])
        self.assertEqual('gx:GaiaXTermsAndConditions', vc['credentialSubject']['type'])
        self.assertEqual('www.example.com/gaia-x-terms-and-cond.json', vc['id'])
        self.assertEqual('VerifiableCredential', vc['type'])
        self.assertEqual('did:web:example.com', vc['issuer'])
        self.assertEqual('assertionMethod', vc['proof']['proofPurpose'])
        self.assertEqual('JsonWebSignature2020', vc['proof']['type'])
        self.assertEqual('did:web:example.com#JWK2020-RSA-key0', vc['proof']['verificationMethod'])

    @patch("generator.common.crypto.load_jwk_from_file")
    def test_create_and_sign_legal_person_vc(self, load_jwk_mock):
        # set return value of mocked methods
        load_jwk_mock.return_value = self.key

        # run test
        vc = self.discovery.create_and_sign_legal_person_vc(
            csp=self.csp,
            lrn_cred_ids='www.example.com/vat_id.json',
            cred_settings=self.cred_settings)

        # check results
        self.assertEqual(['https://www.w3.org/2018/credentials/v1',
                          'https://w3id.org/security/suites/jws-2020/v1',
                          'https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#'],
                         vc['@context'])
        self.assertEqual('did:web:example.com', vc['credentialSubject']['id'])
        self.assertEqual('gx:LegalParticipant', vc['credentialSubject']['type'])
        self.assertEqual('Acme', vc['credentialSubject']['gx:legalName'])
        self.assertEqual('DE-SN', vc['credentialSubject']['gx:headquarterAddress']['gx:countrySubdivisionCode'])
        self.assertEqual('DE-SN', vc['credentialSubject']['gx:legalAddress']['gx:countrySubdivisionCode'])
        self.assertEqual('www.example.com/vat_id.json', vc['credentialSubject']['gx:legalRegistrationNumber']['id'])
        self.assertEqual('www.example.com/legal-person.json', vc['id'])
        self.assertEqual('VerifiableCredential', vc['type'])
        self.assertEqual('did:web:example.com', vc['issuer'])
        self.assertEqual('assertionMethod', vc['proof']['proofPurpose'])
        self.assertEqual('JsonWebSignature2020', vc['proof']['type'])
        self.assertEqual('did:web:example.com#JWK2020-RSA-key0', vc['proof']['verificationMethod'])

    @patch("generator.common.crypto.load_jwk_from_file")
    def test_create_verifiable_presentation(self, load_jwk_mock):
        # set return value of mocked methods
        load_jwk_mock.return_value = self.key

        # run test
        vp = self.discovery.create_verifiable_presentation(
            vcs=[{"foo": "bar"}, {"bar": "foo"}],
            cred_settings=self.cred_settings)

        # check results
        self.assertEqual("https://www.w3.org/2018/credentials/v1",
                         vp['@context'])
        self.assertEqual('VerifiablePresentation', vp['type'])
        self.assertEqual({'foo': 'bar'}, vp['verifiableCredential'][0])
        self.assertEqual({'bar': 'foo'}, vp['verifiableCredential'][1])
        self.assertEqual('assertionMethod', vp['proof']['proofPurpose'])
        self.assertEqual('JsonWebSignature2020', vp['proof']['type'])
        self.assertEqual('did:web:example.com#JWK2020-RSA-key0', vp['proof']['verificationMethod'])


if __name__ == "__main__":
    unittest.main()
