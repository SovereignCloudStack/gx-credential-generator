#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# gx-sd-generator.py
"""Script to generate Gaia-X JSON-LD for credentials.
  Uses openstack-discovery.py and k8s-discovery.py to
  collect the data.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
SPDX-License-Identifier: EPL-2.0
"""

import getopt
import importlib
import json
import sys
from time import time

import yaml

ostack = importlib.import_module("openstack-discovery")
k8s = importlib.import_module("k8s-discovery")

# Global variables
debug = False
outjson = False
wizard = False
ofile = "/dev/stdout"
indent = "  "
uriprefix = "https://scs.community/sd/"
gxid = "test"
svcname = "SCS Test"
gxsvo = "gx:"
policy = "IaaS Test"


def valtype(val, typ="xsd:string"):
    "Wrapper to return dict pairs with @value and @type as needed in JSON-LD"
    return {"@value": val, "@type": typ}


def getdocshash(url, hashmeth):
    "Calculate hash from terms document at URL"
    import requests

    req = requests.get(url)
    req.raise_for_status()
    # req.raw.decode_content = True
    hval = hashmeth(req.content)  # .text would be better for HTML
    return hval.hexdigest()


def getdocsha512(url):
    "Calculate SHA512 from terms document at URL"
    import hashlib

    return getdocshash(url, hashlib.sha512)


def getdocsha256(url):
    "Calculate SHA256 from terms document at URL"
    import hashlib

    return getdocshash(url, hashlib.sha256)


def gettandc():
    "Generate Terms and Conditions structure"
    return {
        "@type": gxsvo + "SOTermsAndConditions",
        gxsvo + "URL": valtype(uriprefix + "terms.pdf"),
        gxsvo + "hash": getdocsha256(uriprefix + "terms.pdf"),
    }


def getdae():
    "Generate dataAccountExport structure"
    return {
        "@type": gxsvo + "dataAccountExport",
        gxsvo + "requestType": "API",
        gxsvo + "accessType": "digital",
        gxsvo + "formatType": "application/json",
    }


def getprovby():
    "Generate providedBy structure"
    # import requests
    # req = requests.get(uriprefix + "participant.json")
    # req.raise_for_status()
    # return req.json()["selfDescriptionCredential"]["credentialSubject"]
    return {
        "@id": "https://scs.community/LegalPerson-khnps661nnlgghoq4is18",
        "@type": gxsvo + "LegalParticipant",
        gxsvo + "legalAddress": {
            "@type": gxsvo + "legalAddress",
            gxsvo + "countrySubdivisionCode": valtype("DE-BE"),
        },
        gxsvo + "headquarterAddress": {
            "@type": gxsvo + "legalAddress",
            gxsvo + "countrySubdivisionCode": valtype("DE-BE"),
        },
        gxsvo + "legalRegistrationNumber": {
            "@type": gxsvo + "legalRegistrationNumber",
            # At least one of taxID, vatID, EUID, EORI or leiCode must be defined.
            gxsvo + "leiCode": valtype("123"),
            gxsvo + "vatID": valtype("123"),
            gxsvo + "EORI": valtype("123"),
            gxsvo + "EUID": valtype("123"),
            gxsvo + "taxID": valtype("123"),
        },
    }


def gxjsonldheader():
    "Dict to generate JSON-LD header for Gaia-X SDs"
    import gx_context

    jout = gx_context.gxcontext
    jout.update(gx_context.gxtype)
    myid = uriprefix + "gxserviceIaaSOfferingOpenStack-" + gxid + f"-{int(time())}.json"
    jout["@id"] = myid
    if wizard:
        del jout["@context"]
        jout["id"] = jout.pop("@id")
        jout["type"] = jout.pop("@type")

    name = valtype("OpenStack IaaS Service " + svcname)
    # svcmodel = valtype("pay per use")
    webadr = valtype(uriprefix, "xsd:anyURI")

    # TODO: dependsOn
    # TODO: aggregationOf
    jout[gxsvo + "providedBy"] = getprovby()
    jout[gxsvo + "policy"] = policy
    jout[gxsvo + "name"] = name
    jout[gxsvo + "webAddress"] = webadr
    jout[gxsvo + "termsAndConditions"] = gettandc()
    jout[gxsvo + "dataAccountExport"] = getdae()
    jout[gxsvo + "SDAutoGeneratedBy"] = (
        "https://github.com/SovereignCloudStack/gx-credential-generator/"
    )
    return jout


