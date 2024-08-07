
import json
from datetime import datetime, timezone
from generator.common import crypto

from typing import List

from generator.common import const

from jinja2 import Environment, FileSystemLoader, select_autoescape



class CredentialDiscovery:
    """
    Discovery for mandatory and optional Gaia-X Credentials in context of Gaia-X.
    """

    def __init__(self):
        self.jinja_env = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=select_autoescape()
        )

    def create_and_sign_legal_person_vc(self, cred_id: str, lrn_cred_id: str, csp: dict, cred_settings: dict) -> dict:
        # TODO: Support list of legal registration number VCs
        """ Create and sign Gaia-X Credential for Legal Person."""
        return self._create_and_sign_cred(template="credentials/legal-person_20.10.json",
                                          content={'csp': csp, 'cred_id': cred_id, 'lrn_cred_id': lrn_cred_id},
                                          cred_settings=cred_settings)

    def create_gaia_x_terms_and_conditions_vc(self, cred_id: str, csp: dict, cred_settings: dict) -> dict:
        """ Create and sign Gaia-X Credential for Gaia-X terms and conditions."""
        return self._create_and_sign_cred(template="credentials/terms-and-conditions_22.10.json",
                                          content={'csp': csp, 'cred_id': cred_id},
                                          cred_settings=cred_settings)

    def create_verifiable_presentation(self, vcs: List[dict], cred_settings: dict) -> dict:
        cred = {
            "@context": "https://www.w3.org/2018/credentials/v1",
            "type": "VerifiablePresentation",
            "verifiableCredential": list()
        }

        vp = self.jinja_env.get_template("credentials/verifiable-presenation_22.10.json").render(vcs = vcs)

        [cred['verifiableCredential'].append(vc) for vc in vcs]
        #crypto.sign_cred(cred=cred,
        #                 key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
        #                 verification_method=cred_settings[const.CONFIG_CRED_VER_METH])

        return vp

    def _create_and_sign_cred(self, template: str, content: dict, cred_settings: dict) -> dict:
        # TODO: Use python classes instead of jinja2 templates here as soon as GXDCH is in sync with latest Gaia-X
        # Credential Schema from https://gitlab.com/gaia-x/technical-committee/service-characteristics
        content['date'] = str(datetime.now(tz=timezone.utc).isoformat())
        cred = json.loads(self.jinja_env.get_template(template).render(content))
        print("=============== T&A ==================")
        print(json.dumps(cred, indent=4))
        import generator.common.utils as utils

        print("=============== T&A - signed ==================")
        signed_cred = utils.sign_doc(cred, crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]), cred_settings[const.CONFIG_CRED_VER_METH])
        print(json.dumps(signed_cred, indent=4))

        #crypto.sign_cred(cred=cred,
        #                 key=crypto.load_jwk_from_file(cred_settings[const.CONFIG_CRED_KEY]),
        #                 verification_method=cred_settings[const.CONFIG_CRED_VER_METH])
        return signed_cred

    #def request_vat_id_vc(self, csp: dict, cred_id) -> dict:
    #    resp = self.not_service.request_reg_number_vc(csp=csp, cred_id=cred_id)
    #    if resp.ok:
    #        return resp.json()
    #    else:
    #        resp.raise_for_status()

    #def request_compliance_vc(self, vp: str, vp_id):
    #    resp = self.comp_service.request_compliance_vc(vp, vp_id)
    #    if resp.ok:
    #        return resp.json()
    #    else:
    #        resp.raise_for_status()
