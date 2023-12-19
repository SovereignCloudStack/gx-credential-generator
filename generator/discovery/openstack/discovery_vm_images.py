import typing

from generator.common.gx_schema import Architectures as cpu_arch_types
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Disk
from generator.common.gx_schema import Memory
from generator.common.gx_schema import MemorySize
from generator.common.gx_schema import OperatingSystem
from generator.common.gx_schema import VMImage as GX_Image

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

        # collect all properties
        cpu_req = self._get_cpu_req(os_image.architecture)
        ram_req = self._get_min_ram_req(os_image.min_ram)
        root_disk_req = self._get_min_disk_req(os_image.min_disk)
        operatingSystem = self._get_operation_system_info(os_image.os_version, os_image.os_distro)

        #license = operatingSystem.license
        #copyright_owner = operatingSystem.copyrightOwnedBy
        #resource_policy= const.DEFAULT_RESOURCE_POLICY

        # read mandatory attributes from config or use default values
        try:
            license = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_LICENSE]
        except KeyError:
            pass
        try:
            copyright_owner = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_COPYRIGHT]
        except KeyError:
            pass
        try:
            resource_policy = self.config[const.CONFIG_VM_IMAGE][os_image.name][const.CONFIG_RESOURCE_POLICY]
        except KeyError:
            pass

        #return GX_Image(copyrightOwnedBy=copyright_owner,
        #                license=license,
        #                resourcePolicy=resource_policy,
        #                cpuReq=cpu_req,
        #                ramReq=ram_req,
        #                rootDiskReq=root_disk_req,
        #                operatingSystem=operatingSystem,
        #                version=os_image.os_version)#

    @staticmethod
    def _get_cpu_req(arch: str) -> CPU:
        if arch == "i686":
            return CPU(cpuArchitecture="x86-32")
        if arch in ["x86_64", "ia64"]:
            return CPU(cpuArchitecture="x86-64")
        if arch == "aarch6":
            return CPU(cpuArchitecture="AArch-32")
        if arch in ["alpha", "armv7l", "lm32", "openrisc", "parisc", "parisc64", "unicore32"]:
            return CPU(cpuArchitecture="RISC-V")
        return CPU(cpuArchitecture=cpu_arch_types.other)

    @staticmethod
    def _get_min_ram_req(min_ram_size: str) -> Memory:
        # Memory size tend to be measured in MB (1,000,000 bytes) and not MiB (1.048576 bytes) the RAM industry.
        # But OpenStack uses MiB.
        size = MemorySize(value=float(min_ram_size * 1.048576), unit=const.UNIT_MB)
        return Memory(memorySize=size)

    @staticmethod
    def _get_min_disk_req(disk_size: str) -> Disk:
        size = MemorySize(value=float(disk_size * 1.073741824), unit=const.UNIT_GB)
        return Disk(diskSize=size)

    def _get_operation_system_info(self, os_version: str, os_distro: str) -> OperatingSystem:
        # Copyright owner and license not supported as Image properties, currently --> Default values are used
        if os_distro == "arch":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_ARCH,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ARCH),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ARCH),
                                   license=self._get_license(const.CONFIG_OS_ARCH))
        if os_distro == "centos":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_CENTOS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CENTOS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_CENTOS),
                                   license=self._get_license(const.CONFIG_OS_CENTOS))
        if os_distro == "debian":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_DEBIAN,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_DEBIAN),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_DEBIAN),
                                   license=self._get_license(const.CONFIG_OS_DEBIAN))
        if os_distro == "fedora":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_FEDORA,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_FEDORA),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_FEDORA),
                                   license=self._get_license(const.CONFIG_OS_FEDORA))
        if os_distro == "freebsd":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_FREEBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_FREEBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_FREEBSD),
                                   license=self._get_license(const.CONFIG_OS_FREEBSD))
        if os_distro == "gentoo":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_GENTOO,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_GENTOO),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_GENTOO),
                                   license=self._get_license(const.CONFIG_OS_GENTOO))
        if os_distro == "mandrake":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_MANDRAKE,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MANDRAKE),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MANDRAKE),
                                   license=self._get_license(const.CONFIG_OS_MANDRAKE))
        if os_distro == "mandriva":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_MANDRIVA,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MANDRIVA),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MANDRIVA),
                                   license=self._get_license(const.CONFIG_OS_MANDRIVA))
        if os_distro == "mes":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_MES,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MES),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MES),
                                   license=self._get_license(const.CONFIG_OS_MES))
        if os_distro == "msdos":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_MSDOS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_MSDOS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_MSDOS),
                                   license=self._get_license(const.CONFIG_OS_MSDOS))
        if os_distro == "netbsd":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_NETBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NETBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_NETBSD),
                                   license=self._get_license(const.CONFIG_OS_NETBSD))
        if os_distro == "netware":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_NOVELL,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_NOVELL),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_NOVELL),
                                   license=self._get_license(const.CONFIG_OS_NOVELL))
        if os_distro == "openbsd":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_OPENBSD,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_OPENBSD),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_OPENBSD),
                                   license=self._get_license(const.CONFIG_OS_OPENBSD))
        if os_distro == "opensolaris":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_SOLARIS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_SOLARIS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_SOLARIS),
                                   license=self._get_license(const.CONFIG_OS_SOLARIS))
        if os_distro == "opensuse":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_OPEN_SUSE,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_OPEN_SUSE),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_OPEN_SUSE),
                                   license=self._get_license(const.CONFIG_OS_OPEN_SUSE))
        if os_distro == "rocky":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_ROCKY,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ROCKY),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ROCKY),
                                   license=self._get_license(const.CONFIG_OS_ROCKY))
        if os_distro == "rhel":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_RHEL,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_RHEL),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_RHEL),
                                   license=self._get_license(const.CONFIG_OS_RHEL))
        if os_distro == "sled":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_SLED,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_SLED),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_SLED),
                                   license=self._get_license(const.CONFIG_OS_SLED))
        if os_distro == "ubuntu":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_UBUNTU,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_UBUNTU),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_UBUNTU),
                                   license=self._get_license(const.CONFIG_OS_UBUNTU))
        if os_distro == "windows":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_WINDOWS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_WINDOWS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_WINDOWS),
                                   license=self._get_license(const.CONFIG_OS_WINDOWS))
        if os_distro == "cirros":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_CIRROS,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_CIRROS),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_CIRROS),
                                   license=self._get_license(const.CONFIG_OS_CIRROS))
        if os_distro == "almalinux":
            return OperatingSystem(version=os_version, osDistribution=const.CONFIG_OS_ALMALINUX,
                                   resourcePolicy=self._get_resource_policy(const.CONFIG_OS_ALMALINUX),
                                   copyrightOwnedBy=self._get_copyrightowner(const.CONFIG_OS_ALMALINUX),
                                   license=self._get_license(const.CONFIG_OS_ALMALINUX))

        raise ValueError("Unsupported value for operating system distribution found: '" + os_distro + "'")

    def _get_resource_policy(self, os: str) -> str:
        policy = self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_RESOURCE_POLICY]
        if policy == "DEFAULT":
            return const.DEFAULT_RESOURCE_POLICY
        else:
            return policy

    def _get_copyrightowner(self, os: str) -> str:
        return self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_COPYRIGHT]

    def _get_license(self, os: str) -> str:
        return self.config[const.CONFIG_VM_IMAGE][os][const.CONFIG_LICENSE]







