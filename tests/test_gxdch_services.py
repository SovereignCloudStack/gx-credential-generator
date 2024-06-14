import unittest

from generator.discovery.gxdch_services import NotaryService, ComplianceService
from unittest.mock import patch
import uuid


class GxdchTestCase(unittest.TestCase):

    def test_init_notary_service(self):
        self.assertRaises(AttributeError, NotaryService, None)

    def test_init_compliance_service(self):
        self.assertRaises(AttributeError, ComplianceService, None)

    def test_request_registration_number_vc_exception(self):
        not_serv = NotaryService(api="foo")
        self.assertRaises(AttributeError, not_serv.request_reg_number_vc, None, None)

    def test_request_compliance_vc_exception(self):
        comp_serv = ComplianceService(api="foo")
        self.assertRaises(AttributeError, comp_serv.request_compliance_vc, None, None)

    @patch("requests.post")
    def test_request_registration_number_vc(self, post_mock):
        # init test
        post_mock.return_value = {"ok": True}
        cred_id = uuid.uuid4()
        not_serv = NotaryService("https://registrationnumber.notary.gaia-x.eu/v1")

        # run test
        resp = not_serv.request_reg_number_vc(csp={"did": "did:web:example.com", "vat-id": "DE123456789"},
                                              cred_id=cred_id)

        # check results
        self.assertTrue(resp['ok'])
        self.assertEqual(post_mock.call_count, 1)
        self.assertEqual(
            ('https://registrationnumber.notary.gaia-x.eu/v1/registrationNumberVC?vcid=' + str(cred_id),),
            post_mock.call_args.args)
        self.assertEqual(
            {'json': {
                '@context': 'https://www.w3.org/2018/credentials/v1',
                '@type': 'gx:legalRegistrationNumber',
                'gx:vatID': 'DE123456789',
                'id': 'did:web:example.com'}},
            post_mock.call_args.kwargs)

    @patch("requests.post")
    def test_request_compliance_vc(self, post_mock):
        # init test
        post_mock.return_value = {"ok": True}
        comp_serv = ComplianceService("https://compliance.lab.gaia-x.eu/v1-staging/api/credential-offers")

        # run test
        resp = comp_serv.request_compliance_vc(vcs=[{"foo": "bar"}], vp_id="example.json")

        # Check results
        self.assertTrue(resp['ok'])
        self.assertEqual(1, post_mock.call_count)
        self.assertEqual(
            ('https://compliance.lab.gaia-x.eu/v1-staging/api/credential-offers?vcid=example.json',),
            post_mock.call_args.args)
        self.assertEqual(
            {'json': {
                '@context': 'https://www.w3.org/2018/credentials/v1',
                '@type': 'VerifiablePresentation',
                'verifiableCredential': '[{"foo": "bar"}]'}},
            post_mock.call_args.kwargs)

    if __name__ == "__main__":
        unittest.main()
