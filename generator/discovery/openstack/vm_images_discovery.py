from linkml_runtime.utils.metamodelcore import URI

from generator.common.expections import MissingMandatoryAttribute

from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import CheckSum
from generator.common.gx_schema import ChecksumAlgorithm
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Disk
from generator.common.gx_schema import Memory
from generator.common.gx_schema import MemorySize
from generator.common.gx_schema import OperatingSystem
from generator.common.gx_schema import Signature
from generator.common.gx_schema import SignatureAlgorithm
from generator.common.gx_schema import SPDX
from generator.common.gx_schema import UpdateStrategy
from generator.common.gx_schema import VMImage as GX_Image

from generator.common.json_ld import JsonLdObject

from openstack.connection import Connection
from openstack.image.v2.image import Image as OS_Image

import generator.common.const as const

from typing import Dict, Union, List

from datetime import datetime


# TODO:; Check imag meta dafta props standard, ob dort klar ist, das einige Properties uer properties stehhen und nicht direkt abgefrgat werden klnnen mur iber propeertiues[metadfate}
class VmDiscovery():

    # def __init__(self) -> None:
    #    with open("config/config.yaml", "r") as config_file:
    #        self.config = yaml.safe_load(config_file)

    def __init__(self, conn: Connection, config: Dict) -> None:
        self.conn = conn
        self.config = config

    # def collect_vm_images(self, conn: Connection) -> List[str]:
    def discover_vm_images(self) -> List[JsonLdObject]:
        """
        Return one credential for each VM image provided by openstack cloud.

        @return: list of VM images
        @rtype: list[JsonLdObject]
        """
        images = list()
        for image in self.conn.list_images():
            images.append(
                JsonLdObject(
                    self._convert_to_gx_image(image), gx_id=image.id))
        return images

    def _convert_to_gx_image(self, os_image: OS_Image) -> GX_Image:
        """
        Convert Openstack image to a Gaia-X virtual machine image.
        @param os_image: Openstack image properties
        @type os_image: OS_Image
        @return: Gaia-X virtual machine image
        @rtype GX_Image
        """

        # Initialize Gaia-X Image
        gx_image = GX_Image(copyrightOwnedBy="TBA",
                            license="TBA",
                            resourcePolicy=const.DEFAULT_RESOURCE_POLICY)

        # Discover optional attributes
        self._add_secure_boot(os_image, gx_image)
        self._add_firmeware_type(os_image, gx_image)
        self._add_watchdog_action(os_image, gx_image)
        self._add_vmpu(os_image, gx_image)
        self._add_video_ram(os_image, gx_image)
        self._add_multiqueue_enabled(os_image, gx_image)
        self._add_update_strategy(os_image, gx_image)
        self._add_name(os_image, gx_image)
        self._add_description(os_image, gx_image)
        self._add_cpu_req(os_image, gx_image)
        self._add_min_ram_req(os_image, gx_image)
        self._add_min_disk_req(os_image, gx_image)
        self._add_operation_system_info(os_image, gx_image)
        self._add_build_date(os_image, gx_image)
        self._add_license_included(os_image, gx_image)
        self._add_patch_level(os_image, gx_image)
        self._add_version(os_image, gx_image)
        self._add_checksum(os_image, gx_image)
        self._add_signature(os_image, gx_image)

        # Discover mandatory attribute
        self._add_license(os_image, gx_image)
        self._add_copyrigthowner(os_image, gx_image)
        self._add_resource_policy(os_image, gx_image)

        return gx_image

    @staticmethod
    def _add_cpu_req(os_image: OS_Image, gx_image: GX_Image) -> None:
        if os_image.architecture == "i686":
            gx_image.cpuReq = CPU(cpuArchitecture="x86-32")
        elif os_image.architecture in ["x86_64", "ia64"]:
            gx_image.cpuReq = CPU(cpuArchitecture="x86-64")
        elif os_image.architecture == "aarch6":
            gx_image.cpuReq = CPU(cpuArchitecture="AArch-32")
        elif os_image.architecture in ["alpha", "armv7l", "lm32", "openrisc", "parisc", "parisc64", "unicore32"]:
            gx_image.cpuReq = CPU(cpuArchitecture="RISC-V")
        else:
            gx_image.cpuReq = CPU(cpuArchitecture=CpuArch.other)

    @staticmethod
    def _add_min_ram_req(os_image: OS_Image, gx_image: GX_Image) -> None:
        # Memory size tend to be measured in MB (1,000,000 bytes) and not MiB (1.048576 bytes) the RAM industry.
        # But OpenStack uses MiB.
        try:
            size = MemorySize(value=float(os_image.min_ram * 1.048576), unit=const.UNIT_MB)
            mem_req = Memory(memorySize=size)
            try:
                mem_req.hardwareEncryption = os_image.hw_mem_encryption
            except AttributeError:
                pass
            gx_image.ramReq = mem_req
        except AttributeError as e:
            raise MissingMandatoryAttribute(e.args)

    @staticmethod
    def _add_min_disk_req(image: OS_Image, gx_image: GX_Image) -> None:
        try:
            size = MemorySize(value=float(image.min_disk * 1.073741824), unit=const.UNIT_GB)
            gx_image.rootDiskReq = Disk(diskSize=size, diskBusType=image.hw_disk_bus)
        except AttributeError as e:
            raise MissingMandatoryAttribute(e.args)

    def _add_operation_system_info(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # Copyright owner and license not supported as Image properties, currently --> Default values from config are used

        if os_image.os_distro == "arch":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_ARCH,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ARCH),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ARCH),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_ARCH)))
        elif os_image.os_distro == "centos":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_CENTOS,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CENTOS),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_CENTOS),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_CENTOS)))
        elif os_image.os_distro == "debian":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_DEBIAN,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_DEBIAN),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_DEBIAN),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_DEBIAN)))
        elif os_image.os_distro == "fedora":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_FEDORA,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_FEDORA),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_FEDORA),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_FEDORA)))
        elif os_image.os_distro == "freebsd":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_FREEBSD,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_FREEBSD),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_FREEBSD),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_FREEBSD)))
        elif os_image.os_distro == "gentoo":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_GENTOO,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_GENTOO),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_GENTOO),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_GENTOO)))
        elif os_image.os_distro == "mandrake":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_MANDRAKE,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_MANDRAKE),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_MANDRAKE),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_MANDRAKE)))
        elif os_image.os_distro == "mandriva":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_MANDRIVA,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_MANDRIVA),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_MANDRIVA),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_MANDRIVA)))
        elif os_image.os_distro == "mes":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_MES,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MES),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MES),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_MES)))
        elif os_image.os_distro == "msdos":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_MSDOS,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MSDOS),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MSDOS),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_MSDOS)))
        elif os_image.os_distro == "netbsd":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_NETBSD,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NETBSD),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_NETBSD),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_NETBSD)))
        elif os_image.os_distro == "netware":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_NOVELL,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NOVELL),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_NOVELL),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_NOVELL)))
        elif os_image.os_distro == "openbsd":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_OPENBSD,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_OPENBSD),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_OPENBSD),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_OPENBSD)))
        elif os_image.os_distro == "opensolaris":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_SOLARIS,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_SOLARIS),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_SOLARIS),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_SOLARIS)))
        elif os_image.os_distro == "opensuse":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_OPEN_SUSE,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_OPEN_SUSE),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_OPEN_SUSE),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_OPEN_SUSE)))
        elif os_image.os_distro == "rocky":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_ROCKY,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ROCKY),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ROCKY),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_ROCKY)))
        elif os_image.os_distro == "rhel":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_RHEL,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_RHEL),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_RHEL),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_RHEL)))
        elif os_image.os_distro == "sled":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_SLED,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_SLED),
                                                       copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_SLED),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_SLED)))
        elif os_image.os_distro == "ubuntu":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_UBUNTU,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_UBUNTU),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_UBUNTU),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_UBUNTU)))
        elif os_image.os_distro == "windows":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_WINDOWS,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_WINDOWS),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_WINDOWS),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_WINDOWS)))
        elif os_image.os_distro == "cirros":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_CIRROS,
                                                       resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CIRROS),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_CIRROS),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_CIRROS)))
        elif os_image.os_distro == "almalinux":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version,
                                                       osDistribution=const.CONFIG_OS_ALMALINUX,
                                                       resourcePolicy=self._get_resource_policy(
                                                           const.CONFIG_OS_ALMALINUX),
                                                       copyrightOwnedBy=self._get_copyrightowner(
                                                           const.CONFIG_OS_ALMALINUX),
                                                       license=self._get_license(
                                                           self._get_license_from_config(const.CONFIG_OS_ALMALINUX)))
        else:
            raise ValueError("Unsupported value for operating system distribution found: '" + os_image.os_distro + "'")

    def _get_resource_policy(self, os: str) -> str:
        policy = self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_RESOURCE_POLICY]
        if policy == "DEFAULT":
            return const.DEFAULT_RESOURCE_POLICY
        else:
            return policy

    def _get_copyrightowner(self, os: str) -> str:
        return self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_COPYRIGHT]

    def _add_copyrigthowner(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.copyrightOwnedBy = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_COPYRIGHT]
        except KeyError:
            gx_image.copyrightOwnedBy = gx_image.operatingSystem.copyrightOwnedBy

    def _add_license(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            for license in self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_LICENSE]:
                gx_image.license.append(URI(license))
        except KeyError:
            gx_image.license = gx_image.operatingSystem.license

    def _add_resource_policy(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            gx_image.resourcePolicy = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_RESOURCE_POLICY]
        except KeyError:
            gx_image.resourcePolicy = [const.DEFAULT_RESOURCE_POLICY]

    def _get_license_from_config(self, os: str) -> str:
        return self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_LICENSE]

    @staticmethod
    def _get_license(licenses: List[str]) -> List[Union[str, SPDX]]:
        license_list = list()

        for l in licenses:
            if l.startswith("http"):
                license_list.append(URI(l))
            else:
                license_list.append(l)
        return license_list

    @staticmethod
    def _add_secure_boot(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.needs_secure_boot:
                return
            gx_image.secureBoot = os_image.needs_secure_boot
        except AttributeError:
            pass

    @staticmethod
    def _add_firmeware_type(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_firmware_type:
                return
            gx_image.firmwareType = os_image.hw_firmware_type
        except AttributeError:
            gx_image.firmwareType = const.DEFAULT_FIRMWARE_TYPE

    @staticmethod
    def _add_watchdog_action(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_watchdog_action:
                return
            gx_image.watchDogAction = os_image.hw_watchdog_action
        except AttributeError:
            pass

    @staticmethod
    def _add_vmpu(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_pmu:
                return
            gx_image.vPMU = os_image.hw_pmu
        except AttributeError:
            pass

    @staticmethod
    def _add_video_ram(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_video_ram:
                return
            gx_image.videoRamSize = MemorySize(value=float(os_image.hw_video_ram))
        except AttributeError:
            pass

    @staticmethod
    def _add_multiqueue_enabled(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_vif_multiqueue_enabled:
                return
            gx_image.multiQueues = os_image.hw_vif_multiqueue_enabled
        except AttributeError:
            pass

    @staticmethod
    def _add_update_strategy(os_image: OS_Image, gx_image: GX_Image) -> None:
        os_image.updateStrategy = UpdateStrategy()

        # collect mandatory attributes
        try:
            os_image.updateStrategy.replaceFrequency = os_image.properties['replace_frequency']
            os_image.updateStrategy.oldVersionsValidUntil = os_image.properties['uuid_validity']
            os_image.updateStrategy.providedUntil = os_image.properties['provided_until']
        except KeyError as e:
            raise MissingMandatoryAttribute(e.args)

        # collect optional attributes
        try:
            os_image.updateStrategy.hotfixHours = os_image.properties['hotfix_hours']
        except KeyError:
            pass

    @staticmethod
    def _add_description(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.description = os_image.properties[
                'image_description']
        except KeyError:
            pass
        try:
            gx_image.description = gx_image.description + " Managed by " + os_image.properties[
                'managed_by_VENDOR']
        except KeyError:
            pass

    @staticmethod
    def _add_name(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.name:
                return
            gx_image.name = os_image.name
        except KeyError:
            pass

    @staticmethod
    def _add_build_date(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.buildDate = datetime.strptime(os_image.properties['image_build_date'], "%Y-%m-%d")
        except KeyError:
            pass

    @staticmethod
    def _add_license_included(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.licenseIncluded = os_image.properties['licenseIncluded']
        except KeyError:
            pass

    @staticmethod
    def _add_patch_level(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.patchLevel = os_image.properties['patchlevel']
        except KeyError:
            pass

    @staticmethod
    def _add_version(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.version = os_image.properties['internal_version']
        except KeyError:
            pass

    @staticmethod
    def _add_checksum(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            algo = VmDiscovery._get_checksum_algo(os_image.hash_algo)
            value = os_image.hash_value
            gx_image.checksum = CheckSum(checkSumValue=value, checkSumCalculation=algo)
        except AttributeError:
            pass

    @staticmethod
    def _get_checksum_algo(algo: str) -> str:
        if algo == 'sha512':
            return 'sha-512'
        if algo == 'sha224':
            return 'sha-224'
        if algo == 'sha256':
            return 'sha-256'
        if algo == 'sha384':
            return 'sha-384'
        if algo in ['sha-3', 'md5', 'ripemd-160', 'blake2', 'blake3']:
            return algo
        return ChecksumAlgorithm.other

    @staticmethod
    def _add_maintenance_until(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.maintenance = os_image.properties['maintained_until']
        except KeyError:
            pass

    @staticmethod
    def _add_file_size(os_image: OS_Image, gx_image: GX_Image) -> None:
        gx_image.file = MemorySize(value=float(os_image.size * 1.073741824), unit=const.UNIT_GB)

    def _add_signature(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.signature = Signature(
                signatureValue=os_image.img_signature,
                hashAlgorithm=self._get_checksum_algo(os_image.img_signature_hash_method),
                signatureAlgorithm=self._get_signature_algo(os_image.img_signature_key_type))
        except AttributeError:
            pass

    @staticmethod
    def _get_signature_algo(algo: str) -> str:
        if algo.startswith("SHA-"):
            return "RSA-Signature"
        return SignatureAlgorithm.other

    def _add_aggregation_of(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        pass
        # ToDo: add aggrenation of
