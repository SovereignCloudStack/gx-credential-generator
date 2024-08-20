"""Generator of Gaia-X Credentials for CSPs.
"""
import json
from datetime import datetime, timezone

import generator.common.const as const
from generator.common import credentials, crypto
from generator.common.config import Config
from generator.discovery.gxdch_services import (ComplianceService,
                                                NotaryService, RegistryService)


class CspGenerator:

    def __init__(self, conf: Config) -> None:
        self.notary = NotaryService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_NOT]))
        self.compliance = ComplianceService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_COMP]))
        self.registry = RegistryService(conf.get_value([const.CONST_GXDCH, const.CONST_GXDCH_REG]))

        self.csp = conf.get_value([const.CONFIG_CSP])
        self.cred_settings = conf.get_value([const.CONFIG_CRED])
        self.cred_base_url = self.cred_settings[const.CONFIG_CRED_BASE_CRED_URL]

    def generate(self, auto_sign: bool = False) -> dict:
        """
        Generate Gaia-X compliant Gaia-X Credential for CSP. This includes the following Verifiable Credentials (VC).
          - VC on signed Gaia-X terms and conditions
          - VC on CSP's legal registration number, such as LEI or VAT id
          - VC on CSP's properties as Gaia-X Legal Person
          - VC on CSP's Gaia-X compliance

        @param auto_sign True, if Gaia-X terms and conditions should be automatically signed. Else user has to confirm
        terms and conditions manually on user prompt.
        @return: dictionary of VCs
        """
        # sign Gaia-X terms and conditions
        print('Create and sign VC of type "gx:GaiaXTermsAndConditions" for CSP...', end='')
        tandc_vc = self._sign_gaia_x_terms_and_conditions(auto_sign=auto_sign)
        if tandc_vc is None:
            return
        print('ok')

        # retrieve legal registration number from GXDCH Notary
        print('Request VC of type for "gx:LegalRegistrationNumber" for CSP at GXDCH Notary Service...', end='')
        lrn_vc = self.notary.request_reg_number_vc(
            csp=self.csp,
            cred_id=self.cred_base_url + "/lrn.json",
            cred_subject_id=self.cred_base_url + "/lrn_cs.json")
        print('ok')

        # create Gaia-X Credential for CSP as Legal Person
        print('Create and sign VC of type "gx:LegalPerson for CSP"...', end='')
        lp_vc = self._sign_legal_person(lrn_vc['credentialSubject']['id'])
        print('ok')

        # request Gaia-X compliance credential for CSP as Legal Person
        print('Request VC of type "gx:compliance" for CSP at GXDCH Compliance Service...', end='')
        vp = credentials.convert_to_vp(creds=[tandc_vc, lrn_vc, lp_vc])
        cs_vc = self.compliance.request_compliance_vc(vp, self.cred_base_url + "/csp_compliance.json")
        print('ok')
        return {'tandc': tandc_vc, 'lrn': lrn_vc, 'lp': lp_vc, 'cs': json.loads(cs_vc), 'vp_csp': vp}
        
    def _sign_gaia_x_terms_and_conditions(self, auto_sign: bool = False) -> dict:
        """
        Create a Gaia-X Credential on signed Gaia-X terms and conditions.

        @param auto_sign: If true, Gaia-X terms and conditions are signed automatically,
        otherwise user is requested of confirm terms and conditions
        @return: Gaia-X Credential on signed Gaia-X terms and conditions as dictionary.
        """
        tand = self.registry.get_gx_tandc()
        if not auto_sign:
            print("Do you agree Gaia-X Terms and conditions version " + tand['version'] + ".")
            print()
            print("-------------------------- Gaia-X Terms and Conditions --------------------------------------------")
            print(tand['text'])
            print("-------------------------- ------------------------------------------------------------------------")
            print()
            print("Please type 'y' for 'I do agree' and 'n' for 'I do not agree': ")

            resp = input()
            while resp.lower() not in ['y', 'n']:
                print("Please type 'y' for 'I do agree' and 'n' for 'I do not agree: '")
                resp = input()

            if resp.lower() == 'n':
                # user did not agree Gaia-X terms and conditions, we have to abort here
                print("Gaia-X terms and conditions were not signed - process aborted!")
                return

        tandc_vc = dict()
        tandc_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
        tandc_vc['type'] = "VerifiableCredential"
        tandc_vc['id'] = self.cred_base_url + "/tandc.json"
        tandc_vc['issuer'] = self.csp['did']
        tandc_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
        tandc_vc['credentialSubject'] = {
            "type": "gx:GaiaXTermsAndConditions",
            "gx:termsAndConditions": tand['text'],
            "id": self.cred_base_url + "/tandc_cs.json"
        }
        return crypto.sign_cred(cred=tandc_vc,
                                key=crypto.load_jwk_from_file(self.cred_settings[const.CONFIG_CRED_KEY]),
                                verification_method=self.cred_settings[const.CONFIG_CRED_VER_METH])

    def _sign_legal_person(self, lrn_cred_id: str):
        """
        Create Gaia-X Credential for CSP as Legal Person.

        @param lrn_cred_id: Id of Verifiable Credential attesting CSP's legal registration number.
        @return: Gaia-X Credential on CSP as Legal Person as dictionary.
        """
        lp_vc = dict()
        lp_vc['@context'] = [const.VC_CONTEXT, const.JWS_CONTEXT, const.REG_CONTEXT]
        lp_vc['type'] = "VerifiableCredential"
        lp_vc['id'] = self.cred_base_url + "/legal_person.json"
        lp_vc['issuer'] = self.csp['did']
        lp_vc['issuanceDate'] = str(datetime.now(tz=timezone.utc).isoformat())
        lp_vc['credentialSubject'] = {
            "id": self.cred_base_url + "/legal_person_cs.json",  # I think "self.csp['did']" is correct, but Gaia-X expects link,
            # "id": self.csp['did'],
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
        return crypto.sign_cred(cred=lp_vc,
                                key=crypto.load_jwk_from_file(self.cred_settings[const.CONFIG_CRED_KEY]),
                                verification_method=self.cred_settings[const.CONFIG_CRED_VER_METH])
