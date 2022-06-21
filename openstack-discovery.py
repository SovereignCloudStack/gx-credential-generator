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
import yaml, json

# Global variables
if "OS_CLOUD" in os.environ:
    cloud = os.environ["OS_CLOUD"]
else:
    cloud = ""
conn = None
outjson = False
ofile = '/dev/stdout'
indent = "  "
uriprefix = "https://scs.community/sd/"
gxid = "test"
svcname = "SCS Test"

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
    def __init__(self, conn):
        self.conn = conn
        self.flavors = self.get_openstack_flavors()

    def get_openstack_flavors(self):
        """Use OpenStack conn (global var conn) to get flavor list from
           compute service. Populate flavor list."""
        flvs = list()
        for flv_id in self.conn.compute.flavors(id):
            flvs.append(osFlavor(flv_id).toyaml())
            # TODO:
            # (a) parse extra specs if any
            # (b) parse SCS flavor names
        self.flavors = flvs
        return flvs

def valtype(val, tp = 'xsd:string'):
    return { '@value': val, '@type': tp }

def appenddicts(d1, *kwd):
    d = d1
    for k in kwd:
        d.update(k)
    return d

def getdocsha512(url):
    import requests, hashlib
    r = requests.get(url)
    r.raise_for_status()
    #r.raw.decode_content = True
    h = hashlib.sha512(r.content)   # .text would be better for HTML
    return h.hexdigest()


def gxjsonld(cld):
    import gx_context
    gxsvo = "gx-service-offering:"
    jout = gx_context.gxcontext
    jout.update(gx_context.gxtype)
    myid = uriprefix+"gxserviceIaaSOfferingOpenStack-"+gxid+".json"
    jout["@id"] = myid
    provby   = valtype(uriprefix+"participant.json")
    name     = valtype("OpenStack IaaS Service " + svcname)
    #svcmodel = valtype("pay per use")
    webadr   = valtype(uriprefix, 'xsd:anyURI')
    termsdoc = uriprefix+"terms.pdf"
    # calc sha512
    termssha = getdocsha512(termsdoc)
    tandc    = { gxsvo+"url": valtype(uriprefix+"terms.pdf"),
                 gxsvo+"hash": valtype(termssha) }
    #TODO: dependsOn
    #TODO: aggregationOf
    jout["credentialSubject"] = {
            "id": myid,
            gxsvo+"providedBy": provby,
            gxsvo+"name": name,
            gxsvo+"webAddress": webadr,
            gxsvo+"TermsAndConditions": tandc,
            gxsvo+"OpenStackService": { gxsvo+"compute": { gxsvo+"flavor": cld.compute.flavors }}
            }
    return jout


class osCloud:
    def __init__(self, conn):
        self.conn = conn
        self.regions = list(conn.identity.regions())
        self.services = []
        #self.services = list(conn.identity.services())
        #self.services = conn.list_services()
        for svc in conn.service_catalog:
            self.services.append(osService(svc))
        self.compute = osCompute(conn)
        #print(conn)
    def __str__(self):
        strg = ""
        if not outjson:
            strg = "#Regions: %s\n#Services\n#%s\n" % (self.regions, self.services)
        if self.compute.flavors:
            if not outjson:
                yout = dict(compute = dict(flavor = self.compute.flavors))
                strg += yaml.dump(yout, default_flow_style=False)
            else:
                #jout = dict(compute = dict(flavor = self.compute.flavors))
                jout = gxjsonld(self)
                strg += json.dumps(jout, indent = indent)

        return strg


def usage(err = 1):
    print("Usage: openstack-discovery.py [options]", file=sys.stderr)
    print("Options: -g/--gaia-x: output Gaia-X JSON-LD instead of YAML (YAML is default)")
    print("         -j/--json:   output compact Gaia-X JSON-LD instead of YAML")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print("         -c CLOUD/--os-cloud=CLOUD: use OpenStack cloud CLOUD (default: $OS_CLOUD)")
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


def main(argv):
    global cloud, conn, outjson, indent
    global ofile
    try:
        opts, args = getopt.gnu_getopt(argv[1:], "c:f:hgj", ("os-cloud=", "file", "help", "gaia-x", "json"))
    except getopt.GetoptError as exc:
        usage(1)
    for opt in opts:
        if opt[0] == "-h" or opt[0] == "--help":
            usage(0)
        elif opt[0] == "-c" or opt[0] == "--os-cloud":
            cloud = opt[1]
        elif opt[0] == "-f" or opt[0] == "--file":
            ofile = opt[1]
        elif opt[0] == "-g" or opt[0] == "--gaia-x":
            outjson = True
        elif opt[0] == "-j" or opt[0] == "--json":
            outjson = True
            indent = None
    if args:
        usage(1)
    if not cloud:
        print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    conn = openstack.connect(cloud=cloud)
    mycloud = osCloud(conn)
    print(mycloud, file = open(ofile, 'a'))



if __name__ == "__main__":
    main(sys.argv)

# vim:fenc=utf-8:ts=4:sw=4:noet:sts=4:ai
