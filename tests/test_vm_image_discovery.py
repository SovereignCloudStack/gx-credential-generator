import json
import unittest
import yaml
import os

from generator.common import const

from pathlib import Path
from datetime import datetime, date

from generator.common.json_ld import JsonLdObject
from generator.common.config import Config
from generator.common.gx_schema import CheckSum
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Disk
from generator.common.gx_schema import Memory
from generator.common.gx_schema import MemorySize
from generator.common.gx_schema import OperatingSystem
from generator.common.gx_schema import WatchDogActions
from generator.common.gx_schema import VMImage as GX_Image
from generator.common.gx_schema import VMDiskType, FirmType, WatchDogActions, ChecksumAlgorithm, RNGTypes, \
    UpdateStrategy, UpdateFrequency, Signature, SignatureAlgorithm, HypervisorType, MaintenanceSubscription

from generator.common.json_ld import to_json_ld
from generator.discovery.openstack.vm_images_discovery import VmDiscovery

from openstack.image.v2.image import Image as OS_Image

from pyshacl import validate

from tests.common import OpenstackTestcase
from tests.common import MockConnection
import tests.common

GX_IMAGE_1 = JsonLdObject(
    gx_id='image_1',
    gx_object=GX_Image(name='Image1',
                       description='Image 1',
                       aggregationOfResources=[],
                       copyrightOwnedBy=['Microsoft Corporation'],
                       license=['https://www.microsoft.com/licensing'],
                       resourcePolicy=['default: allow intent'],
                       checksum=CheckSum(checkSumCalculation='sha-512',
                                         checkSumValue='7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182'),
                       signature=None,
                       version=None,
                       patchLevel=None,
                       buildDate=datetime(2023, 11, 1, 0, 0),
                       fileSize=None,
                       operatingSystem=OperatingSystem(name=None, description=None,
                                                       aggregationOfResources=[],
                                                       copyrightOwnedBy=['Microsoft Corporation'],
                                                       license=['https://www.microsoft.com/licensing'],
                                                       resourcePolicy=['default: allow intent'],
                                                       checksum=None, signature=None,
                                                       version='Stable', patchLevel=None, buildDate=None,
                                                       osDistribution='Microsoft Windows'),
                       cpuReq=CPU(vendor=None, generation=None, defaultOversubscriptionRatio=None,
                                  supportedOversubscriptionRatio=None, cpuArchitecture='x86-64', cpuFlag=[],
                                  smtEnabled=False, numberOfCores=2, numberOfThreads=4, baseFrequency=None,
                                  boostFrequency=None, lastLevelCacheSize=None, thermalDesignPower=None),
                       gpuReq=None,
                       ramReq=Memory(vendor=None, generation=None, defaultOversubscriptionRatio=None,
                                     supportedOversubscriptionRatio=None,
                                     memorySize=MemorySize(value=0.0,
                                                           unit='https://qudt.org/vocab/unit/MegaBYTE'),
                                     memoryClass='other', memoryRank='other',
                                     eccEnabled=False, hardwareEncryption=False),
                       videoRamSize=MemorySize(value=20.0, unit='https://qudt.org/vocab/unit/MegaBYTE'),
                       rootDiskReq=Disk(vendor=None, generation=None, defaultOversubscriptionRatio=None,
                                        supportedOversubscriptionRatio=None,
                                        diskSize=MemorySize(value=21.47483648,
                                                            unit='https://qudt.org/vocab/unit/GigaBYTE'),
                                        diskType='other', diskBusType='SCSI'),
                       encryption=None,
                       checkSum=None,
                       secureBoot=True,
                       vPMU=False,
                       multiQueues=True,
                       updateStrategy=None,
                       licenseIncluded=False,
                       maintenance={'subscriptionIncluded': False, 'subscriptionRequired': True,
                                    'maintainedUntil': date(2024, 5, 31)},
                       vmImageDiskFormat='RAW',
                       hypervisorType='other',
                       firmwareType='other',
                       hwRngTypeOfImage='None',
                       watchDogAction='reset'))

GX_IMAGE_2 = JsonLdObject(
    gx_id='image_2',
    gx_object=GX_Image(
        copyrightOwnedBy=['Microsoft Corporation'],
        license=['https://www.microsoft.com/licensing'],
        resourcePolicy=['default: allow intent'],
        maintenance={'subscriptionIncluded': False, 'subscriptionRequired': False},
        hypervisorType=HypervisorType("other")))