def usage(err=1):
    "output help"
    print("Usage: gx-sd-generator.py [options] [command]", file=sys.stderr)
    print(
        "Options: -g/--gaia-x: output Gaia-X JSON-LD instead of YAML (YAML is default)"
    )
    print(
        "         -w/--wizard: remove @context and '@' from @id and @type in generated SD to use it in Gaia-X Wizard"
    )
    print("         -j/--json:   output compact Gaia-X JSON-LD instead of YAML")
    print(
        "         -f FILE/--file=FILE: write output to FILE_time.yaml/json (default: stdout)"
    )
    print(
        "         -c CLOUD/--os-cloud=CLOUD: use OpenStack cloud CLOUD (default: $OS_CLOUD)"
    )
    print(
        "         -k KCFG/--kubeconfig=KCFG: use kubeconfig file KCFG (default: $KUBECONFIG)"
    )
    print("         -K KCTX/--context=KCTX: use kubeconfig context KCTX")
    print("         -f FILE/--file=FILE: write output to FILE (default: stdout)")
    print(
        "         -u URI/--uri=URI: use URI prefix. URI/particpant.json and URI/terms.pdf needed"
    )
    print("         -n NAME/--name=NAME: use name in self description")
    print("         -i ID/--gxid=ID: use ID in self description")
    print("         -t TMO/--timeout=TMO: Timeout for the API connections/requests")
    print("Command: openstack: collect OpenStack data (default)")
    print("         k8s:       collect Kubernetes data")
    sys.exit(err)


def output(mycloud=None, myk8s=None):
    "Compose string to be output"
    if outjson:
        dct = gxjsonldheader()
        if mycloud:
            prefix = "ex:"
            dct[prefix + "OpenStackService"] = mycloud.values(prefix=prefix)
        if myk8s:
            dct[gxsvo + "K8sClusterService"] = myk8s.values()
        return json.dumps(dct, indent=indent)
    dct = {}
    if mycloud:
        dct["openstack"] = mycloud.values()
    if myk8s:
        dct["k8sCluster"] = myk8s.values()
    yaml.emitter.Emitter.process_tag = noop
    return yaml.dump(dct, default_flow_style=False)


def noop(self, *args, **kw):
    pass


def main(argv):
    "Entry point for main program"
    global debug, ofile, outjson, indent, wizard
    global uriprefix, gxid, svcname
    timeout = 12
    mycloud = None
    myk8s = None
    # Defaults for OpenStack and K8s are set by imports
    # Arg parser
    try:
        args: list[str]
        opts, args = getopt.gnu_getopt(
            argv[1:],
            "c:f:hgwjdu:n:i:t:k:K:",
            (
                "os-cloud=",
                "file=",
                "help",
                "gaia-x",
                "wizard",
                "json",
                "debug",
                "uri=",
                "name=",
                "id=",
                "timeout=",
                "kubeconfig=",
                "context=",
            ),
        )
    except getopt.GetoptError:  # as exc:
        usage(1)
    for opt in opts:
        if opt[0] == "-h" or opt[0] == "--help":
            usage(0)
        elif opt[0] == "-c" or opt[0] == "--os-cloud":
            ostack.cloud = opt[1]
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
            ostack.outjson = True
        elif opt[0] == "-w" or opt[0] == "--wizard":
            wizard = True
        elif opt[0] == "-t" or opt[0] == "--timeout":
            timeout = int(opt[1])
        elif opt[0] == "-j" or opt[0] == "--json":
            outjson = True
            ostack.outjson = True
            indent = None
        elif opt[0] == "-k" or opt[0] == "--kubeconfig":
            k8s.config = opt[1]
        elif opt[0] == "-K" or opt[0] == "--context":
            k8s.context = opt[1]

    if not args or args[0] == "openstack":  # default
        if ostack.cloud:
            conn = ostack.ostackconn(ostack.cloud, timeout)
            mycloud = ostack.osCloud(conn)
    elif args[0] == "k8s":
        if k8s.config:
            conn = k8s.kubeconn(k8s.config, k8s.context, timeout)
            # conn = k8s.kubeconn(k8s.config, ctx)
            myk8s = k8s.KubeCluster(conn)
    else:
        usage(1)
    if not mycloud and not myk8s:
        usage(1)
    if ofile == "/dev/stdout":
        print(output(mycloud, myk8s), file=sys.stdout)
    else:
        if ostack.outjson:
            file_name = f"{ofile}_{int(time())}.json"
        else:
            file_name = f"{ofile}_{int(time())}.yaml"
        print(output(mycloud, myk8s), file=open(file_name, mode="a", encoding="UTF-8"))


if __name__ == "__main__":
    main(sys.argv)
