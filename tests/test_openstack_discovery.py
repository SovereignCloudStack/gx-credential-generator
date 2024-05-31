import unittest
from unittest.mock import MagicMock, patch

from generator.common import const
from generator.common.gx_schema import (CPU, Architectures, Disk, Memory,
                                        MemorySize, ServerFlavor, VMImage)
from generator.discovery.openstack.openstack_discovery import \
    OpenstackDiscovery
from tests.common import MockConnection, get_config

GX_IMAGE_1 = VMImage(
    copyrightOwnedBy=["Fedora-Project"],
    license=["https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/"],
    resourcePolicy=["default: allow intent"],
)

GX_FLAVOR_1 = ServerFlavor(
    cpu=CPU(
        cpuArchitecture=Architectures.Other,
        defaultOversubscriptionRatio=1,
        numberOfCores=4,
    ),
    ram=Memory(
        memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
    bootVolume=Disk(
        diskSize=MemorySize(value=10, unit=const.UNIT_MB)
    )
)


class OpenstackDiscoveyTestCase(unittest.TestCase):

    def setUp(self):
        self.discovery = OpenstackDiscovery(
            conn=MockConnection(images=[], flavors=[]), config=get_config())

    @patch("generator.discovery.openstack.vm_images_discovery.VmImageDiscovery.discover")
    @patch("generator.discovery.openstack.server_flavor_discovery.ServerFlavorDiscovery.discover")
    @patch("requests.get")
    def test_discovery(self, request_get, flavor_discovery, image_discovery):
        # Mock openstack calls
        request_get.side_effect = [MagicMock(status_code=200, text="foo"), MagicMock(status_code=200, text="foo")]
        flavor_discovery.return_value = [GX_FLAVOR_1]
        image_discovery.return_value = [GX_IMAGE_1]

        # run test
        self.discovery.discover()

        # check results
        image_discovery.assert_called_once()
        flavor_discovery.assert_called_once()


if __name__ == "__main__":
    unittest.main()
