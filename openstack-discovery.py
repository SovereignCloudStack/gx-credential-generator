#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# openstack-discovery.py
"""
Talk to OpenStack APIs to discover environment
Save discovered information in classes that reflect G-X attributes
These can then be dumped as YAML or as Gaia-X JSON-LD Self-Description.

(c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022 - 6/2022
(c) Mathias Fechner <fechner@osism.tech>, 3/2022
SPDX-License-Identifier: EPL-2.0
"""

import sys
import os
import getopt
import json
import yaml
import openstack

# Global variables
if "OS_CLOUD" in os.environ:
    cloud = os.environ["OS_CLOUD"]
else:
    cloud = ""
debug = False
outjson = False
ofile = '/dev/stdout'
indent = "  "
uriprefix = "https://scs.community/sd/"
gxid = "test"
svcname = "SCS Test"


def valtype(val, typ='xsd:string'):
    "Wrapper to return dict pairs with @value and @type as needed in JSON-LD"
    return {'@value': val, '@type': typ}


def appenddicts(dct1, *kwd):
    "Return dict d1 with items from kwd added"
    dct = dct1
    for k in kwd:
        dct.update(k)
    return dct


def versinfo(connprox, stype, region):
    "Get list of supported versions and microversions from OS service"
    vrdata = connprox.get_all_version_data(region_name=region)
    for reg in vrdata:
        try:
            vdata = vrdata[reg]["public"]
            break
        except AttributeError:
            pass
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
    def __init__(self, dct, regfilter):
        self.id = dct["id"]
        self.region = regfilter
        self.ep = None
        # interface: we only look at public
        for ept in dct["endpoints"]:
            if ept["interface"] == "public" and (not regfilter or ept["region_id"] == regfilter):
                self.ep = ept["url"]
        self.type = dct["type"]
        self.name = dct["name"]
        self.consumed = False

    def __str__(self):
        "textual representation"
        return f"{self.type}|{self.name}|{self.ep}"

    # def __repr__(self):
    #     return str(self)


class osService:
    "A generic openStack service, with a proxy connection object from SDK"
    def __init__(self, conn, stype, name, region, prj_id, ept, quiet=True):
        "c'tor for the OpenStack service to be caled by subclasses"
        self.fulltype = stype
        if stype[-2] == 'v' and stype[-1].isnumeric():
            stype = stype[:-2]
        stype = stype.replace('-', '_')
        self.stype = stype
        self.region = region
        self.conn = None
        self.apiver = None
        self.ep = None
        self.versdata = None
        self.extensions = None
        self.azs = None
        try:
            if debug:
                print(f"#INFO: Creating Conn for {stype}:{name}", file=sys.stderr)
            self.conn = conn.__getattribute__(stype)
            self.conn.service_name = name
            self.conn.region_name = region
            self.apiver = self.conn.get_api_major_version()
        except Exception as exc:
            if not quiet:
                print(f"#ERROR: No service proxy of type {stype} in SDK.\n{exc}", file=sys.stderr)
            # return
        if self.conn is None or (self.conn.version is None and self.apiver is None):
            print(f"#WARNING: Skipping over {stype} b/c it advertizes no version", file=sys.stderr)
            self.conn = None
            return
        try:
            self.ep = self.conn.get_endpoint().replace(prj_id, "${OS_PROJECT_ID}")
        except Exception:  # as exc:
            if stype == "identity":
                self.ep = conn.auth["auth_url"]
            else:
                if self.conn:
                    print(f"#ERROR: No endpoint found for service {self.stype} in region {region}",
                          file=sys.stderr)
                    # raise exc
                    self.conn = None
                    return
        self.versdata = versinfo(self.conn, self.fulltype, region)
        try:
            # self.extensions = list(map(lambda x: x.name, self.conn.extensions()))
            self.extensions = list(map(lambda x: x.alias, self.conn.extensions()))
        except Exception as exc:
            if not quiet:
                print(f"#WARNING: Service {self.fulltype} does not support getting extensions.\n{exc}",
                      file=sys.stderr)
        try:
            self.azs = list(filter(lambda x: x.state['available'] is True, self.conn.availability_zones()))
        except Exception:
            try:
                self.azs = list(filter(lambda x: x.state == 'available', self.conn.availability_zones()))
            except Exception as exc:
                if not quiet:
                    print(f"#WARNING: Service {self.fulltype} does not support getting AZs.\n{exc}",
                          file=sys.stderr)
        # FIXME: We are not using ept, is that right?

    def values(self):
        "return dict representing stored values"
        dct = {self.stype: {"name": self.conn.service_name,
                            "endpoint": self.ep,
                            # "region": self.region,
                            "versions": self.versdata}}
        if self.extensions:
            dct[self.stype]["extensions"] = self.extensions
        if self.azs:
            # dct[self.stype]["availability_zones"] = list(map(lambda x: x.name, self.azs))
            dct[self.stype]["availability_zones"] = [x.name for x in self.azs]
        return dct

    def __str__(self):
        "textual representation"
        return str(self.values())


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

    def values(self):
        ydct = dict(name = self.name,
                    numberOfvCPUs = self.numberOfvCPUs,
                    ramSize = dict(Value=self.ramSize/1024, Unit='GiB'))
        if self.diskSize:
            ydct['diskSize'] = dict(Value=self.diskSize, Unit='GB')
        # TODO: cpuType, cpuGen, diskType output
        return ydct


