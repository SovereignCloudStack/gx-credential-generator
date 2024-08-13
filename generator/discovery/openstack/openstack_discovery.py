""""General openstack discovery class.
"""

from hashlib import sha256

import requests
from openstack.connection import Connection
from requests.exceptions import HTTPError

from generator.common import const
from generator.common.config import Config
from generator.common.gx_schema import (DataAccountExport, TermsAndConditions,
                                        VirtualMachineServiceOffering)
from generator.discovery.openstack.server_flavor_discovery import \
    ServerFlavorDiscovery
from generator.discovery.openstack.vm_images_discovery import VmImageDiscovery


class OpenstackDiscovery:
    """Abstraction for openStack cloud with all its services."""

    def __init__(self, conn: Connection, config: Config) -> None:
        self.conn = conn
        # self.regions = list(conn.identity.regions())
        self.config = config

    def discover(self) -> VirtualMachineServiceOffering:
        """
        Discover all attributes of OS Cloud as Gaia-X VirtualMachineServiceOffering.

        @return: all attributes as Gaia-X VirtualMachineServiceOffering
        @rtype List[dict]
        """
        images = VmImageDiscovery(self.conn, self.config).discover()
        flavors = ServerFlavorDiscovery(self.conn, self.config).discover()

        # Create Virtual Service Offering object
        data_export_account = DataAccountExport(
            requestType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_REQ_TYPE,
                ]
            ),
            accessType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_ACCESS_TYPE,
                ]
            ),
            formatType=self.config.get_value(
                [
                    const.CONFIG_IAAS,
                    const.CONFIG_IAAS_DATA_EXPORT,
                    const.CONFIG_IAAS_DATA_EXPORT_FORMAT_TYPE,
                ]
            ),
        )
        service_tac = []
        for url in self.config.get_value(
                [const.CONFIG_IAAS, const.CONFIG_IAAS_T_AND_C]
        ):
            httpResponse = requests.get(url)
            if httpResponse.status_code == 200:
                content = httpResponse.text
                service_tac.append(
                    TermsAndConditions(
                        url=url, hash=sha256(content.encode("utf-8")).hexdigest()
                    )
                )
            else:
                raise HTTPError(
                    "Cloud not retrieve terms and conditions from '"
                    + url + "'. HTTP Status code: " + str(httpResponse.status_code)
                )

        if len(service_tac) == 0:
            raise ValueError(
                "Service offerings terms and conditions MUST not be empty. Please check config.yaml. There MUST be at least on entry."
                + const.CONFIG_IAAS + "." + const.CONFIG_IAAS_T_AND_C
            )

        return VirtualMachineServiceOffering(
            providedBy=self.config.get_value([const.CONFIG_CSP, const.CONFIG_DID]),
            dataAccountExport=data_export_account,
            servicePolicy=self.config.get_value(
                [const.CONFIG_IAAS, const.CONFIG_IAAS_SERVICE_POLICY]
            ),
            serviceOfferingTermsAndConditions=service_tac,
            codeArtifact=images,
            instantiationReq=flavors,
        )
