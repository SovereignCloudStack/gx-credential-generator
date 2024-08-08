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
    """Wrapper class for all configuration settings. Configuration settings are stored in yaml file on drive and
      imported as a nested dictionary."""
    def __init__(self, config: dict):
        self.config = config

    def get_value(self, keys: List[str]):
        """
        Return configuration value. Config settings are stored as yaml and imported as nested dict.
        E.g. { 'key1': {'key2': {'key3': 'foo'}}}

        The list of keys are required to step down throught nested dicts to requested value.
        E.g. ['key1', 'key2', 'key3'] returns 'foo'
        @param keys: list of keys
        @return: value
        """
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
