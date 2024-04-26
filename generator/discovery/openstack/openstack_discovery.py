""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import List

from openstack.connection import Connection

from generator.common.config import Config
from generator.common.const import CONFIG_WALLET, CONFIG_FILESYSTEM_WALLET, CONFIG_IAAS_DID, CONFIG_DID

from generator.common.const import CONFIG_DID, CONFIG_CPS_DID

from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmDiscovery
from generator.common.gx_schema import VirtualMachineServiceOffering, DataAccountExport, TermsAndConditions
from generator.wallet.filesystem_wallet import FileSystemWallet


class OpenStackDiscovery:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        if not (conn or config):
            raise ValueError("None for argument 'conn' or 'config' not allowed!")
        self.conn = conn
        self.config = config
        if CONFIG_FILESYSTEM_WALLET in config.get_value([CONFIG_WALLET]):
            self.wallet = FileSystemWallet(config.get_value([CONFIG_WALLET, CONFIG_FILESYSTEM_WALLET, "path"]))
        self.iaas_did = config.get_value([CONFIG_DID, CONFIG_IAAS_DID])

    def discover(self) -> VirtualMachineServiceOffering:
        """
        Discover all claims of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """

        flavors = ServerFlavorDiscovery(self.conn, self.config).discover()
        images = VmDiscovery(self.conn, self.config).discover()
        data_export = self._get_data_export_schema()
        #terms_and_conditions = self._get_terms_and_conditions(self.config.get_value([CONFIG_IAAS_DID]))

        # create top level Virtual Machine Service Offering
        vm_so = VirtualMachineServiceOffering(instantiationReq=flavors,
                                              codeArtifact=images,
                                              providedBy=self.config.get_value([CONFIG_DID, CONFIG_CPS_DID]))

        return vm_so


    def _get_data_export_schema(self) -> DataAccountExport:
        cred = self.wallet.get_credentials_of_subject(subject_id=self.iaas_did, type=DataAccountExport)

        pass

    def _get_terms_and_conditions(self, iaas_did: str) -> TermsAndConditions:
        pass
