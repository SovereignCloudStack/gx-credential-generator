"""""
These classe reflect the class 'Resource' of Gaia-X Credential schema.
"""

from __future__ import annotations

from generator.gx.gx_credential import  GxCredential


class Resource(GxCredential):
    aggregation_of_resources: Resource

    def __init__(self, aggregation_of_resources: Resource = None) -> None:
        self.aggregation_of_resources = aggregation_of_resources

    def generate_gx_cred(self) -> str:
        return super().generate_gx_cred()
