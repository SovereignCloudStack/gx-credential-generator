#!/usr/bin/env python3
#
# openstack-discovery.py
#
# Talk to OpenStack APIs to discover environment
# Save discovered information in classes that reflect G-X attributes
# These can then be dumped as YAMLs or other forms
#
# (c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022 - 6/2022
# (c) Mathias Fechner <fechner@osism.tech>, 3/2022
# SPDX-License-Identifier: EPL-2.0

import sys, os, getopt

import openstack
import yaml

# Global variables
if "OS_CLOUD" in os.environ:
    cloud = os.environ["OS_CLOUD"]
else:
    cloud = ""
conn = None
ofile = '/dev/stdout'

class osService:
    def __init__(self, dct):
        self.id = dct["id"]
        # interface: we only look at public
        for ep in dct["endpoints"]:
            if ep["interface"] != "public":
                continue
            self.url = ep["url"]
            self.region = ep["region_id"]
        self.type = dct["type"]
        self.name = dct["name"]
    def __str__(self):
        return "%s|%s|%s" % (self.type, self.name, self.url)
    def __repr__(self):
        return str(self)

class osCompute:
    def __init__(self):
        self.flavors = []

class osCloud:
    def __init__(self):
        self.regions = []
        self.services = []
        self.compute = osCompute()
    def __str__(self):
        strg = "#Regions: %s\n#Services\n#%s" % (self.regions, self.services)
        if self.compute.flavors:
            yout = dict(compute = dict(flavor = self.compute.flavors))
            strg += '\n' + yaml.dump(yout, default_flow_style=False)
        return strg


def usage(err = 1):
    print("Usage: openstack-discovery.py [options]", file=sys.stderr)
    if not cloud:
        print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    sys.exit(err)

class osFlavor:
    def __init__(self, flv):
        self.name = flv['name']
        # Note: cpuType, cpuGeneration, diskType are MR34 ideas,
        # slightly different from and less comprehensive than
        # the abstraction in SCS flavor spec. Convert later.
        self.cpuType = ""
        self.cpuGeneration = ""
        self.numberOfvCPUs = flv['vcpus']
        self.ramSize = flv['ram']       # MiB
        self.diskSize = flv['disk']     # GB
        self.diskType = ""

    def toyaml(self):
        ydct = dict(name = self.name,
                    numberOfvCPUs = self.numberOfvCPUs,
                    ramSize = dict(Value = self.ramSize/1024, Unit = 'GiB')
                )
        if self.diskSize:
            ydct['diskSize'] = dict(Value = self.diskSize, Unit = 'GB')
        # TODO: cpuType, cpuGen, diskType output
        return ydct


def get_openstack_flavors():
    """Use OpenStack conn (global var conn) to get flavor list from
       compute service. Populate flavor list."""

    flvs = list()
    for flv_id in conn.compute.flavors(id):
        flvs.append(osFlavor(flv_id).toyaml())

        # TODO:
        # (a) parse extra specs if any
        # (b) parse SCS flavor names
    return flvs

def main(argv):
    global cloud, conn
    global ofile
    try:
        opts, args = getopt.gnu_getopt(argv[1:], "c:f:h", ("os-cloud=", "file", "help"))
    except getopt.GetoptError as exc:
        usage(1)
    for opt in opts:
        if opt[0] == "-h" or opt[0] == "--help":
            usage(0)
        elif opt[0] == "-c" or opt[0] == "--os-cloud":
            cloud = opt[1]
        elif opt[0] == "-f" or opt[0] == "--file":
            ofile = opt[1]

    if args:
        usage(1)
    conn = openstack.connect(cloud=cloud)
    mycloud = osCloud()
    mycloud.regions = list(conn.identity.regions())
    #mycloud.services = list(conn.identity.services())
    #mycloud.services = conn.list_services()
    for svc in conn.service_catalog:
        mycloud.services.append(osService(svc))
    #print(conn)
    mycloud.compute.flavors = get_openstack_flavors()
    print(mycloud, file = open(ofile, 'a'))



if __name__ == "__main__":
    main(sys.argv)

# vim:fenc=utf-8:ts=4:sw=4:noet:sts=4:ai
