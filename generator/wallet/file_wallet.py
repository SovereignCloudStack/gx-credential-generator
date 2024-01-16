import json
import os

from generator.common.json_ld import JsonLdObject, get_json_ld_context, to_json_ld
from generator.wallet.wallet import WalletConnector


class FileSystemWallet(WalletConnector, object):
    """
    Abstraction for filesystem acting as a wallet.
    """

    def __init__(self, dir: str) -> None:
        super().__init__()
        self.dir = dir

    def store_credential(self, credential: JsonLdObject) -> None:
        super().store_credential(credential)

        with open(
            os.path.join(self.dir, "vm_image_" + credential.gx_id + ".json-ld"), "w"
        ) as json_file:
            props = get_json_ld_context()
            props["@graph"] = [credential]
            json.dump(props, json_file, indent=4, default=to_json_ld)

    def get_provider_cred_did(self, service_offering: str) -> str:
        return super().get_provider_cred_did(service_offering)
