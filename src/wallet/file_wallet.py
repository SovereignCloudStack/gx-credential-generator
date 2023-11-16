from wallet import WalletConnector


class FileSystemWallet(WalletConnector):
    """
    Abstraction for filesystem acting as wallet.
    """

    def get_provider_cred_did(self, service_offering: str) -> str:
        return super().get_provider_cred_did(service_offering)
