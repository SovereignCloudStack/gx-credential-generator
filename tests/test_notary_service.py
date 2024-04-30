import unittest

from generator.gxdch.notary_service import NotaryService

class NotaryServiceTestCase(unittest.TestCase):
    def test_issue_registration_number_vc(self):
        not_serv = NotaryService("https://registrationnumber.notary.gaia-x.eu/v1/registrationNumberVC")
        resp = not_serv.issue_reg_number_vc(csp_did="did:web:example.com", reg_number="DE281093504")
        print(resp)




if __name__ == "__main__":
    unittest.main()
