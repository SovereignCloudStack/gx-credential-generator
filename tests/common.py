import unittest
from typing import List

from openstack.compute.v2.flavor import Flavor as OS_Flavor
from openstack.image.v2.image import Image as OS_Image

from generator.common.gx_schema import (CPU, GPU, CheckSum, CodeArtifact,
                                        Device, Disk, Encryption, GaiaXEntity,
                                        Hypervisor, Image,
                                        InstantiationRequirement, Memory,
                                        OperatingSystem, Resource,
                                        ServerFlavor, Signature,
                                        SoftwareResource, VirtualResource,
                                        VMImage)
from generator.common.json_ld import JsonLdObject


class OpenstackTestcase(unittest.TestCase):
    def get_jsonobject_by_id(
        self, id: str, objects: List[JsonLdObject]
    ) -> JsonLdObject:
        """
        Return for JSON LD object with given id in given list.
        @param id: id of JSON LD object to be returned
        @type id: str
        @param objects: list of JSON LD objects
        @type objects: List[JsonLdObject]
        @return: JSON LD object with given id if any, else None
        @rtype JsonLdObject
        """
        for o in objects:
            if o.gx_id == id:
                return o

    def check_gaia_x_entity(self, ob_1: GaiaXEntity, ob_2: GaiaXEntity):
        self.assertEqual(ob_1.name, ob_2.name, "GaiaXEntity.name")
        self.assertEqual(ob_1.description, ob_2.description, "GaiaXEntity.description")

    def check_resource(self, ob_1: Resource, ob_2: Resource):
        self.assertEqual(
            ob_1.aggregationOfResources,
            ob_2.aggregationOfResources,
            "Resource.aggregationOf",
        )

    def check_virtual_resource(self, ob_1: VirtualResource, ob_2: VirtualResource):
        self.check_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.copyrightOwnedBy,
            ob_2.copyrightOwnedBy,
            "VirtualResource.copyrightOwnedBy",
        )
        self.assertEqual(ob_1.license, ob_2.license, "VirtualResource.license")
        self.assertEqual(
            ob_1.resourcePolicy, ob_2.resourcePolicy, "VirtualResource.resourcePolicy"
        )

    def check_software_resource(self, ob_1: SoftwareResource, ob_2: SoftwareResource):
        self.check_virtual_resource(ob_1, ob_2)
        if ob_1.checksum:
            self.check_checksum(ob_1.checksum, ob_2.checksum)
        if ob_1.signature:
            self.check_signature(ob_1.signature, ob_2.signature)
        self.assertEqual(ob_1.version, ob_2.version, "SoftwareResource.version")
        self.assertEqual(
            ob_1.patchLevel, ob_2.patchLevel, "SoftwareResource.patchLevel"
        )
        self.assertEqual(ob_1.buildDate, ob_2.buildDate, "SoftwareResource.buildDate")

    def check_checksum(self, ob_1: CheckSum, ob_2: CheckSum):
        self.assertEqual(
            ob_1.checkSumCalculation,
            ob_2.checkSumCalculation,
            "Checksum.checkSumCalculation",
        )
        self.assertEqual(
            ob_1.checkSumValue, ob_2.checkSumValue, "Checksum.checkSumValue"
        )

    def check_signature(self, ob_1: Signature, ob_2: Signature):
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

    def check_encryption(self, ob_1: Encryption, ob_2: Encryption):
        self.assertEqual(ob_1.cipher, ob_2.cipher, "Encryption.cipher")
        self.assertEqual(
            ob_1.keyManagement, ob_2.keyManagement, "Encryption.keyManagement"
        )

    def check_operating_system(self, ob_1: OperatingSystem, ob_2: OperatingSystem):
        self.check_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.osDistribution, ob_2.osDistribution, "OperatingSystem.osDistribution"
        )

    def check_hypervisor(self, ob_1: Hypervisor, ob_2: Hypervisor):
        self.check_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.hypervisorType, ob_2.hypervisorType, "Hypervisor.hypervisorType"
        )

    def check_device(self, ob_1: Device, ob_2: Device):
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

    def check_disk(self, ob_1: Disk, ob_2: Disk):
        self.assertEqual(
            ob_1.diskSize.value, ob_2.diskSize.value, "Disk.diskSize.value"
        )
        self.assertEqual(ob_1.diskSize.unit, ob_2.diskSize.unit, "Disk.diskSize.unit")
        self.assertEqual(ob_1.diskType, ob_2.diskType, "Disk.diskType")
        self.assertEqual(ob_1.diskBusType, ob_2.diskBusType, "Disk.diskBusType")

    def check_cpu(self, ob_1: CPU, ob_2: CPU):
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

    def check_gpu(self, ob_1: GPU, ob_2: GPU):
        pass

    def check_mem(self, ob_1: Memory, ob_2: Memory):
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

    def check_code_artifact(self, ob_1: CodeArtifact, ob_2: CodeArtifact):
        self.check_gaia_x_entity(ob_1, ob_2)

    def check_image(self, ob_1: Image, ob_2: Image):
        self.check_code_artifact(ob_1, ob_1)
        self.assertEqual(ob_1.fileSize, ob_2.fileSize, "Image.fileSize")
        if ob_1.operatingSystem:
            self.check_operating_system(ob_1.operatingSystem, ob_2.operatingSystem)
        if ob_1.cpuReq:
            self.check_cpu(ob_1.cpuReq, ob_2.cpuReq)
        if ob_1.gpuReq:
            self.check_gpu(ob_1.gpuReq, ob_2.gpuReq)
        if ob_1.ramReq:
            self.check_mem(ob_1.ramReq, ob_2.ramReq)
        if ob_1.videoRamSize:
            self.assertEqual(
                ob_1.videoRamSize.value, ob_2.videoRamSize.value, "VideoRamSize.value"
            )
            self.assertEqual(
                ob_1.videoRamSize.unit, ob_2.videoRamSize.unit, "VideoRamSize.unit"
            )

        if ob_1.encryption:
            self.check_encryption(ob_1.encryption, ob_2.encryption)
        if ob_1.checksum:
            self.check_checksum(ob_1.checksum, ob_2.checksum)

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

    def check_vm_image(self, ob_1: VMImage, ob_2: VMImage):
        self.check_image(ob_1, ob_2)
        self.assertEqual(
            ob_1.vmImageDiskFormat,
            str(ob_2.vmImageDiskFormat),
            "VM_Image.vmImageDiskFormat",
        )
        self.assertEqual(
            ob_1.hypervisorType, str(ob_2.hypervisorType), "VM_Image.hypervisorType"
        )
        self.assertEqual(
            ob_1.firmwareType, str(ob_2.firmwareType), "VM_Image.firmwareType"
        )
        self.assertEqual(
            ob_1.hwRngTypeOfImage,
            str(ob_2.hwRngTypeOfImage),
            "VM_Image.hwRngTypeOfImage",
        )
        self.assertEqual(
            ob_1.watchDogAction, str(ob_2.watchDogAction), "VM_Image.watchDogAction"
        )

    def check_installation_requirement(
        self, ob_1: InstantiationRequirement, ob_2: InstantiationRequirement
    ):
        self.check_gaia_x_entity(ob_1, ob_2)

    def check_hypervisor(self, ob_1: Hypervisor, ob_2: Hypervisor):
        self.check_software_resource(ob_1, ob_2)
        self.assertEqual(
            ob_1.hypervisorType, str(ob_2.hypervisorType), "Hypervisor.hypervisorType"
        )

    def check_flavor(self, ob_1: ServerFlavor, ob_2: ServerFlavor):
        # self.check_installation_requirement(ob_1, ob_2)
        self.check_cpu(ob_1.cpu, ob_2.cpu)
        self.check_mem(ob_1.ram, ob_2.ram)
        self.check_gpu(ob_1.gpu, ob_2.gpu)
        self.check_disk(ob_1.bootVolume, ob_2.bootVolume)
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
            self.check_disk(ob_1.additionalVolume[i], ob_2.additionalVolume[i])


class MockConnection:
    """
    Wrap connection to OpenStack Cluster
    """

    images = []
    flavors = []

    def __init__(self, images: List[OS_Image] = None, flavors: List[OS_Flavor] = None):
        self.images = images
        self.flavors = flavors

    def list_images(self):
        return self.images

    def list_flavors(self):
        return self.flavors
