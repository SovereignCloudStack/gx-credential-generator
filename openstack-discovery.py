#!/usr/bin/env python3
#
# openstack-discovery.py
#
# Talk to OpenStack APIs to discover environment
# Save discovered information in classes that reflect G-X attributes
# These can then be dumped as YAMLs or other forms
#
# (c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022
# SPDX-License-Identifier: EPL-2.0

import sys, os, getopt
from enum import Enum

import openstack
import yaml

# Global variables
if "OS_CLOUD" in os.environ:
    cloud = os.environ["OS_CLOUD"]
else:
    cloud = ""
conn = None
ofile = '/dev/stdout'

# These should be moved to a helper file,
# to be used by OpenStack and also k8s discovery

class cpu:
    class VCPUtype(Enum):
        UNKNOWN = 0
        DEDCORE = 1
        DEDTHREAD = 2
        LIMOVERSUBSCR = 3
        UNLIMITED = 4
    def __init__(self, ncores, vtp = VCPUtype(0)):
        # Gaia-X attrs
        self.cores = ncores
        #self.threads = 0
        #self.freq = 0
        #self.boostFreq = 0
        #self.cache = 0
        # This would not be interesting typically
        #self.socketType = ""
        # Virt. attrs
        self.dedication = vtp

class mem:
    def __init__(self, gb, ecc=True):
        self.memGB = gb
        self.ECC = ecc

class disk:
    class Disktype(Enum):
        UNKNOWN = 0
        NETWORK = 1
        HDD = 2
        SSD = 3
        NVME = 4
    def __init__(self, size, tp = Disktype(0)):
        self.sizeGB = size
        self.diskType = tp

class flavor:
    def __init__(self, nm, cpus, memsz, disksz):
        self.name = nm
        self.cpu  = cpu(cpus)
        self.mem  = mem(memsz)
        self.disk = disk(disksz)


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

class osCloud:
    def __init__(self):
        self.regions = []
        self.services = []
    def __str__(self):
        return "#Regions: %s\n#Services\n%s" % (self.regions, self.services)


def usage(err = 1):
    print("Usage: openstack-discovery.py [options]", file=sys.stderr)
    print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    sys.exit(err)


def get_openstack_flavors():
    "Uses openstack reported flavor attributes"
    flavors = []
    for flv_id in conn.compute.flavors(id):
        flv_name = flv_id['name']
        flv_cores = flv_id['vcpus']
        flv_ram = flv_id['ram']
        flv_disk = flv_id['disk']
        # TODO: Parse SCS names for further information
        # TODO: Parse eventual extra_specs
        flavors.append(flavor(flv_name, flv_cores, flv_ram/1024, flv_disk))
    return flavors

def yaml_output_flavors(flavors):
    data = []
    for flv in flavors:
         data.append(dict(
            Name = flv.name,
            Specs = dict (
                    cores =  flv.cpu.cores,
                    memGB =  flv.mem.memGB,
                    diskGB = flv.disk.sizeGB
                )
            ))
    with open(ofile, 'a') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


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
    print(mycloud)
    flavors = get_openstack_flavors()
    yaml_output_flavors(flavors)


if __name__ == "__main__":
    main(sys.argv)

# vim:fenc=utf-8:ts=4:sw=4:noet:sts=4:ai
