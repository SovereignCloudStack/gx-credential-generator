#!/usr/bin/python3
#
# gax-cpu.py
#
# These classes reflect the Gaia-X view on physical infra
#
# (c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022 - 6/2022
# SPDX-License-Identifier: EPL-2.0


class CPU:
    def __init__(self):
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
    def __init__(self):
        self.memGB = 0
        self.ECC = True
