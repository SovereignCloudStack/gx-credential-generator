"""Discovery for properties of virtual machine images.
"""
from datetime import datetime
from typing import List, Union

from linkml_runtime.utils.metamodelcore import URI
from openstack.connection import Connection
from openstack.image.v2.image import Image as OS_Image

import generator.common.const as const
from generator.common.config import Config
from generator.common.gx_schema import CPU, SPDX
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (CheckSum, ChecksumAlgorithm, Disk,
                                        DiskBusType, FirmType, HypervisorType,
                                        LatestN, MaintenanceSubscription,
                                        Memory, MemorySize, OperatingSystem,
                                        OSDistribution, RNGTypes, Signature,
                                        SignatureAlgorithm, UpdateFrequency,
                                        UpdateStrategy, Validity1, Validity2,
                                        VMDiskType)
from generator.common.gx_schema import VMImage as GX_Image
from generator.common.gx_schema import WatchDogActions

VALID_UNTIL_LOOKUP = {
    "none": Validity1.none.text,
    "notice": Validity1.notice.text,
    "forever": Validity2.forever.text,
}

ARCH_LOOKUP = {
    "i686": "x86-32",
    "x86_64": "x86-64",
    "ia64": "x86-64",
    "aarch6": "AArch-32",
    "alpha": "RISC-V",
    "armv7l": "RISC-V",
    "lm32": "RISC-V",
    "openrisc": "RISC-V",
    "parisc": "RISC-V",
    "parisc64": "RISC-V",
    "unicore32": "RISC-V",
}

DISK_BUS_LOOKUP = {
    "sata": DiskBusType.SATA,
    "pata": DiskBusType.PATA,
    "scsi": DiskBusType.SCSI,
    "sas": DiskBusType.SAS,
    "nvme": DiskBusType.NVMe,
}

DISK_LOOKUP = {
    "raw": VMDiskType.RAW,
    "qcow2": VMDiskType.QCOW2,
    "vhd": VMDiskType.VHD,
    "iso": VMDiskType.ISO,
    "cvf": VMDiskType.CVF,
    "cva": VMDiskType.CVA,
}

FIRM_WARE_LOOKUP = {"bios": FirmType.BIOS, "uefi": FirmType.UEFI}

WATCH_DOG_LOOKUP = {
    "disabled": WatchDogActions.disabled,
    "reset": WatchDogActions.reset,
    "poweroff": WatchDogActions.poweroff,
    "pause": WatchDogActions.pause,
}

HASH_ALGO_LOOKUP = {
    "sha512": "sha-512",
    "sha224": "sha-224",
    "sha256": "sha-256",
    "sha384": "sha-384",
    "sha-3": "sha-3",
    "md5": "md5",
    "ripemd-160": "ripemd-160",
    "blake2": ChecksumAlgorithm.blake2,
    "blake3": ChecksumAlgorithm.blake3,
}
HYPER_LOOKUP = {
    "xen": HypervisorType.Xen,
    "quemu": HypervisorType.quemu,
    "hyperv": "Hyper - V",
    "kvm": HypervisorType.KVM,
    "esxi": HypervisorType.ESXi,
}

PROVIDED_UNTIL_LOOKUP = {"none": Validity1.none.text, "notice": Validity1.notice.text}

UPDATE_STRATEGY_LOOKUP = {
    "yearly": UpdateFrequency.yearly,
    "monthly": UpdateFrequency.monthly,
    "weekly": UpdateFrequency.weekly,
    "daily": UpdateFrequency.daily,
    "never": UpdateFrequency.never,
    "critical_bug": "critical_bug",
}


