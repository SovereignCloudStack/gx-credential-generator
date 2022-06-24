# gx-self-description-generator
Tools for creating Gaia-X Self-Descriptions (OpenStack, k8s, ...)

## OpenStack
We want to collect discoverable information from an OpenStack cloud,
assuming that we have access to it (as normal tenant user).

We start with the region list and then read the OpenStack catalog to collect
- OS_AUTH_URL (Keystone Endpoint)
- List of services (along with supported versions, min thr. max)
- Per service: extensions (cinderv3, nova)
- Flavors for compute incl. flavor details (SCS spec)
- AZs (for nova, cinderv3, neutron)
- UI (URL, type: horizon or custom)

This then should be output as JSON-LD (or YAML-LD) for the Gaia-X catalogue.

References:
<https://gaia-x.gitlab.io/gaia-x-community/gaia-x-self-descriptions/service/service.html>
<https://gitlab.com/gaia-x/gaia-x-community/gx-hackathon/gx-hackathon-3/-/blob/main/gxfs-track/self-descriptions/service_taxonomy.md>
<https://gitlab.com/gaia-x/gaia-x-community/gx-hackathon/gx-hackathon-3/-/blob/main/gxfs-track/self-descriptions/sd_attributes.md>
<https://github.com/SovereignCloudStack/Docs/blob/main/Design-Docs/flavor-naming.md>
<https://github.com/garloff/openstack-api-discovery>

Notes from reviewing the SD attributes:
* Virtualized CPU types: It might be of limited use to reference exact model names, rather characterize properties
  (generation, speed, insn set extensions, ...)
* NICs: Virtual NICs are almost unlimited, but there may be a limited amount of hardware-accelerated
  NICs (using SR-IOV and multiqueue features) available -- these may need to be added to SCS flavor
  naming.
* Other extension hardware like FPGAs need to be specified
* Tenant isolation needs a list of criteria. Virt OK? V(x)LANs OK? Shared storage cluster OK? ...
* Availability Zones: Provider needs to create transparency over what it means. Fire protection zones?
  Power supply zones? Internet connectivity zones? Minimal and maximal physical distance? Network
  latency distance?


## k8s
Same thing for k8s

Collect information on a k8s cluster:
- API endpoint, k8s version
- number and type (flavor) of workers and control nodes
- services (CNI, CSI, registry, ingress, metrics, ...)

For typical k8s aaS offerings, every cluster is different,
and we probably don't want to have a description for every single
customer specific cluster. (Some providers may offer self-service,
so we would not want to push of a new SD into the G-X catalogue on
creation, changing or deletion of clusters.) Still it might be
helpful to have a SD on demand for an existing cluster to characterize
it, so users can use the SD to match it to app requirements.

So the SD for a k8s aaS solution would list possible options and
ranges: What k8s versions are supported, what max number of workers,
flavors, etc.? What services are optionally delivered (and supported)
by the provider?

For KaaS, the option space really needs to be described.
As of now, this can not be discovered, short of using external sources,
like the IaaS SD, the list of node images (osism minio), ...

## Status (2022-06-24)
The current PoC code can discover OpenStack capabilities and produces
an entry for the services in the service catalogue.
For the compute service, there is a flavor list (yet without some
of the details discoverable by SCS specs); for volumes, we
list the types, for loadbalancers, we have a flavor list as well.

Thanks to the work in Hackathon #4, we have an option to export
JSON-LD (use option `--gaia-x` aka. `-g`) that can be signed and
successfully processed by the compilance service at
http://compliance.lab.gaia-x.eu/
Signing and verifying can be combined using the Delta-DAO signer.
https://signer.demo.delta-dao.com/#signer

From an OpenStack perspective, this still incomplete.
- We lack flavor details (though we need SCS specs to discover more)
- We lack a list of public images (along with image details)
- Neutron probably has a few things to detect.

TODO: Create cmd line tool that does signing and interacting with
the compliance service, so we can set up CI testing.

