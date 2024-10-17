import unittest

from openstack.compute.v2.flavor import Flavor as OS_Flavor
from openstack.block_storage.v3.type import Type as OS_TYPE
from openstack.block_storage.v3.type import TypeEncryption

from generator.common import const
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (Disk, DiskBusType, DiskType, Frequency,
                                        Hypervisor, Memory, MemorySize)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.volume_type_discovery import VolumeTypeDiscovery
from generator.vendor.flavor_names import parser_v3
from tests.common import MockConnection, OpenstackTestcase, get_config

OS_TYPE_1 = OS_TYPE(id="type_1", name="foo",)
OS_TYPE_2 = OS_TYPE(
    id="type_2", name="[scs: encrypted] bar",)


class VolumeTypeDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        self.discovery = VolumeTypeDiscovery(
            conn=MockConnection(types=[OS_TYPE_1, OS_TYPE_2]), conf=get_config()
        )

    def test_is_volume_encrypted(self):
        self.assertFalse(self.discovery._is_volume_encrypted("foo"))
        self.assertTrue(self.discovery._is_volume_encrypted("[scs: encrypted] bar"))
        self.assertTrue(self.discovery._is_volume_encrypted("[scs: encrypted, replicated] bar"))
        self.assertFalse(self.discovery._is_volume_encrypted("foo [scs:] bar"))

if __name__ == "__main__":
    unittest.main()
