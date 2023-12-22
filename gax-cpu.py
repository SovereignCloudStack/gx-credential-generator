#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# gax-cpu.py
"""
These classes reflect the Gaia-X view on physical infra

(c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022 - 6/2022
SPDX-License-Identifier: EPL-2.0
"""


class CPU:
    "CPU abstraction according to Gaia-X attributes"
    def __init__(self):
        "c'tor setting all vals to defaults"
        # Gaia-X attrs
        self.numberOfCores = 0
        self.numberOfThreads = 0
        self.frequency = 0
        self.boostFrequency = 0
        self.cacheSize = 0
        # This would not be interesting typically
        self.allowedSocket = ""
        # Virt. attrs -- not in GaX
        self.dedicatedCore = False
        self.dedicatedThread = False
        self.limitOversubscr = False


class MEM:
    "RAM of an instance"
    def __init__(self):
        "c'tor setting all vals to defaults"
        self.memGB = 0
        self.ECC = True
        