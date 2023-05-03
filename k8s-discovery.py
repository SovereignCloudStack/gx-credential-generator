#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# k8s-discovery.py
"""
Talk to Kubernetes API server to discover the cluster properties.
Save discovered information in classes that reflect G-X attributes
These can then be dumped as YAML or as Gaia-X JSON-LD Self-Description.

(c) Kurt Garloff <garloff@osb-alliance.com>, 5/2023
SPDX-License-Identifier: EPL-2.0
"""

import os
import sys
# import getopt
from kubernetes import client, config


# global settings, not yet used
kubeconfig = None
kubecontext = None


def main(argv):
    "main entry point"

    # TODO:
    # - Command line parsing
    # - Use kubeconfig
    # - Use kubecontext

    # This is straight from https://github.com/kubernetes-client/python
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == "__main__":
    main(sys.argv)
