import json
import logging

import requests

import generator.common.const as const


class ComplianceService:
    """ Wrapper class to connect GXDCH Compliance Service. """

    def __init__(self, api_url: str):
        if not api_url:
            raise AttributeError("Parameters MUST not be None")
        self.api = api_url

    def request_compliance_vc(self, vp: dict, vp_id) -> str:
        resp = requests.post(self.api + "/api/credential-offers?vcid=" + vp_id, json.dumps(vp))
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.error(resp.text)
            raise err
        return resp.text


class NotaryService:
    """ Wrapper class to connect GXDCH Notary Service. """

    def __init__(self, api_url: str):
        if not api_url:
            raise AttributeError("Parameters MUST not be None")
        self.api = api_url

    # TODO: Support all kind of registration numbers
    def request_reg_number_vc(self, csp: dict, cred_id: str, cred_subject_id: str) -> dict:
        body = {
            '@context': const.LRN_CONTEXT,
            'type': "gx:legalRegistrationNumber",
            'id': cred_subject_id,  # csp['did'] TODO: I think DID is correct here, but Gaia-X requires credential id, instead of credential subject id
            'gx:vatID': csp[const.CONFIG_CSP_REG_NUMBER][const.CONFIG_CSP_VAT_ID],
        }
        resp = requests.post(self.api + "/registrationNumberVC?vcid=" + str(cred_id), json=body)

        resp.raise_for_status()
        return resp.json()


class RegistryService:
    """ Wrapper class to connect GXDCH Registry Service. """

    def __init__(self, api_url: str):
        if not api_url:
            raise AttributeError("Parameters MUST not be None")
        self.api = api_url

    def get_gx_tandc(self) -> dict:
        resp = requests.get(self.api + "/api/termsAndConditions")
        resp.raise_for_status()
        return resp.json()
