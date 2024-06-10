import requests
from requests import Response
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import uuid


class NotaryService:
    """ Wrapper class to connect GXDCH notary service. """

    def __init__(self, api: str, j_env: Environment):
        if not api or not j_env:
            raise AttributeError("Parameters MUST not be None")
        self.api = api
        self.j_env = j_env

    # TODO: Support all kind of registration numbers
    def issue_reg_number_vc(self, csp: dict) -> Response:
        if not csp:
            raise AttributeError("csp MUST not be None")  #

        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is ins sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics
        cred_id = uuid.uuid1()
        req_tmpl = self.j_env.get_template("http-requests/gxdch-not-request.json")
        req_body = req_tmpl.render(csp=csp)
        return requests.post(self.api + "?vcid=" + str(cred_id), json=json.loads(req_body))
