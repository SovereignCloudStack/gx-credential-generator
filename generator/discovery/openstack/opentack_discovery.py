import openstack
from openstack.connection import Connection
from typing import Dict
import sys

from generator.discovery.openstack.vm_images_discovery import VmDiscovery

class OsCloud:
    "Abstraction for openStack cloud with all its services"
    def __init__(self, conn: Connection, config: Dict) -> None:
        # import copy
        self.conn = conn
        self.auth = conn.auth
        self.regions = list(conn.identity.regions())
        self.config = config

    def discover_properties(self):
        vm_dis = VmDiscovery(self.conn, self.config)
        creds = vm_dis.discover_vm_images()

        # Create per region service catalogs
        """self.regcat = {}
        for region in self.regions:
            reg = region.id
            self.regcat[reg] = []
            for svc in conn.service_catalog:
                svccat = osServiceCat(svc, reg)
                if svccat.ep:
                    self.regcat[reg].append(svccat)
            if debug:
                print(f"#DEBUG: Svc Cat region {reg}: {self.regcat}", file=sys.stderr)
        # Well-known OpenStack services
        self.ostacksvc = {}
        if "project_id" in conn.auth:
            prj_id = conn.auth["project_id"]
        else:
            prj_id = conn.identity.get_project_id()
        # Iterate over regions
        for region in self.regions:
            # Keep list of already handled services to avoid duplicates/aliases
            handled = []
            # Dictionary to collect OpenStack services
            ostacksvc = {}
            reg = region.id
            if debug:
                print(f"#INFO: Creation service catalog for region {reg}", file=sys.stderr)
            # Iterate over service catalog
            for svc in self.regcat[reg]:
                assert svc.ep
                assert reg == svc.region
                # Treating those two legacy services as non-OpenStack (just list EPs)
                if svc.type in [*handled, "compute_legacy", "cloudformation"]:
                    continue
                newsvc = None
                for osClass in OSClasses:
                    if svc.type in osClass.svcID:
                        newsvc = osClass(conn, svc.type, svc.name, reg, prj_id, svc.ep)
                        handled.extend(osClass.svcID)
                        break
                if not newsvc:
                    newsvc = osService(conn, svc.type, svc.name, reg, prj_id, svc.ep)
                    handled.extend((svc.type, newsvc.stype,))
                # Only attach if conn is non-empty
                if newsvc.conn:
                    ostacksvc[newsvc.stype] = newsvc
                    if debug:
                        print(f"#DEBUG: Region {reg} added OS Svc {newsvc}", file=sys.stderr)
                    svc.consumed = True
                elif debug:
                    print(f"#DEBUG: Region {reg} with service {newsvc} without connection", file=sys.stderr)
            # Handle remaining services that are listed
            for svc in self.regcat[reg]:
                if not svc.consumed and svc.type not in ostacksvc:
                    ostacksvc[svc.type] = nonOSService(svc.type, svc.name, svc.ep.replace(prj_id, "${OS_PROJECT_ID}"))
                    if debug:
                        print(f"#DEBUG: Region {reg} added Non-OS {ostacksvc[svc.type]}", file=sys.stderr)
                    svc.consumed = True
            self.ostacksvc[reg] = ostacksvc
        # TODO: Iterate over non-consumed services (global, non-region specifc)

    def values(self, prefix=''):
        "dict representing stored data"
        inner = {"regions": list(map(lambda x: x.id, self.regions))}
        if outjson:
            inner["auth_url"] = valtype(self.auth["auth_url"], "xsd:anyURI")
        else:
            inner["auth_url"] = self.auth["auth_url"]
        for reg, ostacksvc in self.ostacksvc.items():
            inner[reg] = {}
            for svckey in ostacksvc:
                svc = ostacksvc[svckey]
                inner[reg] = appenddicts(inner[reg], svc.values())
                if outjson:
                    inner[reg][svc.stype]["endpoint"] = valtype(svc.ep, "xsd:anyURI")
        if prefix:
            return add_prefix_to_dict_keys(inner, prefix)
        return inner

    def __str__(self):
        # print(self.values())
        if outjson:
            return json.dumps({"OpenStackService": self.values()}, indent=indent)
        return yaml.dump({"openstack": self.values()}, default_flow_style=False)"""
