import json
import os
import unittest
from datetime import datetime

import yaml
from openstack.image.v2.image import Image as OS_Image
from pyshacl import validate

from generator.common.gx_schema import (CPU, CheckSum, Disk, Memory,
                                        MemorySize, OperatingSystem)
from generator.common.gx_schema import VMImage as GX_Image
from generator.common.gx_schema import WatchDogActions
from generator.common.json_ld import JsonLdObject, to_json_ld
from generator.discovery.openstack.images_discovery import ImageDiscovery
from tests.common import MockConnection, OpenstackTestcase


def _get_gx_images():
    return [
        JsonLdObject(
            gx_id="image_1",
            gx_object=GX_Image(
                name="Image1",
                description="Image 1_ext",
                aggregationOfResources=[],
                copyrightOwnedBy=["Canonical"],
                license=["https://ubuntu.com/legal/open-source-licences"],
                resourcePolicy=["default: allow intent"],
                checksum=CheckSum(
                    checkSumCalculation="sha-512", checkSumValue="7f8bababc2c2a948"
                ),
                signature=None,
                version=None,
                patchLevel="1.5.2",
                buildDate=datetime(2023, 12, 1, 0, 0),
                fileSize=None,
                operatingSystem=OperatingSystem(
                    name=None,
                    description=None,
                    aggregationOfResources=[],
                    copyrightOwnedBy=["Canonical"],
                    license=["https://ubuntu.com/legal/open-source-licences"],
                    resourcePolicy=["default: allow intent"],
                    checksum=None,
                    signature=None,
                    version="Stable",
                    patchLevel=None,
                    buildDate=None,
                    osDistribution="Ubuntu",
                ),
                cpuReq=CPU(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    cpuArchitecture="x86-64",
                    cpuFlag=[],
                    smtEnabled=False,
                    numberOfCores=2,
                    numberOfThreads=4,
                    baseFrequency=None,
                    boostFrequency=None,
                    lastLevelCacheSize=None,
                    thermalDesignPower=None,
                ),
                gpuReq=None,
                ramReq=Memory(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    memorySize=MemorySize(
                        value=0.0, unit="https://qudt.org/vocab/unit/MegaBYTE"
                    ),
                    memoryClass="other",
                    memoryRank="other",
                    eccEnabled=False,
                    hardwareEncryption=False,
                ),
                videoRamSize=MemorySize(
                    value=20.0, unit="https://qudt.org/vocab/unit/MegaBYTE"
                ),
                rootDiskReq=Disk(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    diskSize=MemorySize(
                        value=21.47483648, unit="https://qudt.org/vocab/unit/GigaBYTE"
                    ),
                    diskType="other",
                    diskBusType="SCSI",
                ),
                encryption=None,
                checkSum=None,
                secureBoot=True,
                vPMU=False,
                multiQueues=False,
                updateStrategy=None,
                licenseIncluded=False,
                maintenance=None,
                vmImageDiskFormat="RAW",
                hypervisorType="other",
                hwRngTypeOfImage="None",
                watchDogAction=WatchDogActions.reset.text,
            ),
        ),
        JsonLdObject(
            gx_id="image_2",
            gx_object=GX_Image(
                name="Image2",
                description="Image 2",
                aggregationOfResources=[],
                copyrightOwnedBy=["Microsoft Corporation"],
                license=["https://www.microsoft.com/licensing"],
                resourcePolicy=["default: allow intent"],
                checksum=CheckSum(
                    checkSumCalculation="sha-512",
                    checkSumValue="7f8bababc2c2a94880747383750470aee68c7e8840bb8811eaeda1b0ce71d59f40ebb182",
                ),
                signature=None,
                version=None,
                patchLevel=None,
                buildDate=datetime(2023, 11, 1, 0, 0),
                fileSize=None,
                operatingSystem=OperatingSystem(
                    name=None,
                    description=None,
                    aggregationOfResources=[],
                    copyrightOwnedBy=["Microsoft Corporation"],
                    license=["https://www.microsoft.com/licensing"],
                    resourcePolicy=["default: allow intent"],
                    checksum=None,
                    signature=None,
                    version="Stable",
                    patchLevel=None,
                    buildDate=None,
                    osDistribution="Microsoft Windows",
                ),
                cpuReq=CPU(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    cpuArchitecture="x86-64",
                    cpuFlag=[],
                    smtEnabled=False,
                    numberOfCores=2,
                    numberOfThreads=4,
                    baseFrequency=None,
                    boostFrequency=None,
                    lastLevelCacheSize=None,
                    thermalDesignPower=None,
                ),
                gpuReq=None,
                ramReq=Memory(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    memorySize=MemorySize(
                        value=0.0, unit="https://qudt.org/vocab/unit/MegaBYTE"
                    ),
                    memoryClass="other",
                    memoryRank="other",
                    eccEnabled=False,
                    hardwareEncryption=False,
                ),
                videoRamSize=MemorySize(
                    value=20.0, unit="https://qudt.org/vocab/unit/MegaBYTE"
                ),
                rootDiskReq=Disk(
                    vendor=None,
                    generation=None,
                    defaultOversubscriptionRatio=None,
                    supportedOversubscriptionRatio=None,
                    diskSize=MemorySize(
                        value=21.47483648, unit="https://qudt.org/vocab/unit/GigaBYTE"
                    ),
                    diskType="other",
                    diskBusType="SCSI",
                ),
                encryption=None,
                checkSum=None,
                secureBoot=True,
                vPMU=False,
                multiQueues=False,
                updateStrategy=None,
                licenseIncluded=False,
                maintenance=None,
                vmImageDiskFormat="RAW",
                hypervisorType="other",
                firmwareType="other",
                hwRngTypeOfImage="None",
                watchDogAction="reset",
            ),
        ),
    ]


