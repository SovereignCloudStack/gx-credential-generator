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


class VmDiscovery():

    def __init__(self, conn: Connection) -> None:
        self.conn = conn


    #def collect_vm_images(self, conn: Connection) -> List[str]:
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
        Converts image properties coming from Openstack to Gaia-X Credential compliant VM image.
        @param os_image: Openstack image properties
        @return: Gaia-X compliant virtual machine image
        """

        # collect all properties
        cpu_req = self._get_cpu_req(os_image.architecture)
        ram_req = self._get_min_ram_req(os_image.min_ram)
        root_disk_req = self._get_min_disk_req(os_image.min_disk)

        return GX_Image(copyrightOwnedBy='TBA',
                        license="TBA",
                        resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                        cpuReq=cpu_req,
                        ramReq=ram_req,
                        rootDiskReq=root_disk_req,
                        version=os_image.os_version)

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
        size = MemorySize(value = float(min_ram_size * 1.048576), unit=const.UNIT_MB)
        return Memory(memorySize = size)

    @staticmethod
    def _get_min_disk_req(disk_size: str) -> Disk:
        size = MemorySize(value = float(disk_size * 1.073741824), unit=const.UNIT_GB)
        return Disk(diskSize = size)


    def _get_operation_system(os_version: str, os_distro: str) -> OperatingSystem:
        if os_distro == "arch":
            return OperatingSystem(version=os_version, os_distro="Arch Linux")
        if os_distro == "centos":
            return OperatingSystem(version=os_version, os_distro="CentOS Linux")