OS_IMAGE_1 = OS_Image(hw_scsi_model="virtio - scsi",
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
                      min_ram=0,
                      min_disk=20,
                      owner="477ba6f14a5b43abe85b2966be7ebe136",
                      os_hash_algo="sha512",
                      os_hash_value="7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182",
                      id="image_2",
                      visibility="public",
                      properties={
                          'image_build_date': '2023-11-01',
                          'image_description': 'Image 2',
                          'provided_until': 'none',
                          'replace_frequency': 'weekly',
                          'uuid_validity': 'last-3',
                          'patchlevel': '1.5.2',
                          'license_required': True,
                          'license_included': False,
                          'subscription_required': True,
                          'subscription_included': False,
                          'maintained_until': datetime.strptime("2024-05-31", "%Y-%m-%d")
                      })
OS_IMAGE_2 = OS_Image(os_distro="windows",
                      id="image_2",
                      visibility="public")


class VMImageDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        current_dir = Path(__file__).parent
        if current_dir.name == "tests":
            config_file = str(Path(current_dir.parent, "config/config.yaml"))
        else:
            config_file = str(Path(current_dir, "config/config.yaml"))

        with open(config_file, "r") as config_file:
            self.config = yaml.safe_load(config_file)
            self.discovery = VmDiscovery(conn=MockConnection([OS_IMAGE_1, OS_IMAGE_2]),
                                         conf=Config(self.config))

    def test_discovery_vm_images(self):
        actual_gax_images = self.discovery.discover_vm_images()
        self.assert_vm_image(GX_IMAGE_1.gx_object, actual_gax_images[0].gx_object)
        self.assert_vm_image(GX_IMAGE_2.gx_object, actual_gax_images[1].gx_object)

    def _test_json_ld(self):
        current_dir = Path(__file__).parent
        if current_dir.name == "tests":
            shacl_file = str(Path(current_dir, "gaia-x.shacl.ttl"))
        else:
            shacl_file = str(Path(current_dir, "tests/gaia-x.shacl.ttl"))

        conforms, _, _ = validate(data_graph=json.dumps(
            GX_IMAGE_1,
            indent=4, default=to_json_ld),
            shacl_graph=shacl_file,
            data_graph_format="json-ld",
            shacl_graph_format="ttl"
        )
        self.assertTrue(conforms)

    def test_get_disk_format(self):
        self.assertEqual(VMDiskType("RAW"), self.discovery._get_disk_format(OS_Image(disk_format="foo")))
        self.assertEqual(VMDiskType("RAW"), self.discovery._get_disk_format(OS_Image(disk_format="RAW")))
        self.assertEqual(VMDiskType("RAW"), self.discovery._get_disk_format(OS_Image(disk_format="raw")))
        self.assertEqual(VMDiskType("VHD"), self.discovery._get_disk_format(OS_Image(disk_format="vHd")))
        self.assertEqual(VMDiskType("RAW"), self.discovery._get_disk_format(OS_Image()))

    def test_get_secure_boot(self):
        self.assertTrue(self.discovery._get_secure_boot(OS_Image(needs_secure_boot=True)))
        self.assertFalse(self.discovery._get_secure_boot(OS_Image(needs_secure_boot=False)))
        self.assertFalse(self.discovery._get_secure_boot(OS_Image()))

    def test_get_firmeware_type(self):
        self.assertEqual(FirmType("BIOS"), self.discovery._get_firmeware_type(OS_Image(hw_firmware_type="BIOS")))
        self.assertEqual(FirmType("BIOS"), self.discovery._get_firmeware_type(OS_Image(hw_firmware_type="bioS")))
        self.assertEqual(FirmType("other"), self.discovery._get_firmeware_type(OS_Image(hw_firmware_type="foo")))
        self.assertEqual(FirmType("other"), self.discovery._get_firmeware_type(OS_Image()))

    def test_get_watchdog_action(self):
        self.assertEqual(WatchDogActions("reset"),
                         self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="reset")))
        self.assertEqual(WatchDogActions("reset"),
                         self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="Reset")))
        self.assertEqual(WatchDogActions("disabled"),
                         self.discovery._get_watchdog_action(OS_Image(hw_watchdog_action="foo")))
        self.assertEqual(WatchDogActions("disabled"), self.discovery._get_watchdog_action(OS_Image()))

    def test_get_vmpu(self):
        self.assertTrue(self.discovery._get_vmpu(OS_Image(hw_pmu=True)))
        self.assertFalse(self.discovery._get_vmpu(OS_Image(hw_pmu=False)))
        self.assertFalse(self.discovery._get_vmpu(OS_Image()))

    def test_get_cpu_req(self):
        self.assertEqual(CPU(cpuArchitecture='x86-64', numberOfCores=2, numberOfThreads=4),
                         self.discovery._get_cpu_req(OS_Image(architecture="x86_64", hw_cpu_cores=2, hw_cpu_threads=4)))
        self.assertEqual(CPU(cpuArchitecture='x86-64'),
                         self.discovery._get_cpu_req(OS_Image(architecture="x86_64")))
        self.assertEqual(CPU(cpuArchitecture="other"),
                         self.discovery._get_cpu_req(OS_Image()))

    def test_get_multiqueue_enabled(self):
        self.assertTrue(self.discovery._get_multiqueue_enabled(OS_Image(is_hw_vif_multiqueue_enabled=True)))
        self.assertFalse(self.discovery._get_multiqueue_enabled(OS_Image(is_hw_vif_multiqueue_enabled=False)))
        self.assertFalse(self.discovery._get_multiqueue_enabled(OS_Image()))

    def test_get_checksum(self):
        self.assertEqual(CheckSum(checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("md5")),
                         self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="md5")))
        self.assertEqual(CheckSum(checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("md5")),
                         self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="MD5")))
        self.assertEqual(CheckSum(checkSumValue="a123", checkSumCalculation=ChecksumAlgorithm("other")),
                         self.discovery._get_checksum(OS_Image(hash_value="a123", hash_algo="foo")))
        self.assertIsNone(self.discovery._get_checksum(OS_Image()))

    def test_get_rng_model(self):
        self.assertEqual(RNGTypes("None"), self.discovery._get_rng_model(OS_Image()))

    def test_get_file_size(self):
        self.assertEqual(MemorySize(value=1.073741824, unit=const.UNIT_GB),
                         self.discovery._get_file_size(OS_Image(size=1)))
        self.assertIsNone(self.discovery._get_file_size(OS_Image()))

    def test_get_video_ram(self):
        self.assertEqual(MemorySize(value=12, unit=const.UNIT_MB),
                         self.discovery._get_video_ram_size(OS_Image(hw_video_ram=12)))
        self.assertIsNone(self.discovery._get_video_ram_size(OS_Image()))

    def test_get_update_strategy(self):
        self.assertEqual(
            UpdateStrategy(replaceFrequency="yearly", oldVersionsValidUntil="notice", providedUntil="notice"),
            self.discovery._get_update_strategy(
                OS_Image(replace_frequency="yearly", uuid_validity="notice", provided_until="notice")))
        self.assertEqual(
            UpdateStrategy(replaceFrequency="yearly", oldVersionsValidUntil="notice", providedUntil="notice",
                           hotfixHours=5),
            self.discovery._get_update_strategy(
                OS_Image(replace_frequency="yearly", uuid_validity="notice", provided_until="notice", hotfix_hours=5)))

        self.assertIsNone(self.discovery._get_update_strategy(OS_Image()))

    def test_get_description(self):
        self.assertEqual("image",
                         self.discovery._get_description(OS_Image(image_description="image")))
        self.assertEqual("image Managed by me",
                         self.discovery._get_description(OS_Image(image_description="image", managed_by_VENDOR="me")))
        self.assertIsNone(self.discovery._get_description(OS_Image()))

    def test_get_name(self):
        self.assertEqual("image",
                         self.discovery._get_name(OS_Image(name="image")))
        self.assertIsNone(self.discovery._get_name(OS_Image()))

    def test_get_build_date(self):
        self.assertEqual(datetime(year=2023, month=12, day=31),
                         self.discovery._get_build_date(OS_Image(image_build_date="2023-12-31")))
        self.assertIsNone(self.discovery._get_build_date(OS_Image()))

    def test_get_license_included(self):
        self.assertTrue(self.discovery._get_license_included(OS_Image(licenseIncluded=True)))
        self.assertFalse(self.discovery._get_license_included(OS_Image(licenseIncluded=False)))
        self.assertFalse(self.discovery._get_license_included(OS_Image()))

    def test_get_patch_level(self):
        self.assertEqual("v1.2.0", self.discovery._get_patch_level(OS_Image(patchlevel="v1.2.0")))
        self.assertFalse(self.discovery._get_license_included(OS_Image()))

    def test_get_version(self):
        self.assertEqual("v1.2.0", self.discovery._get_version(OS_Image(internal_version="v1.2.0")))
        self.assertIsNone(self.discovery._get_version(OS_Image()))

    def test_get_maintenance(self):
        self.assertEqual(
            MaintenanceSubscription(subscriptionIncluded=True,
                                    subscriptionRequired=True,
                                    maintainedUntil= date(2024, 5, 31)),
            self.discovery._get_maintenance(
                OS_Image(subscription_required=True,
                         subscription_included=True,
                         maintained_until=datetime.strptime("2024-05-31", "%Y-%m-%d"))))
        self.assertEqual(
            MaintenanceSubscription(subscriptionIncluded=True,
                                    subscriptionRequired=True),
            self.discovery._get_maintenance(
                OS_Image(subscription_required=True,
                         subscription_included=True)))
        self.assertEqual(
            MaintenanceSubscription(subscriptionIncluded=False,
                                    subscriptionRequired=True),
            self.discovery._get_maintenance(
                OS_Image(subscription_required=True)))
        self.assertEqual(
            MaintenanceSubscription(subscriptionIncluded=False,
                                    subscriptionRequired=False),
            self.discovery._get_maintenance(
                OS_Image()))
    def test_get_signature(self):
        self.assertEqual(Signature(
            signatureValue="e123",
            hashAlgorithm=ChecksumAlgorithm.md5,
            signatureAlgorithm="RSA-Signature"),
            self.discovery._get_signature(
                OS_Image(img_signature="e123", img_signature_hash_method="md5", img_signature_key_type="SHA-123")))
        self.assertEqual(Signature(
            signatureValue="e123",
            hashAlgorithm=ChecksumAlgorithm.md5,
            signatureAlgorithm="RSA-Signature"),
            self.discovery._get_signature(
                OS_Image(img_signature="e123", img_signature_hash_method="MD5", img_signature_key_type="Sha-123")))
        self.assertEqual(Signature(
            signatureValue="e123",
            hashAlgorithm=ChecksumAlgorithm.other,
            signatureAlgorithm="other"),
            self.discovery._get_signature(
                OS_Image(img_signature="e123", img_signature_hash_method="bar", img_signature_key_type="foo")))
        self.assertIsNone(self.discovery._get_signature(OS_Image()))

    def test_get_hypervisor(self):
        self.assertEqual(HypervisorType("KVM"),
                         self.discovery._get_hypervisor_type(OS_Image(hypervisor_type="KVM")))
        self.assertEqual(HypervisorType("KVM"),
                         self.discovery._get_hypervisor_type(OS_Image(hypervisor_type="Kvm")))
        self.assertIsNone(self.discovery._get_min_ram_req(OS_Image()))

    def test_get_min_ram_req(self):
        self.assertEqual(Memory(memorySize=MemorySize(1.048576, unit=const.UNIT_MB), hardwareEncryption=True),
                         self.discovery._get_min_ram_req(OS_Image(min_ram=1, hw_mem_encryption=True)))
        self.assertEqual(Memory(memorySize=MemorySize(0, unit=const.UNIT_MB), hardwareEncryption=False),
                         self.discovery._get_min_ram_req(OS_Image(min_ram=0)))
        self.assertIsNone(self.discovery._get_min_ram_req(OS_Image()))

    def test_get_min_disk_req(self):
        self.assertEqual(Disk(diskSize=MemorySize(1.073741824, unit=const.UNIT_GB), diskBusType="SATA"),
                         self.discovery._get_min_disk_req(OS_Image(min_disk=1, hw_disk_bus="SATA")))
        self.assertEqual(Disk(diskSize=MemorySize(0, unit=const.UNIT_GB), diskBusType="other"),
                         self.discovery._get_min_disk_req(OS_Image(min_disk=0)))
        self.assertIsNone(self.discovery._get_min_disk_req(OS_Image()))

    def test_get_operating_system(self):
        self.assertEqual(
            OperatingSystem(version="1",
                            osDistribution=const.CONFIG_OS_DEBIAN,
                            resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                            copyrightOwnedBy="Ian Murdock and others",
                            license=["https://www.debian.org/legal/licenses/index.en.html"]),
            self.discovery._get_operation_system(OS_Image(os_version="1", os_distro="debian")))
        self.assertEqual(
            OperatingSystem(version="1",
                            osDistribution=const.CONFIG_OS_FREEBSD,
                            resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                            copyrightOwnedBy="The FreeBSD Project",
                            license=["GPL-3.0-only", "LGPL-2.0"]),
            self.discovery._get_operation_system(OS_Image(os_version="1", os_distro="FreeBSD")))


if __name__ == '__main__':
    unittest.main()
