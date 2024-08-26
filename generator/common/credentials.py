from typing import List

from generator.common import const


def convert_to_vp(creds: List[dict]) -> str:
    return {
        '@context': const.VP_CONTEXT,
        'type': "VerifiablePresentation",
        'verifiableCredential': creds,
    }
