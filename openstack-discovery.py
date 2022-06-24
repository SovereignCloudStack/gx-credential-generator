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

def valtype(val, tp = 'xsd:string'):
    "Wrapper to return dict pairs with @value and @type as needed in JSON-LD"
    return { '@value': val, '@type': tp }

def appenddicts(d1, *kwd):
    "Return dict d1 with items from kwd added"
    d = d1
    for k in kwd:
        d.update(k)
    return d


def versinfo(connprox, stype, region = "RegionOne"):
    "Get list of supported versions and microversions from OS service"
    vdata = connprox.get_all_version_data()[region]["public"]
    for keys in vdata:
        versdata = vdata[keys]
        if keys == stype:
            break
    vinfo = list(map(lambda x: {'version': x.version, 'url': x.url,
                                'status': x.status,
                                'min_microversion': x.min_microversion,
                                'max_microversion': x.max_microversion},
                      filter(lambda x: x.max_microversion, versdata)))
    vinfo.extend(list(map(lambda x: {'version': x.version, 'url': x.url, 'status': x.status},
                          filter(lambda x: not x.max_microversion, versdata))))
    return vinfo


class osServiceCat:
    "OpenStack service catalog"
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

class osService:
    "A generic openStack service, with a proxy connection object from SDK"
    def __init__(self, conn, stype, name, region = "RegionOne", quiet = True):
        self.fulltype = stype
        if stype[-2] == 'v' and stype[-1].isnumeric():
            stype = stype[:-2]
        stype = stype.replace('-', '_')
        self.stype = stype
        try:
            self.conn = conn.__getattribute__(stype)
            self.conn.service_name = name
        except AttributeError as e:
            self.conn = None
            if not quiet:
                print("No service proxy of type %s in SDK.\n%s" % (stype, e))
            return
        try:
            self.ep = self.conn.get_endpoint().replace(conn.auth["project_id"], "${OS_PROJECT_ID}")
        except Exception as e:
            if stype == "identity":
                self.ep = conn.auth["auth_url"]
            else:
                if self.conn:
                    raise e
        self.versdata = versinfo(self.conn, self.fulltype, region)
        try:
            #self.extensions = list(map(lambda x: x.name, self.conn.extensions()))
            self.extensions = list(map(lambda x: x.alias, self.conn.extensions()))
        except Exception as e:
            self.extensions = None
            if not quiet:
                print("WARNING: Service %s does not support getting extensions.\n%s" % (self.fulltype, e))
        try:
            self.azs = list(filter(lambda x: x.state['available'] == True, self.conn.availability_zones()))
        except:
            self.azs = None
            try:
                self.azs = list(filter(lambda x: x.state == 'available', self.conn.availability_zones()))
            except Exception as e:
                if not quiet:
                    print("WARNING: Service %s does not support getting AZs.\n%s" % (self.fulltype, e))

    def __repr__(self):
        dct = { self.stype: { "name": self.conn.service_name,
                              "endpoint": self.ep,
                              "versions": self.versdata
                            }
              }
        if self.extensions:
            dct[self.stype]["extensions"] = self.extensions
        if self.azs:
            dct[self.stype]["availability_zones"] = list(map(lambda x: x.name, self.azs))
        return dct

class osFlavor:
    "Abstraction for flavors"
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

    def __repr__(self):
        ydct = dict(name = self.name,
                    numberOfvCPUs = self.numberOfvCPUs,
                    ramSize = dict(Value = self.ramSize/1024, Unit = 'GiB')
                )
        if self.diskSize:
            ydct['diskSize'] = dict(Value = self.diskSize, Unit = 'GB')
        # TODO: cpuType, cpuGen, diskType output
        return ydct

class osCompute(osService):
    svcID = ("compute", "computev2", "compute_legacy")
    #def __init__(self, conn, region="RegionOne"):
    def __init__(self, conn, stype, name, region="RegionOne"):
        super().__init__(conn, stype, name, region, False)
        self.flavors = self.get_openstack_flavors()
    def __repr__(self):
        dct = super().__repr__()
        dct[self.stype]["flavors"] = self.flavors
        return dct

    def get_openstack_flavors(self):
        """Use OpenStack conn (global var conn) to get flavor list from
           compute service. Populate flavor list."""
        flvs = list()
        for flv_id in self.conn.flavors(id):
            flvs.append(osFlavor(flv_id).__repr__())
            # TODO:
            # (a) parse extra specs if any
            # (b) parse SCS flavor names
        self.flavors = flvs
        return flvs

class azInfo:
    "Convert zoneXxx dict into class with Xxx attributes for availability zones"
    def __init__(self, dct):
        for key in dct:
            if key[:4] == "zone":
                newkey = key[4].lower() + key[5:]
            else:
                newkey = key
            self.__setattr__(newkey, dct[key])

class osVolume(osService):
    "osService specialization for volumes (cinderv3)"
    svcID = ("volumev3", "volumev2", "volume")
    def __init__(self, conn, stype, name, region="RegionOne"):
        super().__init__(conn, stype, name, region, True)
        self.voltypes = list(self.conn.types())
        # TODO: Fixup azs and exts
        r = self.conn.request('/extensions', 'GET')
        ext = json.loads(r.text)["extensions"]
        self.extensions = list(map(lambda x: x["alias"], ext))
        r = self.conn.request('/os-availability-zone', 'GET')
        azs = json.loads(r.text)["availabilityZoneInfo"]
        self.azs = list(map(lambda x: azInfo(x), filter(lambda x: x["zoneState"]["available"] == True, azs)))

    def __repr__(self):
        dct = super().__repr__()
        dct[self.stype]["volume_types"] = list(map(
            lambda x: { "name": x.name, "public": x.is_public }, self.voltypes))
        return dct