class osCompute(osService):
    "Abstraction for compute service (nova)"
    svcID = ("compute", "computev2", "compute_legacy")

    # def __init__(self, conn, region="RegionOne"):
    def __init__(self, conn, stype, name, region, prj_id, ept):
        super().__init__(conn, stype, name, region, prj_id, ept, False)
        self.flavors = self.get_openstack_flavors()

    def values(self):
        dct = super().values()
        dct[self.stype]["flavors"] = self.flavors
        return dct

    def get_openstack_flavors(self):
        """Use OpenStack conn (global var conn) to get flavor list from
           compute service. Populate flavor list."""
        flvs = []
        for flv_id in self.conn.flavors(id):
            flvs.append(osFlavor(flv_id).values())
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

    def __init__(self, conn, stype, name, region, prj_id, ept):
        super().__init__(conn, stype, name, region, prj_id, ept, True)
        self.voltypes = list(self.conn.types())
        # TODO: Fixup azs and exts
        req = self.conn.request('/extensions', 'GET')
        ext = json.loads(req.text)["extensions"]
        self.extensions = list(map(lambda x: x["alias"], ext))
        req = self.conn.request('/os-availability-zone', 'GET')
        azs = json.loads(req.text)["availabilityZoneInfo"]
        # self.azs = list(map(lambda x: azInfo(x), filter(lambda x: x["zoneState"]["available"] is True, azs)))
        self.azs = [azInfo(x) for x in azs if x["zoneState"]["available"]]

    def values(self):
        dct = super().values()
        # dct[self.stype]["volume_types"] = list(map(
        #     lambda x: {"name": x.name, "public": x.is_public}, self.voltypes))
        dct[self.stype]["volume_types"] = [{"name": x.name, "public": x.is_public} for x in self.voltypes]
        return dct


class osLoadBalancer(osService):
    "osService specialization for load balancers"
    svcID = ("load_balancer", "load-balancer")

    def __init__(self, conn, stype, name, region, prj_id, ept):
        super().__init__(conn, stype, name, region, prj_id, ept, True)
        try:
            self.flavors = self.conn.flavors()
            self.flavors = list(map(lambda x: {"name": x.name, "description": x.description},
                                    filter(lambda x: x.is_enabled, self.flavors)))
        except Exception as exc:
            print(exc, file=sys.stderr)
            self.flavors = None

    def values(self):
        dct = super().values()
        if self.flavors:
            dct[self.stype]["flavors"] = self.flavors
        return dct

# TODO: List of public images with properties


# TODO: Network class needs more detection; have AZs for routers and nets, endpoint not per region
class osNetwork(osService):
    "osService specialization for network"
    svcID = ("network")

    def __init__(self, conn, stype, name, region, prj_id, ept):
        super().__init__(conn, stype, name, region, prj_id, ept, True)
        self.ep = ept
    # TODO: Fixup AZs


# Known-classes
OSClasses = [osCompute, osVolume, osLoadBalancer, osNetwork]


def getdocshash(url, hashmeth):
    "Calculate hash from terms document at URL"
    import requests
    req = requests.get(url)
    req.raise_for_status()
    # req.raw.decode_content = True
    hval = hashmeth(req.content)   # .text would be better for HTML
    return hval.hexdigest()


def getdocsha512(url):
    "Calculate SHA512 from terms document at URL"
    import hashlib
    return getdocshash(url, hashlib.sha512)


def getdocsha256(url):
    "Calculate SHA512 from terms document at URL"
    import hashlib
    return getdocshash(url, hashlib.sha256)


