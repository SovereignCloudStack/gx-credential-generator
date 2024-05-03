import os

import requests
from requests import Response
from typing import List
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import uuid


class NotaryService:
    """ Wrapper class to connect GXDCH notary service. """
    def __init__(self, api: str, templates: Environment):
        if not api or not templates:
            raise AttributeError("Parameters MUST not be None")
        self.api = api
        self.templates = templates

    def issue_vat_id_vc(self, csp: dict) -> Response:
        if not csp:
            raise AttributeError("csp MUST not be None")  #

        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is ins sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics
        cred_id = uuid.uuid1()
        req_tmpl = self.templates.get_template("http-requests/gxdch-not-request.json")
        req_body = req_tmpl.render(csp=csp)
        return requests.post(self.api + "?vcid=" + str(cred_id), json=json.loads(req_body))
