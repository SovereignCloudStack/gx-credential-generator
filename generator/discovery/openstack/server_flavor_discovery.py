"""Script to discovery server flavor properties.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import List, Optional

from openstack.compute.v2.flavor import Flavor as OS_Flavor
from openstack.connection import Connection

from generator.common import const
from generator.common.config import Config
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (Disk, DiskType, Frequency, Hypervisor,
                                        HypervisorType, Memory, MemorySize)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.vendor.flavor_names import Flavorname, parser_v3

# map SCS hypervisor names to corresponding GX type and config key
HYPERVISOR_LOOKUP = {
    "kvm": (HypervisorType.KVM, const.CONFIG_HV_KVM),
    "xen": (HypervisorType.Xen, const.CONFIG_HV_XEN),
    "vmw": (HypervisorType.other, const.CONFIG_HV_VMW),
    "hyv": (getattr(HypervisorType, "Hyper-V"), const.CONFIG_HV_HYV),
}
# map SCS cpu vendor/architecture letter to architecture, vendor and list of generations
CPUVENDOR_LOOKUP = {
    # Intel x86-64
    "i": (
        "x86-64",
        "Intel",
        ("pre Skylake", "Skylake", "Cascade Lake", "Ice Lake", "Sapphire Rapids"),
    ),
    # AMD (Zen) x86-64
    "z": (
        "x86-64",
        "AMD",
        ("pre Zen", "Zen-1 (Naples)", "Zen-2 (Rome)", "Zen-3 (Milan)", "Zen-4 (Genoa)"),
    ),
    # ARM v8+
    "a": (
        "AArch-64",
        "ARM",
        (
            "pre Cortex A76",
            "A76/NeoN1 class",
            "A78/x1/NeoV1 class",
            "A71x/NeoN2 (ARMv9)",
        ),
    ),
    # RISC-V
    "r": (
        "RISC-V",
        None,
        (),
    ),
}


class ServerFlavorDiscovery:
    """
    Discovery for openstack server flavor properties.
    """
    def __init__(self, conn: Connection, conf: Config) -> None:
        self.conn = conn
        self.conf = conf

    def discover(self) -> List[GX_Flavor]:
        """
        Return one JsonLdObject for each public server flavor discovery at openstack cloud.

        @return: list of public server flavors
        @rtype: list[JsonLdObject]
        """
        flavors = list()
        for fl in self.conn.list_flavors():
            if fl.is_public:
                flavors.append(self._convert_to_gx(fl))
        return flavors

    def _convert_to_gx(self, os_flavor: OS_Flavor) -> GX_Flavor:
        """
        Convert Openstack flavor to Gaia-X server flavor.
        @param os_flavor: Openstack server flavor specification
        @type os_flavor: Flavor
        @return: Gaia-X server flavor specification
        @rtype ServerFlavor
        """

        try:
            flavorname = parser_v3(os_flavor.name)
        except ValueError:
            flavorname = None
        # Initialize Gaia-X Server Flavor
        disks = self._get_disks(os_flavor, flavorname)
        gx_flavor = GX_Flavor(
            # name=os_flavor.name,
            cpu=self._get_cpu(os_flavor, flavorname),
            ram=self._get_ram(os_flavor, flavorname),
            bootVolume=disks[0],
        )

        if len(disks) > 1:
            gx_flavor.additionalVolume = disks[1:]

        # Discover optional attributes
        self._parse_optional_flavor_properties(flavorname, gx_flavor)
        self._add_description(os_flavor, gx_flavor)

        return gx_flavor

    def _get_cpu(self, os_flavor: OS_Flavor, flavorname: Optional[Flavorname]) -> CPU:
        """
        Return Gaia-X compliance CPU specification of given OpenStack flavor.
        @param os_flavor: OpenStack flavor
        @type os_flavor: OS_Flavor
        @return: Gaia-X compliant CPU definition
        @rtype CPU
        """
        cpu = CPU(cpuArchitecture=CpuArch.Other, numberOfCores=os_flavor.vcpus)
        if flavorname:
            cpu.smtEnabled = (
                flavorname.cpuram.cputype != "C"
            )  # FIXME this is unclear to me, see #85

            cpu.defaultOversubscriptionRatio = 1
            if flavorname.cpuram.cputype == "V":
                cpu.defaultOversubscriptionRatio = 5
            elif flavorname.cpuram.cputype == "L":
                cpu.defaultOversubscriptionRatio = 16
        return cpu

    def _get_ram(
            self, os_flavor: OS_Flavor, flavorname: Optional[Flavorname]
    ) -> Memory:
        """
        Return Gaia-X RAM definition specified in given OpenStack flavor.
        @param os_flavor: OpenStack Flavor
        @type Flavor
        @return: Gaia-X compliance RAM definition
        @rtype Memory
        """
        size = MemorySize(value=float(os_flavor.ram), unit=const.UNIT_MB)
        mem = Memory(memorySize=size)
        if flavorname:
            mem.eccEnabled = not flavorname.cpuram.raminsecure
            if flavorname.cpuram.ramoversubscribed:
                mem.defaultOversubscriptionRatio = 2
        return mem

    def _get_disks(
            self, os_flavor: OS_Flavor, flavorname: Optional[Flavorname]
    ) -> List[Disk]:
        """
        Return all disk specification found in given Openstack flavor.
        @param os_flavor: Openstack flavor specification
        @type os_flavor: Flavor
        @return: list of Gaia-X disk specifications
        """
        disks = []
        if flavorname and flavorname.disk:
            disk_type = DiskType.other.text
            disk_bus_types = DiskType.other.text
            if flavorname.disk.disktype == "n":
                disk_type = "shared network storage"
            elif flavorname.disk.disktype == "h":
                disk_type = "local HDD"
            elif flavorname.disk.disktype == "s":
                disk_type = "local SSD"
            elif flavorname.disk.disktype == "p":
                disk_type = "local HDD"
                disk_bus_types = "NVMe"
            for i in range(int(flavorname.disk.nrdisks)):
                disks.append(
                    Disk(
                        diskSize=MemorySize(
                            value=flavorname.disk.disksize, unit=const.UNIT_GB
                        ),
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

    def _parse_optional_flavor_properties(
            self, flavorname: Optional[Flavorname], gx_flavor: GX_Flavor
    ):
        """Parse and return optional flavor properties, such as CPU architecture, CPU frequency or hypervisor.
        @param os_flavor Openstack flavor
        @type os_flavor Flavor
        @param gx_flavor Gaia-X Flavor specification
        @type gx_flavor ServerFlavor
        """
        if flavorname is None:
            return
        if flavorname.hype and flavorname.hype.hype in HYPERVISOR_LOOKUP:
            hv_type, conf_key = HYPERVISOR_LOOKUP[flavorname.hype.hype]
            gx_flavor.hypervisor = Hypervisor(
                hypervisorType=hv_type,
                copyrightOwnedBy=self.conf.get_copyright_owner(conf_key),
                license=self.conf.get_license(conf_key),
                resourcePolicy=self.conf.get_resource_policy(conf_key),
            )
        if flavorname.hwvirt and flavorname.hwvirt.hwvirt:
            gx_flavor.hardwareAssistedVirtualization = True
        if flavorname.cpubrand:
            arch, vendor, gens = CPUVENDOR_LOOKUP[flavorname.cpubrand.cpuvendor]
            gx_flavor.cpu.cpuArchitecture = CpuArch(arch)
            if vendor is not None:
                gx_flavor.cpu.vendor = vendor
            idx = flavorname.cpubrand.cpugen
            if idx is not None and idx < len(gens):
                gx_flavor.cpu.generation = gens[idx]
            # parse frequency
            if flavorname.cpubrand.perf:
                freq = 0.5 * len(flavorname.cpubrand.perf) + 2.25
                gx_flavor.cpu.baseFrequency = Frequency(value=freq, unit=const.UNIT_GHZ)

    def _add_description(self, os_flavor: OS_Flavor, gx_flavor: GX_Flavor) -> None:
        """
        Add description to flavor.
        @param os_flavor OpenStack flavor specification
        @type os_flavor: Flavor
        @param gx_flavor Gaia-X flavor specification
        @type gx_flavor: ServerFlavor
        """
        gx_flavor.description = os_flavor.description
