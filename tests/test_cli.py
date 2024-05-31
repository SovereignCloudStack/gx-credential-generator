import json
import unittest
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from generator import cli
from generator.common import const
from tests.common import MockConnection, get_absolute_path

EXPECTED_RESULT = {
    "@context": {
        "gx": "https://w3id.org/gaia-x/ONTOLOGY_VERSION#",
        "qudt": "http://qudt.org/vocab/",
        "schema": "http://schema.org/",
        "vcard": "http://www.w3.org/2006/vcard/ns#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "ex": "https://example.com/"
    },
    "@graph": "foo"
}


class CliTestCase(unittest.TestCase):

    @patch("generator.discovery.openstack.openstack_discovery.OpenstackDiscovery.discover")
    @patch("openstack.connect")
    def test_openstack(self, os_connect, os_discover):
        # Mock openstack calls
        os_connect.return_value = MockConnection(images=[], flavors=[])
        os_discover.return_value = "foo"

        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
        )
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        os_connect.assert_called_once()
        os_discover.assert_called_once()
        self.assertEqual(json.dumps(EXPECTED_RESULT, indent=4) + "\n", result.output)

    @patch("openstack.connect")
    def _test_openstack_empty(self, os_connect):
        # Mock openstack calls
        os_connect.return_value = MockConnection()
        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
        )

        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        with open(
                get_absolute_path("tests/data/empty_credential.json"), mode="r"
        ) as json_file:
            expected_output = json.load(json_file)
            received_output = json.loads(result.output)
            self.assertEqual(expected_output, received_output)

    @patch("openstack.connect")
    def _test_openstack_exception(self, os_connect):
        # Mock openstack calls
        mock_con = MockConnection(images=[], flavors=[])
        mock_con.authorize = MagicMock(name='method')
        mock_con.authorize.side_effect = [Exception(), None]
        os_connect.return_value = mock_con
        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
        )
        self.assertIsNone(result.exception)
        self.assertEqual(1, result.exit_code)

    def _test_kubernetes(self):
        # TODO: Implement test case
        runner = CliRunner()
        result = runner.invoke(cli.kubernetes)
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        pass


if __name__ == "__main__":
    unittest.main()
