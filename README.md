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
- <https://gaia-x.gitlab.io/gaia-x-community/gaia-x-self-descriptions/service/service.html>
- <https://gitlab.com/gaia-x/gaia-x-community/gx-hackathon/gx-hackathon-3/-/blob/main/gxfs-track/self-descriptions/service_taxonomy.md>
- <https://gitlab.com/gaia-x/gaia-x-community/gx-hackathon/gx-hackathon-3/-/blob/main/gxfs-track/self-descriptions/sd_attributes.md>
- <https://github.com/SovereignCloudStack/Docs/blob/main/Design-Docs/flavor-naming.md>
- <https://github.com/garloff/openstack-api-discovery>

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
- Metadata
- API Version
- Nodes information
- Pods information

## K8s as-a-Service (KaaS) offering considerations

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


## Quick Start Guide

1. Clone the repository into a location of your choice
```bash
git clone git@github.com:SovereignCloudStack/gx-self-description-generator.git
cd gx-self-description-generator
```

2. Install scripts dependencies (installing them into a Python [virtualenv](https://virtualenv.pypa.io/en/stable/) is recommended)
```bash
pip install -r requirements.txt
```

3. Create `clouds.yaml` configuration file
  - Gaia-x generator has to be configured with user credentials, auth-url, ... to access your Openstack cloud. This is done using [clouds.yaml](https://docs.openstack.org/python-openstackclient/ussuri/configuration/index.html) 
  - Make sure the following keys exist in our `clouds.yaml`
     - `auth.user_domain_name`
     - `auth.project_domain_name`
     - `region_name`

4. Generate Gaia-X Self-Descriptions

   - OpenStack to json file (timestamp and extension is added to file name and script assumes OpenStack access (as normal tenant user)
   ```bash
   ./gx-sd-generator.py --gaia-x --os-cloud=<os-cloud> --file=<file-name>
   ```
   - To use generated Gaia-X Self-Description in [Gaia-X Wizard](https://wizard.lab.gaia-x.eu/) add `--wizard` option
     - '@' has to be removed from @id and @type in generated SD, to be able to sign and verify it in Gaia-X Wizard
   - K8s (script assumes K8s access)
   ```bash
   ./gx-sd-generator.py k8s
   ```

4. Start the gaiax-pipeline
- To modify the airflow pipeline you have to touch the gaiax-pipeline.py file inside the dags folder
```
cd devops
docker-compose up -d
```

## Simple SelfDescription validator

Generated SelfDescriptions could be validated against their schemas (shapes) by the 
simple SD validator script. Visit the `sd` directory and try to validate your 
generated SD. Find the examples in `sd` directory and do the validation as follows:
```bash
./sd/validate.py sd/example.jsonld sd/example.ttl
```

### GX SelfDescription - Service Offering minimal example

SD definition `sd/gx_service_offering_example.jsonld` should represent
a minimal GX Service Offering example that is valid against the latest GX shacl shapes `sd/gx_shapes_latest.ttl`.
The latest GX shacl shapes (at the time of Hackathon#6 23/05/3-4) are
used by the [GX wizard](https://wizard.lab.gaia-x.eu/), and they have been downloaded from the [GX registry](https://registry.lab.gaia-x.eu/v1/api/trusted-shape-registry/v1/shapes/trustframework).

Try to validate a minimal example against the latest GX shapes (feel free to remove some
required attribute and check validation result):
```bash
./sd/validate.py sd/gx_service_offering_example.jsonld sd/gx_shapes_latest.ttl
```

## Docker

The docker environment creates a general and portable environment for the gx-sd-generator module. Before running the container, don't forget to mount your credentials for the correct path. OpenStack-related secret located under `~/.config/openstack`

**Example codes:**

Running the gx-sd-generator.py on an example cloud:
```docker
docker run -v "<secret_location>:/root/.config/openstack" $(docker build -q .)  ./gx-sd-generator.py --os-cloud gx-h61.1
```

Running the container in an interactive mode:
```docker
docker run -it -v "${PWD}/os_secret:/root/.config/openstack" $(docker build -q .) test bash
```

or you can use the following to create a temp location for the secrets:

```shell
mkdir -p os_secret && cp secret1 /os_secret
docker run -v "${PWD}/os_secret:/root/.config/openstack" $(docker build -q .)  ./gx-sd-generator.py --os-cloud gx-h61.1
```

## Status (2023-05-04)
The current PoC code can discover OpenStack capabilities and produces
an entry for the services in the service catalogue, with name,
(micro)versions, availability zones and extensions (where supported).

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

During Hackathon#6, the JSON-LD was updated match the current
shapes thanks to the work from dNation. A validator was added.

Tecnalia contributed work to characterize K8s clusters in Hackathon#6
as well as an Airflow automation pipeline.

TODO: Create cmd line tool that does signing and interacting with
the compliance service, so we can set up CI testing.

From a Gaia-X perspective, SCS generator is still incomplete, as it does not generate W3C Verifiable Credentials. A concept on how to make generator Gaia-X compliant and integrate it into Gaia-x Tool box, can be found [here](doc/xfsc.md).

