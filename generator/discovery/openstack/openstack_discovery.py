""""General openstack discovery class.

(c) Anja Strunk <anja.strunk@cloudandheat.com>, 2/2024
SPDX-License-Identifier: EPL-2.0
"""
import json
import os
from typing import List
from datetime import datetime
from jwcrypto.jws import JWS, JWK
from requests.exceptions import HTTPError
from openstack.connection import Connection

from generator.common.config import Config
from generator.common import const
from generator.common.json_ld import JsonLdObject
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmDiscovery
from generator.gxdch.notary_service import NotaryService
from generator.gxdch.compliance_service import ComplianceService

from generator.common import crypto
from hashlib import sha256
from generator.common import utils
from jinja2 import Environment, FileSystemLoader, select_autoescape
import rdflib


class OsCloud:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        # import copy
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

        self.csp = self.config.get_value([const.CONFIG_CSP])
        self.signing = self.config.get_value([const.CONFIG_SIGN])

    def discover(self) -> List[JsonLdObject]:
        """
        Discover all attributes of OS Cloud.

        @return: all attributes as list
        @rtype List[JsonLdObject]
        """

        tac_vc = self._sign_gaia_x_terms_and_conditions()
        vat_id_vc = self._get_vat_id_vc()

        pass
        # print(json.dumps(tac_vc, indent=2))

        #return csp_reg_number_vc
        # return (VmDiscovery(self.conn, self.config).discover() + ServerFlavorDiscovery(self.conn,
        #                                                                               self.config).discover())

    def _sign_gaia_x_terms_and_conditions(self) -> dict:
        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is ins sync with latest Gaia-X
        #  Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics
        # read Gaia-X terms and conditions from file
        tac = ""
        with open(os.path.abspath("../config/gaia-x-terms-and-conditions.txt"), "r") as tac_file:
            for line in tac_file:
                tac += line

        # calculate date and hash of Gaia-X terms and conditions
        now = datetime.today().isoformat()
        tac_hash = crypto.get_sha256(tac)

        # create terms and conditions credential
        cred = self.templates.get_template("credentials/terms-and-credentials_22.10.json").render(csp=self.csp, hash=tac_hash,
                                                                                            date=now, cred_id=self.signing[const.CONFIG_SIGN_BASE_CRED_URL])
        cred_dict = json.loads(cred)

        # sign verifiable credential for Gaia-X terms and conditions
        return crypto.sign_cred(cred=cred_dict,
                                private_key=crypto.load_JWK_from_file(self.signing[const.CONFIG_SIGN_KEY]),
                                verification_method=self.signing[const.CONFIG_SIGN_VER_METH])

    def _get_vat_id_vc(self) -> dict:
        for ns in self.not_services:
            resp = ns.issue_vat_id_vc(csp=self.csp)
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
