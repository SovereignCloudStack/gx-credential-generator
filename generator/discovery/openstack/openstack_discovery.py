from abc import ABCMeta,abstractmethod
from typing import List

from openstack.connection import Connection

from generator.common import const
from generator.common.config import Config
from generator.common.json_ld import JsonLdObject


class OpenStackDiscovery(metaclass=ABCMeta):

    def __init__(self, conn: Connection, conf: Config) -> None:
        self.conn = conn
        self.conf = conf
    @abstractmethod
    def discover(self) -> List[JsonLdObject]:
        pass

    import generator.common.const as const

    def get_copyright_owner(self, software: str) -> List[str]:
        return self.conf.get_value([const.COMFIG_SOFTWARE, software, const.CONFIG_COPYRIGHT])

    def get_license(self, software: str) -> List[str]:
        return self.conf.get_value([const.COMFIG_SOFTWARE,software,const.CONFIG_LICENSE])

    def get_resource_policy(self, software: str) -> List[str]:
        return self.conf.get_value([const.COMFIG_SOFTWARE,software,const.CONFIG_RESOURCE_POLICY])




