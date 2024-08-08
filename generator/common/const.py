"""
Constants used by SCS GX Credential Generator.
"""
CONFIG_FILE = "config/config.yaml"

# General keys
CONFIG_DID = "did"
CONFIG_DID = "did"
CONFIG_TaC = "terms-and-conditions"

# Credentials keys
CONFIG_CRED = "Credentials"
CONFIG_CRED_KEY = "key"
CONFIG_CRED_VER_METH = "verification-method"
CONFIG_CRED_BASE_CRED_URL = "base_url"

# IaaS configuration keys
CONFIG_IAAS = "IaaS"
CONFIG_IAAS_DATA_EXPORT = "data-account-export"
CONFIG_IAAS_DATA_EXPORT_REQ_TYPE = "request-type"
CONFIG_IAAS_DATA_EXPORT_ACCESS_TYPE = "access-type"
CONFIG_IAAS_DATA_EXPORT_FORMAT_TYPE = "format-type"
CONFIG_IAAS_SERVICE_POLICY = "service-policy"
CONFIG_IAAS_T_AND_C = "terms-and-conditions"

# CPS configuration keys
CONFIG_CSP = "CPS"
CONFIG_CSP_NAME = "legal-name"
CONFIG_CSP_LEG_AD = "legal-address-country-code"
CONFIG_CSP_HQ_ADR = "headquarter-address-country-code"
CONFIG_CSP_VAT_ID = "vat-id"

# GXDCH
CONST_GXDCH = "gxdch"
CONST_GXDCH_NOT = "notary-service"
CONST_GXDCH_COMP = "compliance-service"
CONST_GXDCH_REG = "registry-service"

# Default values
DEFAULT_RESOURCE_POLICY = "default: allow intent"
DEFAULT_FIRMWARE_TYPE = "other"
DEFAULT_WATCHDOG_ACTION = "none"

# URIs for units according to GX Credential Schema
UNIT_MB = "https://qudt.org/vocab/unit/MegaBYTE"
UNIT_GB = "https://qudt.org/vocab/unit/GigaBYTE"
UNIT_GHZ = "https://qudt.org/vocab/unit/GigaHZ"

# Dicovery keys
CONFIG_VM_IMAGE = "vm image"
CONFIG_RESOURCE_POLICY = "resource-policy"
CONFIG_LICENSE = "license"
CONFIG_COPYRIGHT = "copyright-owner"
CONFIG_OPERATING_SYSTEM = "operating system"
CONFIG_OWN_IMAGES = "own images"
CONFIG_AGGREGATION_OF = "aggregation of"
CONFIG_WALLETS = "wallets"
CONFIG_DEFAULT = "default"
CONFIG_CLOUD_RESOURCES = "cloud resources:"
CONFIG_SOFTWARE = "software resources"
CONFIG_FILESYSTEM_WALLET = "filesystem"
CONFIG_XFSC_WALLET = "xfsc"

CONFIG_OS_ALP = "Alpine Linux"
CONFIG_OS_ARCH = "Arch Linux"
CONFIG_OS_CENTOS = "CentOS Linux"
CONFIG_OS_DEBIAN = "Debian"
CONFIG_OS_FEDORA = "Fedora"
CONFIG_OS_FREEBSD = "FreeBSD"
CONFIG_OS_GENTOO = "Gentoo Linux"
CONFIG_OS_MANDRAKE = "Mandrakelinux"
CONFIG_OS_MANDRIVA = "Mandriva Linux"
CONFIG_OS_MES = "Mandriva Enterprise Server"
CONFIG_OS_MSDOS = "MS-DOS"
CONFIG_OS_NETBSD = "NetBSD"
CONFIG_OS_NOVELL = "Novell NetWare"
CONFIG_OS_OPENBSD = "OpenBSD"
CONFIG_OS_SUSE = "SUSE Linux Enterprise Server"
CONFIG_OS_SOLARIS = "OpenSolaris"
CONFIG_OS_OPEN_SUSE = "openSUSE"
CONFIG_OS_ROCKY = "Rocky Linux"
CONFIG_OS_RHEL = "Red Hat Enterprise Linux"
CONFIG_OS_SLED = "SUSE Linux Enterprise Desktop"
CONFIG_OS_UBUNTU = "Ubuntu"
CONFIG_OS_WINDOWS = "Microsoft Windows"
CONFIG_OS_CIRROS = "CirrOS"
CONFIG_OS_ALMA_LINUX = "AlmaLinux"

CONFIG_HV_KVM = "KVM"
CONFIG_HV_QUEMU = "quemu"
CONFIG_HV_XEN = "Xen"
CONFIG_HV_ESXI = "ESXi"
CONFIG_HV_CH = "Cloud Hypervisor"
CONFIG_HV_VMW = "vmware"
CONFIG_HV_HYV = "hyper-v"

# JSON-LD Context
VC_CONTEXT = "https://www.w3.org/2018/credentials/v1"
VP_CONTEXT = VC_CONTEXT
JWS_CONTEXT = "https://w3id.org/security/suites/jws-2020/v1"
REG_CONTEXT = "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#"
LRN_CONTEXT = "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/participant"

