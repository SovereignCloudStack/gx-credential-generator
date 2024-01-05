import generator.common.json_ld as json_ld

from generator.discovery.openstack.vm_images_discovery import VmDiscovery

from openstack.connection import Connection

from typing import Dict


class OsCloud:
    "Abstraction for openStack cloud with all its services."
    def __init__(self, conn: Connection, config: Dict) -> None:
        # import copy
        self.conn = conn
        self.auth = conn.auth
        self.regions = list(conn.identity.regions())
        self.config = config

    def discover_properties(self) -> dict:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as dict
        """
        props = json_ld.get_json_ld_context()
        props['@graph'] = []

        vm_dis = VmDiscovery(self.conn, self.config)
        for img in vm_dis.discover_vm_images():
            props['@graph'].append(img)
        return props




