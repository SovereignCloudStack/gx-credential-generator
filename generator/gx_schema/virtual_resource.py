"""""
These classe reflect the class 'VirtualResource' of Gaia-X Credential schema.
"""

from __future__ import annotations

from generator.gx_schema.resource import Resource
from generator.gx_schema.participant import Participant

from typing import Union


class VirtualResource(Resource):
    copyright_owned_by: Union[str, Participant]
    license: str
    resource_policy: str

    def __init__(self, copyright_owned_by: Union[str, Participant], license: str,
                 resource_policy: str, aggregation_of_resources: Resource = None) -> None:
        super().__init__(aggregation_of_resources=aggregation_of_resources)
        self.copyright_owned_by = copyright_owned_by
        self.license = license
        self.resource_policy = resource_policy

    def generate_gx_cred(self) -> str:
        return super().generate_gx_cred()
