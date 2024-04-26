from abc import ABC, abstractmethod
from rdflib import Graph


class Wallet(ABC):

    @abstractmethod
    def get_credential_by_id(self, cred_id: str, type: str = None) -> Graph:
        pass

    @abstractmethod
    def get_credentials_of_subject(self, subject_id: str, type: str = None) -> Graph:
        pass
