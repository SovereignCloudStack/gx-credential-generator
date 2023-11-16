from abc import ABC
from abc import abstractmethod


class GxCredential(ABC):
    @abstractmethod
    def generate_gx_cred(self) -> str:
        return ""
