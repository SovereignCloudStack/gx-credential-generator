from typing import Dict, List

import generator.common.const as const


def get_copyright_owner(config: Dict, software: str) -> List[str]:
    return config[const.COMFIG_SOFTWARE][software][const.CONFIG_COPYRIGHT]


def get_license(config: Dict, software: str) -> List[str]:
    return config[const.COMFIG_SOFTWARE][software][const.CONFIG_LICENSE]


def get_resource_policy(config: Dict, software: str) -> List[str]:
    return config[const.COMFIG_SOFTWARE][software][const.CONFIG_RESOURCE_POLICY]
