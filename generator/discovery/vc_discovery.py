from generator.common.config import Config
from generator.common import const
import requests
from requests import Response
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import uuid
import datetime
from generator.common import crypto

class ParticipantGenerator:

    def __init__(self,templates: Environment, csp: dict, cred_option: dict):
        self.csp = csp
        self.cred_option = cred_option
        self.templates = templates


    def create_and_sign_participant_vc(self):
        pass

    def _create_and_sign_gaia_x_terms_and_conditions(self) -> dict:
        """ Create and sign Gaia-X Credentuial for Gaia-X terms and conditions."""

        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is in sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics

        now = datetime.today().isoformat()
        cred_id = self.cred_option[const.CONFIG_CRED_BASE_CRED_URL] + "/gaia-x-terms-and-cond.json/"
        cred = self.templates.get_template("credentials/terms-and-credentials_22.10.json").render(csp=self.csp,
                                                                                                  date=now,
                                                                                                  cred_id=cred_id)
        cred = json.loads(cred)
        crypto.sign_cred(cred=cred,
                         private_key=crypto.load_jwk_from_file(self.cred_option[const.CONFIG_CRED_KEY]),
                         verification_method=self.cred_option[const.CONFIG_CRED_VER_METH])
        return cred
