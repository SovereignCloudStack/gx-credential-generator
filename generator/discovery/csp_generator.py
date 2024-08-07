"""Generator of Gaia-X Credentials for CSPs.
"""
import json
from datetime import datetime, timezone

import generator.common.const as const
from generator.common import crypto
from generator.common.config import Config
from generator.discovery.vc_discovery import CredentialDiscovery
from generator.discovery.gxdch_services import NotaryService, ComplianceService
from generator.common import utils


class CspGenerator:

    def __init__(self, conf: Config) -> None:
        self.vc_discovery = CredentialDiscovery()
        self.notary = NotaryService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_NOT]))
        self.compliance = ComplianceService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_COMP]))

        self.csp = conf.get_value([const.CONFIG_CSP])
        self.cred_settings = conf.get_value([const.CONFIG_CRED])
        self.cred_base_url = conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL])

    def generate(self) -> dict:
        """Generate Gaia-X compliant Gaia-X Credential for CSP. This includes """
        # sign Gaia-X terms and conditions
        tac_vc = self._sign_gaia_x_terms_and_conditions()

        # retrieve legal registration number from GXDCH Notary
        lrn_cred_id = self.cred_base_url + "/lrn.json"
        lrn_vc = self.notary.request_reg_number_vc(csp=self.csp, cred_id=lrn_cred_id)

        # create Gaia-X Credential for CSP as Legal Person
        lp_vc = self._sign_legal_person(lrn_cred_id)

        # TODO: Remove jina templates
        vp_id = self.cred_base_url + "/compliance.json"
        vp = self.vc_discovery.create_verifiable_presentation(vcs=[lrn_vc, tac_vc, lp_vc],
                                                            cred_settings=self.cred_settings)
        # Add Signature
        #vp_signed = crypto.sign_cred(cred=vp,
        #                 key=crypto.load_jwk_from_file(self.cred_settings['key']),
        #                 verification_method=self.cred_settings['verification-method'])

        cs_vc = self.compliance.request_compliance_vc(vp, vp_id)

        return {'tac_vc': tac_vc, 'lrn_vc': lrn_vc, 'lp_vc': lp_vc, 'cs_vc': cs_vc }


    def _sign_gaia_x_terms_and_conditions(self) -> dict:
        """ Create a Gaia-X Credential on signed Gaia-X terms and conditions."""
        tan_vc = dict()
        tan_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
        tan_vc['type'] = "VerifiableCredential"
        tan_vc['id'] = self.cred_base_url + "/tandc.json"
        tan_vc['issuer'] = self.csp['did']
        tan_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
        tan_vc['credentialSubject'] = {
            "type": "gx:GaiaXTermsAndConditions",
            "gx:termsAndConditions": "The PARTICIPANT signing the Self-Description agrees as follows:\n- to update its descriptions about any changes, be it technical, organizational, or legal - especially but not limited to contractual in regards to the indicated attributes present in the descriptions.\n\nThe keypair used to sign Verifiable Credentials will be revoked where Gaia-X Association becomes aware of any inaccurate statements in regards to the claims which result in a non-compliance with the Trust Framework and policy rules defined in the Policy Rules and Labelling Document (PRLD).",
            "id": self.csp['did']
        }
        # TODO: Replace by own method in crypto
        return utils.sign_doc(tan_vc,
                              crypto.load_jwk_from_file(self.cred_settings[const.CONFIG_CRED_KEY]),
                              self.cred_settings[const.CONFIG_CRED_VER_METH])

    def _sign_legal_person(self, lrn_cred_id: str):
        """ Create Gaia-X Credential for CSP as Legal Person."""
        lp_vc = dict()
        lp_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
        lp_vc['type'] = "VerifiableCredential"
        lp_vc['id'] = self.cred_base_url + "/legal_person.json"
        lp_vc['issuer'] = self.csp['did']
        lp_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
        lp_vc['credentialSubject'] = {
            "id": self.csp['did'],
            "type": "gx:LegalParticipant",
            "gx:legalName": self.csp['legal-name'],
            "gx:legalRegistrationNumber": {
                "id": lrn_cred_id
            },
            "gx:headquarterAddress": {
                "gx:countrySubdivisionCode": self.csp['legal-address-country-code']
            },
            "gx:legalAddress": {
                "gx:countrySubdivisionCode": self.csp['headquarter-address-country-code']
            }
        }

        # TODO: Replace by own method in crypto
        return utils.sign_doc(lp_vc,
                              crypto.load_jwk_from_file(self.cred_settings[const.CONFIG_CRED_KEY]),
                              self.cred_settings[const.CONFIG_CRED_VER_METH])
