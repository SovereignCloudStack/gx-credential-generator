import unittest
from unittest.mock import MagicMock, patch

import yaml
from click.testing import CliRunner
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from jwcrypto.jwt import JWK

from generator import cli
from generator.common import config, const
from generator.common.gx_schema import (DataAccountExport, TermsAndConditions,
                                        VirtualMachineServiceOffering)
from tests.common import MockConnection, get_absolute_path


class CliTestCase(unittest.TestCase):

    @patch("generator.discovery.gxdch_services.ComplianceService.request_compliance_vc")
    @patch("generator.common.crypto.load_jwk_from_file")
    @patch("generator.discovery.openstack.openstack_discovery.OpenstackDiscovery.discover")
    @patch("openstack.connect")
    def test_generatate_vsmo(self, os_connect, os_discover, load_jwk, gxdch_req_compl):
        # Mock openstack calls
        os_connect.return_value = MockConnection(images=[], flavors=[])
        os_discover.return_value = VirtualMachineServiceOffering(
            providedBy="foo",
            serviceOfferingTermsAndConditions=[TermsAndConditions(
                url="https://example.com/tandc",
                hash="123")],
            dataAccountExport=DataAccountExport(
                requestType="API",
                accessType="digital",
                formatType="plain"),
            codeArtifact=["foo"],
            instantiationReq=["bar"])
        load_jwk.return_value = JWK.from_pem(rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048).private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()))
        csp_vcs = {'tandc': {"credentialSubject": {"type": "gx:GaiaXTermsAndConditions"}},
                   "lrn": {"credentialSubject": {"type": "gx:LegalRegistrationNumber", "id": "foo"}},
                   "lp": {"credentialSubject": {"type": "gx:LegalParticipant", "id": "foo"}}}
        gxdch_req_compl.return_value = "{\"credentialSubject\": {\"type\": \"gx:ComplianceCredential\", \"id\": \"foo\"}}"

        with open(get_absolute_path(const.CONFIG_FILE), "r") as config_file:
            conf = config.Config(yaml.safe_load(config_file))

        vcs = cli.create_vmso_vcs(conf, "myCloud", csp_vcs)
        os_connect.assert_called_once()
        os_discover.assert_called_once()
        gxdch_req_compl.assert_called_once()

        self.assertEqual(3, len(vcs))
        self.assertEqual("gx:ServiceOffering", vcs[0]['credentialSubject']["type"])
        self.assertEqual("gx:ComplianceCredential", vcs[1]['credentialSubject']["type"])
        self.assertEqual("gx:VirtualMachineServiceOffering", vcs[2]['credentialSubject']["type"])

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli.create_vmso_vcs")
    def test_openstack(self, gen_vmso, gen_csp):
        gen_vmso.return_value = ["foo"]
        gen_csp.return_value = ["bar"]

        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
        )

        gen_csp.assert_called_once()
        gen_vmso.assert_called_once()

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        self.assertEqual("\"bar\"\n\"foo\"\n", result.output)

    @patch("openstack.connect")
    def test_init_connection(self, os_connect):
        # Mock openstack calls
        mock_con = MockConnection(images=[], flavors=[])
        mock_con.authorize = MagicMock(name='method')
        mock_con.authorize.side_effect = [Exception(), None]
        os_connect.return_value = mock_con

        con = cli.init_openstack_connection("myCloud")
        self.assertIsNotNone(con)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    def test_csp(self, gen_csp):
        gen_csp.return_value = {"vc": "bar"}

        runner = CliRunner()
        result = runner.invoke(
            cli.csp, "--config=" + get_absolute_path(const.CONFIG_FILE)
        )

        gen_csp.assert_called_once()

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        self.assertEqual("\"bar\"\n", result.output)

    def _test_kubernetes(self):
        # TODO: Implement test case
        runner = CliRunner()
        result = runner.invoke(cli.kubernetes)
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        pass


if __name__ == "__main__":
    unittest.main()
