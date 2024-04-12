#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# gx-context.py
"""
Some settings for the JSON-LD SDs needed in Gaia-X

(c) Kurt Garloff <garloff@osb-alliance.com>, 6/2022
SPDX-License-Identifier: EPL-2.0
"""
gxcontext = {
    "@context": {
        "gx": "https://https://registry.lab.gaia-x.eu//v1$/gx#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    }
}
gxtype = {"@type": "gx:ServiceOffering"}
