""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

import requests
from openstack.connection import Connection
from requests.exceptions import HTTPError
from typing import List

from generator.common import const
from generator.common.config import Config
from generator.common.gx_schema import (DataAccountExport, TermsAndConditions,
                                        VirtualMachineServiceOffering)
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmImageDiscovery

from hashlib import sha256
from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.discovery.vc_discovery import CredentialDiscovery

from generator.discovery.gxdch_services import ComplianceService, NotaryService


class OpenstackDiscovery:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        self.conn = conn
        # self.regions = list(conn.identity.regions())
        self.config = config
        self.not_services = []
        self.compliance_services = []
        self.templates = Environment(
            loader=FileSystemLoader("../templates"),
            autoescape=select_autoescape()
        )
        for not_ep in config.get_value([const.CONST_GXDCH, const.CONST_GXDCH_NOT]):
            self.not_services.append(NotaryService(not_ep, self.templates))
        for comp_ep in config.get_value([const.CONST_GXDCH, const.CONST_GXDCH_COMP]):
            self.compliance_services.append(ComplianceService(comp_ep, self.templates))
        self.vc_discovery = CredentialDiscovery(templates=self.templates)

    def generate_gx_credentials(self) -> List[dict]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[dict]
        """
        csp = self.config.get_value([const.CONFIG_CSP])
        cred_settings = self.config.get_value([const.CONFIG_CRED])
        vm_offering_vc = self._get_vm_offering()
        tandc_vc = self.vc_discovery.create_gaia_x_terms_and_conditions_vc(
            csp=csp,
            cred_settings=cred_settings)
        lrn_vc = self.vc_discovery.request_vat_id_vc(not_services=self.not_services)
        lp_vc = self.vc_discovery.create_and_sign_legal_person_vc(
            cred_settings=cred_settings,
            csp=csp,
            lrn_cred_ids=lrn_vc['id']
        )
        return [vm_offering_vc, tandc_vc, lrn_vc, lp_vc]

    def _get_vm_offering(self) -> VirtualMachineServiceOffering:
        images = VmImageDiscovery(self.conn, self.config).discover()
        flavors = ServerFlavorDiscovery(self.conn, self.config).discover()

        # Create Virtual Service Offering object
        data_export_account = DataAccountExport(
            requestType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_REQ_TYPE,
                ]
            ),
            accessType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_ACCESS_TYPE,
                ]
            ),
            formatType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_FORMAT_TYPE,
                ]
            ),
        )
        service_tac = []
        for url in self.config.get_value(
                [const.CONFIG_IAAS, const.CONFIG_IAAS_T_AND_C]
        ):
            httpResponse = requests.get(url)
            if httpResponse.status_code == 200:
                content = httpResponse.text
                service_tac.append(
                    TermsAndConditions(
                        url=url, hash=sha256(content.encode("utf-8")).hexdigest()
                    )
                )
            else:
                raise HTTPError(
                    "Cloud not retrieve terms and conditions from '"
                    + url + "'. HTTP Status code: " + str(httpResponse.status_code)
                )

        if len(service_tac) == 0:
            raise ValueError(
                "Service offerings terms and conditions MUST not be empty. Please check config.yaml. There MUST be at least on entry in "
                + const.CONFIG_IAAS + "." + const.CONFIG_IAAS_T_AND_C
            )

        return VirtualMachineServiceOffering(
            providedBy=self.config.get_value([const.CONFIG_CSP, const.CONFIG_DID]),
            dataAccountExport=data_export_account,
            servicePolicy=self.config.get_value(
                [const.CONFIG_IAAS, const.CONFIG_IAAS_SERVICE_POLICY]
            ),
            serviceOfferingTermsAndConditions=service_tac,
            codeArtifact=images,
            instantiationReq=flavors,
        )
