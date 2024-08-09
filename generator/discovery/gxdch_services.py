import json

import requests
import generator.common.const as const


class ComplianceService:
    """ Wrapper class to connect GXDCH Compliance Service. """

    def __init__(self, api: str):
        if not api:
            raise AttributeError("Parameters MUST not be None")
        self.api = api

    def request_compliance_vc(self, vp: str, vp_id) -> str:
        resp = requests.post(self.api + "?vcid=" + vp_id, vp)
        if resp.ok:
            return resp.text
        else:
            resp.raise_for_status()


class NotaryService:
    """ Wrapper class to connect GXDCH Notary Service. """

    def __init__(self, api: str):
        self.api = api

    # TODO: Support all kind of registration numbers
    def request_reg_number_vc(self, csp: dict, cred_id: str, cred_subject_id: str) -> dict:
        body = dict()
        body['@context'] = const.LRN_CONTEXT
        body['type'] = "gx:legalRegistrationNumber"
        body['id'] = cred_subject_id #csp['did'] TODO: I think DID is correct here, but Gaia-X requires credential id, instead of credential subject id
        body['gx:vatID'] = csp['vat-id']

        resp = requests.post(self.api + "registrationNumberVC?vcid=" + str(cred_id), json=body)

        if resp.ok:
            return resp.json()
        else:
            resp.raise_for_status()


class RegistryService:
    """ Wrapper class to connect GXDCH Registry Service. """

    def __init__(self, api: str):
        self.api = api

    def get_gx_tandc(self) -> dict:
        resp = requests.get(self.api + "/api/termsAndConditions")

        if resp.ok:
            return resp.json()
        else:
            resp.raise_for_status()
