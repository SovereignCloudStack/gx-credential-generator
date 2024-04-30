import os

import requests
from requests import Response
from typing import List
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import uuid

class NotaryService:

    def __init__(self, api: str, jinja2_templates: str):
        if not api or not jinja2_templates:
            raise AttributeError("Parameters MUST not be None")
        self.api = api
        self.jinja_env = Environment(
            loader=FileSystemLoader(jinja2_templates),
            autoescape=select_autoescape()
        )
        print(os.getcwd())

    def issue_vat_id_vc(self, vat_id: str, csp_did: str) -> Response:
        if vat_id is None or csp_did is None:
            raise AttributeError("reg_number or csp_did MUST not be None")#

        cred_id = uuid.uuid1()
        req_tmpl = self.jinja_env.get_template("http-requests/gxdch-not-request.json")
        req_body = req_tmpl.render(csp_did=csp_did, vat_id=vat_id)
        return requests.post(self.api + "?vcid=" + str(cred_id), json=json.loads(req_body))
