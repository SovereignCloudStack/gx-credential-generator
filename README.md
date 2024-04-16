# gx-credential-generator

Tool for
creating [Gaia-X Credentials](https://gitlab.com/gaia-x/technical-committee/architecture-document/-/blob/master/architecture_document/gx_conceptual_model.md#gaia-x-credentials),
previously known as Gaia-X Self-Descriptions, for SCS-compliant cloud
infrastructures (OpenStack, k8s, ...)

**NOTE**: Gx-Credential Generator is work in progress, currently, and
documentation may be not up-to-date.

## Introduction

### OpenStack

We want to collect discoverable information from an OpenStack cloud,
assuming that we have access to it (as normal tenant user).

We read the OpenStack catalog to collect

- public VM Images

This then should be output as GX-compliant credential in JSON-LD for the Gaia-X
catalogue.

### k8s

We want to collect discoverable information from a k8s cloud,
assuming that we have access to it.

Collect information on a k8s cluster:

- Metadata
- API Version
- Nodes information
- Pods information

#### K8s as-a-Service (KaaS) offering considerations

For typical k8s aaS offerings, every cluster is different,
and we probably don't want to have a description for every single
customer specific cluster. (Some providers may offer self-service,
so we would not want to push of a new GX Credential into the GX catalogue on
creation, changing or deletion of clusters.) Still it might be
helpful to have a GX Credential on demand for an existing cluster to
characterize
it, so users can use the GX Credentials to match it to app requirements.

So the GX Credential for a k8s aaS solution would list possible options and
ranges: What k8s versions are supported, what max number of workers,
flavors, etc.? What services are optionally delivered (and supported)
by the provider?

For KaaS, the option space really needs to be described.
As of now, this can not be discovered, short of using external sources,
like the IaaS GX Credential, the list of node images (osism minio), ...

## Quick Start Guide

1. Clone the repository into a location of your choice

   ```bash
   git clone git@github.com:SovereignCloudStack/gx-credential-generator.git
   cd gx-credential-generator
   ```

2. Install scripts dependencies (installing them into a
   Python [virtualenv](https://virtualenv.pypa.io/en/stable/) is recommended)

   ```bash
   pip install -r requirements.txt
   ```

### OpenStack

a. Create `clouds.yaml` configuration file

- GX credential Generator requires access to OpenStack cluster as normal tenant
  user and has to be configured with these user credentials to access your
  Openstack cloud. This is done
  using [clouds.yaml](https://docs.openstack.org/python-openstackclient/ussuri/configuration/index.html).
  clouds.yaml is a yaml file containing several cloud configurations. Each
  configuration is referred by name.
- Make sure the following keys exist in our `clouds.yaml`.
  - `auth.user_domain_name`
  - `auth.project_domain_name`
  - `region_name`

b. Generate Gaia-X Credentials

- To print OpenStack properties in JSON-LD

  ```bash
  python3 cli.py openstack <os-cloud>
  ```

### K8s

Generate Gaia-X Credentials

- To print K8s properties ...

  ```bash
  ./gx-cred-generator.py k8s
  ```

### Airflow Pipeline

Start the gaiax-pipeline (deprecated)

- To modify the airflow pipeline you have to touch the gaiax-pipeline.py file
  inside the dags folder

  ```bash
  cd devops
  docker-compose up -d
  ```

### Validation

Generated GX Credentials could be validated against their schemas (shapes) by
the
simple SD validator script. Visit the `sd` directory and try to validate your
generated SD. Find the examples in `sd` directory and do the validation as
follows:

Try to validate a minimal example against the latest GX shapes (feel free to
remove some
required attribute and check validation result):

```bash
./sd/validate.py sd/gx_service_offering_example.jsonld sd/gx_shapes_latest.ttl
```

## Compliance

GX Credential Generator creates credentials compliant with the latest (
3024/01/19) Credential Schema, which can be downloaded from
the [GX registry](https://registry.lab.gaia-x.eu/v1/api/trusted-shape-registry/v1/shapes/trustframework).
GX Credential Generator **does not** create W3C
complaint [Verifiable Credentials](https://www.w3.org/TR/vc-data-model/).

## Configuration

GX Credential generator is configured by `config.yaml`. The configuration
includes:

- Mandatory: Default values for mandatory attributes
- Optional: Values for optional attributes
- Optional: Wallets

### Mandatory Attributes

Gaia-X Credential schema dictates mandatory attributes for some class. If values
for mandatory attributes can not be access from OpenStack or K8S cluster,
default values are taken from configuration file in section `default`.
Providers are able to change default values. In doing so, attribute values for *
*ALL** instances of impacted cloud resource are modified.

#### CopyrightOwner, License and ResourcePolicy of VM images

`copyrightOwner`, `license` and `resourcePolicy` are mandatory attributes for VM
Images and their operating systems. As these values are not accessible from
OpenStack cloud, default values are used. The values for operating system are
defined in the section `operating system` with one subsection for each operating
system. Operating systems are referred by name, e.g. for Alpine Linux:

```yaml
default:
  operating system:
    Alpine Linux:
      copyright owner: "Alpine Linux"
      resource policy: "default: allow intent"
      license:
        - https://gitlab.alpinelinux.org/alpine/aports/-/issues/9074
```

By default, generator uses operating system values for VM Image as well. I.e. by
default, VM Image and operating system have the same values
for `copyrigth owner`, `license` and `resourcePolicy`. Providers are able to
change values for each VM image, individually. Therefore, the
section `own images` in `cloud resources` exists. To set individual values for a
specific VM image, add a new section, started by image's name (as defined in
OpenStack cloud) to configuration file. The following example defines ìndividual
values for `copyrightOwner`, `license` and `resourcePolicy` for VM image
called `AlmaLinux 8`.

```yaml
cloud resources:
  own images:
    AlmaLinux 8:
      copyright owner:
        - "AlmaLinux OS Foundation"
        - "ACME Company"
      resource policy: "allow: all"
      license:
        - https://www.example.org
```

### Optional Attributes

As with mandatory attributes, GX Credential Schemas supports optional attributes
whose values can not be retrieved from OpenStack. These values can be set in the
section `cloud resources` as well.

#### AggregationOf of VM Images

GX Credential schema allows to describe cloud resources, such VM images, in a
fine granular manner, by using attribute `aggregationOf`. This attribute refers
a list of GX credentials either as [DID](https://www.w3.org/TR/did-core/) or as
file path relative to generators working directory. The latter is copied to
cloud resource's credentials. For more details on GX credential schema and its
attributes, please
refer [Gaia-X Service Characteristics GitLab](https://gitlab.com/gaia-x/technical-committee/service-characteristics)

## Docker

The docker environment creates a general and portable environment for the
gx-cred-generator module. Before running the container, don't forget to mount
your credentials for the correct path. OpenStack-related secret are located
under `~/.config/openstack`.

**Example codes:**

First of all, build the image:

```shell
docker build -t gx-credential-generator .
```

Running the `gx-cred-generator.py` on an example cloud:

```shell
docker run -v "<secret_location>:/root/.config/openstack" gx-credential-generator ./gx-cred-generator.py --os-cloud gx-h61.1
```

Running the container in an interactive mode:

```shell
docker run -it -v "<secret_location>:/root/.config/openstack" gx-credential-generator bash
```

or you can use the following to create a temp location for the secrets:

```shell
mkdir -p os_secret && cp secret1 ./os_secret
docker run -v "${PWD}/os_secret:/root/.config/openstack" gx-credential-generator ./gx-cred-generator.py --os-cloud gx-h61.1
```

## Development Hints

### Running the tests

First, install the test dependencies **in addition** to the main dependencies
into
your virtualenv as described above
under ["Quick Start Guide"](#quick-start-guide):

```shell
pip install -r test-requirements.txt
```

Then, tests can be run with:

```shell
python3 -m pytest tests/
```

### Updating the dependency pins

We pin dependencies with `pip-compile`
from [pip-tools](https://pypi.org/project/pip-tools/),
which can be installed with:

```shell
pip install pip-tools
```

If you change one of the `*.in` files, you need to regenerate the
concrete `requirements.txt`
files as follows (the order is important):

```shell
pip-compile requirements.in
pip-compile test-requirements.in
```

By default, `pip-compile` doesn't update the pinned versions. This can be
changed by adding the
`--upgrade` flag to the above invocations:

```shell
pip-compile --upgrade requirements.in
pip-compile --upgrade test-requirements.in
```

Whenever the concrete `requirements.txt` file change you also shouldn't forget
to re-run the
`pip install -r ...` steps again.

