from typing import List
from generator.common import const, crypto
import json

def convert_to_vp(creds: List[dict]) -> str:
    vp = dict()
    vp['@context'] = const.VP_CONTEXT
    vp['type'] = "VerifiablePresentation"
    vp['verifiableCredential'] = creds
    return json.dumps(vp)