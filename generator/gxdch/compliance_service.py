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
