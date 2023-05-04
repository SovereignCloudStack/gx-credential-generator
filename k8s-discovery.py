#!/usr/bin/env python3
# vim: set ts=4 sw=4 et:
#
# openstack-discovery.py
"""
Talk to OpenStack APIs to discover environment
Save discovered information in classes that reflect G-X attributes
These can then be dumped as YAML or as Gaia-X JSON-LD Self-Description.

(c) Tecnalia: Raúl Miñón, Ana I. Torre, Gorka Benguria, Gorka Zarate, Juan López de Armentia  <raul.minon@tecnalia.com>, 3/2023 - 4/2023
SPDX-License-Identifier: EPL-2.0
"""

import os
import sys

# import openstack
from kubernetes import client, config as cfg

# Global variables
if "KUBECONFIG" in os.environ:
    config = os.environ["KUBECONFIG"]
else:
    config = ""
debug = False
outjson = False
ofile = '/dev/stdout'
indent = "  "


class ContainerVolume:
    def __init__(self, mount_path, v_name, read_only):
        self.mount_path = mount_path
        self.v_name = v_name
        self.read_only = read_only


class ContainerPort:
    def __init__(self, container_port, port_name, protocol, port_host_ip, host_port):
        self.container_port = container_port
        self.port_name = port_name
        self.protocol = protocol
        self.port_host_ip = port_host_ip
        self.port_host_port = host_port


class KubeContainer:
    def __init__(self, env, c_image, command, image_pull_policy, c_name, ports, volumes):
        self.env = env
        self.c_image = c_image
        self.command = command
        self.image_pull_policy = image_pull_policy
        self.c_name = c_name
        self.ports = ports
        self.volumes = volumes


class KubeNodeCapacity:

    def __init__(self, cpu, ephemeral_storage, hugepages_1Gi, hugepages_2Mi, memory, pods):
        self.cpu = cpu
        self.ephemeral_storage = ephemeral_storage
        self.hugepages_1Gi = hugepages_1Gi
        self.hugepages_2Mi = hugepages_2Mi
        self.memory = memory
        self.pods = pods


class KubeNode():
    def __init__(self, hostname, internal_ip, capacity):
        self.hostname = hostname
        self.internal_ip = internal_ip
        self.capacity = capacity


class KubePod:
    def __init__(self, host_ip, pod_i_ps, phase, start_time, qos_class, image, image_id, name, namespace, labels, uid,
                 containers):
        self.host_ip = host_ip
        self.pod_i_ps = pod_i_ps
        self.phase = phase
        self.start_time = start_time
        self.qos_class = qos_class
        self.image = image
        self.image_id = image_id
        self.name = name
        self.namespace = namespace
        self.labels = labels
        self.uid = uid
        self.containers = containers