def gxjsonldheader():
    "Dict to generate JSON-LD header for Gaia-X SDs"
    import gx_context
    import time
    gxsvo = "gx-service-offering:"
    jout = gx_context.gxcontext
    jout.update(gx_context.gxtype)
    myid = uriprefix + "gxserviceIaaSOfferingOpenStack-" + gxid + f"-{time.time()}.json"
    jout["@id"] = myid
    provby   = valtype(uriprefix + "participant.json")
    name     = valtype("OpenStack IaaS Service " + svcname)
    # svcmodel = valtype("pay per use")
    webadr   = valtype(uriprefix, 'xsd:anyURI')
    termsdoc = uriprefix + "terms.pdf"
    # calc sha256
    termssha = getdocsha256(termsdoc)
    tandc    = {gxsvo + "url": valtype(uriprefix + "terms.pdf"),
                gxsvo + "hash": valtype(termssha)}
    # TODO: dependsOn
    # TODO: aggregationOf
    jout["credentialSubject"] = {
        "id": myid,
        gxsvo + "providedBy": provby,
        gxsvo + "name": name,
        gxsvo + "webAddress": webadr,
        gxsvo + "TermsAndConditions": tandc,
        gxsvo + "SDAutoGeneratedBy": "https://github.com/SovereignCloudStack/gx-self-description-generator/"}
    return jout


class nonOSService:
    "Non-OpenStack services listed in the service catalogue"
    def __init__(self, stype, name, url):
        self.stype = stype
        self.name = name
        self.ep = url

    def values(self):
        "return dict with stored values"
        return {self.stype: {"name": self.name, "endpoint": self.ep}}


class osCloud:
    "Abstraction for openStack cloud with all its services"
    def __init__(self, conn):
        # import copy
        self.conn = conn
        self.auth = conn.auth
        self.regions = list(conn.identity.regions())
        # Create per region service catalogs
        self.regcat = {}
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
                        print(f"#DEBUG: Region {reg} added OS Svc {newsvc}" % (reg, newsvc), file=sys.stderr)
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

    def values(self):
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
        if not outjson:
            return {"openstack": inner}
        jout = gxjsonldheader()
        jout["credentialSubject"]["gxsvo+OpenStackService"] = inner
        return jout

    def __str__(self):
        # print(self.values())
        if outjson:
            return json.dumps(self.values(), indent=indent)
        return yaml.dump(self.values(), default_flow_style=False)


def usage(err=1):
    "output help"
    print("Usage: openstack-discovery.py [options]", file=sys.stderr)
    print("Options: -g/--gaia-x: output Gaia-X JSON-LD instead of YAML (YAML is default)")
    print("         -j/--json:   output compact Gaia-X JSON-LD instead of YAML")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print("         -c CLOUD/--os-cloud=CLOUD: use OpenStack cloud CLOUD (default: $OS_CLOUD)")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print("         -u URI/--uri=URI: use URI prefix. URI/particpant.json and URI/terms.pdf needed")
    print("         -n NAME/--name=NAME: use name in self description")
    print("         -i ID/--gxid=ID: use ID in self description")
    print("         -t TMO/--timeout=TMO: Timeout for the API connections/requests")
    if not cloud:
        print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    sys.exit(err)


def main(argv):
    "Entry point for main program"
    global cloud, outjson, indent
    global uriprefix, gxid, svcname, debug
    global ofile
    timeout = 12
    try:
        opts, args = getopt.gnu_getopt(argv[1:], "c:f:hgjdu:n:i:t:",
                                       ("os-cloud=", "file=", "help", "gaia-x", "json",
                                        "debug", "uri=", "name=", "id=", "timeout="))
    except getopt.GetoptError:  # as exc:
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
        elif opt[0] == "-d" or opt[0] == "--debug":
            debug = True
        elif opt[0] == "-g" or opt[0] == "--gaia-x":
            outjson = True
        elif opt[0] == "-t" or opt[0] == "--timeout":
            timeout = int(opt[1])
        elif opt[0] == "-j" or opt[0] == "--json":
            outjson = True
            indent = None
    if args:
        usage(1)
    if not cloud:
        print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    conn = openstack.connect(cloud=cloud, timeout=timeout)
    conn.config.config['api_timeout'] = timeout
    mycloud = osCloud(conn)
    if ofile == "/dev/stdout":
        print(mycloud, file=sys.stdout)
    else:
        print(mycloud, file=open(ofile, 'a', encoding="UTF-8"))


if __name__ == "__main__":
    main(sys.argv)
