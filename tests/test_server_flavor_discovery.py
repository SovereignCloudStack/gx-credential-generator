import json
import os
import unittest
import yaml

from generator.common import const

from datetime import datetime

from generator.common.json_ld import JsonLdObject
from generator.common.gx_schema import CheckSum
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Disk
from generator.common.gx_schema import Memory
from generator.common.gx_schema import MemorySize
from generator.common.gx_schema import OperatingSystem
from generator.common.gx_schema import WatchDogActions
from generator.common.gx_schema import VMImage as GX_Image
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.common.gx_schema import Architectures as CpuArch

from generator.common.json_ld import to_json_ld
from generator.discovery.openstack.server_flavor_discovery import ServerFlavorDiscovery


from openstack.image.v2.image import Image as OS_Image
from openstack.compute.v2.flavor import Flavor as OS_Flavor

from pyshacl import validate

from tests.common import OpenstackTestcase
from tests.common import TestConnection


def _get_gx_flavors():
    return [JsonLdObject(
        gx_id='flavor_1',
        gx_object=GX_Flavor(
            #name='Flavor_1', description='Flavor 1_ext',
                            cpu=CPU(vendor=None, generation=None, defaultOversubscriptionRatio=None,
                                      supportedOversubscriptionRatio=None,
                                      cpuArchitecture='x86-64',
                                      cpuFlag=[], smtEnabled=False, numberOfCores=2, numberOfThreads=4,
                                      baseFrequency=None,
                                      boostFrequency=None, lastLevelCacheSize=None,
                                      thermalDesignPower=None), gpuReq=None,
                            ram=Memory(vendor=None, generation=None, defaultOversubscriptionRatio=None,
                                         supportedOversubscriptionRatio=None,
                                         memorySize=MemorySize(value=0.0,
                                                               unit='https://qudt.org/vocab/unit/MegaBYTE'),
                                         memoryClass='other', memoryRank='other', eccEnabled=False,
                                         hardwareEncryption=False),
            ))]

def _get_os_flavors():
    return [OS_Flavor(name="ABC",
                      vcpus=2,
                      ram=32
                     )]


class VMImageDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        cur_dir = os.getcwd()
        if cur_dir.endswith('tests'):
            path = cur_dir[0:-5] + '/config/config.yaml'
        else:
            path = cur_dir + '/config/config.yaml'
        with open(path, 'r') as config_file:
           self.config = yaml.safe_load(config_file)
           self.discovery = ServerFlavorDiscovery(conn=TestConnection(None), config=self.config)

    def test_get_disk_caps(self):
        self.assertEqual((3, 10, "local SSD", None), self.discovery._get_disk_caps("3x10s"))
        self.assertEqual((1, 10, "local HDD", "NVMe"), self.discovery._get_disk_caps("10p"))
        self.assertEqual((1, 10, "other", None), self.discovery._get_disk_caps("10"))
        self.assertEqual((1, 0, "shared network storage", None), self.discovery._get_disk_caps("n"))
        self.assertEqual((2, 10, "other", None), self.discovery._get_disk_caps("2x10"))
        self.assertEqual((2, 10, "local HDD", "NVMe"), self.discovery._get_disk_caps("2x10p"))

    def test_get_mem(self):
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=3.5, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-3.5-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB), eccEnabled = True),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4u-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB), defaultOversubscriptionRatio = 2),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4o-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4uo-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB), eccEnabled = True, defaultOversubscriptionRatio = 2),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4ou-10n", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C_", ram=10)))
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="test", ram=10)))

    def test_get_cpu(self):
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other),
            self.discovery._get_cpu(OS_Flavor(name="ABC", ram=10)))
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other, defaultOversubscriptionRatio=1, numberOfCores=2),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2C-4", ram=10)))
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other, defaultOversubscriptionRatio=1, numberOfCores=2, smtEnabled=True),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2T-4", ram=10)))
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other, defaultOversubscriptionRatio=5, numberOfCores=2, smtEnabled=True),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2V-4", ram=10)))
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other, defaultOversubscriptionRatio=16, numberOfCores=2, smtEnabled=True),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2L-4", ram=10)))

    def test_get_disks(self):
        pass

    def test_parse_optional_flavor_properties(self):

        self.discovery._parse_optional_flavor_properties(OS_Flavor(name="abc", vcpu=2, ram=32), GX_Flavor(
            #name=os_flavor.name,
            cpu=CPU(cpuArchitecture=CpuArch.other),
            ram=Memory(memorySize=MemorySize(value=0, unit=const.UNIT_MB)),
            bootVolume=Disk(diskSize=MemorySize(value=0, unit=const.UNIT_GB))))



    """def test_discovery_vm_images(self):
        actual_gax_images = self.discovery.discover()
        expected_gax_images = _get_gx_images()

        self.assertEqual(len(expected_gax_images), len(expected_gax_images))

        for image_1 in actual_gax_images:
            for image_2 in expected_gax_images:
                if image_1.gx_id == image_2.gx_id:
                    self.check_vm_image(image_1.gx_object, image_2.gx_object)

    def test_json_ld(self):

        conforms, _, _ = validate(data_graph=json.dumps(
            _get_gx_images()[0],
            indent=4, default=to_json_ld),
            shacl_graph="tests/gaia-x.shacl.ttl",
            data_graph_format="json-ld",
            shacl_graph_format="ttl"
        )
        self.assertTrue(conforms)"""


if __name__ == '__main__':
    unittest.main()
