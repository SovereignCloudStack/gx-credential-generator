import unittest
from unittest.mock import MagicMock, patch

from generator.common import const
from generator.common.gx_schema import (CpuCapabilities, CPU, Architectures, Disk, MemoryCapabilities, Memory,
                                        MemorySize, ServerFlavor, VMImage, StorageConfiguration)
from generator.discovery.openstack.openstack_discovery import \
    OpenstackDiscovery
from tests.common import MockConnection, OpenstackTestcase, get_config

GX_IMAGE_1 = VMImage(
    copyrightOwnedBy=["Fedora-Project"],
    license=["https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/"],
    resourcePolicy=["default: allow intent"],
)

GX_FLAVOR_1 = ServerFlavor(
    cpu=CpuCapabilities(
        pCPU=CPU(
            cpuArchitecture=Architectures.Other,
            defaultOversubscriptionRatio=1,
            numberOfCores=4),
        vCPUs=4),
    memory=MemoryCapabilities(
        memory = Memory(
            memorySize=MemorySize(value=10, unit=const.UNIT_MB))),
        bootVolume=Disk(
            diskSize=MemorySize(value=10, unit=const.UNIT_MB)
    )
)

GX_VOL_TYPE_1 = StorageConfiguration()




class OpenstackDiscoveyTestCase(OpenstackTestcase):

    def setUp(self):
        self.discovery = OpenstackDiscovery(
            conn=MockConnection(images=[], flavors=[]), config=get_config())

    @patch("generator.discovery.openstack.volume_type_discovery.VolumeTypeDiscovery.discover")
    @patch("generator.discovery.openstack.vm_images_discovery.VmImageDiscovery.discover")
    @patch("generator.discovery.openstack.server_flavor_discovery.ServerFlavorDiscovery.discover")
    @patch("requests.get")
    def test_generate_gx_credentials(self, request_get, flavor_discovery, image_discovery, vol_type_discovery):
        # Mock openstack calls
        request_get.side_effect = [MagicMock(status_code=200, text="foo"), MagicMock(status_code=200, text="foo")]
        flavor_discovery.return_value = [GX_FLAVOR_1]
        image_discovery.return_value = [GX_IMAGE_1]
        vol_type_discovery.return_value = [GX_VOL_TYPE_1]

        # run tests
        self.discovery.discover()

        # check results
        image_discovery.assert_called_once()
        flavor_discovery.assert_called_once()
        vol_type_discovery.assert_called_once()

        # Todo test returned services


if __name__ == "__main__":
    unittest.main()
