import unittest

from openstack.compute.v2.flavor import Flavor as OS_Flavor

from generator.common import const
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (Disk, DiskBusType, DiskType, Frequency,
                                        Hypervisor, Memory, MemorySize)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from tests.common import MockConnection, OpenstackTestcase, get_config

OS_FLAVOR_1 = OS_Flavor(id="flavor_1", name="ABC", vcpus=2, ram=16, disk=0)
OS_FLAVOR_2 = OS_Flavor(
    id="flavor_2", name="SCS-4L-32uo-3x50s-_kvm_z3hh", vcpus=2, ram=16, disk=0
)


class VMServerFlavorDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        self.discovery = ServerFlavorDiscovery(
            conn=MockConnection(flavors=[OS_FLAVOR_1, OS_FLAVOR_2]), conf=get_config())

    def test_get_cpu(self):
        self.assertEqual(
            CPU(cpuArchitecture=CpuArch.other, numberOfCores=0),
            self.discovery._get_cpu(OS_Flavor(name="ABC", ram=10)),
        )
        self.assertEqual(
            CPU(
                cpuArchitecture=CpuArch.other,
                defaultOversubscriptionRatio=1,
                numberOfCores=2,
            ),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2C-4", ram=10)),
        )
        self.assertEqual(
            CPU(
                cpuArchitecture=CpuArch.other,
                defaultOversubscriptionRatio=1,
                numberOfCores=2,
                smtEnabled=True,
            ),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2T-4", ram=10)),
        )
        self.assertEqual(
            CPU(
                cpuArchitecture=CpuArch.other,
                defaultOversubscriptionRatio=5,
                numberOfCores=2,
                smtEnabled=True,
            ),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2V-4", ram=10)),
        )
        self.assertEqual(
            CPU(
                cpuArchitecture=CpuArch.other,
                defaultOversubscriptionRatio=16,
                numberOfCores=2,
                smtEnabled=True,
            ),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2L-4", ram=10)),
        )
        self.assertEqual(
            CPU(
                cpuArchitecture=CpuArch.other,
                numberOfCores=4,
            ),
            self.discovery._get_cpu(OS_Flavor(name="SCS-2:8", ram=10, vcpus=4)),
        )

    def test_get_mem(self):
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4-10n", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=3.5, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-3.5-10n", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=4, unit=const.UNIT_MB), eccEnabled=True),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4u-10n", ram=10)),
        )
        self.assertEqual(
            Memory(
                memorySize=MemorySize(value=4, unit=const.UNIT_MB),
                defaultOversubscriptionRatio=2,
            ),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4o-10n", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4ou-10n", ram=10)),
        )
        self.assertEqual(
            Memory(
                memorySize=MemorySize(value=4, unit=const.UNIT_MB),
                eccEnabled=True,
                defaultOversubscriptionRatio=2,
            ),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C-4uo-10n", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2C_", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="SCS-2V:8", ram=10)),
        )
        self.assertEqual(
            Memory(memorySize=MemorySize(value=10, unit=const.UNIT_MB)),
            self.discovery._get_ram(OS_Flavor(name="test", ram=10)),
        )

    def test_get_disk_caps(self):
        self.assertEqual(
            (3, 10, DiskType("local SSD"), DiskBusType("other")),
            self.discovery._get_disk_caps("3x10s"),
        )
        self.assertEqual(
            (1, 10, DiskType("local HDD"), DiskBusType("NVMe")),
            self.discovery._get_disk_caps("10p"),
        )
        self.assertEqual(
            (1, 10, DiskType("other"), DiskBusType("other")),
            self.discovery._get_disk_caps("10"),
        )
        self.assertEqual(
            (1, 0, DiskType("shared network storage"), DiskBusType("other")),
            self.discovery._get_disk_caps("n"),
        )
        self.assertEqual(
            (2, 10, DiskType("other"), DiskBusType("other")),
            self.discovery._get_disk_caps("2x10"),
        )
        self.assertEqual(
            (2, 10, DiskType("local HDD"), DiskBusType("NVMe")),
            self.discovery._get_disk_caps("2x10p"),
        )

    def test_get_disks(self):
        # no SCS standard compliant flavor name
        self.assertEqual(
            [Disk(diskSize=MemorySize(value=50, unit=const.UNIT_GB))],
            self.discovery._get_disks(OS_Flavor(name="abc", ram=32, disk=50)),
        )
        # invalid SCS flavor name
        self.assertEqual(
            [Disk(diskSize=MemorySize(value=50, unit=const.UNIT_GB))],
            self.discovery._get_disks(OS_Flavor(name="SCS-2C:10n", ram=32, disk=50)),
        )

        # SCS compliant flavor name
        self.assertEqual(
            [
                Disk(diskSize=MemorySize(value=10, unit=const.UNIT_GB)),
                Disk(diskSize=MemorySize(value=10, unit=const.UNIT_GB)),
            ],
            self.discovery._get_disks(OS_Flavor(name="SCS-2C-4-2x10", disk=50)),
        )

    def test_parse_optional_flavor_properties(self):
        # check hypervisor
        os_flavor = OS_Flavor(name="SCS-2C-4-10_kvm")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_hv = self._init_gx_flavor(hv=True)
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_hv, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10_kvm_hwv")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_hv = self._init_gx_flavor(hv=True, hw_virt=True)
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_hv, gx_flavor)

        # check hardware virtualization
        os_flavor = OS_Flavor(name="SCS-2C-4-10_hwv")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_hw = self._init_gx_flavor(hw_virt=True)
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_hw, gx_flavor)

        # check CPU architecture, frequency and generation
        os_flavor = OS_Flavor(name="SCS-2C-4-10n_i")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"), cpu_vendor="Intel"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_i3")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"), cpu_vendor="Intel", cpu_gen="Ice Lake"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_i3h")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"),
            cpu_vendor="Intel",
            cpu_gen="Ice Lake",
            cpu_freq=Frequency(value=2.75, unit=const.UNIT_GHZ),
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_z")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"), cpu_vendor="AMD"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_z4")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"), cpu_vendor="AMD", cpu_gen="Zen-4 (Genoa)"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_z4hh")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("x86-64"),
            cpu_vendor="AMD",
            cpu_gen="Zen-4 (Genoa)",
            cpu_freq=Frequency(value=3.25, unit=const.UNIT_GHZ),
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_a")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("AArch-64"), cpu_vendor="ARM"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_a2")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("AArch-64"), cpu_vendor="ARM", cpu_gen="A78/x1/NeoV1 class"
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_a2hhh")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(
            cpu_arc=CpuArch("AArch-64"),
            cpu_vendor="ARM",
            cpu_gen="A78/x1/NeoV1 class",
            cpu_freq=Frequency(value=3.75, unit=const.UNIT_GHZ),
        )
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

        os_flavor = OS_Flavor(name="SCS-2C-4-10n_r")
        gx_flavor = self._init_gx_flavor()
        gx_flavor_cpu = self._init_gx_flavor(cpu_arc=CpuArch("RISC-V"))
        self.discovery._parse_optional_flavor_properties(os_flavor, gx_flavor)
        self.assertEqual(gx_flavor_cpu, gx_flavor)

    def test_discovery(self):
        received_gax_flavors = self.discovery.discover()

        # init expected objects
        gax_flavor_1 = self._init_gx_flavor(ram=16, disk=0, number_of_cores=2)

        gax_flavor_2 = self._init_gx_flavor(ram=32, disk=50, cpu_arc=CpuArch("x86-64"), cpu_vendor="AMD",
                                            cpu_gen="Zen-3 (Milan)", cpu_freq=Frequency(value=3.25, unit=const.UNIT_GHZ), number_of_cores=4)
        gax_flavor_2.cpu.defaultOversubscriptionRatio = 16
        gax_flavor_2.cpu.smtEnabled = True
        gax_flavor_2.ram.eccEnabled = True
        gax_flavor_2.ram.defaultOversubscriptionRatio = 2
        gax_flavor_2.bootVolume = Disk(
                diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                diskType=DiskType("local SSD"))
        gax_flavor_2.additionalVolume = [
            Disk(
                diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                diskType=DiskType("local SSD"),
            ),
            Disk(
                diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                diskType=DiskType("local SSD"),
            ),
        ]

        # compare
        self.assert_flavor(gax_flavor_1, received_gax_flavors[0].gx_object)
        self.assert_flavor(gax_flavor_2, received_gax_flavors[1].gx_object)

    def _init_gx_flavor(
            self,
            ram: int = 32,
            disk: int = 50,
            cpu_arc: CpuArch = CpuArch.other,
            number_of_cores=1,
            cpu_vendor: str = None,
            cpu_gen: str = None,
            cpu_freq: Frequency = None,
            hw_virt: bool = False,
            hv: bool = False
    ) -> GX_Flavor:
        gx_flavor = GX_Flavor(
            # name=os_flavor.name,
            cpu=CPU(
                cpuArchitecture=cpu_arc,
                vendor=cpu_vendor,
                generation=cpu_gen,
                baseFrequency=cpu_freq,
                numberOfCores=number_of_cores,
            ),
            ram=Memory(memorySize=MemorySize(value=ram, unit=const.UNIT_MB)),
            bootVolume=Disk(diskSize=MemorySize(value=disk, unit=const.UNIT_GB)),
            hardwareAssistedVirtualization=hw_virt)
        if hv:
            gx_flavor.hypervisor = Hypervisor(
                hypervisorType="KVM",
                copyrightOwnedBy=self.discovery.get_copyright_owner(const.CONFIG_HV_KVM),
                license=self.discovery.get_license(const.CONFIG_HV_KVM),
                resourcePolicy=self.discovery.get_resource_policy(const.CONFIG_HV_KVM))

        return gx_flavor


if __name__ == "__main__":
    unittest.main()
