import unittest

from openstack.image.v2.image import Image as OS_Image

from generator.discovery.openstack.openstack_discovery import OsCloud
from tests.common import MockConnection, get_config

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


class OpenstackDiscoveryTestCase(unittest.TestCase):
    def setUp(self):
        self.cloud = OsCloud(MockConnection([OS_IMAGE_1]), config=get_config())

    def _test_discover_properties(self):
        print(self.cloud.discover_properties())
        self.assertEqual(True, False)  # add assertion here


if __name__ == "__main__":
    unittest.main()
