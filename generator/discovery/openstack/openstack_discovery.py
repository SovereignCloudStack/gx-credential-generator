#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# openstack_discovery.py
"""Script to generate GX Credentials in JSON-LD.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
(c) Anja Strunk <anja.strunk@cloudandheat.com>, 1/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import List

from openstack.connection import Connection

from generator.common.config import Config
from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.vm_images_discovery import VmDiscovery


class OsCloud:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        # import copy
        self.conn = conn
        # self.regions = list(conn.identity.regions())
        self.config = config

    def discover_properties(self) -> List[JsonLdObject]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """
        creds = list()

        vm_dis = VmDiscovery(self.conn, self.config)
        creds.extend(vm_dis.discover_vm_images())

        return creds
