from wallet import WalletConnector


class XFSCWallet(WalletConnector):
    """
    Abstraction XFSC wallet, called Organization Credential Manager.
    See https://projects.eclipse.org/projects/technology.xfsc
    """

    def get_provider_cred_did(self, service_offering: str) -> str:
        return super().get_provider_cred_did(service_offering)
