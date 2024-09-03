# gx-credential-generator

![Static Badge](https://img.shields.io/badge/version-1.0.0-green)
![Static Badge](https://img.shields.io/badge/Gaia--X_Release-Tagus-blue?color=%23D901D9)
![Static Badge](https://img.shields.io/badge/Gaia--X_Compliance-Conformity-blue?color=%23D901D9)

Tool for creating compliant Gaia-X Credentials, previously known as Gaia-X Self-Description, for SCS-compliant cloud infrastructures.
To get familiar with Gaia-X Credentials, please consult the corresponding [documentation](https://docs.gaia-x.eu/).

## Table of Contents

 1. [Introduction](#introduction)
 2. [Quick Start](#quick-start-guide)
 3. [User Guide](#user-guide)
 4. [Developer Guide](#developer-guide)

## Introduction

Gaia-X Ontology defines classes and attributes, which Gaia-X offers to describe CSPs as well as services to be published in a Gaia-X catalogue.

A service and/or CSP is supposed to be "Gaia-X compliant", if their Gaia-X Credential(s) fulfill a set of special requirements.
These requirements are defined in [Gaia-X Policy and Rules Documents](https://docs.gaia-x.eu/policy-rules-committee/policy-rules-conformity-document/23.10/) as well as [Gaia-X Trust Framework](https://docs.gaia-x.eu/policy-rules-committee/trust-framework/22.10/).
gx-credential-generator automatically discovers CSP's and service's properties and creates Gaia-X Credentials for

- Cloud Service Provider of SCS-compliant cloud infrastructure
- OpenStack as an IaaS Offering
- Kubernetes as a CaaS Offering

Each description may consist of several Gaia-X Credentials, each of them attesting other properties.
All credentials are bundled in a so called [Presentation](https://www.w3.org/TR/vc-data-model/#presentations-0) and send to [GXDCH Compliance Service](https://gaia-x.eu/gxdch/), which issues a Compliance Credential to certify Gaia-X compliance of given CSP and/or service.

Gaia-X defines several level of compliance, each with a different trust level. gx-credential-generator supports the very basic level, called "Conformity" and is compliant Gaia-X Tagus release.

### Cloud Service Provider

gx-credential-generator outputs the following Gaia-X Credentials for a CSP in order to be Gaia-X compliant

- Gaia-X Terms and Conditions signed by CSP as an instance Gaia-X class `GaiaXTermsAndConditions`
- Legal Registration number issued by a Notary Service accredited by GXDCH as an instancec of Gaia-x class `LegalRegistrationNumber`
- Gaia-X mandatory attributes for CSP as an instance of Gaia-X class `LegalPeron`
- Compliance Credentials for CSP issued by GXDCH Compliance Service as an instance of Gaia-X class `compliance`

CSP's properties are not discoverable and read out from configuration file. See [configuration](#configuration) section for more details.

### OpenStack

gx-credential-generator collects discoverable information from an OpenStack cloud, bundles them to Gaia-X Credentials and requests for compliance at GXDCH.

Besides the Gaia-X Credentials of CSP of OpenStack cloud, with are required by Gaia-X, the follwing Gaia-X Credentials will be created:

- Mandatory properties for IaaS Offering as an instance of Gaia-X `ServiceOffering`
- Detailed description of OpenStack cloud as an instance of Gaia-X `VirtualMachineServiceOffering`
- Compliance Credentials for OpenStack cloud issued by GXDCH Compliance Service as an instance of Gaia-X class `compliance`

To discover cloud properties, gx-credential generator requires access to OpenStack cloud as normal tenant user.

gx-credential-generator read the OpenStack catalog to collect

- public VM Images and their properties, such as operation system or hardware requirements
- public Server Flavors, such as number and capability of virtual CPUs or size of root disk

### k8s

Comming soon.

## Quick Start Guide

### 1. Clone the repository into a location of your choice

```bash
git clone git@github.com:SovereignCloudStack/gx-credential-generator.git
cd gx-credential-generator
```

### 2. Install scripts dependencies

Installing dependecies into a Python [virtualenv](https://virtualenv.pypa.io/en/stable/) is recommended

   ```bash
   pip install -r requirements.txt
   ```

### Cloud Service Provider

### 1. Create configuration file

gx-credential-generator requires some configuration options. See [configuration](#configuration) section for more details.

#### 2. Run gx-credential-generator

Create Gaia-X Credential for CSP without specifying a configuration file. This implies the default path at `/etc/gx-credential-generator/config.yaml`, which must exist:

```commandline
python3 -m generator.cli csp
```

Gaia-X terms and conditions are prompt and you are asked to agree to them. Type 'y' to agree or 'no' to dis-agree.

**Note**: If you do not agree Gaia-X terms and conditions, process will be aborted and none Gaia-X credential is created.

Each Gaia-X Credential is serialized in [JSON-LD](https://json-ld.org/) and stored in a separate file prefixed as follows:

- lp: Gaia-X Credential containing CSP's legal address and headquarter address
- lrn: Gaia-X Credential for CSP's legal registration number issued by GXDCH Notary Service. gx-credential-generator reaches out to Notary Service by itself.
- tandc: Gaia-X Terms and Conditions signed by CSP
- vp_csp: Presentation of all Gaia-X Credentials to be sent to GXDCH Compliance Service to assert compliance
- cs_csp: Compliance Credential for CSP as Gaia-X `LegalPerson` issued by GXDCH Compliance Service

Gaia-X Credential files are placed in current working directory, be default. To change output directory use parameter `--out-dir`:

```commandline
python3 -m generator.cli csp --out-dir=my-output-dir
```

Running the gx-credential-generator with a specified configuration file path use parameter `--config`:

```commandline
python3 -m generator.cli csp --config=my-config.yaml
```

You can prevent to prompt Gaia-X terms and conditions using option `--auto-sign`. This implies you agree to them:

```commandline
python3 -m generator.cli csp --auto-sign
```

### OpenStack

#### 1. Create `clouds.yaml` configuration file

gx-credential-generator requires access to OpenStack cluster as normal tenant
  user and has to be configured with these user credentials to access your
  Openstack cloud. This is done
  using [clouds.yaml](https://docs.openstack.org/python-openstackclient/ussuri/configuration/index.html).
  clouds.yaml is a yaml file containing several cloud configurations. Each configuration is referred by name.

SMake sure the following keys exist in our `clouds.yaml`.

- `auth.user_domain_name`
- `auth.project_domain_name`
- `region_name`

#### 2. Create configuration file

gx-credential-generator requires some configuration options. See [configuration](#configuration) section for more details.

#### 3. Run gx-credential-generator

The command to run gx-credential-generator for OpenStack cloud is similar to the one to run gx-credential-generator for CSP. Also arguments `--config`, `--out-dir` and `--auto-sign` are available and act like for CSP.

Create Gaia-X Credential for Openstack cloud

  ```bash
  python3 -m generator.cli openstack <os-cloud>
  ```

As Gaia-X requires to define a provider for each published service offering, gx-credential-generator creates Gaia-X Credentials for CSP at very run for OpenStack cloud, too.

Each Gaia-X Credential is serialized in [JSON-LD](https://json-ld.org/) and stored in a separate file. Credentials for CSP correspond to the ones generated by command `csp`. Credentials for OpenStack cloud are prefixed as follows:

- so: Mandatory properties for OpenStack cloud
- vmso: Detailed description of OpenStack cloud
- vp_so: Presentation of all Gaia-X Credentials to be sent to GXDCH Compliance Service to assert compliance
- cs_so: Compliance Credentials for OpenStack cloud as Gaia-X `ServiceOffering` issued by GXDCH Compliance Service

### K8s

Comming soon!

## User Guide

### Configuration

gx-credential-generartor is configured by `config.yaml`. The configuration
includes:

- Values for mandatory attributes for CSP and service offering, which are not discoverable
- Prerequisites to create and sign Gaia-X Credentials
- Enpoints to GXDCH services

### Mandatory Attributes

Gaia-X Credential schema dictates mandatory attributes for some class.
If values for mandatory attributes can not be discovered from OpenStack or K8S cluster, default values are taken from configuration.
Providers are able to change default values.
In doing so, attribute values for **ALL** instances of impacted cloud resource are modified.

#### CopyrightOwner, License and ResourcePolicy of VM images and Operating System

`copyrightOwner`, `license` and `resourcePolicy` are mandatory attributes for VM
Images and their operating systems. As these values are not accessible from
OpenStack cloud, default values are used. The values for operating system are
defined in the section ``software resources`` with one subsection for each operating
system. Operating systems are referred by name, e.g. for Alpine Linux:

```yaml
software resources:
  Alpine Linux:
    copyright owner: "Alpine Linux"
    resource policy: "default: allow intent"
    license:
      - https://gitlab.alpinelinux.org/alpine/aports/-/issues/9074
```

By default, gx-credential-generator uses operating system values for VM Image as well. I.e. by
default, VM Image and operating system have the same values
for `copyrigthOwner`, `license` and `resourcePolicy`. Providers are able to
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

### Prerequisites to create and sign Gaia-X Credential

gx-credential-generator creates Gaia-X Credentials, which refer to [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/). Verifiable Credentials requires a proof, e.g. a digital signature of credential's issuer. Therefore some settings, e.g. a private key to sign, are required and defined in section `Credentials` of configuration file.

### Enpoints to GXDCH services

gx-credential-generator interacts with GXDCH service, e.g. to retreive credential for CSP's legal registration number or to assert compliance. To set GXDCH endpoint use section `gxdch`. For a list of available GXSCH endpoints refer to [Gaia-X Framework](https://docs.gaia-x.eu/framework/?tab=clearing-house)

### Docker

----*outdated*---

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

## Developer Guide

### Running the tests

First, install the test dependencies **in addition** to the main dependencies into your virtualenv as described above under ["Quick Start Guide"](#quick-start-guide):

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
