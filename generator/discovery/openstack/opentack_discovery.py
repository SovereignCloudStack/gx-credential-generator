#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# openstack_discovery.py
"""Script to generate GX Credentials in JSON-LD.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
(c) Anja Strunk <anja.strunk@cloudandheat.com>, 1/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import Dict, List

from openstack.connection import Connection

from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.images_discovery import ImageDiscovery
from generator.discovery.openstack.server_flavor_discovery import ServerFlavorDiscovery


class OsCloud:
    "Abstraction for openStack cloud with all its services."

    def __init__(self, conn: Connection, config: Dict) -> None:
        # import copy
        self.conn = conn
        self.auth = conn.auth
        self.regions = list(conn.identity.regions())
        self.config = config

    def discover_properties(self) -> List[JsonLdObject]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """
        creds = list()
        #creds.extend(VmDiscovery(self.conn, self.config).discover())
        creds.extend(ServerFlavorDiscovery(self.conn, self.config).discover())

        return creds