import json

import requests
from requests import Response
from typing import List
from jinja2 import Environment

class ComplianceService:

    def __init__(self, api: str, templates: Environment):
        if not api or not templates:
            raise AttributeError("Parameters MUST not be None")
        self.api = api
        self.templates = templates

    def request_compliance_vc(self, vcs: List[dict]) -> Response:
        if not vcs:
            raise AttributeError("List of verifiable credentials MUST not be None or empty")

        print(vcs)
        body = dict()
        body['@context'] = "https://www.w3.org/2018/credentials/v1"
        body['@type'] = "VerifiablePresentation"
        body['verifiableCredential'] = vcs

        print(body)
        print(json.dumps(body, indent=4))

        return requests.post("https://compliance.lab.gaia-x.eu/v1/api/credential-offers", json=body)
        #return requests.post(self.api, json=body)
