import json
import os
import unittest

import yaml
from openstack.compute.v2.flavor import Flavor as OS_Flavor
from pyshacl import validate

from generator.common import common, const
from generator.common.gx_schema import CPU
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (Disk, DiskBusType, DiskType, Frequency,
                                        Hypervisor, Memory, MemorySize)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.common.json_ld import JsonLdObject, to_json_ld
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from tests.common import MockConnection, OpenstackTestcase


def _get_gx_flavors():
    return [
        JsonLdObject(
            gx_id="flavor_1",
            gx_object=GX_Flavor(
                # name='Flavor_1', description='Flavor 1_ext',
                cpu=CPU(
                    cpuArchitecture=CpuArch.other,
                    numberOfCores=2,
                ),
                ram=Memory(
                    memorySize=MemorySize(
                        value=16, unit="https://qudt.org/vocab/unit/MegaBYTE"
                    )
                ),
                bootVolume=Disk(diskSize=MemorySize(value=0, unit=const.UNIT_GB)),
            ),
        ),
        JsonLdObject(
            gx_id="flavor_2",
            gx_object=GX_Flavor(
                # name='Flavor_1', description='Flavor 1_ext',
                cpu=CPU(
                    cpuArchitecture=CpuArch("x86-64"),
                    vendor="AMD",
                    generation="Zen-3 (Milan)",
                    numberOfCores=4,
                    smtEnabled=True,
                    defaultOversubscriptionRatio=16,
                    baseFrequency=Frequency(value=3.25, unit=const.UNIT_GHZ),
                ),
                ram=Memory(
                    memorySize=MemorySize(
                        value=32, unit="https://qudt.org/vocab/unit/MegaBYTE"
                    ),
                    defaultOversubscriptionRatio=2,
                    eccEnabled=True,
                ),
                bootVolume=Disk(
                    diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                    diskType=DiskType("local SSD"),
                ),
                additionalVolume=[
                    Disk(
                        diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                        diskType=DiskType("local SSD"),
                    ),
                    Disk(
                        diskSize=MemorySize(value=50, unit=const.UNIT_GB),
                        diskType=DiskType("local SSD"),
                    ),
                ],
            ),
        ),
    ]


def _get_os_flavors():
    return [
        OS_Flavor(id="flavor_1", name="ABC", vcpus=2, ram=16, disk=0),
        OS_Flavor(
            id="flavor_2", name="SCS-4L-32uo-3x50s-_kvm_z3hh", vcpus=2, ram=16, disk=0
        ),
    ]


class VMServerFlavorDiscoveryTestcase(OpenstackTestcase):
    def setUp(self):
        cur_dir = os.getcwd()
        if cur_dir.endswith("tests"):
            path = cur_dir[0:-5] + "/config/config.yaml"
        else:
            path = cur_dir + "/config/config.yaml"
        with open(path, "r") as config_file:
            self.config = yaml.safe_load(config_file)
            self.discovery = ServerFlavorDiscovery(
                conn=MockConnection(flavors=_get_os_flavors()), config=self.config
            )

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

    def test_discovery_server_flavor(self):
        expected_gax_flavors = _get_gx_flavors()
        received_gax_flavors = self.discovery.discover()

        self.assertEqual(len(expected_gax_flavors), len(received_gax_flavors))

        for flavor_1 in expected_gax_flavors:
            self.check_flavor(
                flavor_1.gx_object,
                self.get_jsonobject_by_id(
                    flavor_1.gx_id, received_gax_flavors
                ).gx_object,
            )

    def test_json_ld(self):
        cur_dir = os.getcwd()
        if cur_dir.endswith("tests"):
            shacl_file = cur_dir + "/gaia-x.shacl.ttl"
        else:
            shacl_file = cur_dir + "/tests/gaia-x.shacl.ttl"

        flavors = self.discovery.discover()
        conforms, _, _ = validate(
            data_graph=json.dumps(flavors[0], indent=4, default=to_json_ld),
            shacl_graph=shacl_file,
            data_graph_format="json-ld",
            shacl_graph_format="ttl",
        )
        self.assertTrue(conforms)

    def _init_gx_flavor(
        self,
        ram: int = 32,
        disk: int = 50,
        cpu_arc: CpuArch = CpuArch.other,
        cpu_vendor: str = None,
        cpu_gen: str = None,
        cpu_freq: Frequency = None,
        hw_virt: bool = False,
        hv: bool = False,
    ) -> GX_Flavor:
        if hv:
            return GX_Flavor(
                # name=os_flavor.name,
                cpu=CPU(
                    cpuArchitecture=cpu_arc,
                    vendor=cpu_vendor,
                    generation=cpu_gen,
                    baseFrequency=cpu_freq,
                ),
                ram=Memory(memorySize=MemorySize(value=ram, unit=const.UNIT_MB)),
                bootVolume=Disk(diskSize=MemorySize(value=disk, unit=const.UNIT_GB)),
                hardwareAssistedVirtualization=hw_virt,
                hypervisor=Hypervisor(
                    hypervisorType="KVM",
                    copyrightOwnedBy=common.get_copyright_owner(
                        self.config, const.CONFIG_HV_KVM
                    ),
                    license=common.get_license(self.config, const.CONFIG_HV_KVM),
                    resourcePolicy=common.get_resource_policy(
                        self.config, const.CONFIG_HV_KVM
                    ),
                ),
            )
        else:
            return GX_Flavor(
                # name=os_flavor.name,
                cpu=CPU(
                    cpuArchitecture=cpu_arc,
                    vendor=cpu_vendor,
                    generation=cpu_gen,
                    baseFrequency=cpu_freq,
                ),
                ram=Memory(memorySize=MemorySize(value=ram, unit=const.UNIT_MB)),
                bootVolume=Disk(diskSize=MemorySize(value=disk, unit=const.UNIT_GB)),
                hardwareAssistedVirtualization=hw_virt,
            )


if __name__ == "__main__":
    unittest.main()
