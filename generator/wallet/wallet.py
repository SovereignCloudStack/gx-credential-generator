from abc import ABCMeta
from abc import abstractmethod
from linkml_runtime.utils.yamlutils import YAMLRoot


class WalletConnector(ABCMeta):
    """
    Abstraction for wallet connections. A wallet stores Gaia-X credentials and class WalletsConnector
    wraps API calls for different kind of wallets.
    """

    @abstractmethod
    def store_credential(self, credential: YAMLRoot, filename: str = None) -> None:
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