class osLoadBalancer(osService):
    "osService specialization for load balancers"
    svcID = ("load_balancer", "load-balancer")
    def __init__(self, conn, stype, name, region="RegionOne"):
        super().__init__(conn, stype, name, region, True)
        self.flavors = self.conn.flavors()
        self.flavors = list(map(lambda x: {"name": x.name, "description": x.description},
                        filter(lambda x: x.is_enabled, self.flavors)))
    def __repr__(self):
        dct = super().__repr__()
        dct[self.stype]["flavors"] = self.flavors
        return dct

## TODO: List of public images with properties

def getdocsha512(url):
    "Calculate SHA512 from terms document at URL"
    import requests, hashlib
    r = requests.get(url)
    r.raise_for_status()
    #r.raw.decode_content = True
    h = hashlib.sha512(r.content)   # .text would be better for HTML
    return h.hexdigest()


def gxjsonldheader():
    "Dict to generate JSON-LD header for Gaia-X SDs"
    import gx_context, time
    gxsvo = "gx-service-offering:"
    jout = gx_context.gxcontext
    jout.update(gx_context.gxtype)
    myid = uriprefix+"gxserviceIaaSOfferingOpenStack-"+gxid+"-%i.json" % time.time()
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
            gxsvo+"TermsAndConditions": tandc
            }
    return jout

class osCloud:
    "Abstraction for openStack cloud with all its services"
    def __init__(self, conn):
        self.conn = conn
        self.auth = conn.auth
        self.regions = list(conn.identity.regions())
        self.services = []
        for svc in conn.service_catalog:
            self.services.append(osServiceCat(svc))
        self.ostacksvc = {}
        handled = []
        region0 = self.regions[0].id
        # Iterate over service catalog
        for svc in self.services:
            if svc.type in (*handled, "compute_legacy", "cloudformation"):
                continue
            if svc.type in osCompute.svcID:
                newsvc = osCompute(conn, svc.type, svc.name, region0)
                handled.extend(osCompute.svcID)
            elif svc.type in osVolume.svcID:
                newsvc = osVolume (conn, svc.type, svc.name, region0)
                handled.extend(osVolume.svcID)
            elif svc.type in osLoadBalancer.svcID:
                newsvc = osLoadBalancer(conn, svc.type, svc.name, region0)
                handled.extend(osLoadBalancer.svcID)
            else:
                newsvc = osService(conn, svc.type, svc.name, region0)
                handled.extend((svc.type, newsvc.stype,))
                if svc.type == "orchestration":
                    handled.extend("cloudformation")

            if newsvc.conn:
                self.ostacksvc[newsvc.stype] = newsvc

    def __repr__(self):
        inner = { "regions": list(map(lambda x: x.id, self.regions)) }
        if outjson:
            inner["auth_url"] = valtype(self.auth["auth_url"], "xsd:anyURI")
        else:
            inner["auth_url"] = self.auth["auth_url"]
        for svckey in self.ostacksvc:
            svc = self.ostacksvc[svckey]
            inner = appenddicts(inner, svc.__repr__())
            if outjson:
                inner[svc.stype]["endpoint"] = valtype(svc.ep, "xsd:anyURI")
        if not outjson:
            return { "openstack": inner }
        else:
            jout = gxjsonldheader()
            jout["credentialSubject"]["gxsvo+OpenStackService"] = inner
            return jout

    def __str__(self):
        #print(self.__repr__())
        if outjson:
            return json.dumps(self.__repr__(), indent = indent)
        else:
            return yaml.dump(self.__repr__(), default_flow_style=False)


def usage(err = 1):
    print("Usage: openstack-discovery.py [options]", file=sys.stderr)
    print("Options: -g/--gaia-x: output Gaia-X JSON-LD instead of YAML (YAML is default)")
    print("         -j/--json:   output compact Gaia-X JSON-LD instead of YAML")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print("         -c CLOUD/--os-cloud=CLOUD: use OpenStack cloud CLOUD (default: $OS_CLOUD)")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print("         -u URI/--uri=URI: use URI prefix. URI/particpant.json and URI/terms.pdf needed")
    print("         -n NAME/--name=NAME: use name in self description")
    print("         -i ID/--gxid=ID: use ID in self description")
    if not cloud:
        print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    sys.exit(err)


def main(argv):
    global cloud, conn, outjson, indent
    global uriprefix, gxid, svcname
    global ofile
    try:
        opts, args = getopt.gnu_getopt(argv[1:], "c:f:hgju:n:i:", \
                ("os-cloud=", "file=", "help", "gaia-x", "json", "uri=", "name=", "id="))
    except getopt.GetoptError as exc:
        usage(1)
    for opt in opts:
        if opt[0] == "-h" or opt[0] == "--help":
            usage(0)
        elif opt[0] == "-c" or opt[0] == "--os-cloud":
            cloud = opt[1]
        elif opt[0] == "-f" or opt[0] == "--file":
            ofile = opt[1]
        elif opt[0] == "-u" or opt[0] == "--uri":
            uriprefix = opt[1]
        elif opt[0] == "-n" or opt[0] == "--name":
            svcname = opt[1]
        elif opt[0] == "-i" or opt[0] == "--id":
            gxid = opt[1]
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
