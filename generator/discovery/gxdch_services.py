import json

import requests
from requests import Response
from typing import List
import generator.common.const as const

from dataclasses import dataclass


class ComplianceService:

    def __init__(self, api: str):
        if not api:
            raise AttributeError("Parameters MUST not be None")
        self.api = api

    def request_compliance_vc(self, vcs: List[dict], vp_id) -> Response:
        if not vcs or not vp_id:
            raise AttributeError("Parameters MUST not be None or empty.")

        body = dict()
        body['@context'] = const.VP_CONTEXT
        body['type'] = "VerifiablePresentation"
        body['verifiableCredential'] = vcs
        #body['verifiableCredential'] = json.dumps(vcs)
        body = json.dumps(body)

        return requests.post(self.api + "?vcid=" + vp_id, json=body)


class NotaryService:
    """ Wrapper class to connect GXDCH notary service. """

    def __init__(self, api: str):
        if not api:
            raise AttributeError("Parameters MUST not be None")
        self.api = api

    # TODO: Support all kind of registration numbers
    def request_reg_number_vc(self, csp: dict, cred_id: str) -> Response:
        if not csp or not cred_id:
            raise AttributeError("Parameters MUST not be None")

        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is ins sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics
        body = dict()
        body['@context'] = const.LRN_CONTEXT
        body['@type'] = "gx:legalRegistrationNumber"
        body['id'] = csp['did']
        body['gx:vatID'] = csp['vat-id']

        return requests.post(self.api + "registrationNumberVC?vcid=" + str(cred_id), json=body)


@dataclass
class Gxdch:
    """Wrapper class for all GXDCH services."""
    not_service: NotaryService
    comp_service: ComplianceService
