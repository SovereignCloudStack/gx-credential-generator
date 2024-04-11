import unittest
from pathlib import Path
from typing import List

import yaml
from openstack.compute.v2.flavor import Flavor as OS_Flavor
from openstack.image.v2.image import Image as OS_Image

from generator.common.config import Config
from generator.common.gx_schema import (CPU, GPU, CheckSum, CodeArtifact,
                                        Device, Disk, Encryption, GaiaXEntity,
                                        Hypervisor, Image,
                                        InstantiationRequirement, Memory,
                                        OperatingSystem, Resource,
                                        ServerFlavor, Signature,
                                        SoftwareResource, VirtualResource,
                                        VMImage)


def get_absolute_path(relative_path: str) -> str:
    current_dir = Path(__file__).parent
    if current_dir.name == "tests":
        return str(Path(current_dir.parent, relative_path))
    else:
        return str(Path(current_dir, relative_path))


def get_config() -> Config:
    with open(get_absolute_path("config/config.yaml"), "r") as config_file:
        return Config(yaml.safe_load(config_file))


class OpenstackTestcase(unittest.TestCase):

    def assert_gaia_x_entity(self, ob_1: GaiaXEntity, ob_2: GaiaXEntity):
        self.assertEqual(ob_1.name, ob_2.name, "GaiaXEntity.name")
        self.assertEqual(ob_1.description, ob_2.description, "GaiaXEntity.description")

    def assert_resource(self, ob_1: Resource, ob_2: Resource):
        self.assertEqual(
            ob_1.aggregationOfResources,
            ob_2.aggregationOfResources,
            "Resource.aggregationOf",
        )

    def assert_virtual_resource(self, ob_1: VirtualResource, ob_2: VirtualResource):
        self.assert_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.copyrightOwnedBy,
            ob_2.copyrightOwnedBy,
            "VirtualResource.copyrightOwnedBy",
        )
        self.assertEqual(ob_1.license, ob_2.license, "VirtualResource.license")
        self.assertEqual(
            ob_1.resourcePolicy, ob_2.resourcePolicy, "VirtualResource.resourcePolicy"
        )

    def assert_software_resource(self, ob_1: SoftwareResource, ob_2: SoftwareResource):
        self.assert_virtual_resource(ob_1, ob_2)
        if ob_1.checksum:
            self.assert_checksum(ob_1.checksum, ob_2.checksum)
        if ob_1.signature:
            self.assert_signature(ob_1.signature, ob_2.signature)
        self.assertEqual(ob_1.version, ob_2.version, "SoftwareResource.version")
        self.assertEqual(
            ob_1.patchLevel, ob_2.patchLevel, "SoftwareResource.patchLevel"
        )
        self.assertEqual(ob_1.buildDate, ob_2.buildDate, "SoftwareResource.buildDate")

    def assert_checksum(self, ob_1: CheckSum, ob_2: CheckSum):
        self.assertEqual(
            ob_1.checkSumCalculation,
            ob_2.checkSumCalculation,
            "Checksum.checkSumCalculation",
        )
        self.assertEqual(
            ob_1.checkSumValue, ob_2.checkSumValue, "Checksum.checkSumValue"
        )

    def assert_signature(self, ob_1: Signature, ob_2: Signature):
        self.assertEqual(
            ob_1.signatureValue, ob_2.signatureValue, "Signature.signatureValue"
        )
        self.assertEqual(
            ob_1.signatureAlgorithm,
            ob_2.signatureAlgorithm,
            "Signature.signatureAlgorithm",
        )
        self.assertEqual(
            ob_1.hashAlgorithm, ob_2.hashAlgorithm, "Signature.hashAlgorithm"
        )

    def assert_encryption(self, ob_1: Encryption, ob_2: Encryption):
        self.assertEqual(ob_1.cipher, ob_2.cipher, "Encryption.cipher")
        self.assertEqual(
            ob_1.keyManagement, ob_2.keyManagement, "Encryption.keyManagement"
        )

    def assert_operating_system(self, ob_1: OperatingSystem, ob_2: OperatingSystem):
        self.assert_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.osDistribution, ob_2.osDistribution, "OperatingSystem.osDistribution"
        )

    def assert_hypervisor(self, ob_1: Hypervisor, ob_2: Hypervisor):
        self.assert_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.hypervisorType, ob_2.hypervisorType, "Hypervisor.hypervisorType"
        )

    def assert_device(self, ob_1: Device, ob_2: Device):
        self.assertEqual(ob_1.vendor, ob_2.vendor, "Device.vendor")
        self.assertEqual(ob_1.generation, ob_2.generation, "Device.generation")
        self.assertEqual(
            ob_1.defaultOversubscriptionRatio,
            ob_2.defaultOversubscriptionRatio,
            "Device.defaultOversubscriptionRatio",
        )
        self.assertEqual(
            ob_1.supportedOversubscriptionRatio,
            ob_2.supportedOversubscriptionRatio,
            "Device.supportedOversubscriptionRatio",
        )

    def assert_disk(self, ob_1: Disk, ob_2: Disk):
        self.assertEqual(
            ob_1.diskSize.value, ob_2.diskSize.value, "Disk.diskSize.value"
        )
        self.assertEqual(ob_1.diskSize.unit, ob_2.diskSize.unit, "Disk.diskSize.unit")
        self.assertEqual(ob_1.diskType, ob_2.diskType, "Disk.diskType")
        self.assertEqual(ob_1.diskBusType, ob_2.diskBusType, "Disk.diskBusType")

    def assert_cpu(self, ob_1: CPU, ob_2: CPU):
        self.assertEqual(
            ob_1.cpuArchitecture, ob_2.cpuArchitecture, "CPU.cpuArchitecture"
        )
        self.assertEqual(ob_1.cpuFlag, ob_2.cpuFlag, "CPU.cpuFlag")
        self.assertEqual(ob_1.smtEnabled, ob_2.smtEnabled, "CPU.smtEnabled")
        self.assertEqual(ob_1.numberOfCores, ob_2.numberOfCores, "CPU.numberOfCores")
        self.assertEqual(
            ob_1.numberOfThreads, ob_2.numberOfThreads, "CPU.numberOfThreads"
        )
        self.assertEqual(ob_1.baseFrequency, ob_2.baseFrequency, "CPU.baseFrequency")
        self.assertEqual(ob_1.boostFrequency, ob_2.boostFrequency, "CPU.boostFrequency")
        self.assertEqual(
            ob_1.lastLevelCacheSize, ob_2.lastLevelCacheSize, "CPU.lastLevelCacheSize"
        )
        self.assertEqual(
            ob_1.thermalDesignPower, ob_2.thermalDesignPower, "CPU.thermalDesignPower"
        )

    def assert_gpu(self, ob_1: GPU, ob_2: GPU):
        pass

    def assert_mem(self, ob_1: Memory, ob_2: Memory):
        self.assertEqual(
            ob_1.memorySize.value, ob_2.memorySize.value, "Memory.memorySize.value"
        )
        self.assertEqual(
            ob_1.memorySize.unit, ob_2.memorySize.unit, "Memory.memorySize.unit"
        )
        self.assertEqual(ob_1.memoryClass, ob_2.memoryClass, "Memory.memoryClass")
        self.assertEqual(ob_1.memoryRank, ob_2.memoryRank, "Memory.memoryRank")
        self.assertEqual(ob_1.eccEnabled, ob_2.eccEnabled, "Memory.eccEnabled")
        self.assertEqual(
            ob_1.hardwareEncryption,
            ob_2.hardwareEncryption,
            "Memory.hardwareEncryption",
        )

    def assert_code_artifact(self, ob_1: CodeArtifact, ob_2: CodeArtifact):
        self.assert_gaia_x_entity(ob_1, ob_2)

    def assert_image(self, ob_1: Image, ob_2: Image):
        self.assert_code_artifact(ob_1, ob_1)
        self.assertEqual(ob_1.fileSize, ob_2.fileSize, "Image.fileSize")
        if ob_1.operatingSystem is None:
            self.assertIsNone(ob_2.operatingSystem)
        else:
            self.assertIsNotNone(ob_2.operatingSystem)
            self.assert_operating_system(ob_1.operatingSystem, ob_2.operatingSystem)
        if ob_1.cpuReq:
            self.assert_cpu(ob_1.cpuReq, ob_2.cpuReq)
        if ob_1.gpuReq:
            self.assert_gpu(ob_1.gpuReq, ob_2.gpuReq)
        if ob_1.ramReq:
            self.assert_mem(ob_1.ramReq, ob_2.ramReq)
        if ob_1.videoRamSize:
            self.assertEqual(
                ob_1.videoRamSize.value, ob_2.videoRamSize.value, "VideoRamSize.value"
            )
            self.assertEqual(
                ob_1.videoRamSize.unit, ob_2.videoRamSize.unit, "VideoRamSize.unit"
            )
        if ob_1.encryption:
            self.assert_encryption(ob_1.encryption, ob_2.encryption)
        if ob_1.checksum:
            self.assert_checksum(ob_1.checksum, ob_2.checksum)

        self.assertEqual(ob_1.secureBoot, ob_2.secureBoot, "Image.secureBoot")
        self.assertEqual(ob_1.vPMU, ob_2.vPMU, "Image.vPMU")
        self.assertEqual(ob_1.multiQueues, ob_2.multiQueues, "Image.multiQueues")

        if ob_1.updateStrategy:
            self.assertEqual(
                ob_1.updateStrategy.replaceFrequency,
                ob_2.updateStrategy.replaceFrequency,
                "Image.updateStrategy.replaceFrequency",
            )
            self.assertEqual(
                ob_1.updateStrategy.hotfixHours,
                ob_2.updateStrategy.hotfixHours,
                "Image.updateStrategy.hotfixHours",
            )
            self.assertEqual(
                ob_1.updateStrategy.oldVersionsValidUntil,
                ob_2.updateStrategy.oldVersionsValidUntil,
                "Image.updateStrategy.oldVersionsValidUntil",
            )
            self.assertEqual(
                ob_1.updateStrategy.providedUntil,
                ob_2.updateStrategy.providedUntil,
                "Image.updateStrategy.providedUntil",
            )

        self.assertEqual(
            ob_1.licenseIncluded, ob_2.licenseIncluded, "Image.licenseIncluded"
        )
        self.assertEqual(ob_1.maintenance, ob_2.maintenance, "Image.maintenance")

    def assert_vm_image(self, exp: VMImage, act: VMImage):
        self.assert_image(exp, act)
        self.assertEqual(
            exp.vmImageDiskFormat, act.vmImageDiskFormat, "VM_Image.vmImageDiskFormat"
        )
        self.assertEqual(
            exp.hypervisorType, act.hypervisorType, "VM_Image.hypervisorType"
        )
        self.assertEqual(exp.firmwareType, act.firmwareType, "VM_Image.firmwareType")
        self.assertEqual(
            exp.hwRngTypeOfImage, act.hwRngTypeOfImage, "VM_Image.hwRngTypeOfImage"
        )

    def check_instantiation_requirement(
            self, ob_1: InstantiationRequirement, ob_2: InstantiationRequirement
    ):
        self.assert_gaia_x_entity(ob_1, ob_2)

    def check_hypervisor(self, ob_1: Hypervisor, ob_2: Hypervisor):
        self.assert_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.hypervisorType, str(ob_2.hypervisorType), "Hypervisor.hypervisorType")

    def assert_flavor(self, ob_1: ServerFlavor, ob_2: ServerFlavor):
        # self.check_installation_requirement(ob_1, ob_2)
        self.assert_cpu(ob_1.cpu, ob_2.cpu)
        self.assert_mem(ob_1.ram, ob_2.ram)
        self.assert_gpu(ob_1.gpu, ob_2.gpu)
        self.assert_disk(ob_1.bootVolume, ob_2.bootVolume)
        self.assertEqual(
            len(ob_1.additionalVolume),
            len(ob_2.additionalVolume),
            "ServerFlavor.additionalVolume",
        )
        if ob_1.hypervisor:
            self.check_hypervisor(ob_1.hypervisor, ob_2.hypervisor)
        if ob_1.confidentialComputing:
            self.assertEqual(
                ob_1.confidentialComputing,
                str(ob_2.confidentialComputing),
                "ServerFlavor.confidentialComputing",
            )
        self.assertEqual(
            ob_1.hardwareAssistedVirtualization,
            ob_2.hardwareAssistedVirtualization,
            "ServerFlavor.hardwareAssistedVirtualization",
        )
        self.assertEqual(
            ob_1.hwRngTypeOfFlavor,
            ob_2.hwRngTypeOfFlavor,
            "ServerFlavor.hwRngTypeOfFlavor",
        )

        for i in range(9, len(ob_1.additionalVolume) - 1):
            self.assert_disk(ob_1.additionalVolume[i], ob_2.additionalVolume[i])


class MockConnection:
    """
    Wrap connection to OpenStack Cluster
    """

    def __init__(self, images: List[OS_Image] = None, flavors: List[OS_Flavor] = None):
        self.images = images or []
        self.flavors = flavors or []

    def list_images(self) -> List[OS_Image]:
        return self.images

    def list_flavors(self) -> List[OS_Flavor]:
        return self.flavors

    def authorize(self):
        pass
