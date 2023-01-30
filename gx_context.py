#!/usr/bin/python3
# vim: set ts=4 sw=4 et:
#
# gx-context.py
"""
Some settings for the JSON-LD SDs needed in Gaia-X

(c) Kurt Garloff <garloff@osb-alliance.com>, 6/2022
SPDX-License-Identifier: EPL-2.0
"""

gxcontext = {"@context":
             ["http://www.w3.org/ns/shacl#",
              "http://www.w3.org/2001/XMLSchema#",
              "http://w3id.org/gaia-x/resource#",
              "http://w3id.org/gaia-x/participant#",
              "http://w3id.org/gaia-x/service-offering#"]}

gxtype = {"@type":
          ["VerifiableCredential",
           "ServiceOfferingExperimental"]}
