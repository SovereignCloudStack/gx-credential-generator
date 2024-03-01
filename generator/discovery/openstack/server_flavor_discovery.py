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
from generator.common.gx_schema import CPU, SPDX
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


class ServerFlavorDiscovery:
    # def __init__(self) -> None:
    #    with open("config/config.yaml", "r") as config_file:
    #        self.config = yaml.safe_load(config_file)

    def __init__(self, conn: Connection, config: Dict) -> None:
        self.conn = conn
        self.config = config

    # def collect_vm_images(self, conn: Connection) -> List[str]:
    def discover(self) -> List[JsonLdObject]:
        """
        Return one JsonLdObject for each punlic server flavor discovery at openstack cloud.

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
            cpu=self._get_cpu_req(),
            ram=self._get_ram_req(),
            bootVolume=self._get_boot_volume_req()
        )

        # Discover optional attributes
        self._add_name(os_flavor, gx_flavor)

        return gx_flavor

    def _get_cpu_req(self) -> CPU:

        pass

    def _get_ram_req(self, os_flavor: OS_Flavor) -> Memory:
        size = MemorySize(
            value=float(os_flavor.min_ram * 1.048576), unit=const.UNIT_MB
        )
        mem_req = Memory(memorySize=size)
        # try:
        #    mem_req.hardwareEncryption = os_image.hw_mem_encryption
        # except AttributeError:
        #    pass
        return mem_req

    def _get_boot_volume_req(self) -> Disk:
        pass

    @staticmethod
    def _add_name(os_flavor: OS_Flavor, gx_flavor: GX_Flavor) -> None:
        try:
            gx_flavor.name = os_flavor.name
        except KeyError:
            pass

    @staticmethod
    def _add_description(os_flavor: OS_Flavor, gx_flavor: GX_Flavor) -> None:
        try:
            gx_flavor.description = os_flavor.description
        except KeyError:
            pass
