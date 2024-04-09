from typing import List
import os

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
        return _get_value(self.config, keys)
