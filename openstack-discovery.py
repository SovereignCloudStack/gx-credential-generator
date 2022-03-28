#!/usr/bin/python3
#
# openstack-discovery.py
#
# Talk to OpenStack APIs to discover environment
# Save dsicovered information in classes that reflect G-X attributes
# These can then be dumped as YAMLs or other forms
#
# (c) Kurt Garloff <garloff@osb-alliance.com>, 3/2022
# SPDX-License-Identifier: EPL-2.0

import sys, os
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
	def __init(self):
		self.memGB = 0
		self.ECC = true


def usage():
	print("Usage: openstack-discovery.py [options]", file=sys.stderr)
	print("You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
	sys.exit(1)


def main(argv):
	usage()

if __name__ == "__main__":
	main(sys.argv)
