from code_artifact import CodeArtifact
"""""
This class reflects the class 'Image' of Gaia-X Credential schema.

"""

from cpu import CPU

class Image(CodeArtifact):

    def __init__(self,
                 fileSize: int,
                 operatingSystem: str,
                 cpuReq: CPU,
                 gpuReq: GPU,
                 ramReq: Memory,
                 videoRamSize: int,
                 rootDiskReq: Disk,
                 encryption: Enrcyption,
                 secureBoot: boolean,
                 vPMU: boolean,
                 updateStrategfy: UpdateStrategy,
                 license_included: boolean,
                 maintenance: Maintenance ) -> None:
        pass

    def generate_gx_cred(self) -> str:
        return super().generate_gx_cred()




