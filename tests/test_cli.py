import os
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
    @patch("generator.cli._print_vcs")
    def test_generatate_vsmo(self, cli_print_vs, os_connect, os_discover, load_jwk, gxdch_req_compl):
        # Mock openstack calls
        cli_print_vs.return_value = None
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

        self.assertEqual(4, len(vcs))
        self.assertEqual("gx:ServiceOffering", vcs['so']['credentialSubject']["type"])
        self.assertEqual("gx:ComplianceCredential", vcs['cs']['credentialSubject']["type"])
        self.assertEqual("gx:VirtualMachineServiceOffering", vcs['vmso']['credentialSubject']["type"])
        self.assertIsNotNone(vcs['vp_so'])

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli.create_vmso_vcs")
    @patch("generator.cli._print_vcs")
    def test_openstack(self, cli_print_vs, gen_vmso, gen_csp):
        cli_print_vs.return_value = None
        gen_vmso.return_value = {"foo": "foo"}
        gen_csp.return_value = {"bar": "bar"}

        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE) + " --auto-sign"
        )

        gen_csp.assert_called_once()
        gen_vmso.assert_called_once()

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli.create_vmso_vcs")
    @patch("generator.cli._print_vcs")
    def test_openstack_auto_sign(self, cli_print_vs, gen_vmso, gen_csp):
        cli_print_vs.return_value = None
        gen_vmso.return_value = {"foo": "foo"}
        gen_csp.return_value = {"bar": "bar"}

        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE) + " --auto-sign"
        )

        gen_csp.assert_called_once()
        gen_vmso.assert_called_once()

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli.create_vmso_vcs")
    @patch("generator.cli._print_vcs")
    def test_openstack_no_auto_sign(self, cli_print_vs, gen_vmso, gen_csp):
        cli_print_vs.return_value = None
        gen_vmso.return_value = {"foo": "foo"}
        gen_csp.return_value = {"bar": "bar"}

        with patch('builtins.input', return_value="n"):
            runner = CliRunner()
            result = runner.invoke(
                cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE) + " --no-auto-sign"
            )

        self.assertEqual(0, gen_csp.call_count)
        self.assertEqual(0, gen_vmso.call_count)

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli.create_vmso_vcs")
    @patch("generator.cli._print_vcs")
    def test_openstack_sign(self, cli_print_vs, gen_vmso, gen_csp):
        cli_print_vs.return_value = None
        gen_vmso.return_value = {"foo": "foo"}
        gen_csp.return_value = {"bar": "bar"}

        with patch('builtins.input', return_value="y"):
            runner = CliRunner()
            result = runner.invoke(
                cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
            )

        gen_csp.assert_called_once()
        gen_vmso.assert_called_once()

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

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
    @patch("generator.cli._print_vcs")
    def test_csp_auto_sign(self, cli_print_vs, gen_csp):
        cli_print_vs.return_value = None
        gen_csp.return_value = {"vc": "bar"}

        runner = CliRunner()
        result = runner.invoke(
            cli.csp, "--config=" + get_absolute_path(const.CONFIG_FILE) + " --auto-sign"
        )

        gen_csp.assert_called_once()
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli._print_vcs")
    def test_csp_sign(self, cli_print_vs, gen_csp):
        cli_print_vs.return_value = None
        gen_csp.return_value = {"vc": "bar"}

        with patch('builtins.input', return_value="y"):
            runner = CliRunner()
            result = runner.invoke(
                cli.csp, "--config=" + get_absolute_path(const.CONFIG_FILE)
            )
        gen_csp.assert_called_once()
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    @patch("generator.discovery.csp_generator.CspGenerator.generate")
    @patch("generator.cli._print_vcs")
    def test_csp_no_auto_sign(self, cli_print_vs, gen_csp):
        cli_print_vs.return_value = None
        gen_csp.return_value = {"vc": "bar"}

        with patch('builtins.input', return_value="n"):
            runner = CliRunner()
            result = runner.invoke(
                cli.csp, "--config=" + get_absolute_path(const.CONFIG_FILE) + " --no-auto-sign"
            )

        self.assertEqual(0, gen_csp.call_count)
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    def _test_kubernetes(self):
        # TODO: Implement test case
        runner = CliRunner()
        result = runner.invoke(cli.kubernetes)
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)

    def test_print_vcs(self):
        out_dir = os.getcwd()
        vcs = {'so': {'foo': 'bar'}, 'lrn': {'bar': 'foo'}}
        with patch('builtins.open', unittest.mock.mock_open()) as m1:
            cli._print_vcs(vcs=vcs, out_dir=out_dir)
            self.assertEqual(2, m1.call_count)

        with patch('builtins.open', unittest.mock.mock_open()) as m2:
            cli._print_vcs(vcs=vcs)
            self.assertEqual(2, m2.call_count)

        with patch('builtins.open', unittest.mock.mock_open()):
            self.assertRaises(NotADirectoryError, cli._print_vcs, vcs, "/foo")


if __name__ == "__main__":
    unittest.main()
