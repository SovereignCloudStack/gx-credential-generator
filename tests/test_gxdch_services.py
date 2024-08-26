import unittest
import uuid
from unittest.mock import patch

from requests.exceptions import HTTPError

from generator.discovery.gxdch_services import (ComplianceService,
                                                NotaryService, RegistryService)


class GxdchTestCase(unittest.TestCase):

    def test_init_notary_service(self):
        self.assertRaises(AttributeError, NotaryService, None)

    def test_init_compliance_service(self):
        self.assertRaises(AttributeError, ComplianceService, None)

    def test_init_registry_service(self):
        self.assertRaises(AttributeError, RegistryService, None)

    @patch("requests.post")
    def test_request_registration_number_vc(self, post_mock):
        # init test
        post_mock.return_value.ok = True
        post_mock.return_value.json.return_value = "foo"
        cred_id = uuid.uuid4()
        cred_subject_id = uuid.uuid4()

        # run test
        not_serv = NotaryService("https://exampple.com/gxdch/notary")
        resp = not_serv.request_reg_number_vc(
            csp={"did": "did:web:example.com", "registration_numbers": {"vat-id": "DE123456789"}},
            cred_subject_id=cred_subject_id, cred_id=cred_id)

        # check results
        self.assertEqual(
            'https://exampple.com/gxdch/notary/registrationNumberVC?vcid=' + str(cred_id),
            post_mock.call_args.args[0])
        self.assertEqual(
            {'json': {
                '@context': 'https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/participant',
                'type': 'gx:legalRegistrationNumber',
                'gx:vatID': 'DE123456789',
                'id': cred_subject_id}},
            post_mock.call_args.kwargs)
        self.assertEqual("foo", resp)

    @patch("requests.post")
    def test_request_registration_number_vc_exception(self, post_mock):
        # init test
        post_mock.side_effect = HTTPError(409)

        # run test
        not_serv = NotaryService("https://exampple.com/gxdch/notary")

        # check results
        self.assertRaises(HTTPError, not_serv.request_reg_number_vc,
                          csp={"did": "did:web:example.com", "registration_numbers": {"vat-id": "DE123456789"}},
                          cred_subject_id="foo", cred_id="bar")

    @patch("requests.post")
    def test_request_compliance_vc(self, post_mock):
        # init test
        post_mock.return_value.ok = True
        post_mock.return_value.text = "foo"

        # run test
        comp_serv = ComplianceService("https://example.com/gxdch/compliance-service")
        resp = comp_serv.request_compliance_vc(vp={"foo": "bar"}, vp_id="example.json")

        # Check results
        self.assertEqual(1, post_mock.call_count)
        self.assertEqual(
            'https://example.com/gxdch/compliance-service/api/credential-offers?vcid=example.json',
            post_mock.call_args.args[0])
        self.assertEqual("{\"foo\": \"bar\"}", post_mock.call_args.args[1])
        self.assertEqual("foo", resp)

    @patch("requests.post")
    def test_request_compliance_vc_exception(self, post_mock):
        # init test
        post_mock.side_effect = HTTPError(409)

        # run test
        comp_serv = ComplianceService("https://example.com/gxdch/compliance-service")

        # Check results
        self.assertRaises(HTTPError, comp_serv.request_compliance_vc, vp="{\\\"foo\\\": \\\"bar\\\"}",
                          vp_id="example.json")

    @patch("requests.get")
    def test_get_gx_tandc(self, get_mock):
        get_mock.return_value.ok = True
        get_mock.return_value.json.return_value = {'version': "22.10", "text": "foo"}

        reg = RegistryService("https://example/gxdch/registry")
        tandc = reg.get_gx_tandc()

        get_mock.called_with("https://example/gxdch/registry" + "/api/termsAndConditions")
        self.assertEqual({'version': "22.10", "text": "foo"}, tandc)

    @patch("requests.get")
    def test_get_gx_tandc_exception(self, get_mock):
        get_mock.side_effect = HTTPError(409)
        reg = RegistryService("https://example/gxdch/registry")
        self.assertRaises(HTTPError, reg.get_gx_tandc)


if __name__ == "__main__":
    unittest.main()
