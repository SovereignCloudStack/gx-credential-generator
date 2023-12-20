import typing

from generator.common.gx_schema import Architectures as cpu_arch_types
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Disk
from generator.common.gx_schema import Memory
from generator.common.gx_schema import MemorySize
from generator.common.gx_schema import OperatingSystem
from generator.common.gx_schema import UpdateStrategy
from generator.common.gx_schema import UpdateFrequency
from generator.common.gx_schema import VMImage as GX_Image

from generator.common.exceptions import MissingMandatoryAttribute

from openstack.connection import Connection
from openstack.image.v2.image import Image as OS_Image
from typing import List

import generator.common.const as const

from typing import Dict


class VmDiscovery():

    def __init__(self, conn: Connection, config: Dict) -> None:
        self.conn = conn
        self.config = config

    # def collect_vm_images(self, conn: Connection) -> List[str]:
    def discover_vm_images(self) -> List[GX_Image]:
        """
        Return one credential for each VM image provided by openstack cloud accessible via given CONNECTION.

        @param conn: Connection to openstack cloud VM images are to be collected
        @return: list of VM images
        """

        images = list()
        for image in self.conn.list_images():
            self._convert_to_gx_image(image)

        return images

    def _convert_to_gx_image(self, os_image: OS_Image) -> GX_Image:
        """
        Converts Openstack image to a Gaia-X virtual machine image.
        @param os_image: Openstack image properties
        @return: Gaia-X virtual machine image
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
            gx_image.cpuReq = CPU(cpuArchitecture=cpu_arch_types.other)

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
        # Copyright owner and license not supported as Image properties, currently --> Default values are used
        if os_image.os_distro == "arch":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_ARCH,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ARCH),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ARCH),
                                   license=self._get_license(const.CONFIG_OS_ARCH))
        elif os_image.os_distro == "centos":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_CENTOS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CENTOS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_CENTOS),
                                   license=self._get_license(const.CONFIG_OS_CENTOS))
        elif os_image.os_distro == "debian":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_DEBIAN,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_DEBIAN),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_DEBIAN),
                                   license=self._get_license(const.CONFIG_OS_DEBIAN))
        elif os_image.os_distro == "fedora":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_FEDORA,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_FEDORA),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_FEDORA),
                                   license=self._get_license(const.CONFIG_OS_FEDORA))
        elif os_image.os_distro == "freebsd":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_FREEBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_FREEBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_FREEBSD),
                                   license=self._get_license(const.CONFIG_OS_FREEBSD))
        elif os_image.os_distro == "gentoo":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_GENTOO,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_GENTOO),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_GENTOO),
                                   license=self._get_license(const.CONFIG_OS_GENTOO))
        elif os_image.os_distro == "mandrake":
            gx_image.operatingSystem = OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_MANDRAKE,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MANDRAKE),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MANDRAKE),
                                   license=self._get_license(const.CONFIG_OS_MANDRAKE))
        elif os_image.os_distro == "mandriva":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_MANDRIVA,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MANDRIVA),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MANDRIVA),
                                   license=self._get_license(const.CONFIG_OS_MANDRIVA))
        elif os_image.os_distro == "mes":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_MES,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MES),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MES),
                                   license=self._get_license(const.CONFIG_OS_MES))
        elif os_image.os_distro == "msdos":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_MSDOS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MSDOS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MSDOS),
                                   license=self._get_license(const.CONFIG_OS_MSDOS))
        elif os_image.os_distro == "netbsd":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_NETBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NETBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_NETBSD),
                                   license=self._get_license(const.CONFIG_OS_NETBSD))
        elif os_image.os_distro == "netware":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_NOVELL,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NOVELL),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_NOVELL),
                                   license=self._get_license(const.CONFIG_OS_NOVELL))
        elif os_image.os_distro == "openbsd":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_OPENBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_OPENBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_OPENBSD),
                                   license=self._get_license(const.CONFIG_OS_OPENBSD))
        elif os_image.os_distro == "opensolaris":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_SOLARIS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_SOLARIS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_SOLARIS),
                                   license=self._get_license(const.CONFIG_OS_SOLARIS))
        elif os_image.os_distro == "opensuse":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_OPEN_SUSE,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_OPEN_SUSE),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_OPEN_SUSE),
                                   license=self._get_license(const.CONFIG_OS_OPEN_SUSE))
        elif os_image.os_distro == "rocky":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_ROCKY,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ROCKY),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ROCKY),
                                   license=self._get_license(const.CONFIG_OS_ROCKY))
        elif os_image.os_distro == "rhel":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_RHEL,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_RHEL),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_RHEL),
                                   license=self._get_license(const.CONFIG_OS_RHEL))
        elif os_image.os_distro == "sled":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_SLED,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_SLED),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_SLED),
                                   license=self._get_license(const.CONFIG_OS_SLED))
        elif os_image.os_distro == "ubuntu":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_UBUNTU,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_UBUNTU),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_UBUNTU),
                                   license=self._get_license(const.CONFIG_OS_UBUNTU))
        elif os_image.os_distro == "windows":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_WINDOWS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_WINDOWS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_WINDOWS),
                                   license=self._get_license(const.CONFIG_OS_WINDOWS))
        elif os_image.os_distro == "cirros":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_CIRROS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CIRROS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_CIRROS),
                                   license=self._get_license(const.CONFIG_OS_CIRROS))
        elif os_image.os_distro == "almalinux":
            gx_image.operatingSystem =  OperatingSystem(version=os_image.os_version, osDistribution=const.CONFIG_OS_ALMALINUX,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ALMALINUX),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ALMALINUX),
                                   license=self._get_license(const.CONFIG_OS_ALMALINUX))
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
            gx_image.license = gx_image.operatingSystem.copyrightOwnedBy

    def _add_license(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            gx_image.license = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_LICENSE]
        except KeyError:
            gx_image.license = gx_image.operatingSystem.license
    def _add_resource_policy(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            gx_image.rresource_policy = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_RESOURCE_POLICY]
        except KeyError:
            gx_image.rresource_policy = const.DEFAULT_RESOURCE_POLICY

    def _get_license(self, os: str) -> str:
        return self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_LICENSE]

    def _add_secure_boot(self, os_image: OS_Image, gx_image:GX_Image) -> None:
        try:
            if not os_image.needs_secure_boot:
                return
            gx_image.secureBoot = os_image.needs_secure_boot
        except AttributeError:
            pass

    def _add_firmeware_type(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_firmware_type:
                return
            gx_image.firmwareType = os_image.hw_firmware_type
        except AttributeError:
            gx_image.firmwareType = const.DEFAULT_FIRMWARE_TYPE

    def _add_watchdog_action(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_watchdog_action:
                return
            gx_image.watchDogAction = os_image.hw_watchdog_action
        except AttributeError:
            pass

    def _add_vmpu(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.hw_pmu:
                return
            gx_image.vPMU = os_image.hw_pmu
        except AttributeError:
            pass

    def _add_video_ram(self, os_image: OS_Image, gx_image:GX_Image) -> None:
        try:
            if not os_image.hw_video_ram:
                return
            gx_image.videoRamSize = MemorySize(value=float(os_image.hw_video_ram))
        except AttributeError:
            pass

    def _add_multiqueue_enabled(self, os_image: OS_Image, gx_image:GX_Image) -> None:
        try:
            if not os_image.hw_vif_multiqueue_enabled:
                return
            gx_image.multiQueues = os_image.hw_vif_multiqueue_enabled
        except AttributeError:
            pass

    def _add_update_strategy(self, os_image: OS_Image, gx_image: GX_Image) -> None:
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

    def _add_description(self, os_image: OS_Image, gx_image: GX_Image) -> None:
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

    def _add_name(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            if not os_image.name:
                return
            gx_image.name = os_image.name
        except KeyError:
            pass

    def _add_build_date(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.buildDate = os_image.properties['image_build_date']
        except KeyError:
            pass

    @staticmethod
    def _add_license_included(os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.licenseIncluded = os_image.properties['licenseIncluded']
        except KeyError:
            gx_image.licenseIncluded = False


    # ToDo: add aggrenation of
