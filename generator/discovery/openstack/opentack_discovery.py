from typing import Dict, List

from openstack.connection import Connection

from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.vm_images_discovery import VmDiscovery


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

        @return: all attributes as list of YAMLRoot
        """
        creds = list()

        vm_dis = VmDiscovery(self.conn, self.config)
        creds.extend(vm_dis.discover_vm_images())

        return creds
