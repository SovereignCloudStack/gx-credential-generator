""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from typing import List

from requests.exceptions import HTTPError
from openstack.connection import Connection

from generator.common.config import Config
from generator.common.const import CONST_GXDCH, CONST_GXDCH_NOT, CONFIG_CSP, CONFIG_CSP_VAT_ID, CONFIG_DID, CONST_GXDCH_COMP
from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmDiscovery
from generator.gxdch.notary_service import NotaryService
from generator.gxdch.compliance_service import ComplianceService


class OsCloud:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        # import copy
        self.conn = conn
        # self.regions = list(conn.identity.regions())
        self.config = config
        self.not_services = []
        self.compliance_services = []
        for not_ep in config.get_value([CONST_GXDCH, CONST_GXDCH_NOT]):
            self.not_services.append(NotaryService(not_ep, "templates"))
        for comp_ep in config.get_value([CONST_GXDCH, CONST_GXDCH_COMP]):
            self.compliance_services.append(ComplianceService(comp_ep, "templates"))


    def discover(self) -> List[JsonLdObject]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """
        # retrieve mandatory verifiable credentials
        csp_did = self.config.get_value([CONFIG_CSP, CONFIG_DID])
        csp_reg_number = self.config.get_value([CONFIG_CSP, CONFIG_CSP_VAT_ID])
        csp_reg_number_vc = dict()

        for ns in self.not_services:
            resp = ns.issue_vat_id_vc(vat_id=csp_reg_number, csp_did=csp_did)
            if resp.ok:
                csp_reg_number_vc = resp.json()
                break
            elif resp.status_code > 500:
                # internal server error, try another notarization service
                continue
            else:
                try:
                    # we need this extra round here, as failure cause is not forwarded to exception,
                    # but contains important information for bug fixing
                    resp.raise_for_status()
                except HTTPError as e:
                    raise HTTPError(e, resp.text)

        if csp_reg_number_vc is None:
            raise AttributeError("Cloud not retrieve VC for CSP registration number. " +
                                 "None of provided GXDCH Notary Services returned valid VC.")

        return csp_reg_number_vc
        #return (VmDiscovery(self.conn, self.config).discover() + ServerFlavorDiscovery(self.conn,
        #                                                                               self.config).discover())
