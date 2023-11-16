"""""
These classe reflect the class 'CodeArtifact' of Gaia-X Credential schema.
"""
from generator.gx.gx_credential import GxCredential



class CodeArtifact(GxCredential):

    def __init__(self, ) -> None:
        pass

    def generate_gx_cred(self) -> str:
        return super().generate_gx_cred()
