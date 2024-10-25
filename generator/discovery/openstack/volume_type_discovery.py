from datetime import datetime
from distutils.command.config import config
from typing import List, Union
import re

import generator.common.const as const
from generator.common.config import Config

from generator.common.gx_schema import BlockStorageConfiguration as GX_Type
from generator.common.gx_schema import Encryption

from openstack.connection import Connection
from openstack.block_storage.v3.type import Type as OS_Type


class VolumeTypeDiscovery:

    def __init__(self, conn: Connection, conf: Config) -> None:
        """
        Constructor.
        @param conn: Openstack Connection
        @param conf: configuration
        """
        self.conn = conn
        self.conf = conf

    def discover(self) -> List[GX_Type]:
        """
        Return one credential for each public VM image offered by openstack cloud.

        @return: list of VM images
        """
        types = []
        for t in self.conn.list_volume_types():
            types.append(self._convert_to_gx_type(t))
        return types

    def _convert_to_gx_type(self, v_type: OS_Type) -> GX_Type:
        gx_vol_type = GX_Type(name=v_type.name, description=v_type.description)

        if self._is_volume_encrypted(v_type.description):
            gx_vol_type.storageEncryption = {
                'id': self.conf.get_value([const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-encryption-" + v_type.id
            }
        if self._is_volume_replicated(v_type.description):
            gx_vol_type.storageRedundancyMechanism = [{
                'id': self.conf.get_value(
                    [const.CONFIG_CRED, const.CONFIG_CRED_BASE_CRED_URL]) + "/storage-replication-" + v_type.id
            }]

        return gx_vol_type

    def _is_volume_encrypted(self, vol_desc) -> bool:
        if not vol_desc:
            return False
        return True if re.search(r'\[scs:.*\s+encrypted[, \]].*', vol_desc) else False

    def _is_volume_replicated(self, vol_desc) -> bool:
        if not vol_desc:
            return False
        return True if re.search(r'\[scs:.*\s+replicated[, \]].*', vol_desc) else False
