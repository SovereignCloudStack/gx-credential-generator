import unittest

from jsonasobj import JsonObj
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

OS_TYPE_1 = OS_TYPE(id="type_1", name="default",)
OS_TYPE_2 = OS_TYPE(
    id="type_2", name="encrypted", description="[scs: encrypted]",)
OS_TYPE_3 = OS_TYPE(
    id="type_3", name="replicated", description="[scs: replicated]",)
OS_TYPE_4 = OS_TYPE(
    id="type_4", name="replicated and encrypted", description="[scs: encrypted, replicated] bar",)
OS_TYPE_5 = OS_TYPE(
    id="type_5", name="replicated", description="[scs: encrypted1, replicated] foo",)
OS_TYPE_6 = OS_TYPE(
    id="type_6", name="encrypted", description="[scs: encrypted, replicated1] bar",)


class VolumeTypeDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        self.conf = get_config()
        self.discovery = VolumeTypeDiscovery(
            conn=MockConnection(types=[OS_TYPE_1,
                                       OS_TYPE_2,
                                       OS_TYPE_3,
                                       OS_TYPE_4,
                                       OS_TYPE_5,
                                       OS_TYPE_6]), conf=self.conf
        )

    def test_discover(self):
        actual_gax_vol_types =  self.discovery.discover()
        self.assertIsNone(actual_gax_vol_types[0].storageEncryption)
        self.assertEqual(self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-encryption-type_2",
                          actual_gax_vol_types[1].storageEncryption['id'])
        self.assertIsNone(actual_gax_vol_types[2].storageEncryption)
        self.assertEqual(self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-encryption-type_4",
                          actual_gax_vol_types[3].storageEncryption['id'])
        self.assertIsNone(actual_gax_vol_types[4].storageEncryption)
        self.assertEqual(
            self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-encryption-type_6",
            actual_gax_vol_types[5].storageEncryption['id'])

        self.assertIsNone(actual_gax_vol_types[0].storageRedundancyMechanism)
        self.assertIsNone(actual_gax_vol_types[1].storageRedundancyMechanism)
        self.assertEqual(self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-replication-type_3",
                          actual_gax_vol_types[2].storageRedundancyMechanism[0]['id'])
        self.assertEqual(
            self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-replication-type_4",
            actual_gax_vol_types[3].storageRedundancyMechanism[0]['id'])
        self.assertEqual(
            self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-replication-type_5",
            actual_gax_vol_types[4].storageRedundancyMechanism[0]['id'])
        self.assertIsNone(actual_gax_vol_types[5].storageRedundancyMechanism)


if __name__ == "__main__":
    unittest.main()