class VmImageDiscovery:
    """Discover VM image properties."""

    def __init__(self, conn: Connection, conf: Config) -> None:
        """
        Constructor.
        @param conn: Openstack Connection
        @param conf: configuration
        """
        self.conn = conn
        self.conf = conf

    # def collect_vm_images(self, conn: Connection) -> List[str]:
    def discover(self) -> List[GX_Image]:
        """
        Return one credential for each public VM image offered by openstack cloud.

        @return: list of VM images
        """
        images = []
        for image in self.conn.list_images():
            if image.visibility == "public":
                images.append(self._convert_to_gx_image(image))
        return images

    def _convert_to_gx_image(self, os_image: OS_Image) -> GX_Image:
        """
        Convert Openstack image to a Gaia-X virtual machine image.

        @param os_image: Openstack image properties
        @return: Gaia-X virtual machine image
        """

        # Initialize Gaia-X Image
        gx_image = GX_Image(
            copyrightOwnedBy="TBA",
            license="TBA",
            resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
        )

        # Discover optional attributes
        gx_image.vmImageDiskFormat = self._get_disk_format(os_image)
        gx_image.secureBoot = self._get_secure_boot(os_image)
        gx_image.firmwareType = self._get_firmware_type(os_image)
        gx_image.watchDogAction = self._get_watchdog_action(os_image)
        gx_image.vPMU = self._get_hw_pmu(os_image)
        gx_image.cpuReq = self._get_cpu_req(os_image)
        gx_image.multiQueues = self._get_multiqueue_enabled(os_image)
        gx_image.checksum = self._get_checksum(os_image)
        gx_image.hwRngTypeOfImage = self._get_rng_model(os_image)
        gx_image.videoRamSize = self._get_video_ram_size(os_image)
        gx_image.file_size = self._get_file_size(os_image)
        gx_image.updateStrategy = self._get_update_strategy(os_image)
        gx_image.description = self._get_description(os_image)
        gx_image.name = self._get_name(os_image)
        gx_image.ramReq = self._get_min_ram_req(os_image)
        gx_image.rootDiskReq = self._get_min_disk_req(os_image)
        os = self._get_operation_system(os_image)
        if os is not None:
            gx_image.operatingSystem = os
        gx_image.buildDate = self._get_build_date(os_image)
        gx_image.licenseIncluded = self._get_license_included(os_image)
        gx_image.patchLevel = self._get_patch_level(os_image)
        gx_image.version = self._get_version(os_image)
        gx_image.maintenance = self._get_maintenance(os_image)
        gx_image.signature = self._get_signature(os_image)
        gx_image.hypervisorType = self._get_hypervisor_type(os_image)

        # Discover mandatory attribute
        self._add_license(os_image, gx_image)
        self._add_copyright_owner(os_image, gx_image)
        self._add_resource_policy(os_image, gx_image)

        return gx_image

    @staticmethod
    def _get_disk_format(os_image: OS_Image) -> VMDiskType:
        if os_image.disk_format is not None:
            return VMDiskType(
                DISK_LOOKUP.get(os_image.disk_format.lower(), VMDiskType.RAW)
            )
        return VMDiskType(VMDiskType.RAW)

    @staticmethod
    def _get_secure_boot(os_image: OS_Image) -> bool:
        return bool(os_image.needs_secure_boot)

    @staticmethod
    def _get_firmware_type(os_image: OS_Image) -> FirmType:
        if (
                os_image.properties is not None and "hw_firmware_type" in os_image.properties
        ):
            return FirmType(
                FIRM_WARE_LOOKUP.get(
                    os_image.properties["hw_firmware_type"].lower(), FirmType.other
                )
            )
        else:
            return FirmType(FirmType.other)

    @staticmethod
    def _get_watchdog_action(os_image: OS_Image) -> WatchDogActions:
        if os_image.hw_watchdog_action is not None:
            return WatchDogActions(
                WATCH_DOG_LOOKUP.get(
                    os_image.hw_watchdog_action.lower(), WatchDogActions.disabled
                )
            )
        return WatchDogActions(WatchDogActions.disabled)

    @staticmethod
    def _get_hw_pmu(os_image: OS_Image) -> bool:
        if os_image.properties and "hw_pmu" in os_image.properties:
            return bool(os_image.properties["hw_pmu"])
        else:
            return False

    @staticmethod
    def _get_cpu_req(os_image: OS_Image) -> CPU:
        cpu = CPU(
            cpuArchitecture=CpuArch(
                ARCH_LOOKUP.get(os_image.architecture, CpuArch.Other)
            )
        )

        if hasattr(os_image, "hw_cpu_cores"):
            cpu.numberOfCores = os_image.hw_cpu_cores
        if hasattr(os_image, "hw_cpu_threads"):
            cpu.numberOfThreads = os_image.hw_cpu_threads
        return cpu

    @staticmethod
    def _get_multiqueue_enabled(os_image: OS_Image) -> bool:
        return bool(os_image.is_hw_vif_multiqueue_enabled)

    @staticmethod
    def _get_file_size(os_image: OS_Image) -> MemorySize:
        if os_image.size is not None:
            return MemorySize(
                value=float(os_image.size * 1.073741824), unit=const.UNIT_GB
            )

    @staticmethod
    def _get_checksum(os_image: OS_Image) -> CheckSum:
        if os_image.hash_value is not None:
            return CheckSum(
                checkSumValue=os_image.hash_value,
                checkSumCalculation=ChecksumAlgorithm(
                    HASH_ALGO_LOOKUP.get(
                        os_image.hash_algo.lower(), ChecksumAlgorithm.other
                    )
                ),
            )

    @staticmethod
    def _get_rng_model(os_image: OS_Image) -> RNGTypes:
        return RNGTypes("None")

    @staticmethod
    def _get_min_ram_req(os_image: OS_Image) -> Memory:
        if os_image.min_ram is not None:
            # Memory size tend to be measured in MB (1,000,000 bytes) and not MiB (1.048576 bytes) the RAM industry.
            # But OpenStack uses MiB.
            mem = Memory(
                memorySize=MemorySize(
                    value=float(os_image.min_ram * 1.048576), unit=const.UNIT_MB
                )
            )
            if os_image.properties and "hw_mem_encryption" in os_image.properties:
                mem.hardwareEncryption = os_image.properties["hw_mem_encryption"]
            return mem

    @staticmethod
    def _get_min_disk_req(os_image: OS_Image) -> Disk:
        if os_image.min_disk is not None:
            disk = Disk(
                diskSize=MemorySize(
                    value=float(os_image.min_disk * 1.073741824), unit=const.UNIT_GB
                )
            )
            if os_image.hw_disk_bus:
                disk.diskBusType = DiskBusType(
                    DISK_BUS_LOOKUP.get(os_image.hw_disk_bus.lower(), "other")
                )
            else:
                disk.diskBusType = DiskBusType("other")
            return disk

    def _get_operation_system(self, os_image: OS_Image) -> OperatingSystem:
        # Copyright owner and license not supported as Image properties, currently --> Default values from config are used
        if os_image.os_distro is None:
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=OSDistribution.others,
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="TBA",
                license="https://www.example.com/tba")

        if os_image.os_distro.lower() == "arch":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_ARCH,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_ARCH),
                copyrightOwnedBy=self._get_copyright_owner_for_os(const.CONFIG_OS_ARCH),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_ARCH)
                ),
            )
        elif os_image.os_distro.lower() == "centos":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_CENTOS,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_CENTOS),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_CENTOS
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_CENTOS)
                ),
            )
        elif os_image.os_distro.lower() == "debian":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_DEBIAN,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_DEBIAN),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_DEBIAN
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_DEBIAN)
                ),
            )
        elif os_image.os_distro.lower() == "fedora":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_FEDORA,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_FEDORA),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_FEDORA
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_FEDORA)
                ),
            )
        elif os_image.os_distro.lower() == "freebsd":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_FREEBSD,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_FREEBSD
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_FREEBSD
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_FREEBSD)
                ),
            )
        elif os_image.os_distro.lower() == "gentoo":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_GENTOO,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_GENTOO),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_GENTOO
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_GENTOO)
                ),
            )
        elif os_image.os_distro.lower() == "mandrake":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_MANDRAKE,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_MANDRAKE
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_MANDRAKE
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_MANDRAKE)
                ),
            )
        elif os_image.os_distro.lower() == "mandriva":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_MANDRIVA,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_MANDRIVA
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_MANDRIVA
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_MANDRIVA)
                ),
            )
        elif os_image.os_distro.lower() == "mes":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_MES,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_MES),
                copyrightOwnedBy=self._get_copyright_owner_for_os(const.CONFIG_OS_MES),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_MES)
                ),
            )
        elif os_image.os_distro.lower() == "msdos":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_MSDOS,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_MSDOS),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_MSDOS
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_MSDOS)
                ),
            )
        elif os_image.os_distro.lower() == "netbsd":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_NETBSD,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_NETBSD),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_NETBSD
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_NETBSD)
                ),
            )
        elif os_image.os_distro.lower() == "netware":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_NOVELL,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_NOVELL),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_NOVELL
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_NOVELL)
                ),
            )
        elif os_image.os_distro.lower() == "openbsd":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_OPENBSD,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_OPENBSD
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_OPENBSD
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_OPENBSD)
                ),
            )
        elif os_image.os_distro.lower() == "opensolaris":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_SOLARIS,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_SOLARIS
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_SOLARIS
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_SOLARIS)
                ),
            )
        elif os_image.os_distro.lower() == "opensuse":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_OPEN_SUSE,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_OPEN_SUSE
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_OPEN_SUSE
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_OPEN_SUSE)
                ),
            )
        elif os_image.os_distro.lower() == "suse":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_SUSE,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_SUSE),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_OPEN_SUSE
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_SUSE)
                ),
            )
        elif os_image.os_distro.lower() == "rocky":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_ROCKY,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_ROCKY),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_ROCKY
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_ROCKY)
                ),
            )
        elif os_image.os_distro.lower() == "rhel":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_RHEL,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_RHEL),
                copyrightOwnedBy=self._get_copyright_owner_for_os(const.CONFIG_OS_RHEL),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_RHEL)
                ),
            )
        # sled not yet supported by Gaia-X
        # elif os_image.os_distro.lower() == "sled":
        #    return OperatingSystem(
        #        version=os_image.os_version,
        #        osDistribution=const.CONFIG_OS_SLED,
        #        resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_SLED),
        #        copyrightOwnedBy=self._get_copyright_owner_for_os(const.CONFIG_OS_SLED),
        #        license=self._get_license_list(
        #            self._get_license_for_os(const.CONFIG_OS_SLED)
        #        ),
        #    )
        elif os_image.os_distro.lower() == "ubuntu":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_UBUNTU,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_UBUNTU),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_UBUNTU
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_UBUNTU)
                ),
            )
        elif os_image.os_distro.lower() == "windows":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_WINDOWS,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_WINDOWS
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_WINDOWS
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_WINDOWS)
                ),
            )
        elif os_image.os_distro.lower() == "cirros":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_CIRROS,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_CIRROS),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_CIRROS
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_CIRROS)
                ),
            )
        elif os_image.os_distro.lower() == "almalinux":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_ALMA_LINUX,
                resourcePolicy=self._get_resource_policy_for_os(
                    const.CONFIG_OS_ALMA_LINUX
                ),
                copyrightOwnedBy=self._get_copyright_owner_for_os(
                    const.CONFIG_OS_ALMA_LINUX
                ),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_ALMA_LINUX)
                ),
            )
        elif os_image.os_distro.lower() == "alpinelinux":
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution=const.CONFIG_OS_ALP,
                resourcePolicy=self._get_resource_policy_for_os(const.CONFIG_OS_ALP),
                copyrightOwnedBy=self._get_copyright_owner_for_os(const.CONFIG_OS_ALP),
                license=self._get_license_list(
                    self._get_license_for_os(const.CONFIG_OS_ALP)
                ),
            )
        else:
            return OperatingSystem(
                version=os_image.os_version,
                osDistribution="others",
                resourcePolicy=const.DEFAULT_RESOURCE_POLICY,
                copyrightOwnedBy="TBA",
                license="TBA",
            )

    def _get_resource_policy_for_os(self, os: str) -> str:
        return self.conf.get_value(
            [
                const.CONFIG_SOFTWARE,
                os,
                const.CONFIG_RESOURCE_POLICY,
            ]
        )

    def _get_copyright_owner_for_os(self, os: str) -> List[str]:
        return self.conf.get_value(
            [
                const.CONFIG_SOFTWARE,
                os,
                const.CONFIG_COPYRIGHT,
            ]
        )

    def _get_license_for_os(self, os: str) -> List[str]:
        return self.conf.get_value(
            [
                const.CONFIG_SOFTWARE,
                os,
                const.CONFIG_LICENSE,
            ]
        )

    def _add_copyright_owner(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        try:
            gx_image.copyrightOwnedBy = self.conf.get_value(
                [
                    const.CONFIG_CLOUD_RESOURCES,
                    const.CONFIG_OWN_IMAGES,
                    os_image.name,
                    const.CONFIG_COPYRIGHT,
                ]
            )
        except KeyError:
            # copyright owner not found in config, use default one
            gx_image.copyrightOwnedBy = gx_image.operatingSystem.copyrightOwnedBy

    def _add_license(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            # config contains image's specific license
            gx_image.license = self.conf.get_value(
                [
                    const.CONFIG_CLOUD_RESOURCES,
                    const.CONFIG_OWN_IMAGES,
                    os_image.name,
                    const.CONFIG_LICENSE,
                ]
            )
        except KeyError:
            # license owner not found in config, use default one
            gx_image.license = gx_image.operatingSystem.license

    def _add_resource_policy(self, os_image: OS_Image, gx_image: GX_Image) -> None:
        # read mandatory attributes from config or use default values
        try:
            # check if comfig contains image's specific resource policy
            gx_image.resourcePolicy = self.conf.get_value(
                [
                    const.CONFIG_CLOUD_RESOURCES,
                    const.CONFIG_OWN_IMAGES,
                    os_image.name,
                    const.CONFIG_RESOURCE_POLICY,
                ]
            )
        except KeyError:
            # license owner not found in config, use default one
            gx_image.resourcePolicy = const.DEFAULT_RESOURCE_POLICY

    @staticmethod
    def _get_license_list(licenses: List[str]) -> List[Union[str, SPDX]]:
        license_list = list()
        for lic in licenses:
            if lic.startswith("http"):
                license_list.append(URI(lic))
            else:
                license_list.append(lic)
        return license_list

    @staticmethod
    def _get_video_ram_size(os_image: OS_Image) -> MemorySize:
        if os_image.hw_video_ram is not None:
            return MemorySize(value=float(os_image.hw_video_ram), unit=const.UNIT_MB)

    @staticmethod
    def _get_update_strategy(os_image: OS_Image) -> UpdateStrategy:
        if os_image.properties is not None:
            update_strategy = UpdateStrategy()
            if "replace_frequency" in os_image.properties:
                rep_freq = UPDATE_STRATEGY_LOOKUP.get(
                    os_image.properties["replace_frequency"]
                )
                if rep_freq is not None:
                    update_strategy.replaceFrequency = UpdateFrequency(rep_freq)
            if "uuid_validity" in os_image.properties:
                old_version = os_image.properties["uuid_validity"]
                if old_version.lower().startswith("latest-"):
                    # latest N old version will be provided
                    latest = int(old_version.split("-")[1])
                    update_strategy.oldVersionsValidUntil = LatestN(value=latest)
                else:
                    try:
                        # is date provided?
                        update_strategy.oldVersionsValidUntil = datetime.strptime(
                            old_version, "%Y-%m-%d"
                        ).date()
                    except ValueError:
                        # no date provided, try to lookup
                        update_strategy.oldVersionsValidUntil = VALID_UNTIL_LOOKUP.get(
                            old_version
                        )
            if "provided_until" in os_image.properties:
                provided_until = str(os_image.properties["provided_until"])
                try:
                    # is date provided?
                    update_strategy.providedUntil = datetime.strptime(provided_until, "%Y-%m-%d").date()
                except ValueError:
                    update_strategy.providedUntil = PROVIDED_UNTIL_LOOKUP.get(
                        provided_until
                    )
            else:
                update_strategy.providedUntil = None
            if "hotfix_hours" in os_image.properties and os_image.properties["hotfix_hours"]:
                try:
                    hot_h = int(os_image.properties["hotfix_hours"])
                    if hot_h >= 0:
                        update_strategy.hotfixHours = int(
                            os_image.properties["hotfix_hours"]
                        )
                except ValueError:
                    # int cast fails
                    pass
            return update_strategy

    @staticmethod
    def _get_description(os_image: OS_Image) -> str:
        if (
                os_image.properties is not None and "image_description" in os_image.properties
        ):
            if "managed_by_VENDOR" in os_image.properties:
                return (os_image.properties["image_description"] + " Managed by " + os_image.properties[
                    "managed_by_VENDOR"])
            else:
                return os_image.properties["image_description"]

    @staticmethod
    def _get_name(os_image: OS_Image) -> str:
        return os_image.name or None

    @staticmethod
    def _get_build_date(os_image: OS_Image) -> datetime:
        if (
                os_image.properties is not None and "image_build_date" in os_image.properties
        ):
            return datetime.strptime(
                os_image.properties["image_build_date"], "%Y-%m-%d"
            )

    @staticmethod
    def _get_license_included(os_image: OS_Image) -> bool:
        return os_image.properties and os_image.properties.get("licenseIncluded", False)

    @staticmethod
    def _get_patch_level(os_image: OS_Image) -> str:
        return os_image.properties and os_image.properties.get("patchlevel", None)

    @staticmethod
    def _get_version(os_image: OS_Image) -> str:
        return os_image.properties and os_image.properties.get("internal_version", None)

    @staticmethod
    def _get_maintenance(os_image: OS_Image) -> MaintenanceSubscription:
        maint = MaintenanceSubscription(
            subscriptionRequired=False, subscriptionIncluded=False
        )
        maint.subscriptionIncluded = bool(
            os_image.properties and os_image.properties.get("subscription_included", None)
        )
        maint.subscriptionRequired = bool(
            os_image.properties and os_image.properties.get("subscription_required", None)
        )
        if (
                os_image.properties is not None and "maintained_until" in os_image.properties
        ):
            main_until = os_image.properties["maintained_until"]
            maint.maintainedUntil = datetime.strptime(main_until, "%Y-%m-%d").date()
        return maint

    @staticmethod
    def _get_signature(os_image: OS_Image) -> Signature:
        if os_image.properties is not None and "img_signature" in os_image.properties:
            value = os_image.properties["img_signature"]
            hash_algo = ChecksumAlgorithm(
                HASH_ALGO_LOOKUP.get(
                    os_image.properties["img_signature_hash_method"].lower(),
                    ChecksumAlgorithm.other,
                )
            )
            sig_algo = SignatureAlgorithm.other
            if os_image.properties["img_signature_key_type"].lower().startswith("sha-"):
                sig_algo = "RSA-Signature"
            return Signature(
                signatureValue=value,
                hashAlgorithm=hash_algo,
                signatureAlgorithm=sig_algo,
            )

    @staticmethod
    def _get_hypervisor_type(os_image: OS_Image) -> HypervisorType:
        if os_image.hypervisor_type is not None:
            return HypervisorType(HYPER_LOOKUP.get(os_image.hypervisor_type.lower(), HypervisorType.other))
        else:
            return HypervisorType(HypervisorType.other)
