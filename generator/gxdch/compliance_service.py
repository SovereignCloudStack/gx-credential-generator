import requests
from requests import Response
from typing import List


class ComplianceService:

    def __init__(self, api: str, jinja2_templates: str):
        if not api or not jinja2_templates:
            raise AttributeError("Parameters MUST not be None")
        self.api = api

    def issue_reg_number_vc(self, reg_number: str, csp_did: str) -> Response:
        if reg_number is None or csp_did is None:
            raise AttributeError("reg_number or csp_did MUST not be None")
        body = {
            "@context": [
                "https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/participant"
            ],
            "type": "gx:legalRegistrationNumber",
            "id": csp_did,
            "gx:vatID": reg_number
        }
        return requests.post(self.api, json=body)
