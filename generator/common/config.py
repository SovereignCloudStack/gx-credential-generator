from typing import List

from generator.common import const


def _get_value(config, keys: List[str]):
    if not keys:
        return config

    value = config[keys[0]]
    if isinstance(value, dict):
        keys.remove(keys[0])
        return _get_value(value, keys)
    else:
        return value


class Config:
    def __init__(self, config):
        self.config = config

    def get_value(self, keys: List[str]):
        try:
            return _get_value(self.config, keys)
        except KeyError:
            raise KeyError("Config file missing following keys: " + str(keys))

    def get_copyright_owner(self, software: str) -> List[str]:
        return self.get_value([const.CONFIG_SOFTWARE, software, const.CONFIG_COPYRIGHT])

    def get_license(self, software: str) -> List[str]:
        return self.get_value([const.CONFIG_SOFTWARE, software, const.CONFIG_LICENSE])

    def get_resource_policy(self, software: str) -> List[str]:
        return self.get_value(
            [const.CONFIG_SOFTWARE, software, const.CONFIG_RESOURCE_POLICY]
        )
