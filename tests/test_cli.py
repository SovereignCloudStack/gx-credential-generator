import json
import unittest
from unittest.mock import patch

from click.testing import CliRunner
from openstack.image.v2.image import Image as OS_Image

import cli
from generator.common import const
from tests.common import MockConnection, get_absolute_path

OS_IMAGE_1 = OS_Image(
    hw_scsi_model="virtio - scsi",
    os_distro="windows",
    hw_watchdog_action="reset",
    hw_rng_model="virtio",
    os_version="Stable",
    hypervisor_type="qemu",
    hw_video_ram=20,
    hw_vif_multiqueue_enabled=True,
    hw_pmu=False,
    hw_disk_bus="SCSI",
    hw_cpu_cores=2,
    hw_cpu_threads=4,
    architecture="x86_64",
    name="Image2",
    disk_format="RAW",
    container_format="bare",
    needs_secure_boot=True,
    size="9116319744",
    virtual_size="9116319744",
    checksum="a516d5aea8ebc358dd316dd67266a2ba",
    min_ram=1,
    min_disk=20,
    owner="477ba6f14a5b43abe85b2966be7ebe136",
    os_hash_algo="sha512",
    os_hash_value="7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182",
    id="image_2",
    visibility="public",
    properties={
        "image_build_date": "2023-11-01",
        "image_description": "Image 2",
        "provided_until": "none",
        "replace_frequency": "weekly",
        "uuid_validity": "last-3",
        "patchlevel": "1.5.2",
        "license_required": True,
        "license_included": False,
        "subscription_required": True,
        "subscription_included": False,
        "maintained_until": "2024-05-31",
    },
)


class CliTestCase(unittest.TestCase):
    @patch("openstack.connect")
    def test_openstack(self, os_connect):
        # Mock openstack calls
        os_connect.return_value = MockConnection(images=[OS_IMAGE_1])
        runner = CliRunner()
        result = runner.invoke(
            cli.openstack, "myCloud --config=" + get_absolute_path(const.CONFIG_FILE)
        )
        self.assertIsNone(result.exception)
        self.assertEqual(0, result.exit_code)
        with open(get_absolute_path("tests/data/vm_image_2.json"), "r") as json_file:
            expected_output = json.load(json_file)
            received_outout = json.loads(result.output)
            self.assertEqual(expected_output, received_outout)

    def test_kubernetes(self):
        # TODO: Implement test case
        pass


if __name__ == "__main__":
    unittest.main()
