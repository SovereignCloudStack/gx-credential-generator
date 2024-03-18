#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# images_discovery.py
"""Script to discovery server flavor properties.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

import re
from typing import Dict, List, Tuple

from openstack.compute.v2.flavor import Flavor as OS_Flavor
from openstack.connection import Connection

from generator.common import common, const
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (Disk, DiskBusType, DiskType, Frequency,
                                        Hypervisor, Memory, MemorySize,
                                        PermissibleValue)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.common.json_ld import JsonLdObject


class ServerFlavorDiscovery:
    # def __init__(self) -> None:
    #    with open("config/config.yaml", "r") as config_file:
    #        self.config = yaml.safe_load(config_file)

    def __init__(self, conn: Connection, config: Dict) -> None:
        self.conn = conn
        self.config = config

    def discover(self) -> List[JsonLdObject]:
        """
        Return one JsonLdObject for each public server flavor discovery at openstack cloud.

        @return: list of public server flavors
        @rtype: list[JsonLdObject]
        """
        flavors = list()
        for fl in self.conn.list_flavors():
            if fl.is_public:
                flavors.append(JsonLdObject(self._convert_to_gx(fl), gx_id=fl.id))
        return flavors

    def _convert_to_gx(self, os_flavor: OS_Flavor) -> GX_Flavor:
        """
        Convert Openstack flavor to Gaia-X server flavor.
        @param os_flavor: Openstack server flavor specification
        @type os_flavor: Flavor
        @return: Gaia-X server flavor specification
        @rtype ServerFlavor
        """

        # Initialize Gaia-X Server Flavor
        disks = self._get_disks(os_flavor)
        gx_flavor = GX_Flavor(
            # name=os_flavor.name,
            cpu=self._get_cpu(os_flavor),
            ram=self._get_ram(os_flavor),
            bootVolume=disks[0],
        )

        if len(disks) > 1:
            gx_flavor.additionalVolume = additionalVolume = disks[1:]

        # Discover optional attributes
        self._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self._add_description(os_flavor, gx_flavor)

        return gx_flavor

    def _get_cpu(self, os_flavor: OS_Flavor) -> CPU:
        """
        Return Gaia-X compliance CPU specification of given OpenStack flavor.
        @param os_flavor: OpenStack flavor
        @type Flavor
        @return: Gaia-X complinat CPU definition
        @rtype CPU
        """
        cpu = CPU(cpuArchitecture=CpuArch.other, numberOfCores=os_flavor.vcpus)
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            parts = os_flavor.name.split("-")
            if len(parts) >= 2:
                cpu_suffix = parts[1][-1]
                cpu.numberOfCores = int(parts[1][-2])
                if cpu_suffix.endswith("i"):
                    cpu_suffix = parts[1][-2]
                    cpu.numberOfCores = int(parts[1][-3])
                if cpu_suffix == "C":
                    cpu.smtEnabled = False
                    cpu.defaultOversubscriptionRatio = 1
                elif cpu_suffix.endswith("T"):
                    cpu.smtEnabled = True
                    cpu.defaultOversubscriptionRatio = 1
                elif cpu_suffix.endswith("V"):
                    cpu.smtEnabled = True
                    cpu.defaultOversubscriptionRatio = 5
                elif cpu_suffix.endswith("L"):
                    cpu.smtEnabled = True
                    cpu.defaultOversubscriptionRatio = 16
        return cpu

    def _get_ram(self, os_flavor: OS_Flavor) -> Memory:
        """
        Return Gaia-X RAM definition specified in given OpenStack flavor.
        @param os_flavor: OpenStack Flavor
        @type Flavor
        @return: Gaia-X compliance RAM definition
        @rtype Memory
        """
        size = MemorySize(value=float(os_flavor.ram), unit=const.UNIT_MB)
        mem = Memory(memorySize=size)
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            parts = os_flavor.name.split("-")
            if len(parts) >= 3:
                mem_cap = parts[2]
                if mem_cap.endswith("ou"):
                    # this order of memory suffixes is not allows
                    return mem
                elif mem_cap.endswith("uo"):
                    mem.eccEnabled = True
                    mem.defaultOversubscriptionRatio = 2
                    mem.eccEnabled = True
                    mem.memorySize.value = float(mem_cap[0:-2])
                elif mem_cap.endswith("u"):
                    mem.eccEnabled = True
                    mem.memorySize.value = float(mem_cap[0:-1])
                elif mem_cap.endswith("o"):
                    mem.defaultOversubscriptionRatio = 2
                    mem.memorySize.value = float(mem_cap[0:-1])
                else:
                    mem.memorySize.value = float(mem_cap)
        return mem

    def _get_disks(self, os_flavor: OS_Flavor) -> List[Disk]:
        """
        Return all disk specification found in given Openstack flavor.
        @param os_flavor: Openstack flavor specification
        @type os_flavor: Flavor
        @return: list of Gaia-X disk specifications
        """
        disks = []
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            parts = os_flavor.name.split("-")
            if len(parts) < 4:
                # either no SCS compliant flavor name or disk spec missing
                disks.append(
                    Disk(diskSize=MemorySize(value=os_flavor.disk, unit=const.UNIT_GB))
                )
            else:
                # SCS compliant flavor name with spec of disk capabilities
                number, size, disk_type, disk_bus_types = self._get_disk_caps(parts[3])
                for i in range(int(number)):
                    disks.append(
                        Disk(
                            diskSize=MemorySize(value=size, unit=const.UNIT_GB),
                            diskType=disk_type,
                            diskBusType=disk_bus_types,
                        )
                    )
        else:
            # no SCS compliant flavor name. Use disk property to set disk spec
            disks.append(
                Disk(diskSize=MemorySize(value=os_flavor.disk, unit=const.UNIT_GB))
            )

        return disks

    def _get_disk_caps(self, disk_caps: str) -> Tuple[int, int, DiskType, DiskBusType]:
        """
        Extracts disk capabilities encoded in flavor name according to SCS flavor naming standard.
        @param disk_caps: Disk capabilities encoded as string according to SCS flavor naming standard.
        @type disk_caps: str
        @return:
        """
        disk_type = DiskType.other.text
        disk_bus_types = DiskType.other.text
        number = 1

        # parse disk type and disk bus type
        if re.search(r"\d+$", disk_caps):
            # no disk type set
            size = disk_caps[0 : len(disk_caps)]
        else:
            # disk type set
            size = disk_caps[0 : len(disk_caps) - 1]
            # parse disk type and disk bus type
            if disk_caps.endswith("n"):
                disk_type = "shared network storage"
            elif disk_caps.endswith("h"):
                disk_type = "local HDD"
            elif disk_caps.endswith("s"):
                disk_type = "local SSD"
            elif disk_caps.endswith("p"):
                disk_type = "local HDD"
                disk_bus_types = "NVMe"
        try:
            number, size = size.split("x")
        except ValueError:
            if len(size) == 0:
                # no size set
                size = 0

        return int(number), int(size), DiskType(disk_type), DiskBusType(disk_bus_types)

    def _parse_optional_flavor_properties(
        self, os_flavor: OS_Flavor, gx_flavor: GX_Flavor
    ):
        """Parse and return optional flavor properties, such as CPU architecture, CPU frequency or hypervisor.
        @param os_flavor Openstack flavor
        @type os_flavor Flavor
        @param gx_flavor Gaia-X Flavor specification
        @type gx_flavor ServerFlavor
        """
        parts = os_flavor.name.split("_")
        for suffix in parts:
            if suffix.startswith("SCS"):
                continue
            # parse hypervisor
            elif suffix == "kvm":
                gx_flavor.hypervisor = Hypervisor(
                    hypervisorType="KVM",
                    copyrightOwnedBy=common.get_copyright_owner(
                        self.config, const.CONFIG_HV_KVM
                    ),
                    license=common.get_license(self.config, const.CONFIG_HV_KVM),
                    resourcePolicy=common.get_resource_policy(
                        self.config, const.CONFIG_HV_KVM
                    ),
                )
            elif suffix == "xen":
                gx_flavor.hypervisor = Hypervisor(
                    hypervisorType="Xen",
                    copyrightOwnedBy=common.get_copyright_owner(
                        self.config, const.CONFIG_HV_XEN
                    ),
                    license=common.get_license(self.config, const.CONFIG_HV_XEN),
                    resourcePolicy=common.get_resource_policy(
                        self.config, const.CONFIG_HV_XEN
                    ),
                )
            elif suffix == "vmw":
                gx_flavor.hypervisor = Hypervisor(
                    hypervisorType="KVM",
                    copyrightOwnedBy=common.get_copyright_owner(
                        self.config, const.CONFIG_HV_VMW
                    ),
                    license=common.get_license(self.config, const.CONFIG_HV_VMW),
                    resourcePolicy=common.get_resource_policy(
                        self.config, const.CONFIG_HV_VMW
                    ),
                )
            elif suffix == "hyv":
                gx_flavor.hypervisor = Hypervisor(
                    hypervisorType="Hyper-V",
                    copyrightOwnedBy=common.get_copyright_owner(
                        self.config, const.CONFIG_HV_HYV
                    ),
                    license=common.get_license(self.config, const.CONFIG_HV_HYV),
                    resourcePolicy=common.get_resource_policy(
                        self.config, const.CONFIG_HV_HYV
                    ),
                )
            # parse hardware assisted virtualization
            elif suffix == "hwv":
                gx_flavor.hardwareAssistedVirtualization = True
            # parse CPU architecture details
            elif suffix.startswith("i"):
                # Intel x86-64
                gx_flavor.cpu.cpuArchitecture = CpuArch("x86-64")
                gx_flavor.cpu.vendor = "Intel"
                if suffix.startswith("i0"):
                    gx_flavor.cpu.generation = "pre Skylake"
                elif suffix.startswith("i1"):
                    gx_flavor.cpu.generation = "Skylake"
                elif suffix.startswith("i2"):
                    gx_flavor.cpu.generation = "Cascade Lake"
                elif suffix.startswith("i3"):
                    gx_flavor.cpu.generation = "Ice Lake"
                elif suffix.startswith("i4"):
                    gx_flavor.cpu.generation = "Ice Lake"
            elif suffix.startswith("z"):
                #  	AMD (Zen) x86-64
                gx_flavor.cpu.cpuArchitecture = CpuArch("x86-64")
                gx_flavor.cpu.vendor = "AMD"
                if suffix.startswith("z0"):
                    gx_flavor.cpu.generation = "pre Zen"
                elif suffix.startswith("z1"):
                    gx_flavor.cpu.generation = "Zen-1 (Naples)"
                elif suffix.startswith("z2"):
                    gx_flavor.cpu.generation = "Zen-2 (Rome"
                elif suffix.startswith("z3"):
                    gx_flavor.cpu.generation = "Zen-3 (Milan)"
                elif suffix.startswith("z4"):
                    gx_flavor.cpu.generation = "Zen-4 (Genoa)"
            elif suffix.startswith("a"):
                #  	ARM v8+
                gx_flavor.cpu.cpuArchitecture = CpuArch("AArch-64")
                gx_flavor.cpu.vendor = "ARM"
                if suffix.startswith("a0"):
                    gx_flavor.cpu.generation = "pre Cortex A76"
                elif suffix.startswith("a1"):
                    gx_flavor.cpu.generation = "A76/NeoN1 class"
                elif suffix.startswith("a2"):
                    gx_flavor.cpu.generation = "A78/x1/NeoV1 class"
                elif suffix.startswith("a3"):
                    gx_flavor.cpu.generation = "A71x/NeoN2 (ARMv9)"
            elif suffix.startswith("r"):
                #  	RISC-V
                gx_flavor.cpu.cpuArchitecture = CpuArch("RISC-V")
            # parse frequency
            if suffix.endswith("hhh"):
                gx_flavor.cpu.baseFrequency = Frequency(value=3.75, unit=const.UNIT_GHZ)
            elif suffix.endswith("hh"):
                gx_flavor.cpu.baseFrequency = Frequency(value=3.25, unit=const.UNIT_GHZ)
            elif suffix.endswith("h"):
                gx_flavor.cpu.baseFrequency = Frequency(value=2.75, unit=const.UNIT_GHZ)

    def _add_description(self, os_flavor: OS_Flavor, gx_flavor: GX_Flavor) -> None:
        """
        Add description to flavor.
        @param os_flavor OpenStack flavor specification
        @type os_flavor: Flavor
        @param gx_flavor Gaia-X flavor specification
        @type gx_flavor: ServerFlavor
        """
        try:
            gx_flavor.description = os_flavor.description
        except KeyError:
            pass
