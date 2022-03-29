#!/usr/bin/python3
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
import openstack
import yaml

# These should be moved to a helper file,
# to be used by OpenStack and also k8s discovery

class cpu:
	def __init__(self):
		# Gaia-X attrs
		self.cores = 0
		self.threads = 0
		self.freq = 0
		self.boostFreq = 0
		self.cache = 0
		# This would not be interesting typically
		self.socketType = ""
		# Virt. attrs
		self.dedicatedCore = false
		self.dedicatedThread = false
		self.limitOversubscr = false

class mem:
	def __init__(self):
		self.memGB = 0
		self.ECC = true

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


if "OS_CLOUD" in os.environ:
        cloud = os.environ["OS_CLOUD"]
else:
        cloud = ""

def main(argv):
        global cloud        
        try:
                opts, args = getopt.gnu_getopt(argv[1:], "c:h", ("os-cloud=", "help"))
        except getopt.GetoptError as exc:
	        usage(1)
        for opt in opts:
                if opt[0] == "-h" or opt[0] == "--help":
                        usage(0)
                elif opt[0] == "-c" or opt[0] == "--os-cloud":
                        cloud = opt[1]
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


if __name__ == "__main__":
	main(sys.argv)
