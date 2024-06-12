from generator.common import const
from jinja2 import Environment
import json
from datetime import datetime, timezone
from generator.common import crypto
from typing import List
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

from generator.discovery.gxdch_services import NotaryService, ComplianceService


class CredentialDiscovery:
    """
    Discovery for mandatory and optional Gaia-X Credentials in context of Gaia-X.
    """

    def __init__(self, templates: Environment):
        self.templates = templates

    def create_and_sign_legal_person_vc(self, lrn_cred_ids: str, csp: dict, cred_settings: dict) -> dict:
        # TODO: Support list of legal registration number VCs
        """ Create and sign Gaia-X Credential for Legal Person."""
        return self._create_and_sign_cred(id="legal-person.json",
                                          template="credentials/legal-person-credential_20.10.json",
                                          content={'csp': csp, 'lrn_cred_id': lrn_cred_ids},
                                          cred_settings=cred_settings)

    def create_gaia_x_terms_and_conditions_vc(self, csp: dict, cred_settings: dict) -> dict:
        """ Create and sign Gaia-X Credential for Gaia-X terms and conditions."""
        return self._create_and_sign_cred(id="gaia-x-terms-and-cond.json",
                                          template="credentials/terms-and-credentials_22.10.json",
                                          content={'csp': csp},
                                          cred_settings=cred_settings)

    def create_verifiable_presentation(self, vcs: List[dict], cred_settings: dict) -> dict:
        cred = {
            "@context": "https://www.w3.org/2018/credentials/v1",
            "type": "VerifiablePresentation",
            "verifiableCredential": list()
        }

        [cred['verifiableCredential'].append(vc) for vc in vcs]
        crypto.sign_cred(cred=cred,
                         key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                         verification_method=cred_settings[const.CONFIG_CRED_VER_METH])

        return cred

    def _create_and_sign_cred(self, id: str, template: str, content: dict, cred_settings: dict) -> dict:
        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is in sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics

        content['date'] = str(datetime.now(tz=timezone.utc).isoformat())
        content['cred_id'] = cred_settings[const.CONFIG_CRED_BASE_CRED_URL] + "/" + id
        cred = json.loads(self.templates.get_template(template).render(content))
        crypto.sign_cred(cred=cred,
                         key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
                         verification_method=cred_settings[const.CONFIG_CRED_VER_METH])
        return cred

    def request_vat_id_vc(self, not_services: List[NotaryService]) -> dict:
        for ns in not_services:
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

    def request_compliance_vc(self, vcs: List[dict], compl_service: List[ComplianceService]):
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
