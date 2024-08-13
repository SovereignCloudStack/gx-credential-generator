import unittest
from unittest.mock import patch

import yaml
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from jwcrypto.jwt import JWK

from generator.common import config, const
from generator.discovery.csp_generator import CspGenerator
from tests.common import get_absolute_path


class CspPGeneratorTestCase(unittest.TestCase):
    @patch("generator.discovery.gxdch_services.ComplianceService.request_compliance_vc")
    @patch("generator.discovery.gxdch_services.NotaryService.request_reg_number_vc")
    @patch("generator.discovery.gxdch_services.RegistryService.get_gx_tandc")
    @patch("generator.common.crypto.load_jwk_from_file")
    def test_generate(self, load_jwk, get_tandc, request_req_number, request_comp_vc):
        load_jwk.return_value = JWK.from_pem(rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048).private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()))
        get_tandc.return_value = {"version": "22.10", "text": "foo"}
        request_req_number.return_value = {"id": "cred_id", "credentialSubject": {"type": "gx:legalRegistrationNumber", "id": "cred_sub_id"}}
        request_comp_vc.return_value = "{\"credentialSubject\": {\"type\": \"gx:ComplianceCredential\"}}"

        with open(get_absolute_path(const.CONFIG_FILE), "r") as config_file:
            conf = config.Config(yaml.safe_load(config_file))

        csp_gen = CspGenerator(conf)
        csp_vcs = csp_gen.generate(auto_sign=True)

        get_tandc.assert_called_once()
        request_req_number.assert_called_once()
        request_req_number.assert_called_with(
            csp=conf.get_value([const.CONFIG_CSP]),
            cred_id=conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/lrn.json",
            cred_subject_id=conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/lrn_cs.json"
        )
        request_comp_vc.assert_called_once()

        self.assertEqual(conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/tandc.json",
                         csp_vcs['tandc']['id'])
        self.assertEqual(conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/tandc_cs.json", csp_vcs['tandc']['credentialSubject']['id'])
        self.assertEqual("gx:GaiaXTermsAndConditions", csp_vcs['tandc']['credentialSubject']['type'])
        self.assertEqual("foo", csp_vcs['tandc']['credentialSubject']['gx:termsAndConditions'])
        self.assertEqual(conf.get_value([const.CONFIG_CSP, const.CONFIG_DID]), csp_vcs['tandc']['issuer'])
        self.assertIsNotNone(csp_vcs['tandc']['proof'])
        self.assertEqual("cred_id", csp_vcs['lrn']['id'])
        self.assertEqual("cred_sub_id", csp_vcs['lrn']['credentialSubject']['id'])
        self.assertEqual("gx:legalRegistrationNumber", csp_vcs['lrn']['credentialSubject']['type'])
        self.assertEqual(conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/legal_person.json",
                         csp_vcs['lp']['id'])
        self.assertEqual(conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/legal_person_cs.json", csp_vcs['lp']['credentialSubject']['id'])
        self.assertEqual(conf.get_value([const.CONFIG_CSP, const.CONFIG_DID]), csp_vcs['lp']['issuer'])
        self.assertIsNotNone(csp_vcs['lp']['proof'])
        self.assertEqual("gx:LegalParticipant", csp_vcs['lp']['credentialSubject']['type'])
        self.assertEqual("gx:ComplianceCredential", csp_vcs['cs']['credentialSubject']['type'])


if __name__ == '__main__':
    unittest.main()
