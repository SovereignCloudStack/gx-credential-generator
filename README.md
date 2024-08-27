# gx-credential-generator

![Static Badge](https://img.shields.io/badge/version-1.0.0-green)
![Static Badge](https://img.shields.io/badge/Gaia--X_Release-Tagus-blue?color=%23D901D9)
![Static Badge](https://img.shields.io/badge/Gaia--X_Compliance-Conformity-blue?color=%23D901D9)


Tool for creating compliant Gaia-X Credentials, previously known as Gaia-X Self-Description, for SCS-compliant cloud
infrastructures. 
To get familiar with Gaia-X Credentials, please consult the corresponding [documentation](https://docs.gaia-x.eu/).

## Introduction

Gaia-X Ontology defines classes and attributes, which Gaia-X offers to describe CSPs as well as services to be published in a Gaia-X catalogue.

A service and/or CSP is supposed to be "Gaia-X compliant", if their Gaia-X Credential(s) fulfill a set of special requirements. 
These requirements are defined in [Gaia-X Policy and Rules Documents](https://docs.gaia-x.eu/policy-rules-committee/policy-rules-conformity-document/23.10/) as well as [Gaia-X Trust Framework](https://docs.gaia-x.eu/policy-rules-committee/trust-framework/22.10/).
gx-credential generator automatically discovers CSP's and service's properties and creates Gaia-X Credentials for

- Cloud Service Provider of SCS-compliant cloud infrastructure as instance of class `LegalPerson` 
- OpenStack as instances of classes `ServiceOffering` and `VirtualMacuhineServiceOffering`
- Kubernetes as an instance of class `ServiceOffering`

Each description may consist of several Gaia-X Credentials, each of them attesting other properties. 
All credentials are bundled to a so called [Presentation](https://www.w3.org/TR/vc-data-model/#presentations-0) and send to [GXDCH Cpmpliance Service](https://gaia-x.eu/gxdch/), which issues a Compliance Credential to certify Gaia-X compliance of given CSP and/or service.

Gaia-X defines several level of compliance, each with a different security level. gx-credential-generator supports the very basic level, called "Conformity" and is compliant with respect to Gaia-X Tagus release.

### Cloud Service Provider

Gaia-X expects the following three Gaia-X Credentials for a CSP in order to be Gaia-X complaint:

- Gaia-X Terms and Conditions signed by CSP 
- Legal Registration number issued by a Notary Service accredited GXDCH  
- Gaia-X mandatory attributes for CSP

gx-credential-generator generates required credentials and requests Gaia-X compliance for CSP at GXDCH. 

CPS's properties are not discoverable and read out from configuration file. See [configuration](#configuration) section for more details.

### OpenStack

gx-credential-generator collects discoverable information from an OpenStack cloud, bundles them to Gaia-X Credentials and requests for compliance at GXDCH. 

Each Gaia-X Credential is written to a separate JSON-LD file being prefixed as follows:

- so: Gaia-X mandatory attributes for service offerings 
- vmso: Openstack cloud properties including public VM Images as well as Server Flavors
- vp_so: collection of all Gaia-X Credentials to be sent to GXDCH Compliance Service for validation
- cs_so: Compliance Credential for OpenStack as Gaia-X Service Offering

To discover cloud properties, gx-credential generator requires access to OpenStack cloud as normal tenant user. 

gx-credential-generator read the OpenStack catalog to collect

- public VM Images
- public Server Flavors


### k8s

Comming soon.


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

### Cloud Service Provider

gx-credential-generator requires some configuration options. See [configuration](#configuration) section for more details. 

1. Create Gaia-X Credential for CSP without specifying a configuration file. This implies the default path at /etc/gx-credential-generator/config.yaml, which must exist: 

```commandline
python3 -m generator.cli csp
```
Gaia-X terms and condiions are prompt and you are asked to agree to them. Type 'y' to agree or 'no' to not agree.

**Note**: If you do not agree Gaia-X terms and conditions, process will be aborted and none Gaia-X credential are created.

Each Gaia-X Credential is written to a separate JSON-LD file being prefixed as follows:

- lp: Gaia-X Credential containing CSP's legal address and headquarter address
- lrn: Gaia-X Credential for CSP's legal registration number issued by GXDCH Notary Service. gx-credential-generator reaches out to Notary Service automatically.
- tandc: Signed Gaia-X Terms and Conditions
- vp_csp: collection of all Gaia-X Credentials to be sent to GXDCH Compliance Service for validation
- cs_csp: Compliance Credential for CSP as Gaia-X Legal Person

Gaia-X credential files are stored in current working directory, be default. To change output director use parameter `--out-dir`:

```commandline
python3 -m generator.cli csp --out-dir=my-output-dir
```

Running the gx-credential-generator with a specified configuration file path:

```commandline
python3 -m generator.cli csp --auto-sign
```

You can prevent to prompt Gaia-X terms and conditions using option `--auto-sign`. This implies you agree to them:

```commandline
python3 -m generator.cli csp --config=my-config.yaml
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

TBA



## User Guide

### Configuration

GX Credential generator is configured by `config.yaml`. The configuration
includes:

- Values for mandatory attributes of Gaia-X Ontology
- Cryptographical material to sign Gaia-X Credentials and Verifiable Presentations
- Decentralized Identifier ([DID](https://www.w3.org/TR/did-core/)) for CPS and service offering

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

### Cryptographical Material

### Decentralized Identifiers (DID) for CSP and Service Offerings

### Docker

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

## Development Guide

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

### Generate python classes for Gaia-X Ontology

GX-Credential generator uses python classes to create Gaia-X compliant Gaia-X Credentials.
These classes mirror [Gaia-X Ontology](https://gitlab.com/gaia-x/technical-committee/service-characteristics-working-group/service-characteristics) and are generated automatically using [linkML's python generator](https://linkml.io/linkml/generators/python.html).
LinkMl seems to have a bug, as creation of inlined objects fails with `TypeError: unhashable type: 'list'` (see comment in [#70](https://github.com/SovereignCloudStack/gx-credential-generator/issues/70#issuecomment-2122354334)).
As a quick workaround, we comment creation of inlined objects out.


