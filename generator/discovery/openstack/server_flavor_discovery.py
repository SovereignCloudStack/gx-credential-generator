#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# images_discovery.py
"""Script to discovery server flavor properties.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from datetime import datetime
from typing import Dict, List, Union

from linkml_runtime.utils.metamodelcore import URI
from openstack.connection import Connection
from openstack.compute.v2.flavor import Flavor as OS_Flavor

import generator.common.const as const
from generator.common.gx_schema import CPU, SPDX, DiskTypes
from generator.common.gx_schema import Architectures as CpuArch
from generator.common.gx_schema import (
    CheckSum,
    ChecksumAlgorithm,
    Disk,
    HypervisorType,
    Memory,
    MemorySize,
    OperatingSystem,
    Signature,
    SignatureAlgorithm,
    UpdateStrategy,
)
from generator.common.gx_schema import ServerFlavor as GX_Flavor
from generator.common.json_ld import JsonLdObject

import re

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
        Convert Openstack flavor to a Gaia-X server flavor.
        @param os_flavor: Openstack server flavor
        @type os_flavor: OS_Flavor
        @return: Gaia-X server flavor
        @rtype GX_Flavor
        """

        # Initialize Gaia-X Server Flavor
        gx_flavor = GX_Flavor(
            cpu=self._get_cpu(os_flavor),
            ram=self._get_ram(os_flavor),
            bootVolume=self._get_boot_volume(os_flavor)
        )

        # Discover optional attributes
        self._add_description(os_flavor, gx_flavor)

        return gx_flavor

    def _get_cpu(self, os_flavor: OS_Flavor) -> CPU:
        cpu = CPU(cpuArchitecture=CpuArch.other)
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            cpu_cap = os_flavor.name.split("-")[1]
            cpu_suffix = cpu_cap[-1]
            if cpu_cap.endswith('i'):
                cpu_suffix = cpu_cap[-2]
            if cpu_suffix == "C":
                cpu.smtEnabled = False
                cpu.defaultOversubscriptionRatio = 1
            elif cpu_cap.endswith('T'):
                cpu.smtEnabled = True
                cpu.defaultOversubscriptionRatio = 1
            elif cpu_cap.endswith('V'):
                cpu.smtEnabled = True
                cpu.defaultOversubscriptionRatio = 5
            elif cpu_cap.endswith('L'):
                cpu.smtEnabled = True
                cpu.defaultOversubscriptionRatio = 6
        return cpu

    def _get_ram(self, os_flavor: OS_Flavor) -> Memory:
        size = MemorySize(
            value=float(os_flavor.ram), unit=const.UNIT_MB
        )
        mem = Memory(memorySize=size)
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            try:
                mem_cap = os_flavor.name.split("-")[2]
                if mem_cap.endswith("u"):
                    mem.eccEnabled = True
                elif mem_cap.endswith("o"):
                    mem.eccEnabled = True
                elif mem_cap.endswith("ou"):
                    mem.eccEnabled = True
                    mem.defaultOversubscriptionRatio = 2
                    mem.eccEnabled = True
            except IndexError:
                # flavor name does not conform with SCS Flavor Naming Standard v3
                pass
        return mem

    def _get_boot_volume(self, os_flavor: OS_Flavor) -> Disk:
        size = MemorySize(
            value=float(os_flavor.disk), unit=const.UNIT_GB
        )
        disk = Disk(diskSize=size)
        if os_flavor.name.startswith("SCS-"):
            # parse SCS flavor name
            try:
                disk_cap = os_flavor.name.split("-")[3]
                if disk_cap.endswith("n"):
                    disk.diskType = "shared network storage"
                elif disk_cap.endswith("h"):
                    disk.diskType = "local HDD"
                elif disk_cap.endswith("s"):
                    disk.diskType = "local SSD"
                elif disk_cap.endswith("p"):
                    disk.diskType = "local HDD"
                    disk.diskBusType = "NVMe"
            except IndexError:
                # no disk description found
                pass
        return disk

    def _add_description(self, os_flavor: OS_Flavor, gx_flavor: GX_Flavor) -> None:
        try:
            gx_flavor.description = os_flavor.description
        except KeyError:
            pass
