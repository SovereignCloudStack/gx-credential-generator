import unittest

from generator.discovery.gxdch_services import NotaryService
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from unittest.mock import patch


class NotaryServiceTestCase(unittest.TestCase):

    @patch("requests.post")
    def test_issue_registration_number_vc(self, post_mock):
        post_mock.return_value = {"ok": True}
        j_env = Environment(
            loader=FileSystemLoader("../templates"),
            autoescape=select_autoescape()
        )

        not_serv = NotaryService("https://registrationnumber.notary.gaia-x.eu/v1/registrationNumberVC", j_env=j_env)
        resp = not_serv.request_reg_number_vc(csp={"did": "did:web:example.com", "vat-id": "DE281093504"})
        self.assertTrue(resp['ok'])
        self.assertEqual(post_mock.call_count, 1)


if __name__ == "__main__":
    unittest.main()
