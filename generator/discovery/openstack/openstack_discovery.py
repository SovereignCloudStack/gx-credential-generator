""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""

from hashlib import sha256

import requests
from openstack.connection import Connection
from requests.exceptions import HTTPError

from generator.common import const
from generator.common.config import Config
from generator.common.gx_schema import (DataAccountExport, TermsAndConditions,
                                        VirtualMachineServiceOffering)
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmImageDiscovery

from generator.common import crypto
from hashlib import sha256
from generator.common import utils
from jinja2 import Environment, FileSystemLoader, select_autoescape
import rdflib



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

    def discover(self) -> VirtualMachineServiceOffering:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """

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

    def _request_vat_id_vc(self) -> dict:
        for ns in self.not_services:
            resp = ns.request_vat_id_vc(csp=self.csp)
            if resp.ok:
                return resp.json()
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

        raise AttributeError("Cloud not retrieve VC for CSP registration number. " +
                             "None of provided GXDCH Notary Services returned valid VC.")
    def _create_and_sign_legal_person_vc(self, lrn_cred_id):
        # TODO: Use python classes instead of jinjson.dumps(ja2 templates here as soon as GXDCH is in sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics

        # calculate date and credential id
        now = datetime.today().isoformat()
        cred_id = self.signing[const.CONFIG_CRED_BASE_CRED_URL] + "/legal-person/" + str(uuid.uuid4())

        # create legal person credential
        cred = self.templates.get_template("credentials/legal-person-credential_20.10.json").render(csp=self.csp,
                                                                                                    date=now,
                                                                                                    lrn_cred_id=lrn_cred_id,
                                                                                                    cred_id=cred_id)
        # sign credential for Gaia-X legal person
        cred_dict = json.loads(cred)
        return crypto.sign_cred(cred=cred_dict,
                                private_key=crypto.load_jwk_from_file(self.signing[const.CONFIG_CRED_KEY]),
                                verification_method=self.signing[const.CONFIG_CRED_VER_METH])

    def _request_compliance_vc(self, vcs: List[dict]):
        # TDOD: Write generic method for HTTP request
        for cs in self.compliance_services:
            resp = cs.request_compliance_vc(vcs)
            if resp.ok:
                return resp.json()
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

        raise AttributeError("Cloud not retrieve VC for CSP registration number. " +
                             "None of provided GXDCH Notary Services returned valid VC.")