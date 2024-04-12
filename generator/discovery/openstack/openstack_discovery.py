""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import List

from openstack.connection import Connection

from generator.common.config import Config
from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmDiscovery


class OsCloud:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        # import copy
        self.conn = conn
        # self.regions = list(conn.identity.regions())
        self.config = config

    def discover(self) -> List[JsonLdObject]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """
        return (
            VmDiscovery(self.conn, self.config).discover()
            + ServerFlavorDiscovery(self.conn, self.config).discover()
        )