def _get_os_images():
    return [
        OS_Image(
            hw_scsi_model="virtio - scsi",
            os_distro="ubuntu",
            hw_watchdog_action="reset",
            hw_rng_model="virtio",
            os_version="Stable",
            hypervisor_type="qemu",
            hw_video_ram=20,
            hw_vif_multiqueue_enabled=True,
            hw_pmu=False,
            hw_firmware_type="bios",
            hw_disk_bus="SCSI",
            hw_cpu_cores=2,
            hw_cpu_threads=4,
            architecture="x86_64",
            name="Image1",
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
            os_hash_value="7f8bababc2c2a948",
            id="image_1",
            signatureValue="f8bababc2c2a948807473837504760432b99a3dac81629da77142328a9f638fe34371f",
            hashAlgorithm="SHA-224",
            signatureAlgorithm="ECC-CURVES",
            properties={
                "image_build_date": "2023-12-01",
                "hotfix_hours": "0",
                "image_description": "Image 1",
                "provided_until": "none",
                "replace_frequency": "monthly",
                "uuid_validity": "last-3",
                "patchlevel": "1.5.2",
            },
        ),
        OS_Image(
            hw_scsi_model="virtio - scsi",
            os_distro="windows",
            hw_watchdog_action="reset",
            hw_rng_model="virtio",
            os_version="Stable",
            hypervisor_type="qemu",
            hw_video_ram=20,
            hw_vif_multiqueue_enabled=True,
            hw_pmu=False,
            hw_firmware_type="bios",
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
            properties={
                "image_build_date": "2023-11-01",
                "hotfix_hours": "4",
                "image_description": "Image 2",
                "provided_until": "none",
                "replace_frequency": "weekly",
                "uuid_validity": "last-3",
                "license_required": True,
                "license_included": False,
                "subscription_required": True,
                "subscription_included": False,
                "maintained_until": datetime.strptime("2024-05-31", "%Y-%m-%d"),
            },
        ),
    ]


class VMImageDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        cur_dir = os.getcwd()
        if cur_dir.endswith("tests"):
            path = cur_dir[0:-5] + "/config/config.yaml"
        else:
            path = cur_dir + "/config/config.yaml"
        with open(path, "r") as config_file:
            self.config = yaml.safe_load(config_file)
            self.discovery = ImageDiscovery(
                conn=MockConnection(_get_os_images()), config=self.config
            )

    def test_discovery_vm_images(self):
        actual_gax_images = self.discovery.discover()
        expected_gax_images = _get_gx_images()

        self.assertEqual(len(expected_gax_images), len(expected_gax_images))

        for image_1 in actual_gax_images:
            for image_2 in expected_gax_images:
                if image_1.gx_id == image_2.gx_id:
                    self.check_vm_image(image_1.gx_object, image_2.gx_object)

    def test_json_ld(self):
        cur_dir = os.getcwd()
        if cur_dir.endswith("tests"):
            shacl_file = cur_dir + "/gaia-x.shacl.ttl"
        else:
            shacl_file = cur_dir + "/tests/gaia-x.shacl.ttl"

        conforms, _, _ = validate(
            data_graph=json.dumps(_get_gx_images()[0], indent=4, default=to_json_ld),
            shacl_graph=shacl_file,
            data_graph_format="json-ld",
            shacl_graph_format="ttl",
        )

        self.assertTrue(conforms)


if __name__ == "__main__":
    unittest.main()
