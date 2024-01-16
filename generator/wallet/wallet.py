from abc import ABC
from abc import abstractmethod

from generator.common.json_ld import JsonLdObject


class WalletConnector(ABC):
    """
    Abstraction for wallet connections. A wallet stores Gaia-X credentials and class WalletsConnector
    wraps API calls for different kind of wallets.
    """

    @abstractmethod
    def store_credential(self, credential: JsonLdObject) -> None:
        """
        Stores given CREDENTIAL in this wallet.
        @param credential: credential to be stored in JSON-LD
        @type JsonLdObject
        @return: None
        """
        pass

    @abstractmethod
    def get_provider_cred_did(self, service_offering: str) -> str:
        """Returns DID of provider of given service offering.

        Parameters
        ----------
        service_offering : str
            DID of service offering

        Returns
        -------
        str
            DID of service offering's provider
        """
        return ""