class KubeCluster:
    "Abstraction for openStack cloud with all its services"

    def __init__(self, conn):
        # import copy
        self.conn = conn
        # self.auth = conn.auth
        nodes = conn.list_node()

        api_version = nodes.api_version
        metadata = nodes.metadata
        kube_gaia = {}
        self.metadata = metadata
        self.api_version = api_version
        self.kube_nodes = []
        for node in nodes.items:
            addresses = node.status.addresses
            cap = node.status.capacity
            capacity = KubeNodeCapacity(cap['cpu'], cap['ephemeral-storage'], cap['hugepages-1Gi'],
                                        cap['hugepages-2Mi'], cap['memory'], cap['pods'])

            hostname = None
            internal_ip = None
            for address in addresses:
                if address.type == 'Hostname':
                    hostname = address.address
                elif address.type == 'InternalIP':
                    internal_ip = address.address
            self.kube_nodes.append(KubeNode(hostname, internal_ip, capacity))
        pods = conn.list_pod_for_all_namespaces(watch=False)
        self.kube_pods = []
        for pod in pods.items:
            print("%s\t%s\t%s" % (pod.status.pod_ip, pod.metadata.namespace, pod.metadata.name))
            host_ip = pod.status.host_ip
            pod_i_ps = pod.status.pod_i_ps
            phase = pod.status.phase
            start_time = pod.status.start_time
            qos_class = pod.status.qos_class
            image = pod.status.container_statuses[0].image
            image_id = pod.status.container_statuses[0].image_id
            name = pod.metadata.name
            namespace = pod.metadata.namespace
            labels = pod.metadata.labels
            uid = pod.metadata.uid
            containers = []
            for container in pod.spec.containers:
                env = container.env
                c_image = container.image
                command = container.command
                image_pull_policy = container.image_pull_policy
                c_name = container.name
                ports = []
                if container.ports:
                    for port in container.ports:
                        container_port = port.container_port
                        port_name = port.name
                        protocol = port.protocol
                        port_host_ip = port.host_ip
                        host_port = port.host_port
                        ports.append(ContainerPort(container_port, port_name, protocol, port_host_ip, host_port))
                volumes = []
                if container.volume_mounts:
                    for volume in container.volume_mounts:
                        mount_path = volume.mount_path
                        v_name = volume.name
                        read_only = volume.read_only
                        volumes.append(ContainerVolume(mount_path, v_name, read_only))

                containers.append(KubeContainer(env, c_image, command, image_pull_policy, c_name, ports, volumes))

            self.kube_pods.append(
                KubePod(host_ip, pod_i_ps, phase, start_time, qos_class, image, image_id, name, namespace, labels, uid,
                        containers))

        # spec.
        # for service in services

        print(kube_gaia)


def kubeconn():
    "Establish connection to OpenStack cloud cloud (timeout timeout)"
    cfg.load_kube_config()
    return client.CoreV1Api()

    #
    # try:
    #     conn.authorize()
    # except:
    #     print("INFO: Retry connection with 'default' domain", file=sys.stderr)
    #     conn = openstack.connect(cloud=cloud, timeout=timeout, api_timeout=timeout*1.5+4,
    #                              default_domain='default', project_domain_id='default')
    #     conn.authorize()
    # return conn


def main(argv):
    "Entry point for main program"
    global cloud, outjson, indent
    global debug, ofile
    timeout = 12
    # try:
    #     opts, args = getopt.gnu_getopt(argv[1:], "c:f:hjJdu:n:i:t:",
    #                                    ("os-cloud=", "file=", "help", "json", "json-compact",
    #                                     "debug", "uri=", "name=", "id=", "timeout="))
    # except getopt.GetoptError:  # as exc:
    #     usage(1)
    # for opt in opts:
    #     if opt[0] == "-h" or opt[0] == "--help":
    #         usage(0)
    #     elif opt[0] == "-c" or opt[0] == "--os-cloud":
    #         cloud = opt[1]
    #     elif opt[0] == "-f" or opt[0] == "--file":
    #         ofile = opt[1]
    #     elif opt[0] == "-u" or opt[0] == "--uri":
    #         uriprefix = opt[1]
    #     elif opt[0] == "-n" or opt[0] == "--name":
    #         svcname = opt[1]
    #     elif opt[0] == "-i" or opt[0] == "--id":
    #         gxid = opt[1]
    #     elif opt[0] == "-d" or opt[0] == "--debug":
    #         debug = True
    #     elif opt[0] == "-t" or opt[0] == "--timeout":
    #         timeout = int(opt[1])
    #     elif opt[0] == "-j" or opt[0] == "--json":
    #         outjson = True
    #     elif opt[0] == "-J" or opt[0] == "--json-compact":
    #         outjson = True
    #         indent = None
    # if args:
    #     usage(1)
    # if not cloud:
    #     print("ERROR: You need to have OS_CLOUD set or pass --os-cloud=CLOUD.", file=sys.stderr)
    conn = kubeconn()
    my_kube = KubeCluster(conn)
    if ofile == "/dev/stdout":
        print(my_kube, file=sys.stdout)
    else:
        print(my_kube, file=open(ofile, 'a', encoding="UTF-8"))


if __name__ == "__main__":
    main(sys.argv)
