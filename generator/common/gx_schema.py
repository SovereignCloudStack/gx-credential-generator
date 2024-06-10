# Auto generated from gaia-x.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-31T11:26:50
# Schema: gaia-x
#
# id: https://w3id.org/gaia-x/deployment#gaia-x
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional, Union

from jsonasobj2 import JsonObj, as_dict
from linkml_runtime.linkml_model.meta import (EnumDefinition, PermissibleValue,
                                              PvFormulaOptions)
from linkml_runtime.linkml_model.types import (Boolean, Date, Datetime, Float,
                                               Integer, String, Uri)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import \
    dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import camelcase, sfx, underscore
from linkml_runtime.utils.metamodelcore import (URI, Bool, XSDDate,
                                                XSDDateTime, bnode, empty_dict,
                                                empty_list)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (YAMLRoot, extended_float,
                                            extended_int, extended_str)
from rdflib import Namespace, URIRef

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GX = CurieNamespace('gx', 'https://w3id.org/gaia-x/deployment#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/vocab/')
QUDT_SCHEMA = CurieNamespace('qudt_schema', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
DEFAULT_ = GX


# Types

# Class references
class LocalRegistrationNumberLocal(extended_str):
    pass


class VatIDVatID(extended_str):
    pass


class LeiCodeLeiCode(extended_str):
    pass


class EORIEori(extended_str):
    pass


class EUIDEuid(extended_str):
    pass


class LegalPersonRegistrationNumber(extended_str):
    pass


class InterconnectionPointIdentifierCompleteIPI(extended_str):
    pass


class GaiaX(YAMLRoot):
    """
    Top level element of Gaia-X ecosystem.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["GaiaX"]
    class_class_curie: ClassVar[str] = "gx:GaiaX"
    class_name: ClassVar[str] = "GaiaX"
    class_model_uri: ClassVar[URIRef] = GX.GaiaX


@dataclass
class Address(YAMLRoot):
    """
    Full address of the entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Address"]
    class_class_curie: ClassVar[str] = "vcard:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = GX.Address

    countryCode: str = None
    gps: Optional[Union[Union[dict, "GPSLocation"], List[Union[dict, "GPSLocation"]]]] = empty_list()
    streetAddress: Optional[str] = None
    postalCode: Optional[str] = None
    locality: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.countryCode):
            self.MissingRequiredField("countryCode")
        if not isinstance(self.countryCode, str):
            self.countryCode = str(self.countryCode)

        #self._normalize_inlined_as_dict(slot_name="gps", slot_type=GPSLocation, key_name="latitude", keyed=False)

        if self.streetAddress is not None and not isinstance(self.streetAddress, str):
            self.streetAddress = str(self.streetAddress)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.locality is not None and not isinstance(self.locality, str):
            self.locality = str(self.locality)

        super().__post_init__(**kwargs)


@dataclass
class GPSLocation(YAMLRoot):
    """
    Physical GPS coordinates in ISO 6709:2008/Cor 1:2009 format.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["GPSLocation"]
    class_class_curie: ClassVar[str] = "gx:GPSLocation"
    class_name: ClassVar[str] = "GPSLocation"
    class_model_uri: ClassVar[URIRef] = GX.GPSLocation

    latitude: str = None
    longitude: str = None
    altitude: Optional[str] = None
    crs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.latitude):
            self.MissingRequiredField("latitude")
        if not isinstance(self.latitude, str):
            self.latitude = str(self.latitude)

        if self._is_empty(self.longitude):
            self.MissingRequiredField("longitude")
        if not isinstance(self.longitude, str):
            self.longitude = str(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, str):
            self.altitude = str(self.altitude)

        if self.crs is not None and not isinstance(self.crs, str):
            self.crs = str(self.crs)

        super().__post_init__(**kwargs)


@dataclass
class GPSUnit(YAMLRoot):
    """
    Definition of a geographical point.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["GPSUnit"]
    class_class_curie: ClassVar[str] = "gx:GPSUnit"
    class_name: ClassVar[str] = "GPSUnit"
    class_model_uri: ClassVar[URIRef] = GX.GPSUnit

    degrees: int = None
    minutes: Optional[int] = None
    seconds: Optional[int] = None
    decimals: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.degrees):
            self.MissingRequiredField("degrees")
        if not isinstance(self.degrees, int):
            self.degrees = int(self.degrees)

        if self.minutes is not None and not isinstance(self.minutes, int):
            self.minutes = int(self.minutes)

        if self.seconds is not None and not isinstance(self.seconds, int):
            self.seconds = int(self.seconds)

        if self.decimals is not None and not isinstance(self.decimals, float):
            self.decimals = float(self.decimals)

        super().__post_init__(**kwargs)


@dataclass
class GaiaXEntity(YAMLRoot):
    """
    Root class for Gaia-X entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["GaiaXEntity"]
    class_class_curie: ClassVar[str] = "gx:GaiaXEntity"
    class_name: ClassVar[str] = "GaiaXEntity"
    class_model_uri: ClassVar[URIRef] = GX.GaiaXEntity

    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Encryption(YAMLRoot):
    """
    Encryption capabilities of a Gaia-X entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Encryption"]
    class_class_curie: ClassVar[str] = "gx:Encryption"
    class_name: ClassVar[str] = "Encryption"
    class_model_uri: ClassVar[URIRef] = GX.Encryption

    cipher: Union[str, "EncryptionAlgorithm"] = None
    keyManagement: Union[str, "KeyManagement"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cipher):
            self.MissingRequiredField("cipher")
        if not isinstance(self.cipher, EncryptionAlgorithm):
            self.cipher = EncryptionAlgorithm(self.cipher)

        if self._is_empty(self.keyManagement):
            self.MissingRequiredField("keyManagement")
        if not isinstance(self.keyManagement, KeyManagement):
            self.keyManagement = KeyManagement(self.keyManagement)

        super().__post_init__(**kwargs)


@dataclass
class CheckSum(YAMLRoot):
    """
    Detail on how to calculate or verify a checksum.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["CheckSum"]
    class_class_curie: ClassVar[str] = "gx:CheckSum"
    class_name: ClassVar[str] = "CheckSum"
    class_model_uri: ClassVar[URIRef] = GX.CheckSum

    checkSumCalculation: Union[str, "ChecksumAlgorithm"] = None
    checkSumValue: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.checkSumCalculation):
            self.MissingRequiredField("checkSumCalculation")
        if not isinstance(self.checkSumCalculation, ChecksumAlgorithm):
            self.checkSumCalculation = ChecksumAlgorithm(self.checkSumCalculation)

        if self._is_empty(self.checkSumValue):
            self.MissingRequiredField("checkSumValue")
        if not isinstance(self.checkSumValue, str):
            self.checkSumValue = str(self.checkSumValue)

        super().__post_init__(**kwargs)


@dataclass
class Signature(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Signature"]
    class_class_curie: ClassVar[str] = "gx:Signature"
    class_name: ClassVar[str] = "Signature"
    class_model_uri: ClassVar[URIRef] = GX.Signature

    signatureValue: str = None
    hashAlgorithm: Union[str, "ChecksumAlgorithm"] = None
    signatureAlgorithm: Union[str, "SignatureAlgorithm"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.signatureValue):
            self.MissingRequiredField("signatureValue")
        if not isinstance(self.signatureValue, str):
            self.signatureValue = str(self.signatureValue)

        if self._is_empty(self.hashAlgorithm):
            self.MissingRequiredField("hashAlgorithm")
        if not isinstance(self.hashAlgorithm, ChecksumAlgorithm):
            self.hashAlgorithm = ChecksumAlgorithm(self.hashAlgorithm)

        if self._is_empty(self.signatureAlgorithm):
            self.MissingRequiredField("signatureAlgorithm")
        if not isinstance(self.signatureAlgorithm, SignatureAlgorithm):
            self.signatureAlgorithm = SignatureAlgorithm(self.signatureAlgorithm)

        super().__post_init__(**kwargs)


@dataclass
class Device(YAMLRoot):
    """
    Details with respect to properties and capabilities of a hardware or virtualized device.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Device"]
    class_class_curie: ClassVar[str] = "gx:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = GX.Device

    vendor: Optional[str] = None
    generation: Optional[str] = None
    defaultOversubscriptionRatio: Optional[int] = None
    supportedOversubscriptionRatio: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.generation is not None and not isinstance(self.generation, str):
            self.generation = str(self.generation)

        if self.defaultOversubscriptionRatio is not None and not isinstance(self.defaultOversubscriptionRatio, int):
            self.defaultOversubscriptionRatio = int(self.defaultOversubscriptionRatio)

        if self.supportedOversubscriptionRatio is not None and not isinstance(self.supportedOversubscriptionRatio, int):
            self.supportedOversubscriptionRatio = int(self.supportedOversubscriptionRatio)

        super().__post_init__(**kwargs)


@dataclass
class CPU(Device):
    """
    Computational processing unit of virtual and physical machines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["CPU"]
    class_class_curie: ClassVar[str] = "gx:CPU"
    class_name: ClassVar[str] = "CPU"
    class_model_uri: ClassVar[URIRef] = GX.CPU

    cpuArchitecture: Optional[Union[str, "Architectures"]] = "Other"
    cpuFlag: Optional[Union[str, List[str]]] = empty_list()
    smtEnabled: Optional[Union[bool, Bool]] = False
    numberOfCores: Optional[int] = None
    numberOfThreads: Optional[int] = None
    baseFrequency: Optional[Union[dict, "Frequency"]] = None
    boostFrequency: Optional[Union[dict, "Frequency"]] = None
    lastLevelCacheSize: Optional[Union[dict, "MemorySize"]] = None
    thermalDesignPower: Optional[Union[dict, "Power"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cpuArchitecture is not None and not isinstance(self.cpuArchitecture, Architectures):
            self.cpuArchitecture = Architectures(self.cpuArchitecture)

        if not isinstance(self.cpuFlag, list):
            self.cpuFlag = [self.cpuFlag] if self.cpuFlag is not None else []
        self.cpuFlag = [v if isinstance(v, str) else str(v) for v in self.cpuFlag]

        if self.smtEnabled is not None and not isinstance(self.smtEnabled, Bool):
            self.smtEnabled = Bool(self.smtEnabled)

        if self.numberOfCores is not None and not isinstance(self.numberOfCores, int):
            self.numberOfCores = int(self.numberOfCores)

        if self.numberOfThreads is not None and not isinstance(self.numberOfThreads, int):
            self.numberOfThreads = int(self.numberOfThreads)

        if self.baseFrequency is not None and not isinstance(self.baseFrequency, Frequency):
            self.baseFrequency = Frequency(**as_dict(self.baseFrequency))

        if self.boostFrequency is not None and not isinstance(self.boostFrequency, Frequency):
            self.boostFrequency = Frequency(**as_dict(self.boostFrequency))

        if self.lastLevelCacheSize is not None and not isinstance(self.lastLevelCacheSize, MemorySize):
            self.lastLevelCacheSize = MemorySize(**as_dict(self.lastLevelCacheSize))

        if self.thermalDesignPower is not None and not isinstance(self.thermalDesignPower, Power):
            self.thermalDesignPower = Power(**as_dict(self.thermalDesignPower))

        super().__post_init__(**kwargs)


@dataclass
class Disk(Device):
    """
    Capabilities of a physical or virtual hard drive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Disk"]
    class_class_curie: ClassVar[str] = "gx:Disk"
    class_name: ClassVar[str] = "Disk"
    class_model_uri: ClassVar[URIRef] = GX.Disk

    diskSize: Union[dict, "MemorySize"] = None
    diskType: Optional[Union[str, "DiskType"]] = "other"
    diskBusType: Optional[Union[str, "DiskBusType"]] = "other"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.diskSize):
            self.MissingRequiredField("diskSize")
        if not isinstance(self.diskSize, MemorySize):
            self.diskSize = MemorySize(**as_dict(self.diskSize))

        if self.diskType is not None and not isinstance(self.diskType, DiskType):
            self.diskType = DiskType(self.diskType)

        if self.diskBusType is not None and not isinstance(self.diskBusType, DiskBusType):
            self.diskBusType = DiskBusType(self.diskBusType)

        super().__post_init__(**kwargs)


@dataclass
class Endpoint(YAMLRoot):
    """
    An endpoint is a mean to access and interact with a service or a resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Endpoint"]
    class_class_curie: ClassVar[str] = "gx:Endpoint"
    class_name: ClassVar[str] = "Endpoint"
    class_model_uri: ClassVar[URIRef] = GX.Endpoint

    standardConformity: Union[Union[dict, "StandardConformity"], List[Union[dict, "StandardConformity"]]] = None
    endpointURL: Optional[Union[str, URI]] = None
    formalDescription: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.standardConformity):
            self.MissingRequiredField("standardConformity")
        #self._normalize_inlined_as_dict(slot_name="standardConformity", slot_type=StandardConformity, key_name="title", keyed=False)

        if self.endpointURL is not None and not isinstance(self.endpointURL, URI):
            self.endpointURL = URI(self.endpointURL)

        if self.formalDescription is not None and not isinstance(self.formalDescription, str):
            self.formalDescription = str(self.formalDescription)

        super().__post_init__(**kwargs)


@dataclass
class GPU(Device):
    """
    Graphical processing unit of virtual and physical machines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["GPU"]
    class_class_curie: ClassVar[str] = "gx:GPU"
    class_name: ClassVar[str] = "GPU"
    class_model_uri: ClassVar[URIRef] = GX.GPU

    gpuMemory: Optional[Union[dict, "MemorySize"]] = None
    gpuInterconnection: Optional[Union[str, "GPUInterconnetionTypes"]] = "none"
    gpuProcessingUnits: Optional[int] = None
    gpuPassthrough: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gpuMemory is not None and not isinstance(self.gpuMemory, MemorySize):
            self.gpuMemory = MemorySize(**as_dict(self.gpuMemory))

        if self.gpuInterconnection is not None and not isinstance(self.gpuInterconnection, GPUInterconnetionTypes):
            self.gpuInterconnection = GPUInterconnetionTypes(self.gpuInterconnection)

        if self.gpuProcessingUnits is not None and not isinstance(self.gpuProcessingUnits, int):
            self.gpuProcessingUnits = int(self.gpuProcessingUnits)

        if self.gpuPassthrough is not None and not isinstance(self.gpuPassthrough, Bool):
            self.gpuPassthrough = Bool(self.gpuPassthrough)

        super().__post_init__(**kwargs)


@dataclass
class MaintenanceSubscription(YAMLRoot):
    """
    A maintenance subscriptions gives access to bug fixes, security fixes and function updates from software vendor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["MaintenanceSubscription"]
    class_class_curie: ClassVar[str] = "gx:MaintenanceSubscription"
    class_name: ClassVar[str] = "MaintenanceSubscription"
    class_model_uri: ClassVar[URIRef] = GX.MaintenanceSubscription

    subscriptionIncluded: Optional[Union[bool, Bool]] = False
    subscriptionRequired: Optional[Union[bool, Bool]] = False
    maintainedUntil: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subscriptionIncluded is not None and not isinstance(self.subscriptionIncluded, Bool):
            self.subscriptionIncluded = Bool(self.subscriptionIncluded)

        if self.subscriptionRequired is not None and not isinstance(self.subscriptionRequired, Bool):
            self.subscriptionRequired = Bool(self.subscriptionRequired)

        if self.maintainedUntil is not None and not isinstance(self.maintainedUntil, XSDDate):
            self.maintainedUntil = XSDDate(self.maintainedUntil)

        super().__post_init__(**kwargs)


@dataclass
class UpdateStrategy(YAMLRoot):
    """
    Cloud service customer expect cloud images to be updated regularly, in order to always get the image with the
    lasted patches. Technically, an updated image is a new image in cloud service' image catalogue having it's own
    unique image ID and replaces its old version. It is recommended to hide outdated version, but keep them
    referencable by its ID for a transition period for customers' convenience. This class defines important aspects of
    providers image update policy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["UpdateStrategy"]
    class_class_curie: ClassVar[str] = "gx:UpdateStrategy"
    class_name: ClassVar[str] = "UpdateStrategy"
    class_model_uri: ClassVar[URIRef] = GX.UpdateStrategy

    replaceFrequency: Optional[Union[str, "UpdateFrequency"]] = None
    hotfixHours: Optional[int] = None
    oldVersionsValidUntil: Optional[str] = None
    providedUntil: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.replaceFrequency is not None and not isinstance(self.replaceFrequency, UpdateFrequency):
            self.replaceFrequency = UpdateFrequency(self.replaceFrequency)

        if self.hotfixHours is not None and not isinstance(self.hotfixHours, int):
            self.hotfixHours = int(self.hotfixHours)

        if self.oldVersionsValidUntil is not None and not isinstance(self.oldVersionsValidUntil, str):
            self.oldVersionsValidUntil = str(self.oldVersionsValidUntil)

        if self.providedUntil is not None and not isinstance(self.providedUntil, str):
            self.providedUntil = str(self.providedUntil)

        super().__post_init__(**kwargs)


@dataclass
class LatestN(YAMLRoot):
    """
    Number of latest N outdated image versions, which will be valid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["LatestN"]
    class_class_curie: ClassVar[str] = "gx:LatestN"
    class_name: ClassVar[str] = "Latest_N"
    class_model_uri: ClassVar[URIRef] = GX.LatestN

    value: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


class InstantiationRequirement(GaiaXEntity):
    """
    A container class to gather all requirements for compute service offering instantiations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["InstantiationRequirement"]
    class_class_curie: ClassVar[str] = "gx:InstantiationRequirement"
    class_name: ClassVar[str] = "InstantiationRequirement"
    class_model_uri: ClassVar[URIRef] = GX.InstantiationRequirement


@dataclass
class Issuer(YAMLRoot):
    """
    An issuer of W3C Verifiable Credentials and Verifiable Presentations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Issuer"]
    class_class_curie: ClassVar[str] = "gx:Issuer"
    class_name: ClassVar[str] = "Issuer"
    class_model_uri: ClassVar[URIRef] = GX.Issuer

    gaiaxTermsAndConditions: Union[str, "GaiaXTermsAndConditions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.gaiaxTermsAndConditions):
            self.MissingRequiredField("gaiaxTermsAndConditions")
        if not isinstance(self.gaiaxTermsAndConditions, GaiaXTermsAndConditions):
            self.gaiaxTermsAndConditions = GaiaXTermsAndConditions(self.gaiaxTermsAndConditions)

        super().__post_init__(**kwargs)


class RegistrationNumber(YAMLRoot):
    """
    Country's registration number, which identifies one specific entity. Allowed entries are Local, VatID, lei code,
    EODI, and EUID.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["RegistrationNumber"]
    class_class_curie: ClassVar[str] = "gx:RegistrationNumber"
    class_name: ClassVar[str] = "RegistrationNumber"
    class_model_uri: ClassVar[URIRef] = GX.RegistrationNumber


@dataclass
class LocalRegistrationNumber(RegistrationNumber):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["LocalRegistrationNumber"]
    class_class_curie: ClassVar[str] = "gx:LocalRegistrationNumber"
    class_name: ClassVar[str] = "LocalRegistrationNumber"
    class_model_uri: ClassVar[URIRef] = GX.LocalRegistrationNumber

    local: Union[str, LocalRegistrationNumberLocal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.local):
            self.MissingRequiredField("local")
        if not isinstance(self.local, LocalRegistrationNumberLocal):
            self.local = LocalRegistrationNumberLocal(self.local)

        super().__post_init__(**kwargs)


@dataclass
class VatID(RegistrationNumber):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VatID"]
    class_class_curie: ClassVar[str] = "gx:VatID"
    class_name: ClassVar[str] = "VatID"
    class_model_uri: ClassVar[URIRef] = GX.VatID

    vatID: Union[str, VatIDVatID] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vatID):
            self.MissingRequiredField("vatID")
        if not isinstance(self.vatID, VatIDVatID):
            self.vatID = VatIDVatID(self.vatID)

        super().__post_init__(**kwargs)


@dataclass
class LeiCode(RegistrationNumber):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["LeiCode"]
    class_class_curie: ClassVar[str] = "gx:LeiCode"
    class_name: ClassVar[str] = "LeiCode"
    class_model_uri: ClassVar[URIRef] = GX.LeiCode

    leiCode: Union[str, LeiCodeLeiCode] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.leiCode):
            self.MissingRequiredField("leiCode")
        if not isinstance(self.leiCode, LeiCodeLeiCode):
            self.leiCode = LeiCodeLeiCode(self.leiCode)

        super().__post_init__(**kwargs)


@dataclass
class EORI(RegistrationNumber):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["EORI"]
    class_class_curie: ClassVar[str] = "gx:EORI"
    class_name: ClassVar[str] = "EORI"
    class_model_uri: ClassVar[URIRef] = GX.EORI

    eori: Union[str, EORIEori] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.eori):
            self.MissingRequiredField("eori")
        if not isinstance(self.eori, EORIEori):
            self.eori = EORIEori(self.eori)

        super().__post_init__(**kwargs)


@dataclass
class EUID(RegistrationNumber):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["EUID"]
    class_class_curie: ClassVar[str] = "gx:EUID"
    class_name: ClassVar[str] = "EUID"
    class_model_uri: ClassVar[URIRef] = GX.EUID

    euid: Union[str, EUIDEuid] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.euid):
            self.MissingRequiredField("euid")
        if not isinstance(self.euid, EUIDEuid):
            self.euid = EUIDEuid(self.euid)

        super().__post_init__(**kwargs)


@dataclass
class Memory(Device):
    """
    Details with respect to properties and capabilities of RAM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Memory"]
    class_class_curie: ClassVar[str] = "gx:Memory"
    class_name: ClassVar[str] = "Memory"
    class_model_uri: ClassVar[URIRef] = GX.Memory

    memorySize: Union[dict, "MemorySize"] = None
    memoryClass: Optional[Union[str, "MemoryClasses"]] = "other"
    memoryRank: Optional[Union[str, "MemoryRanks"]] = "other"
    eccEnabled: Optional[Union[bool, Bool]] = False
    hardwareEncryption: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.memorySize):
            self.MissingRequiredField("memorySize")
        if not isinstance(self.memorySize, MemorySize):
            self.memorySize = MemorySize(**as_dict(self.memorySize))

        if self.memoryClass is not None and not isinstance(self.memoryClass, MemoryClasses):
            self.memoryClass = MemoryClasses(self.memoryClass)

        if self.memoryRank is not None and not isinstance(self.memoryRank, MemoryRanks):
            self.memoryRank = MemoryRanks(self.memoryRank)

        if self.eccEnabled is not None and not isinstance(self.eccEnabled, Bool):
            self.eccEnabled = Bool(self.eccEnabled)

        if self.hardwareEncryption is not None and not isinstance(self.hardwareEncryption, Bool):
            self.hardwareEncryption = Bool(self.hardwareEncryption)

        super().__post_init__(**kwargs)


@dataclass
class Quantity(YAMLRoot):
    """
    Abstract parent class for all physical quantities, such as frequency, power or length.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = GX.Quantity

    value: float = None
    unit: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class Frequency(Quantity):
    """
    Definition of 'Frequency', according to http://qudt.org/quantitykind/FrequencyDefinition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantitykind/FrequencyDefinition"]
    class_class_curie: ClassVar[str] = "qudt:quantitykind/FrequencyDefinition"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = GX.Frequency

    value: float = None
    unit: str = None

@dataclass
class MemorySize(Quantity):
    """
    The number of bytes, that can be stored on a digital storage.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["MemorySize"]
    class_class_curie: ClassVar[str] = "gx:MemorySize"
    class_name: ClassVar[str] = "MemorySize"
    class_model_uri: ClassVar[URIRef] = GX.MemorySize

    value: float = None
    unit: str = None

@dataclass
class Power(Quantity):
    """
    Definition of 'Power', according to http://qudt.org/quantitykind/Power.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantitykind/Power"]
    class_class_curie: ClassVar[str] = "qudt:quantitykind/Power"
    class_name: ClassVar[str] = "Power"
    class_model_uri: ClassVar[URIRef] = GX.Power

    value: float = None
    unit: str = None

@dataclass
class DataRate(Quantity):
    """
    Definition of 'Data Rate', according to http://qudt.org/quantitykind/DataRate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantitykind/DataRate"]
    class_class_curie: ClassVar[str] = "qudt:quantitykind/DataRate"
    class_name: ClassVar[str] = "DataRate"
    class_model_uri: ClassVar[URIRef] = GX.DataRate

    value: float = None
    unit: str = None

@dataclass
class Time(Quantity):
    """
    Definition of 'Time', according to http://qudt.org/quantitykind/Time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["quantitykind/Time"]
    class_class_curie: ClassVar[str] = "qudt:quantitykind/Time"
    class_name: ClassVar[str] = "Time"
    class_model_uri: ClassVar[URIRef] = GX.Time

    value: float = None
    unit: str = None

@dataclass
class RetentionDuration(Time):
    """
    Sub-class of Time with units relevant for retention durations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["RetentionDuration"]
    class_class_curie: ClassVar[str] = "gx:RetentionDuration"
    class_name: ClassVar[str] = "RetentionDuration"
    class_model_uri: ClassVar[URIRef] = GX.RetentionDuration

    value: float = None
    unit: str = None

@dataclass
class FloatPercentage(YAMLRoot):
    """
    Definition of percentage, according to https://qudt.org/2.1/schema/qudt
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT_SCHEMA["floatPercentage"]
    class_class_curie: ClassVar[str] = "qudt_schema:floatPercentage"
    class_name: ClassVar[str] = "FloatPercentage"
    class_model_uri: ClassVar[URIRef] = GX.FloatPercentage

    value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


class Participant(GaiaXEntity):
    """
    An legal or natural person that is onboarded to Gaia-X and offers, consumes services or operates resources.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Participant"]
    class_class_curie: ClassVar[str] = "gx:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = GX.Participant


@dataclass
class LegalPerson(Participant):
    """
    A legal person, who is uniquely identified by its registration number.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["LegalPerson"]
    class_class_curie: ClassVar[str] = "gx:LegalPerson"
    class_name: ClassVar[str] = "LegalPerson"
    class_model_uri: ClassVar[URIRef] = GX.LegalPerson

    registrationNumber: Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]] = None
    legalAddress: Union[dict, Address] = None
    headquartersAddress: Union[dict, Address] = None
    parentOrganizationOf: Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]] = empty_list()
    subOrganisationOf: Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.registrationNumber):
            self.MissingRequiredField("registrationNumber")
        if not isinstance(self.registrationNumber, list):
            self.registrationNumber = [self.registrationNumber] if self.registrationNumber is not None else []
        self.registrationNumber = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.registrationNumber]

        if self._is_empty(self.legalAddress):
            self.MissingRequiredField("legalAddress")
        if not isinstance(self.legalAddress, Address):
            self.legalAddress = Address(**as_dict(self.legalAddress))

        if self._is_empty(self.headquartersAddress):
            self.MissingRequiredField("headquartersAddress")
        if not isinstance(self.headquartersAddress, Address):
            self.headquartersAddress = Address(**as_dict(self.headquartersAddress))

        if not isinstance(self.parentOrganizationOf, list):
            self.parentOrganizationOf = [self.parentOrganizationOf] if self.parentOrganizationOf is not None else []
        self.parentOrganizationOf = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.parentOrganizationOf]

        if not isinstance(self.subOrganisationOf, list):
            self.subOrganisationOf = [self.subOrganisationOf] if self.subOrganisationOf is not None else []
        self.subOrganisationOf = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.subOrganisationOf]

        super().__post_init__(**kwargs)


@dataclass
class Resource(GaiaXEntity):
    """
    Description of a good or object of the Gaia-X Ecosystem, and may be aggregated in a Service Offering or exist
    independently of it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Resource"]
    class_class_curie: ClassVar[str] = "gx:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = GX.Resource

    aggregationOfResources: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.aggregationOfResources, list):
            self.aggregationOfResources = [self.aggregationOfResources] if self.aggregationOfResources is not None else []
        self.aggregationOfResources = [v if isinstance(v, str) else str(v) for v in self.aggregationOfResources]

        super().__post_init__(**kwargs)


@dataclass
class VirtualResource(Resource):
    """
    It represents static data in any form and necessary information such as dataset, configuration file, license,
    keypair, an AI model, neural network weights, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VirtualResource"]
    class_class_curie: ClassVar[str] = "gx:VirtualResource"
    class_name: ClassVar[str] = "VirtualResource"
    class_model_uri: ClassVar[URIRef] = GX.VirtualResource

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.copyrightOwnedBy):
            self.MissingRequiredField("copyrightOwnedBy")
        if not isinstance(self.copyrightOwnedBy, list):
            self.copyrightOwnedBy = [self.copyrightOwnedBy] if self.copyrightOwnedBy is not None else []
        self.copyrightOwnedBy = [v if isinstance(v, str) else str(v) for v in self.copyrightOwnedBy]

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, list):
            self.license = [self.license] if self.license is not None else []
        self.license = [v if isinstance(v, str) else str(v) for v in self.license]

        if self._is_empty(self.resourcePolicy):
            self.MissingRequiredField("resourcePolicy")
        if not isinstance(self.resourcePolicy, list):
            self.resourcePolicy = [self.resourcePolicy] if self.resourcePolicy is not None else []
        self.resourcePolicy = [v if isinstance(v, str) else str(v) for v in self.resourcePolicy]

        super().__post_init__(**kwargs)


@dataclass
class PhysicalResource(Resource):
    """
    A Physical resource is, but not limited to, a datacenter, a bare-metal service, a warehouse, a plant. Those are
    entities that have a weight and position in physical space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["PhysicalResource"]
    class_class_curie: ClassVar[str] = "gx:PhysicalResource"
    class_name: ClassVar[str] = "PhysicalResource"
    class_model_uri: ClassVar[URIRef] = GX.PhysicalResource

    maintainedBy: Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]] = None
    location: Union[Union[dict, Address], List[Union[dict, Address]]] = None
    ownedBy: Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]] = empty_list()
    manufacturedBy: Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.maintainedBy):
            self.MissingRequiredField("maintainedBy")
        if not isinstance(self.maintainedBy, list):
            self.maintainedBy = [self.maintainedBy] if self.maintainedBy is not None else []
        self.maintainedBy = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.maintainedBy]

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        #self._normalize_inlined_as_dict(slot_name="location", slot_type=Address, key_name="countryCode", keyed=False)

        if not isinstance(self.ownedBy, list):
            self.ownedBy = [self.ownedBy] if self.ownedBy is not None else []
        self.ownedBy = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.ownedBy]

        if not isinstance(self.manufacturedBy, list):
            self.manufacturedBy = [self.manufacturedBy] if self.manufacturedBy is not None else []
        self.manufacturedBy = [v if isinstance(v, LegalPersonRegistrationNumber) else LegalPersonRegistrationNumber(v) for v in self.manufacturedBy]

        super().__post_init__(**kwargs)


@dataclass
class SoftwareResource(VirtualResource):
    """
    A Gaia-X Virtual Resource describing an executable program.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["SoftwareResource"]
    class_class_curie: ClassVar[str] = "gx:SoftwareResource"
    class_name: ClassVar[str] = "SoftwareResource"
    class_model_uri: ClassVar[URIRef] = GX.SoftwareResource

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    checksum: Optional[Union[dict, CheckSum]] = None
    signature: Optional[Union[dict, Signature]] = None
    version: Optional[str] = None
    patchLevel: Optional[str] = None
    buildDate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.checksum is not None and not isinstance(self.checksum, CheckSum):
            self.checksum = CheckSum(**as_dict(self.checksum))

        if self.signature is not None and not isinstance(self.signature, Signature):
            self.signature = Signature(**as_dict(self.signature))

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.patchLevel is not None and not isinstance(self.patchLevel, str):
            self.patchLevel = str(self.patchLevel)

        if self.buildDate is not None and not isinstance(self.buildDate, XSDDateTime):
            self.buildDate = XSDDateTime(self.buildDate)

        super().__post_init__(**kwargs)


@dataclass
class CodeArtifact(SoftwareResource):
    """
    A piece of software that can be executed by a Compute service. It is a subclass of SoftwareResource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["CodeArtifact"]
    class_class_curie: ClassVar[str] = "gx:CodeArtifact"
    class_name: ClassVar[str] = "CodeArtifact"
    class_model_uri: ClassVar[URIRef] = GX.CodeArtifact

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None

@dataclass
class Image(CodeArtifact):
    """
    A software piece that can be executed by a virtual or bare metal Compute services. It is a subclass of
    OperatingSystem and CodeArtifact.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Image"]
    class_class_curie: ClassVar[str] = "gx:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = GX.Image

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    fileSize: Optional[Union[dict, MemorySize]] = None
    operatingSystem: Optional[Union[dict, "OperatingSystem"]] = None
    cpuReq: Optional[Union[dict, CPU]] = None
    gpuReq: Optional[Union[dict, GPU]] = None
    ramReq: Optional[Union[dict, Memory]] = None
    videoRamSize: Optional[Union[dict, MemorySize]] = None
    rootDiskReq: Optional[Union[dict, Disk]] = None
    encryption: Optional[Union[dict, Encryption]] = None
    checkSum: Optional[Union[dict, CheckSum]] = None
    secureBoot: Optional[Union[bool, Bool]] = False
    vPMU: Optional[Union[bool, Bool]] = False
    multiQueues: Optional[Union[bool, Bool]] = False
    updateStrategy: Optional[Union[dict, UpdateStrategy]] = None
    licenseIncluded: Optional[Union[bool, Bool]] = False
    maintenance: Optional[Union[dict, MaintenanceSubscription]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fileSize is not None and not isinstance(self.fileSize, MemorySize):
            self.fileSize = MemorySize(**as_dict(self.fileSize))

        if self.operatingSystem is not None and not isinstance(self.operatingSystem, OperatingSystem):
            self.operatingSystem = OperatingSystem(**as_dict(self.operatingSystem))

        if self.cpuReq is not None and not isinstance(self.cpuReq, CPU):
            self.cpuReq = CPU(**as_dict(self.cpuReq))

        if self.gpuReq is not None and not isinstance(self.gpuReq, GPU):
            self.gpuReq = GPU(**as_dict(self.gpuReq))

        if self.ramReq is not None and not isinstance(self.ramReq, Memory):
            self.ramReq = Memory(**as_dict(self.ramReq))

        if self.videoRamSize is not None and not isinstance(self.videoRamSize, MemorySize):
            self.videoRamSize = MemorySize(**as_dict(self.videoRamSize))

        if self.rootDiskReq is not None and not isinstance(self.rootDiskReq, Disk):
            self.rootDiskReq = Disk(**as_dict(self.rootDiskReq))

        if self.encryption is not None and not isinstance(self.encryption, Encryption):
            self.encryption = Encryption(**as_dict(self.encryption))

        if self.checkSum is not None and not isinstance(self.checkSum, CheckSum):
            self.checkSum = CheckSum(**as_dict(self.checkSum))

        if self.secureBoot is not None and not isinstance(self.secureBoot, Bool):
            self.secureBoot = Bool(self.secureBoot)

        if self.vPMU is not None and not isinstance(self.vPMU, Bool):
            self.vPMU = Bool(self.vPMU)

        if self.multiQueues is not None and not isinstance(self.multiQueues, Bool):
            self.multiQueues = Bool(self.multiQueues)

        if self.updateStrategy is not None and not isinstance(self.updateStrategy, UpdateStrategy):
            self.updateStrategy = UpdateStrategy(**as_dict(self.updateStrategy))

        if self.licenseIncluded is not None and not isinstance(self.licenseIncluded, Bool):
            self.licenseIncluded = Bool(self.licenseIncluded)

        if self.maintenance is not None and not isinstance(self.maintenance, MaintenanceSubscription):
            self.maintenance = MaintenanceSubscription(**as_dict(self.maintenance))

        super().__post_init__(**kwargs)


@dataclass
class PXEImage(Image):
    """
    PXE image for physical machines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["PXEImage"]
    class_class_curie: ClassVar[str] = "gx:PXEImage"
    class_name: ClassVar[str] = "PXE_Image"
    class_model_uri: ClassVar[URIRef] = GX.PXEImage

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    pxeImageDiskFormat: Optional[Union[str, "PXEDiskType"]] = "ISO"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.pxeImageDiskFormat is not None and not isinstance(self.pxeImageDiskFormat, PXEDiskType):
            self.pxeImageDiskFormat = PXEDiskType(self.pxeImageDiskFormat)

        super().__post_init__(**kwargs)


@dataclass
class OperatingSystem(SoftwareResource):
    """
    A special Gaia-X Software Resource describing an operating system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["OperatingSystem"]
    class_class_curie: ClassVar[str] = "gx:OperatingSystem"
    class_name: ClassVar[str] = "OperatingSystem"
    class_model_uri: ClassVar[URIRef] = GX.OperatingSystem

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    osDistribution: Union[str, "OSDistribution"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.osDistribution):
            self.MissingRequiredField("osDistribution")
        if not isinstance(self.osDistribution, OSDistribution):
            self.osDistribution = OSDistribution(self.osDistribution)

        super().__post_init__(**kwargs)


@dataclass
class Hypervisor(SoftwareResource):
    """
    A special Gaia-X Software Resource describing a hypervisor to provided virtual machines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Hypervisor"]
    class_class_curie: ClassVar[str] = "gx:Hypervisor"
    class_name: ClassVar[str] = "Hypervisor"
    class_model_uri: ClassVar[URIRef] = GX.Hypervisor

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    hypervisorType: Union[str, "HypervisorType"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hypervisorType):
            self.MissingRequiredField("hypervisorType")
        if not isinstance(self.hypervisorType, HypervisorType):
            self.hypervisorType = HypervisorType(self.hypervisorType)

        super().__post_init__(**kwargs)


@dataclass
class ServiceOffering(GaiaXEntity):
    """
    A digital service available for order.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ServiceOffering"
    class_name: ClassVar[str] = "ServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    dependsOn: Optional[Union[str, List[str]]] = empty_list()
    aggregationOfResources: Optional[Union[str, List[str]]] = empty_list()
    dataProtectionRegime: Optional[Union[Union[str, "PersonalDataProtectionRegime"], List[Union[str, "PersonalDataProtectionRegime"]]]] = empty_list()
    keyword: Optional[Union[str, List[str]]] = empty_list()
    provisionType: Optional[Union[str, "ProvisionTypes"]] = None
    endpoint: Optional[Union[dict, Endpoint]] = None
    hostedOn: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.providedBy):
            self.MissingRequiredField("providedBy")
        if not isinstance(self.providedBy, LegalPersonRegistrationNumber):
            self.providedBy = LegalPersonRegistrationNumber(self.providedBy)

        if self._is_empty(self.serviceOfferingTermsAndConditions):
            self.MissingRequiredField("serviceOfferingTermsAndConditions")
        #self._normalize_inlined_as_dict(slot_name="serviceOfferingTermsAndConditions", slot_type=TermsAndConditions, key_name="url", keyed=False)

        if self._is_empty(self.servicePolicy):
            self.MissingRequiredField("servicePolicy")
        if not isinstance(self.servicePolicy, list):
            self.servicePolicy = [self.servicePolicy] if self.servicePolicy is not None else []
        self.servicePolicy = [v if isinstance(v, str) else str(v) for v in self.servicePolicy]

        if self._is_empty(self.dataAccountExport):
            self.MissingRequiredField("dataAccountExport")
        #self._normalize_inlined_as_dict(slot_name="dataAccountExport", slot_type=DataAccountExport, key_name="requestType", keyed=False)

        if not isinstance(self.dependsOn, list):
            self.dependsOn = [self.dependsOn] if self.dependsOn is not None else []
        self.dependsOn = [v if isinstance(v, str) else str(v) for v in self.dependsOn]

        if not isinstance(self.aggregationOfResources, list):
            self.aggregationOfResources = [self.aggregationOfResources] if self.aggregationOfResources is not None else []
        self.aggregationOfResources = [v if isinstance(v, str) else str(v) for v in self.aggregationOfResources]

        if not isinstance(self.dataProtectionRegime, list):
            self.dataProtectionRegime = [self.dataProtectionRegime] if self.dataProtectionRegime is not None else []
        self.dataProtectionRegime = [v if isinstance(v, PersonalDataProtectionRegime) else PersonalDataProtectionRegime(v) for v in self.dataProtectionRegime]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        if self.provisionType is not None and not isinstance(self.provisionType, ProvisionTypes):
            self.provisionType = ProvisionTypes(self.provisionType)

        if self.endpoint is not None and not isinstance(self.endpoint, Endpoint):
            self.endpoint = Endpoint(**as_dict(self.endpoint))

        if not isinstance(self.hostedOn, list):
            self.hostedOn = [self.hostedOn] if self.hostedOn is not None else []
        self.hostedOn = [v if isinstance(v, str) else str(v) for v in self.hostedOn]

        super().__post_init__(**kwargs)


@dataclass
class InfrastructureServiceOffering(ServiceOffering):
    """
    A digital service available for order and offering computational, storage and/pr network capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["InfrastructureServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:InfrastructureServiceOffering"
    class_name: ClassVar[str] = "InfrastructureServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.InfrastructureServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

@dataclass
class ComputeServiceOffering(InfrastructureServiceOffering):
    """
    A digital service available for order and offering computational capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ComputeServiceOffering"
    class_name: ClassVar[str] = "ComputeServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ComputeServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    tenantSeparation: Optional[Union[str, "TenantSeparation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.tenantSeparation is not None and not isinstance(self.tenantSeparation, TenantSeparation):
            self.tenantSeparation = TenantSeparation(self.tenantSeparation)

        super().__post_init__(**kwargs)


@dataclass
class VirtualMachineServiceOffering(ComputeServiceOffering):
    """
    A digital service available for order and offering computational capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VirtualMachineServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:VirtualMachineServiceOffering"
    class_name: ClassVar[str] = "VirtualMachineServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.VirtualMachineServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    codeArtifact: Union[Union[dict, "VMImage"], List[Union[dict, "VMImage"]]] = None
    instantiationReq: Union[Union[dict, "ServerFlavor"], List[Union[dict, "ServerFlavor"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeArtifact):
            self.MissingRequiredField("codeArtifact")
        #self._normalize_inlined_as_dict(slot_name="codeArtifact", slot_type=VMImage, key_name="copyrightOwnedBy", keyed=False)

        if self._is_empty(self.instantiationReq):
            self.MissingRequiredField("instantiationReq")
        #self._normalize_inlined_as_dict(slot_name="instantiationReq", slot_type=ServerFlavor, key_name="cpu", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ContainerServiceOffering(ComputeServiceOffering):
    """
    A digital service available for order and providing containers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ContainerServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ContainerServiceOffering"
    class_name: ClassVar[str] = "ContainerServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ContainerServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    codeArtifact: Union[Union[dict, "ContainerImage"], List[Union[dict, "ContainerImage"]]] = None
    instantiationReq: Union[Union[dict, "ContainerResourceLimits"], List[Union[dict, "ContainerResourceLimits"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeArtifact):
            self.MissingRequiredField("codeArtifact")
        #self._normalize_inlined_as_dict(slot_name="codeArtifact", slot_type=ContainerImage, key_name="copyrightOwnedBy", keyed=False)

        if self._is_empty(self.instantiationReq):
            self.MissingRequiredField("instantiationReq")
        #self._normalize_inlined_as_dict(slot_name="instantiationReq", slot_type=ContainerResourceLimits, key_name="confidential", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class BareMetalServiceOffering(ComputeServiceOffering):
    """
    A digital service available for order and offering bare metal computational capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BareMetalServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:BareMetalServiceOffering"
    class_name: ClassVar[str] = "BareMetalServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.BareMetalServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, "TermsAndConditions"], List[Union[dict, "TermsAndConditions"]]] = None
    dataAccountExport: Union[Union[dict, "DataAccountExport"], List[Union[dict, "DataAccountExport"]]] = None
    codeArtifact: Union[Union[dict, PXEImage], List[Union[dict, PXEImage]]] = None
    instantiationReq: Union[Union[dict, "ServerFlavor"], List[Union[dict, "ServerFlavor"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.codeArtifact):
            self.MissingRequiredField("codeArtifact")
        #self._normalize_inlined_as_dict(slot_name="codeArtifact", slot_type=PXEImage, key_name="copyrightOwnedBy", keyed=False)

        if self._is_empty(self.instantiationReq):
            self.MissingRequiredField("instantiationReq")
        #self._normalize_inlined_as_dict(slot_name="instantiationReq", slot_type=ServerFlavor, key_name="cpu", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class TermsAndConditions(YAMLRoot):
    """
    Terms and Conditions applying to a service offering.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["TermsAndConditions"]
    class_class_curie: ClassVar[str] = "gx:TermsAndConditions"
    class_name: ClassVar[str] = "TermsAndConditions"
    class_model_uri: ClassVar[URIRef] = GX.TermsAndConditions

    url: Union[str, URI] = None
    hash: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self._is_empty(self.hash):
            self.MissingRequiredField("hash")
        if not isinstance(self.hash, str):
            self.hash = str(self.hash)

        super().__post_init__(**kwargs)


@dataclass
class DataAccountExport(YAMLRoot):
    """
    List of methods to export data from your account out of the service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["DataAccountExport"]
    class_class_curie: ClassVar[str] = "gx:DataAccountExport"
    class_name: ClassVar[str] = "DataAccountExport"
    class_model_uri: ClassVar[URIRef] = GX.DataAccountExport

    requestType: Union[str, "RequestTypes"] = None
    accessType: Union[str, "AccessTypes"] = None
    formatType: Union[str, "MIMETypes"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.requestType):
            self.MissingRequiredField("requestType")
        if not isinstance(self.requestType, RequestTypes):
            self.requestType = RequestTypes(self.requestType)

        if self._is_empty(self.accessType):
            self.MissingRequiredField("accessType")
        if not isinstance(self.accessType, AccessTypes):
            self.accessType = AccessTypes(self.accessType)

        if self._is_empty(self.formatType):
            self.MissingRequiredField("formatType")
        if not isinstance(self.formatType, MIMETypes):
            self.formatType = MIMETypes(self.formatType)

        super().__post_init__(**kwargs)


@dataclass
class StandardConformity(YAMLRoot):
    """
    Details about standard applied to Gaia-X entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["StandardConformity"]
    class_class_curie: ClassVar[str] = "gx:StandardConformity"
    class_name: ClassVar[str] = "StandardConformity"
    class_model_uri: ClassVar[URIRef] = GX.StandardConformity

    title: str = None
    standardReference: Union[str, URI] = None
    publisher: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.standardReference):
            self.MissingRequiredField("standardReference")
        if not isinstance(self.standardReference, URI):
            self.standardReference = URI(self.standardReference)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        super().__post_init__(**kwargs)


@dataclass
class DataResource(VirtualResource):
    """
    A dataset exposed through a service instance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["DataResource"]
    class_class_curie: ClassVar[str] = "gx:DataResource"
    class_name: ClassVar[str] = "DataResource"
    class_model_uri: ClassVar[URIRef] = GX.DataResource

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    producedBy: Union[str, LegalPersonRegistrationNumber] = None
    exposedThrough: Union[Union[dict, "DataExchangeComponent"], List[Union[dict, "DataExchangeComponent"]]] = None
    containsPII: Union[bool, Bool] = None
    obsoleteDateTime: Optional[Union[str, XSDDateTime]] = None
    expirationDateTime: Optional[Union[str, XSDDateTime]] = None
    dataController: Optional[Union[Union[dict, Participant], List[Union[dict, Participant]]]] = empty_list()
    consent: Optional[Union[Union[dict, "Consent"], List[Union[dict, "Consent"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.producedBy):
            self.MissingRequiredField("producedBy")
        if not isinstance(self.producedBy, LegalPersonRegistrationNumber):
            self.producedBy = LegalPersonRegistrationNumber(self.producedBy)

        if self._is_empty(self.exposedThrough):
            self.MissingRequiredField("exposedThrough")
        if not isinstance(self.exposedThrough, list):
            self.exposedThrough = [self.exposedThrough] if self.exposedThrough is not None else []
        self.exposedThrough = [v if isinstance(v, DataExchangeComponent) else DataExchangeComponent(**as_dict(v)) for v in self.exposedThrough]

        if self._is_empty(self.containsPII):
            self.MissingRequiredField("containsPII")
        if not isinstance(self.containsPII, Bool):
            self.containsPII = Bool(self.containsPII)

        if self.obsoleteDateTime is not None and not isinstance(self.obsoleteDateTime, XSDDateTime):
            self.obsoleteDateTime = XSDDateTime(self.obsoleteDateTime)

        if self.expirationDateTime is not None and not isinstance(self.expirationDateTime, XSDDateTime):
            self.expirationDateTime = XSDDateTime(self.expirationDateTime)

        if not isinstance(self.dataController, list):
            self.dataController = [self.dataController] if self.dataController is not None else []
        self.dataController = [v if isinstance(v, Participant) else Participant(**as_dict(v)) for v in self.dataController]

        #self._normalize_inlined_as_dict(slot_name="consent", slot_type=Consent, key_name="legalBasis", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Consent(YAMLRoot):
    """
    Information on the legitimate processing of information related to PII.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Consent"]
    class_class_curie: ClassVar[str] = "gx:Consent"
    class_name: ClassVar[str] = "Consent"
    class_model_uri: ClassVar[URIRef] = GX.Consent

    legalBasis: str = None
    dataProtectionContactPoint: Union[str, List[str]] = None
    purpose: Union[str, List[str]] = None
    consentWithdrawalContactPoint: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.legalBasis):
            self.MissingRequiredField("legalBasis")
        if not isinstance(self.legalBasis, str):
            self.legalBasis = str(self.legalBasis)

        if self._is_empty(self.dataProtectionContactPoint):
            self.MissingRequiredField("dataProtectionContactPoint")
        if not isinstance(self.dataProtectionContactPoint, list):
            self.dataProtectionContactPoint = [self.dataProtectionContactPoint] if self.dataProtectionContactPoint is not None else []
        self.dataProtectionContactPoint = [v if isinstance(v, str) else str(v) for v in self.dataProtectionContactPoint]

        if self._is_empty(self.purpose):
            self.MissingRequiredField("purpose")
        if not isinstance(self.purpose, list):
            self.purpose = [self.purpose] if self.purpose is not None else []
        self.purpose = [v if isinstance(v, str) else str(v) for v in self.purpose]

        if self._is_empty(self.consentWithdrawalContactPoint):
            self.MissingRequiredField("consentWithdrawalContactPoint")
        if not isinstance(self.consentWithdrawalContactPoint, list):
            self.consentWithdrawalContactPoint = [self.consentWithdrawalContactPoint] if self.consentWithdrawalContactPoint is not None else []
        self.consentWithdrawalContactPoint = [v if isinstance(v, str) else str(v) for v in self.consentWithdrawalContactPoint]

        super().__post_init__(**kwargs)


class DataExchangeComponent(YAMLRoot):
    """
    A service/resource used to make a data resource available.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["DataExchangeComponent"]
    class_class_curie: ClassVar[str] = "gx:DataExchangeComponent"
    class_name: ClassVar[str] = "DataExchangeComponent"
    class_model_uri: ClassVar[URIRef] = GX.DataExchangeComponent


class AvailabilityZone(Resource):
    """
    An availability zone is an aggregation of resources - physical and abstract - in a non-redundant setup often
    associated with a single datacenter room
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["AvailabilityZone"]
    class_class_curie: ClassVar[str] = "gx:AvailabilityZone"
    class_name: ClassVar[str] = "AvailabilityZone"
    class_model_uri: ClassVar[URIRef] = GX.AvailabilityZone


@dataclass
class Datacenter(PhysicalResource):
    """
    A datacenter is an aggregation of availability zones
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Datacenter"]
    class_class_curie: ClassVar[str] = "gx:Datacenter"
    class_name: ClassVar[str] = "Datacenter"
    class_model_uri: ClassVar[URIRef] = GX.Datacenter

    maintainedBy: Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]] = None
    location: Union[Union[dict, Address], List[Union[dict, Address]]] = None
    aggregationOfResources: Union[Union[dict, AvailabilityZone], List[Union[dict, AvailabilityZone]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.aggregationOfResources):
            self.MissingRequiredField("aggregationOfResources")
        if not isinstance(self.aggregationOfResources, list):
            self.aggregationOfResources = [self.aggregationOfResources] if self.aggregationOfResources is not None else []
        self.aggregationOfResources = [v if isinstance(v, AvailabilityZone) else AvailabilityZone(**as_dict(v)) for v in self.aggregationOfResources]

        super().__post_init__(**kwargs)


@dataclass
class Region(Resource):
    """
    A region is an aggregation of datacenters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Region"]
    class_class_curie: ClassVar[str] = "gx:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = GX.Region

    aggregationOfResources: Union[Union[dict, Datacenter], List[Union[dict, Datacenter]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.aggregationOfResources):
            self.MissingRequiredField("aggregationOfResources")
        #self._normalize_inlined_as_dict(slot_name="aggregationOfResources", slot_type=Datacenter, key_name="maintainedBy", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ContainerImage(Image):
    """
    Image available for containers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ContainerImage"]
    class_class_curie: ClassVar[str] = "gx:ContainerImage"
    class_name: ClassVar[str] = "ContainerImage"
    class_model_uri: ClassVar[URIRef] = GX.ContainerImage

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    baseContainerImage: Union[dict, "BaseContainerImage"] = None
    containerFormat: Union[str, "ContainerFormat"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.baseContainerImage):
            self.MissingRequiredField("baseContainerImage")
        if not isinstance(self.baseContainerImage, BaseContainerImage):
            self.baseContainerImage = BaseContainerImage(**as_dict(self.baseContainerImage))

        if self._is_empty(self.containerFormat):
            self.MissingRequiredField("containerFormat")
        if not isinstance(self.containerFormat, ContainerFormat):
            self.containerFormat = ContainerFormat(self.containerFormat)

        super().__post_init__(**kwargs)


@dataclass
class BaseContainerImage(YAMLRoot):
    """
    A set of tags for an image and a repository link
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BaseContainerImage"]
    class_class_curie: ClassVar[str] = "gx:BaseContainerImage"
    class_name: ClassVar[str] = "BaseContainerImage"
    class_model_uri: ClassVar[URIRef] = GX.BaseContainerImage

    containerImageLink: Union[str, URI] = None
    containerImageTag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.containerImageLink):
            self.MissingRequiredField("containerImageLink")
        if not isinstance(self.containerImageLink, URI):
            self.containerImageLink = URI(self.containerImageLink)

        if not isinstance(self.containerImageTag, list):
            self.containerImageTag = [self.containerImageTag] if self.containerImageTag is not None else []
        self.containerImageTag = [v if isinstance(v, str) else str(v) for v in self.containerImageTag]

        super().__post_init__(**kwargs)


@dataclass
class ContainerResourceLimits(InstantiationRequirement):
    """
    InstantiationRequirements for containers (available resources and associated limits).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ContainerResourceLimits"]
    class_class_curie: ClassVar[str] = "gx:ContainerResourceLimits"
    class_name: ClassVar[str] = "ContainerResourceLimits"
    class_model_uri: ClassVar[URIRef] = GX.ContainerResourceLimits

    confidential: Union[bool, Bool] = None
    cpuRequirements: Optional[Union[dict, CPU]] = None
    numberOfCoresLimit: Optional[int] = None
    memoryRequirements: Optional[Union[dict, Memory]] = None
    memoryLimit: Optional[Union[dict, MemorySize]] = None
    gpuRequirements: Optional[Union[dict, GPU]] = None
    gpuLimit: Optional[int] = None
    confidentialComputingTechnology: Optional[Union[dict, "ConfidentialComputing"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidential):
            self.MissingRequiredField("confidential")
        if not isinstance(self.confidential, Bool):
            self.confidential = Bool(self.confidential)

        if self.cpuRequirements is not None and not isinstance(self.cpuRequirements, CPU):
            self.cpuRequirements = CPU(**as_dict(self.cpuRequirements))

        if self.numberOfCoresLimit is not None and not isinstance(self.numberOfCoresLimit, int):
            self.numberOfCoresLimit = int(self.numberOfCoresLimit)

        if self.memoryRequirements is not None and not isinstance(self.memoryRequirements, Memory):
            self.memoryRequirements = Memory(**as_dict(self.memoryRequirements))

        if self.memoryLimit is not None and not isinstance(self.memoryLimit, MemorySize):
            self.memoryLimit = MemorySize(**as_dict(self.memoryLimit))

        if self.gpuRequirements is not None and not isinstance(self.gpuRequirements, GPU):
            self.gpuRequirements = GPU(**as_dict(self.gpuRequirements))

        if self.gpuLimit is not None and not isinstance(self.gpuLimit, int):
            self.gpuLimit = int(self.gpuLimit)

        if self.confidentialComputingTechnology is not None and not isinstance(self.confidentialComputingTechnology, ConfidentialComputing):
            self.confidentialComputingTechnology = ConfidentialComputing(**as_dict(self.confidentialComputingTechnology))

        super().__post_init__(**kwargs)


@dataclass
class DataProtectionPolicy(YAMLRoot):
    """
    A container class for various data protection features, such as backup or replication
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["DataProtectionPolicy"]
    class_class_curie: ClassVar[str] = "gx:DataProtectionPolicy"
    class_name: ClassVar[str] = "DataProtectionPolicy"
    class_model_uri: ClassVar[URIRef] = GX.DataProtectionPolicy

    protectionFrequency: Union[str, "ProtectionFrequency"] = None
    protectionRetention: Union[dict, RetentionDuration] = None
    protectionMethod: Optional[Union[str, "ProtectionMethod"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protectionFrequency):
            self.MissingRequiredField("protectionFrequency")
        if not isinstance(self.protectionFrequency, ProtectionFrequency):
            self.protectionFrequency = ProtectionFrequency(self.protectionFrequency)

        if self._is_empty(self.protectionRetention):
            self.MissingRequiredField("protectionRetention")
        if not isinstance(self.protectionRetention, RetentionDuration):
            self.protectionRetention = RetentionDuration(**as_dict(self.protectionRetention))

        if self.protectionMethod is not None and not isinstance(self.protectionMethod, ProtectionMethod):
            self.protectionMethod = ProtectionMethod(self.protectionMethod)

        super().__post_init__(**kwargs)


@dataclass
class BackupPolicy(DataProtectionPolicy):
    """
    Describe data protection features based on Backup for storage services
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BackupPolicy"]
    class_class_curie: ClassVar[str] = "gx:BackupPolicy"
    class_name: ClassVar[str] = "BackupPolicy"
    class_model_uri: ClassVar[URIRef] = GX.BackupPolicy

    protectionFrequency: Union[str, "ProtectionFrequency"] = None
    protectionRetention: Union[dict, RetentionDuration] = None
    backupLocation: Union[Union[dict, Resource], List[Union[dict, Resource]]] = None
    backupReplication: Optional[Union[Union[dict, "ReplicationPolicy"], List[Union[dict, "ReplicationPolicy"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.backupLocation):
            self.MissingRequiredField("backupLocation")
        if not isinstance(self.backupLocation, list):
            self.backupLocation = [self.backupLocation] if self.backupLocation is not None else []
        self.backupLocation = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.backupLocation]

        #self._normalize_inlined_as_dict(slot_name="backupReplication", slot_type=ReplicationPolicy, key_name="protectionFrequency", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class SnapshotPolicy(DataProtectionPolicy):
    """
    Describe data protection features based on Snapshot for storage services
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["SnapshotPolicy"]
    class_class_curie: ClassVar[str] = "gx:SnapshotPolicy"
    class_name: ClassVar[str] = "SnapshotPolicy"
    class_model_uri: ClassVar[URIRef] = GX.SnapshotPolicy

    protectionFrequency: Union[str, "ProtectionFrequency"] = None
    protectionRetention: Union[dict, RetentionDuration] = None
    snapshotReplication: Optional[Union[Union[dict, "ReplicationPolicy"], List[Union[dict, "ReplicationPolicy"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        #self._normalize_inlined_as_dictself._normalize_inlined_as_dict(slot_name="snapshotReplication", slot_type=ReplicationPolicy, key_name="protectionFrequency", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ReplicationPolicy(DataProtectionPolicy):
    """
    Describe data protection features based on Replication for storage services
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ReplicationPolicy"]
    class_class_curie: ClassVar[str] = "gx:ReplicationPolicy"
    class_name: ClassVar[str] = "ReplicationPolicy"
    class_model_uri: ClassVar[URIRef] = GX.ReplicationPolicy

    protectionFrequency: Union[str, "ProtectionFrequency"] = None
    protectionRetention: Union[dict, RetentionDuration] = None
    synchronousReplication: Optional[Union[bool, Bool]] = None
    consistencyType: Optional[Union[str, "ConsistencyType"]] = None
    replicaNumber: Optional[Union[int, List[int]]] = empty_list()
    geoReplication: Optional[Union[Union[str, "GeoReplicationScope"], List[Union[str, "GeoReplicationScope"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.synchronousReplication is not None and not isinstance(self.synchronousReplication, Bool):
            self.synchronousReplication = Bool(self.synchronousReplication)

        if self.consistencyType is not None and not isinstance(self.consistencyType, ConsistencyType):
            self.consistencyType = ConsistencyType(self.consistencyType)

        if not isinstance(self.replicaNumber, list):
            self.replicaNumber = [self.replicaNumber] if self.replicaNumber is not None else []
        self.replicaNumber = [v if isinstance(v, int) else int(v) for v in self.replicaNumber]

        if not isinstance(self.geoReplication, list):
            self.geoReplication = [self.geoReplication] if self.geoReplication is not None else []
        self.geoReplication = [v if isinstance(v, GeoReplicationScope) else GeoReplicationScope(v) for v in self.geoReplication]

        super().__post_init__(**kwargs)


@dataclass
class QoSMetric(YAMLRoot):
    """
    A quantity representing a performance level that is guaranteed to be met at least X% of the time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["QoSMetric"]
    class_class_curie: ClassVar[str] = "gx:QoSMetric"
    class_name: ClassVar[str] = "QoSMetric"
    class_model_uri: ClassVar[URIRef] = GX.QoSMetric

    metric: Union[dict, Quantity] = None
    guaranteed: Optional[Union[dict, FloatPercentage]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, Quantity):
            self.metric = Quantity(**as_dict(self.metric))

        if self.guaranteed is not None and not isinstance(self.guaranteed, FloatPercentage):
            self.guaranteed = FloatPercentage(**as_dict(self.guaranteed))

        super().__post_init__(**kwargs)


@dataclass
class BandWidth(QoSMetric):
    """
    Contractual bandwidth defined in the service level agreement (SLA).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BandWidth"]
    class_class_curie: ClassVar[str] = "gx:BandWidth"
    class_name: ClassVar[str] = "BandWidth"
    class_model_uri: ClassVar[URIRef] = GX.BandWidth

    metric: Union[dict, DataRate] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, DataRate):
            self.metric = DataRate(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class RoundTripTime(QoSMetric):
    """
    Contractual roundTrip time defined in the SLA. If not specified, then best effort is assumed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["RoundTripTime"]
    class_class_curie: ClassVar[str] = "gx:RoundTripTime"
    class_name: ClassVar[str] = "RoundTripTime"
    class_model_uri: ClassVar[URIRef] = GX.RoundTripTime

    metric: Union[dict, Time] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, Time):
            self.metric = Time(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class Availability(QoSMetric):
    """
    Contractual availability of connection defined in the SLA agreement. Availability is measured in the pseudo-unit
    "percent".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Availability"]
    class_class_curie: ClassVar[str] = "gx:Availability"
    class_name: ClassVar[str] = "Availability"
    class_model_uri: ClassVar[URIRef] = GX.Availability

    metric: Union[dict, Time] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, Time):
            self.metric = Time(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class PacketLoss(QoSMetric):
    """
    Contractual packet loss of connection defined in the SLA agreement. If not specified, then best effort is assumed.
    packetLoss measured in the pseudo-unit "percent"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["PacketLoss"]
    class_class_curie: ClassVar[str] = "gx:PacketLoss"
    class_name: ClassVar[str] = "PacketLoss"
    class_model_uri: ClassVar[URIRef] = GX.PacketLoss

    metric: Union[dict, FloatPercentage] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, FloatPercentage):
            self.metric = FloatPercentage(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class Jitter(QoSMetric):
    """
    Contractual jitter defined in the SLA. If not specified, then best effort is assumed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Jitter"]
    class_class_curie: ClassVar[str] = "gx:Jitter"
    class_name: ClassVar[str] = "Jitter"
    class_model_uri: ClassVar[URIRef] = GX.Jitter

    metric: Union[dict, Time] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, Time):
            self.metric = Time(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class Latency(QoSMetric):
    """
    Contractual latency defined in the SLA. If not specified, then best effort is assumed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Latency"]
    class_class_curie: ClassVar[str] = "gx:Latency"
    class_name: ClassVar[str] = "Latency"
    class_model_uri: ClassVar[URIRef] = GX.Latency

    metric: Union[dict, Time] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, Time):
            self.metric = Time(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class TargetPercentile(QoSMetric):
    """
    target percentile
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["TargetPercentile"]
    class_class_curie: ClassVar[str] = "gx:TargetPercentile"
    class_name: ClassVar[str] = "TargetPercentile"
    class_model_uri: ClassVar[URIRef] = GX.TargetPercentile

    metric: Union[dict, FloatPercentage] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, FloatPercentage):
            self.metric = FloatPercentage(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class Throughput(QoSMetric):
    """
    Metric for throughput.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["Throughput"]
    class_class_curie: ClassVar[str] = "gx:Throughput"
    class_name: ClassVar[str] = "Throughput"
    class_model_uri: ClassVar[URIRef] = GX.Throughput

    metric: Union[dict, DataRate] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, DataRate):
            self.metric = DataRate(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class IOPS(QoSMetric):
    """
    Metric for IOps.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["IOPS"]
    class_class_curie: ClassVar[str] = "gx:IOPS"
    class_name: ClassVar[str] = "IOPS"
    class_model_uri: ClassVar[URIRef] = GX.IOPS

    metric: Union[dict, DataRate] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, DataRate):
            self.metric = DataRate(**as_dict(self.metric))

        super().__post_init__(**kwargs)


@dataclass
class QoS(YAMLRoot):
    """
    Contractual performance values defined in the Service Level Agreement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["QoS"]
    class_class_curie: ClassVar[str] = "gx:QoS"
    class_name: ClassVar[str] = "QoS"
    class_model_uri: ClassVar[URIRef] = GX.QoS

    throughput: Optional[Union[dict, Throughput]] = None
    iops: Optional[Union[dict, IOPS]] = None
    bandWidth: Optional[Union[dict, BandWidth]] = None
    roundTripTime: Optional[Union[dict, RoundTripTime]] = None
    availability: Optional[Union[dict, Availability]] = None
    packetLoss: Optional[Union[dict, PacketLoss]] = None
    jitter: Optional[Union[dict, Jitter]] = None
    latency: Optional[Union[dict, Latency]] = None
    targetPercentile: Optional[Union[dict, TargetPercentile]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.throughput is not None and not isinstance(self.throughput, Throughput):
            self.throughput = Throughput(**as_dict(self.throughput))

        if self.iops is not None and not isinstance(self.iops, IOPS):
            self.iops = IOPS(**as_dict(self.iops))

        if self.bandWidth is not None and not isinstance(self.bandWidth, BandWidth):
            self.bandWidth = BandWidth(**as_dict(self.bandWidth))

        if self.roundTripTime is not None and not isinstance(self.roundTripTime, RoundTripTime):
            self.roundTripTime = RoundTripTime(**as_dict(self.roundTripTime))

        if self.availability is not None and not isinstance(self.availability, Availability):
            self.availability = Availability(**as_dict(self.availability))

        if self.packetLoss is not None and not isinstance(self.packetLoss, PacketLoss):
            self.packetLoss = PacketLoss(**as_dict(self.packetLoss))

        if self.jitter is not None and not isinstance(self.jitter, Jitter):
            self.jitter = Jitter(**as_dict(self.jitter))

        if self.latency is not None and not isinstance(self.latency, Latency):
            self.latency = Latency(**as_dict(self.latency))

        if self.targetPercentile is not None and not isinstance(self.targetPercentile, TargetPercentile):
            self.targetPercentile = TargetPercentile(**as_dict(self.targetPercentile))

        super().__post_init__(**kwargs)


@dataclass
class StorageConfiguration(InstantiationRequirement):
    """
    Represents the attributes that are configurable at service instantiation for storage service offerings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["StorageConfiguration"]
    class_class_curie: ClassVar[str] = "gx:StorageConfiguration"
    class_name: ClassVar[str] = "StorageConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.StorageConfiguration

    storageEncryption: Union[Union[dict, Encryption], List[Union[dict, Encryption]]] = None
    storageCompression: Optional[Union[Union[str, "CompressionAlgorithm"], List[Union[str, "CompressionAlgorithm"]]]] = empty_list()
    storageDeduplication: Optional[Union[Union[str, "DeduplicationMethod"], List[Union[str, "DeduplicationMethod"]]]] = empty_list()
    storageRedundancyMechanism: Optional[Union[Union[str, "StorageRedundancyMechanism"], List[Union[str, "StorageRedundancyMechanism"]]]] = empty_list()
    storageProtection: Optional[Union[Union[dict, DataProtectionPolicy], List[Union[dict, DataProtectionPolicy]]]] = empty_list()
    storageQoS: Optional[Union[Union[dict, QoS], List[Union[dict, QoS]]]] = empty_list()
    blockSize: Optional[Union[Union[dict, MemorySize], List[Union[dict, MemorySize]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.storageEncryption):
            self.MissingRequiredField("storageEncryption")
        #self._normalize_inlined_as_dict(slot_name="storageEncryption", slot_type=Encryption, key_name="cipher", keyed=False)

        if not isinstance(self.storageCompression, list):
            self.storageCompression = [self.storageCompression] if self.storageCompression is not None else []
        self.storageCompression = [v if isinstance(v, CompressionAlgorithm) else CompressionAlgorithm(v) for v in self.storageCompression]

        if not isinstance(self.storageDeduplication, list):
            self.storageDeduplication = [self.storageDeduplication] if self.storageDeduplication is not None else []
        self.storageDeduplication = [v if isinstance(v, DeduplicationMethod) else DeduplicationMethod(v) for v in self.storageDeduplication]

        if not isinstance(self.storageRedundancyMechanism, list):
            self.storageRedundancyMechanism = [self.storageRedundancyMechanism] if self.storageRedundancyMechanism is not None else []
        self.storageRedundancyMechanism = [v if isinstance(v, StorageRedundancyMechanism) else StorageRedundancyMechanism(v) for v in self.storageRedundancyMechanism]

        #self._normalize_inlined_as_dict(slot_name="storageProtection", slot_type=DataProtectionPolicy, key_name="protectionFrequency", keyed=False)

        if not isinstance(self.storageQoS, list):
            self.storageQoS = [self.storageQoS] if self.storageQoS is not None else []
        self.storageQoS = [v if isinstance(v, QoS) else QoS(**as_dict(v)) for v in self.storageQoS]

        #self._normalize_inlined_as_dict(slot_name="blockSize", slot_type=MemorySize, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class FileStorageConfiguration(StorageConfiguration):
    """
    Represents the attributes that are configurable at service instantiation for storage service offerings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["FileStorageConfiguration"]
    class_class_curie: ClassVar[str] = "gx:FileStorageConfiguration"
    class_name: ClassVar[str] = "FileStorageConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.FileStorageConfiguration

    storageEncryption: Union[Union[dict, Encryption], List[Union[dict, Encryption]]] = None
    fileSystemType: Optional[Union[Union[str, "FileSystemType"], List[Union[str, "FileSystemType"]]]] = empty_list()
    highLevelAccessProtocol: Optional[Union[Union[str, "FileAccessProtocol"], List[Union[str, "FileAccessProtocol"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.fileSystemType, list):
            self.fileSystemType = [self.fileSystemType] if self.fileSystemType is not None else []
        self.fileSystemType = [v if isinstance(v, FileSystemType) else FileSystemType(v) for v in self.fileSystemType]

        if not isinstance(self.highLevelAccessProtocol, list):
            self.highLevelAccessProtocol = [self.highLevelAccessProtocol] if self.highLevelAccessProtocol is not None else []
        self.highLevelAccessProtocol = [v if isinstance(v, FileAccessProtocol) else FileAccessProtocol(v) for v in self.highLevelAccessProtocol]

        super().__post_init__(**kwargs)


@dataclass
class BlockStorageConfiguration(StorageConfiguration):
    """
    Represents the attributes that are configurable at service instantiation for storage service offerings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BlockStorageConfiguration"]
    class_class_curie: ClassVar[str] = "gx:BlockStorageConfiguration"
    class_name: ClassVar[str] = "BlockStorageConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.BlockStorageConfiguration

    storageEncryption: Union[Union[dict, Encryption], List[Union[dict, Encryption]]] = None
    blockStorageTechnology: Optional[Union[Union[str, "BlockStorageTechnology"], List[Union[str, "BlockStorageTechnology"]]]] = empty_list()
    lowLevelBlockAccessProtocol: Optional[Union[Union[str, "BlockAccessProtocol"], List[Union[str, "BlockAccessProtocol"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.blockStorageTechnology, list):
            self.blockStorageTechnology = [self.blockStorageTechnology] if self.blockStorageTechnology is not None else []
        self.blockStorageTechnology = [v if isinstance(v, BlockStorageTechnology) else BlockStorageTechnology(v) for v in self.blockStorageTechnology]

        if not isinstance(self.lowLevelBlockAccessProtocol, list):
            self.lowLevelBlockAccessProtocol = [self.lowLevelBlockAccessProtocol] if self.lowLevelBlockAccessProtocol is not None else []
        self.lowLevelBlockAccessProtocol = [v if isinstance(v, BlockAccessProtocol) else BlockAccessProtocol(v) for v in self.lowLevelBlockAccessProtocol]

        super().__post_init__(**kwargs)


@dataclass
class StorageServiceOffering(InfrastructureServiceOffering):
    """
    A digital service available for order and offering storage capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["StorageServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:StorageServiceOffering"
    class_name: ClassVar[str] = "StorageServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.StorageServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    storageConfiguration: Union[dict, StorageConfiguration] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    minimumSize: Optional[Union[dict, MemorySize]] = None
    maximumSize: Optional[Union[dict, MemorySize]] = None
    lifetimeManagement: Optional[int] = None
    versioning: Optional[Union[bool, Bool]] = None
    storageConsistency: Optional[Union[str, "ConsistencyType"]] = None
    dataViews: Optional[Union[bool, Bool]] = None
    multipleViews: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.storageConfiguration):
            self.MissingRequiredField("storageConfiguration")
        if not isinstance(self.storageConfiguration, StorageConfiguration):
            self.storageConfiguration = StorageConfiguration(**as_dict(self.storageConfiguration))

        if self.minimumSize is not None and not isinstance(self.minimumSize, MemorySize):
            self.minimumSize = MemorySize(**as_dict(self.minimumSize))

        if self.maximumSize is not None and not isinstance(self.maximumSize, MemorySize):
            self.maximumSize = MemorySize(**as_dict(self.maximumSize))

        if self.lifetimeManagement is not None and not isinstance(self.lifetimeManagement, int):
            self.lifetimeManagement = int(self.lifetimeManagement)

        if self.versioning is not None and not isinstance(self.versioning, Bool):
            self.versioning = Bool(self.versioning)

        if self.storageConsistency is not None and not isinstance(self.storageConsistency, ConsistencyType):
            self.storageConsistency = ConsistencyType(self.storageConsistency)

        if self.dataViews is not None and not isinstance(self.dataViews, Bool):
            self.dataViews = Bool(self.dataViews)

        if self.multipleViews is not None and not isinstance(self.multipleViews, Bool):
            self.multipleViews = Bool(self.multipleViews)

        super().__post_init__(**kwargs)


@dataclass
class FileStorageServiceOffering(StorageServiceOffering):
    """
    A digital service available for order and offering file storage capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["FileStorageServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:FileStorageServiceOffering"
    class_name: ClassVar[str] = "FileStorageServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.FileStorageServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    storageConfiguration: Union[dict, FileStorageConfiguration] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    accessSemantics: Optional[Union[bool, Bool]] = None
    accessAttributes: Optional[Union[Union[str, "AccessAttribute"], List[Union[str, "AccessAttribute"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.storageConfiguration):
            self.MissingRequiredField("storageConfiguration")
        if not isinstance(self.storageConfiguration, FileStorageConfiguration):
            self.storageConfiguration = FileStorageConfiguration(**as_dict(self.storageConfiguration))

        if self.accessSemantics is not None and not isinstance(self.accessSemantics, Bool):
            self.accessSemantics = Bool(self.accessSemantics)

        if not isinstance(self.accessAttributes, list):
            self.accessAttributes = [self.accessAttributes] if self.accessAttributes is not None else []
        self.accessAttributes = [v if isinstance(v, AccessAttribute) else AccessAttribute(v) for v in self.accessAttributes]

        super().__post_init__(**kwargs)


@dataclass
class BlockStorageServiceOffering(StorageServiceOffering):
    """
    A digital service available for order and offering block storage capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["BlockStorageServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:BlockStorageServiceOffering"
    class_name: ClassVar[str] = "BlockStorageServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.BlockStorageServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    storageConfiguration: Union[dict, BlockStorageConfiguration] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.storageConfiguration):
            self.MissingRequiredField("storageConfiguration")
        if not isinstance(self.storageConfiguration, BlockStorageConfiguration):
            self.storageConfiguration = BlockStorageConfiguration(**as_dict(self.storageConfiguration))

        super().__post_init__(**kwargs)


@dataclass
class ObjectStorageServiceOffering(StorageServiceOffering):
    """
    A digital service available for order and offering object storage capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ObjectStorageServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ObjectStorageServiceOffering"
    class_name: ClassVar[str] = "ObjectStorageServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ObjectStorageServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    storageConfiguration: Union[dict, StorageConfiguration] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    accessAttributes: Optional[Union[Union[str, "AccessAttribute"], List[Union[str, "AccessAttribute"]]]] = empty_list()
    maximumObjectSize: Optional[Union[dict, MemorySize]] = None
    objectAPICompatibility: Optional[Union[Union[str, "StorageAPI"], List[Union[str, "StorageAPI"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.accessAttributes, list):
            self.accessAttributes = [self.accessAttributes] if self.accessAttributes is not None else []
        self.accessAttributes = [v if isinstance(v, AccessAttribute) else AccessAttribute(v) for v in self.accessAttributes]

        if self.maximumObjectSize is not None and not isinstance(self.maximumObjectSize, MemorySize):
            self.maximumObjectSize = MemorySize(**as_dict(self.maximumObjectSize))

        if not isinstance(self.objectAPICompatibility, list):
            self.objectAPICompatibility = [self.objectAPICompatibility] if self.objectAPICompatibility is not None else []
        self.objectAPICompatibility = [v if isinstance(v, StorageAPI) else StorageAPI(v) for v in self.objectAPICompatibility]

        super().__post_init__(**kwargs)


@dataclass
class ConnectivityServiceOffering(InfrastructureServiceOffering):
    """
    Connectivity Infrastructure services are made out of Physical, Link and Network services. Interconnection services
    between providers exist as a subclass of Network services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ConnectivityServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ConnectivityServiceOffering"
    class_name: ClassVar[str] = "ConnectivityServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ConnectivityServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    connectivityConfiguration: Union[Union[dict, "ConnectivityConfiguration"], List[Union[dict, "ConnectivityConfiguration"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    connectivityQoS: Optional[Union[dict, QoS]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.connectivityConfiguration):
            self.MissingRequiredField("connectivityConfiguration")
        if not isinstance(self.connectivityConfiguration, list):
            self.connectivityConfiguration = [self.connectivityConfiguration] if self.connectivityConfiguration is not None else []
        self.connectivityConfiguration = [v if isinstance(v, ConnectivityConfiguration) else ConnectivityConfiguration(**as_dict(v)) for v in self.connectivityConfiguration]

        if self.connectivityQoS is not None and not isinstance(self.connectivityQoS, QoS):
            self.connectivityQoS = QoS(**as_dict(self.connectivityQoS))

        super().__post_init__(**kwargs)


@dataclass
class NetworkConnectivityServiceOffering(ConnectivityServiceOffering):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["NetworkConnectivityServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:NetworkConnectivityServiceOffering"
    class_name: ClassVar[str] = "NetworkConnectivityServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.NetworkConnectivityServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    connectivityConfiguration: Union[Union[dict, "ConnectivityConfiguration"], List[Union[dict, "ConnectivityConfiguration"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    serviceType: Optional[str] = None
    publicIpAddressProvisioning: Optional[Union[str, "PublicIpAddressProvisioningTypes"]] = None
    ipVersion: Optional[Union[str, "IpVersionTypes"]] = None
    tenantSeparation: Optional[Union[str, "TenantSeparation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.serviceType is not None and not isinstance(self.serviceType, str):
            self.serviceType = str(self.serviceType)

        if self.publicIpAddressProvisioning is not None and not isinstance(self.publicIpAddressProvisioning, PublicIpAddressProvisioningTypes):
            self.publicIpAddressProvisioning = PublicIpAddressProvisioningTypes(self.publicIpAddressProvisioning)

        if self.ipVersion is not None and not isinstance(self.ipVersion, IpVersionTypes):
            self.ipVersion = IpVersionTypes(self.ipVersion)

        if self.tenantSeparation is not None and not isinstance(self.tenantSeparation, TenantSeparation):
            self.tenantSeparation = TenantSeparation(self.tenantSeparation)

        super().__post_init__(**kwargs)


@dataclass
class InterconnectionServiceOffering(NetworkConnectivityServiceOffering):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["InterconnectionServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:InterconnectionServiceOffering"
    class_name: ClassVar[str] = "InterconnectionServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.InterconnectionServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    connectivityConfiguration: Union[Union[dict, "ConnectivityConfiguration"], List[Union[dict, "ConnectivityConfiguration"]]] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    connectedNetworkA: Optional[Union[int, List[int]]] = empty_list()
    connectedNetworkZ: Optional[Union[int, List[int]]] = empty_list()
    prefixSetA: Optional[Union[str, List[str]]] = empty_list()
    prefixSetZ: Optional[Union[str, List[str]]] = empty_list()
    vlanConfiguration: Optional[Union[dict, "VLANConfiguration"]] = None
    connectionType: Optional[Union[str, List[str]]] = empty_list()
    interfaceType: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.connectedNetworkA, list):
            self.connectedNetworkA = [self.connectedNetworkA] if self.connectedNetworkA is not None else []
        self.connectedNetworkA = [v if isinstance(v, int) else int(v) for v in self.connectedNetworkA]

        if not isinstance(self.connectedNetworkZ, list):
            self.connectedNetworkZ = [self.connectedNetworkZ] if self.connectedNetworkZ is not None else []
        self.connectedNetworkZ = [v if isinstance(v, int) else int(v) for v in self.connectedNetworkZ]

        if not isinstance(self.prefixSetA, list):
            self.prefixSetA = [self.prefixSetA] if self.prefixSetA is not None else []
        self.prefixSetA = [v if isinstance(v, str) else str(v) for v in self.prefixSetA]

        if not isinstance(self.prefixSetZ, list):
            self.prefixSetZ = [self.prefixSetZ] if self.prefixSetZ is not None else []
        self.prefixSetZ = [v if isinstance(v, str) else str(v) for v in self.prefixSetZ]

        if self.vlanConfiguration is not None and not isinstance(self.vlanConfiguration, VLANConfiguration):
            self.vlanConfiguration = VLANConfiguration(**as_dict(self.vlanConfiguration))

        if not isinstance(self.connectionType, list):
            self.connectionType = [self.connectionType] if self.connectionType is not None else []
        self.connectionType = [v if isinstance(v, str) else str(v) for v in self.connectionType]

        if not isinstance(self.interfaceType, list):
            self.interfaceType = [self.interfaceType] if self.interfaceType is not None else []
        self.interfaceType = [v if isinstance(v, str) else str(v) for v in self.interfaceType]

        super().__post_init__(**kwargs)


@dataclass
class LinkConnectivityServiceOffering(ConnectivityServiceOffering):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["LinkConnectivityServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:LinkConnectivityServiceOffering"
    class_name: ClassVar[str] = "LinkConnectivityServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.LinkConnectivityServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    connectivityConfiguration: Union[Union[dict, "ConnectivityConfiguration"], List[Union[dict, "ConnectivityConfiguration"]]] = None
    protocolType: Union[str, "ProtocolType"] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    vlanConfiguration: Optional[Union[dict, "VLANConfiguration"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.protocolType):
            self.MissingRequiredField("protocolType")
        if not isinstance(self.protocolType, ProtocolType):
            self.protocolType = ProtocolType(self.protocolType)

        if self.vlanConfiguration is not None and not isinstance(self.vlanConfiguration, VLANConfiguration):
            self.vlanConfiguration = VLANConfiguration(**as_dict(self.vlanConfiguration))

        super().__post_init__(**kwargs)


@dataclass
class PhysicalConnectivityServiceOffering(ConnectivityServiceOffering):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["PhysicalConnectivityServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:PhysicalConnectivityServiceOffering"
    class_name: ClassVar[str] = "PhysicalConnectivityServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.PhysicalConnectivityServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    connectivityConfiguration: Union[Union[dict, "ConnectivityConfiguration"], List[Union[dict, "ConnectivityConfiguration"]]] = None
    circuitType: str = None
    interfaceType: str = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.circuitType):
            self.MissingRequiredField("circuitType")
        if not isinstance(self.circuitType, str):
            self.circuitType = str(self.circuitType)

        if self._is_empty(self.interfaceType):
            self.MissingRequiredField("interfaceType")
        if not isinstance(self.interfaceType, str):
            self.interfaceType = str(self.interfaceType)

        super().__post_init__(**kwargs)


@dataclass
class ConnectivityConfiguration(InstantiationRequirement):
    """
    The connectivityConfiguration class encapsulates the configurable attributes of a ConnectivityServiceOffering.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ConnectivityConfiguration"]
    class_class_curie: ClassVar[str] = "gx:ConnectivityConfiguration"
    class_name: ClassVar[str] = "ConnectivityConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.ConnectivityConfiguration

    sourceIdentifierA: Optional[str] = None
    destinationIdentifierZ: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sourceIdentifierA is not None and not isinstance(self.sourceIdentifierA, str):
            self.sourceIdentifierA = str(self.sourceIdentifierA)

        if self.destinationIdentifierZ is not None and not isinstance(self.destinationIdentifierZ, str):
            self.destinationIdentifierZ = str(self.destinationIdentifierZ)

        super().__post_init__(**kwargs)


@dataclass
class PhysicalInterconnectionPointIdentifier(PhysicalResource):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["PhysicalInterconnectionPointIdentifier"]
    class_class_curie: ClassVar[str] = "gx:PhysicalInterconnectionPointIdentifier"
    class_name: ClassVar[str] = "PhysicalInterconnectionPointIdentifier"
    class_model_uri: ClassVar[URIRef] = GX.PhysicalInterconnectionPointIdentifier

    maintainedBy: Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]] = None
    location: Union[Union[dict, Address], List[Union[dict, Address]]] = None
    interconnectionPointIdentifier: Union[str, InterconnectionPointIdentifierCompleteIPI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.interconnectionPointIdentifier):
            self.MissingRequiredField("interconnectionPointIdentifier")
        if not isinstance(self.interconnectionPointIdentifier, InterconnectionPointIdentifierCompleteIPI):
            self.interconnectionPointIdentifier = InterconnectionPointIdentifierCompleteIPI(self.interconnectionPointIdentifier)

        super().__post_init__(**kwargs)


@dataclass
class VirtualInterconnectionPointIdentifier(VirtualResource):
    """
    TBD
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VirtualInterconnectionPointIdentifier"]
    class_class_curie: ClassVar[str] = "gx:VirtualInterconnectionPointIdentifier"
    class_name: ClassVar[str] = "VirtualInterconnectionPointIdentifier"
    class_model_uri: ClassVar[URIRef] = GX.VirtualInterconnectionPointIdentifier

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    interconnectionPointIdentifier: Union[str, InterconnectionPointIdentifierCompleteIPI] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.interconnectionPointIdentifier):
            self.MissingRequiredField("interconnectionPointIdentifier")
        if not isinstance(self.interconnectionPointIdentifier, InterconnectionPointIdentifierCompleteIPI):
            self.interconnectionPointIdentifier = InterconnectionPointIdentifierCompleteIPI(self.interconnectionPointIdentifier)

        super().__post_init__(**kwargs)


@dataclass
class InterconnectionPointIdentifier(YAMLRoot):
    """
    Interconnection Point Identifier is a unique Service Access Point that identifies the location where resources can
    interconnect.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["InterconnectionPointIdentifier"]
    class_class_curie: ClassVar[str] = "gx:InterconnectionPointIdentifier"
    class_name: ClassVar[str] = "InterconnectionPointIdentifier"
    class_model_uri: ClassVar[URIRef] = GX.InterconnectionPointIdentifier

    completeIPI: Union[str, InterconnectionPointIdentifierCompleteIPI] = None
    ipiType: Optional[Union[str, "IPIType"]] = "Other"
    ipiProvider: Optional[str] = None
    specificParameters: Optional[str] = None
    datacenterAllocation: Optional[Union[dict, "DatacenterAllocation"]] = None
    macAddress: Optional[str] = None
    ipAddress: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.completeIPI):
            self.MissingRequiredField("completeIPI")
        if not isinstance(self.completeIPI, InterconnectionPointIdentifierCompleteIPI):
            self.completeIPI = InterconnectionPointIdentifierCompleteIPI(self.completeIPI)

        if self.ipiType is not None and not isinstance(self.ipiType, IPIType):
            self.ipiType = IPIType(self.ipiType)

        if self.ipiProvider is not None and not isinstance(self.ipiProvider, str):
            self.ipiProvider = str(self.ipiProvider)

        if self.specificParameters is not None and not isinstance(self.specificParameters, str):
            self.specificParameters = str(self.specificParameters)

        if self.datacenterAllocation is not None and not isinstance(self.datacenterAllocation, DatacenterAllocation):
            self.datacenterAllocation = DatacenterAllocation(**as_dict(self.datacenterAllocation))

        if self.macAddress is not None and not isinstance(self.macAddress, str):
            self.macAddress = str(self.macAddress)

        if self.ipAddress is not None and not isinstance(self.ipAddress, str):
            self.ipAddress = str(self.ipAddress)

        super().__post_init__(**kwargs)


@dataclass
class DatacenterAllocation(YAMLRoot):
    """
    Details specific situation within the datacenter where the service can be accessed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["DatacenterAllocation"]
    class_class_curie: ClassVar[str] = "gx:DatacenterAllocation"
    class_name: ClassVar[str] = "DatacenterAllocation"
    class_model_uri: ClassVar[URIRef] = GX.DatacenterAllocation

    refersTo: Union[dict, Datacenter] = None
    floor: Optional[str] = None
    rackNumber: Optional[str] = None
    patchPanel: Optional[str] = None
    portNumber: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.refersTo):
            self.MissingRequiredField("refersTo")
        if not isinstance(self.refersTo, Datacenter):
            self.refersTo = Datacenter(**as_dict(self.refersTo))

        if self.floor is not None and not isinstance(self.floor, str):
            self.floor = str(self.floor)

        if self.rackNumber is not None and not isinstance(self.rackNumber, str):
            self.rackNumber = str(self.rackNumber)

        if self.patchPanel is not None and not isinstance(self.patchPanel, str):
            self.patchPanel = str(self.patchPanel)

        if self.portNumber is not None and not isinstance(self.portNumber, int):
            self.portNumber = int(self.portNumber)

        super().__post_init__(**kwargs)


@dataclass
class VLANConfiguration(YAMLRoot):
    """
    TDB
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VLANConfiguration"]
    class_class_curie: ClassVar[str] = "gx:VLANConfiguration"
    class_name: ClassVar[str] = "VLANConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.VLANConfiguration

    vlanType: Optional[Union[str, "VlanType"]] = None
    vlanTag: Optional[int] = None
    vlanEtherType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.vlanType is not None and not isinstance(self.vlanType, VlanType):
            self.vlanType = VlanType(self.vlanType)

        if self.vlanTag is not None and not isinstance(self.vlanTag, int):
            self.vlanTag = int(self.vlanTag)

        if self.vlanEtherType is not None and not isinstance(self.vlanEtherType, str):
            self.vlanEtherType = str(self.vlanEtherType)

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionConfiguration(InstantiationRequirement):
    """
    InstantiationRequirements for compute functions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionConfiguration"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionConfiguration"
    class_name: ClassVar[str] = "ComputeFunctionConfiguration"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionConfiguration

    computeFunctionRuntime: Union[Union[dict, "ComputeFunctionRuntime"], List[Union[dict, "ComputeFunctionRuntime"]]] = None
    computeFunctionQuotas: Optional[Union[Union[dict, "ComputeFunctionQuotas"], List[Union[dict, "ComputeFunctionQuotas"]]]] = empty_list()
    computeFunctionLibrary: Optional[Union[Union[dict, "ComputeFunctionTemplate"], List[Union[dict, "ComputeFunctionTemplate"]]]] = empty_list()
    computeFunctionSDK: Optional[Union[Union[dict, "ComputeFunctionRuntime"], List[Union[dict, "ComputeFunctionRuntime"]]]] = empty_list()
    computeFunctionTrigger: Optional[Union[Union[dict, "ComputeFunctionTrigger"], List[Union[dict, "ComputeFunctionTrigger"]]]] = empty_list()
    computeFunctionDeploymentMethod: Optional[Union[Union[str, "ComputeFunctionDeploymentMethod"], List[Union[str, "ComputeFunctionDeploymentMethod"]]]] = empty_list()
    confidentialComputingTechnology: Optional[Union[dict, "ConfidentialComputing"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.computeFunctionRuntime):
            self.MissingRequiredField("computeFunctionRuntime")
        #self._normalize_inlined_as_dict(slot_name="computeFunctionRuntime", slot_type=ComputeFunctionRuntime, key_name="supportedLanguage", keyed=False)

        if not isinstance(self.computeFunctionQuotas, list):
            self.computeFunctionQuotas = [self.computeFunctionQuotas] if self.computeFunctionQuotas is not None else []
        self.computeFunctionQuotas = [v if isinstance(v, ComputeFunctionQuotas) else ComputeFunctionQuotas(**as_dict(v)) for v in self.computeFunctionQuotas]

        #self._normalize_inlined_as_dict(slot_name="computeFunctionLibrary", slot_type=ComputeFunctionTemplate, key_name="copyrightOwnedBy", keyed=False)

        #self._normalize_inlined_as_dict(slot_name="computeFunctionSDK", slot_type=ComputeFunctionRuntime, key_name="supportedLanguage", keyed=False)

        if not isinstance(self.computeFunctionTrigger, list):
            self.computeFunctionTrigger = [self.computeFunctionTrigger] if self.computeFunctionTrigger is not None else []
        self.computeFunctionTrigger = [v if isinstance(v, ComputeFunctionTrigger) else ComputeFunctionTrigger(**as_dict(v)) for v in self.computeFunctionTrigger]

        if not isinstance(self.computeFunctionDeploymentMethod, list):
            self.computeFunctionDeploymentMethod = [self.computeFunctionDeploymentMethod] if self.computeFunctionDeploymentMethod is not None else []
        self.computeFunctionDeploymentMethod = [v if isinstance(v, ComputeFunctionDeploymentMethod) else ComputeFunctionDeploymentMethod(v) for v in self.computeFunctionDeploymentMethod]

        if self.confidentialComputingTechnology is not None and not isinstance(self.confidentialComputingTechnology, ConfidentialComputing):
            self.confidentialComputingTechnology = ConfidentialComputing(**as_dict(self.confidentialComputingTechnology))

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionQuotas(YAMLRoot):
    """
    Attributes describing quotas for compute functions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionQuotas"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionQuotas"
    class_name: ClassVar[str] = "ComputeFunctionQuotas"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionQuotas

    functionMaximumNumber: Optional[int] = None
    functionStorageLimit: Optional[Union[dict, MemorySize]] = None
    functionTimeLimit: Optional[Union[dict, Time]] = None
    functionMemoryLimit: Optional[Union[dict, MemorySize]] = None
    functionSizeLimit: Optional[Union[dict, MemorySize]] = None
    functionConcurrencyLimit: Optional[int] = None
    functionRequestSizeLimit: Optional[Union[dict, MemorySize]] = None
    functionResponseSizeLimit: Optional[Union[dict, MemorySize]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.functionMaximumNumber is not None and not isinstance(self.functionMaximumNumber, int):
            self.functionMaximumNumber = int(self.functionMaximumNumber)

        if self.functionStorageLimit is not None and not isinstance(self.functionStorageLimit, MemorySize):
            self.functionStorageLimit = MemorySize(**as_dict(self.functionStorageLimit))

        if self.functionTimeLimit is not None and not isinstance(self.functionTimeLimit, Time):
            self.functionTimeLimit = Time(**as_dict(self.functionTimeLimit))

        if self.functionMemoryLimit is not None and not isinstance(self.functionMemoryLimit, MemorySize):
            self.functionMemoryLimit = MemorySize(**as_dict(self.functionMemoryLimit))

        if self.functionSizeLimit is not None and not isinstance(self.functionSizeLimit, MemorySize):
            self.functionSizeLimit = MemorySize(**as_dict(self.functionSizeLimit))

        if self.functionConcurrencyLimit is not None and not isinstance(self.functionConcurrencyLimit, int):
            self.functionConcurrencyLimit = int(self.functionConcurrencyLimit)

        if self.functionRequestSizeLimit is not None and not isinstance(self.functionRequestSizeLimit, MemorySize):
            self.functionRequestSizeLimit = MemorySize(**as_dict(self.functionRequestSizeLimit))

        if self.functionResponseSizeLimit is not None and not isinstance(self.functionResponseSizeLimit, MemorySize):
            self.functionResponseSizeLimit = MemorySize(**as_dict(self.functionResponseSizeLimit))

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionRuntime(YAMLRoot):
    """
    Attributes describing function runtimes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionRuntime"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionRuntime"
    class_name: ClassVar[str] = "ComputeFunctionRuntime"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionRuntime

    supportedLanguage: Union[str, "ComputeFunctionLanguage"] = None
    supportedVersion: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.supportedLanguage):
            self.MissingRequiredField("supportedLanguage")
        if not isinstance(self.supportedLanguage, ComputeFunctionLanguage):
            self.supportedLanguage = ComputeFunctionLanguage(self.supportedLanguage)

        if self._is_empty(self.supportedVersion):
            self.MissingRequiredField("supportedVersion")
        if not isinstance(self.supportedVersion, list):
            self.supportedVersion = [self.supportedVersion] if self.supportedVersion is not None else []
        self.supportedVersion = [v if isinstance(v, str) else str(v) for v in self.supportedVersion]

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionTrigger(YAMLRoot):
    """
    Attributes describing Compute Function Trigger
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionTrigger"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionTrigger"
    class_name: ClassVar[str] = "ComputeFunctionTrigger"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionTrigger

    triggeringService: Optional[Union[dict, ServiceOffering]] = None
    triggeringEvent: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.triggeringService is not None and not isinstance(self.triggeringService, ServiceOffering):
            self.triggeringService = ServiceOffering(**as_dict(self.triggeringService))

        if not isinstance(self.triggeringEvent, list):
            self.triggeringEvent = [self.triggeringEvent] if self.triggeringEvent is not None else []
        self.triggeringEvent = [v if isinstance(v, str) else str(v) for v in self.triggeringEvent]

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionTemplate(CodeArtifact):
    """
    Class for describing a template of compute function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionTemplate"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionTemplate"
    class_name: ClassVar[str] = "ComputeFunctionTemplate"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionTemplate

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    computeFunctionName: str = None
    computeFunctionDescription: str = None
    computeFunctionTemplateRuntime: Union[Union[dict, ComputeFunctionRuntime], List[Union[dict, ComputeFunctionRuntime]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.computeFunctionName):
            self.MissingRequiredField("computeFunctionName")
        if not isinstance(self.computeFunctionName, str):
            self.computeFunctionName = str(self.computeFunctionName)

        if self._is_empty(self.computeFunctionDescription):
            self.MissingRequiredField("computeFunctionDescription")
        if not isinstance(self.computeFunctionDescription, str):
            self.computeFunctionDescription = str(self.computeFunctionDescription)

        if self._is_empty(self.computeFunctionTemplateRuntime):
            self.MissingRequiredField("computeFunctionTemplateRuntime")
        #self._normalize_inlined_as_dict(slot_name="computeFunctionTemplateRuntime", slot_type=ComputeFunctionRuntime, key_name="supportedLanguage", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ComputeFunctionServiceOffering(ComputeServiceOffering):
    """
    A digital service available for order and providing compute functions capabilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ComputeFunctionServiceOffering"]
    class_class_curie: ClassVar[str] = "gx:ComputeFunctionServiceOffering"
    class_name: ClassVar[str] = "ComputeFunctionServiceOffering"
    class_model_uri: ClassVar[URIRef] = GX.ComputeFunctionServiceOffering

    providedBy: Union[str, LegalPersonRegistrationNumber] = None
    serviceOfferingTermsAndConditions: Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]] = None
    dataAccountExport: Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]] = None
    computeFunctionConfiguration: Union[dict, ComputeFunctionConfiguration] = None
    servicePolicy: Union[str, List[str]] = "default:allow intent"
    computeFunctionDebugTools: Optional[Union[bool, Bool]] = None
    computeFunctionEditor: Optional[Union[bool, Bool]] = None
    computeFunctionAllowQuota: Optional[Union[bool, Bool]] = None
    computeFunctionAllowTimeout: Optional[Union[bool, Bool]] = None
    computeFunctionAllowVersioning: Optional[Union[bool, Bool]] = None
    computeFunctionAllowAutoScaling: Optional[Union[bool, Bool]] = None
    computeFunctionAllowFSMount: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.computeFunctionConfiguration):
            self.MissingRequiredField("computeFunctionConfiguration")
        if not isinstance(self.computeFunctionConfiguration, ComputeFunctionConfiguration):
            self.computeFunctionConfiguration = ComputeFunctionConfiguration(**as_dict(self.computeFunctionConfiguration))

        if self.computeFunctionDebugTools is not None and not isinstance(self.computeFunctionDebugTools, Bool):
            self.computeFunctionDebugTools = Bool(self.computeFunctionDebugTools)

        if self.computeFunctionEditor is not None and not isinstance(self.computeFunctionEditor, Bool):
            self.computeFunctionEditor = Bool(self.computeFunctionEditor)

        if self.computeFunctionAllowQuota is not None and not isinstance(self.computeFunctionAllowQuota, Bool):
            self.computeFunctionAllowQuota = Bool(self.computeFunctionAllowQuota)

        if self.computeFunctionAllowTimeout is not None and not isinstance(self.computeFunctionAllowTimeout, Bool):
            self.computeFunctionAllowTimeout = Bool(self.computeFunctionAllowTimeout)

        if self.computeFunctionAllowVersioning is not None and not isinstance(self.computeFunctionAllowVersioning, Bool):
            self.computeFunctionAllowVersioning = Bool(self.computeFunctionAllowVersioning)

        if self.computeFunctionAllowAutoScaling is not None and not isinstance(self.computeFunctionAllowAutoScaling, Bool):
            self.computeFunctionAllowAutoScaling = Bool(self.computeFunctionAllowAutoScaling)

        if self.computeFunctionAllowFSMount is not None and not isinstance(self.computeFunctionAllowFSMount, Bool):
            self.computeFunctionAllowFSMount = Bool(self.computeFunctionAllowFSMount)

        super().__post_init__(**kwargs)


@dataclass
class VMImage(Image):
    """
    Image for virtual machines.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["VMImage"]
    class_class_curie: ClassVar[str] = "gx:VMImage"
    class_name: ClassVar[str] = "VM_Image"
    class_model_uri: ClassVar[URIRef] = GX.VMImage

    copyrightOwnedBy: Union[str, List[str]] = None
    license: Union[str, List[str]] = None
    resourcePolicy: Union[str, List[str]] = None
    vmImageDiskFormat: Optional[Union[str, "VMDiskType"]] = "RAW"
    hypervisorType: Optional[Union[str, "HypervisorType"]] = "other"
    firmwareType: Optional[Union[str, "FirmType"]] = "other"
    hwRngTypeOfImage: Optional[Union[str, "RNGTypes"]] = "None"
    watchDogAction: Optional[Union[str, "WatchDogActions"]] = "disabled"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.vmImageDiskFormat is not None and not isinstance(self.vmImageDiskFormat, VMDiskType):
            self.vmImageDiskFormat = VMDiskType(self.vmImageDiskFormat)

        if self.hypervisorType is not None and not isinstance(self.hypervisorType, HypervisorType):
            self.hypervisorType = HypervisorType(self.hypervisorType)

        if self.firmwareType is not None and not isinstance(self.firmwareType, FirmType):
            self.firmwareType = FirmType(self.firmwareType)

        if self.hwRngTypeOfImage is not None and not isinstance(self.hwRngTypeOfImage, RNGTypes):
            self.hwRngTypeOfImage = RNGTypes(self.hwRngTypeOfImage)

        if self.watchDogAction is not None and not isinstance(self.watchDogAction, WatchDogActions):
            self.watchDogAction = WatchDogActions(self.watchDogAction)

        super().__post_init__(**kwargs)


@dataclass
class ServerFlavor(InstantiationRequirement):
    """
    Description of the available hardware configuration, such as processor, ram and disk capacities, of a physical or
    virtual servers that can be launched.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ServerFlavor"]
    class_class_curie: ClassVar[str] = "gx:ServerFlavor"
    class_name: ClassVar[str] = "ServerFlavor"
    class_model_uri: ClassVar[URIRef] = GX.ServerFlavor

    cpu: Union[dict, CPU] = None
    ram: Union[dict, Memory] = None
    bootVolume: Union[dict, Disk] = None
    gpu: Optional[Union[dict, GPU]] = None
    network: Optional[str] = None
    additionalVolume: Optional[Union[Union[dict, Disk], List[Union[dict, Disk]]]] = empty_list()
    confidentialComputing: Optional[Union[dict, "ConfidentialComputing"]] = None
    hypervisor: Optional[Union[dict, Hypervisor]] = None
    hardwareAssistedVirtualization: Optional[Union[bool, Bool]] = False
    hwRngTypeOfFlavor: Optional[Union[str, "RNGTypes"]] = "None"

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cpu):
            self.MissingRequiredField("cpu")
        if not isinstance(self.cpu, CPU):
            self.cpu = CPU(**as_dict(self.cpu))

        if self._is_empty(self.ram):
            self.MissingRequiredField("ram")
        if not isinstance(self.ram, Memory):
            self.ram = Memory(**as_dict(self.ram))

        if self._is_empty(self.bootVolume):
            self.MissingRequiredField("bootVolume")
        if not isinstance(self.bootVolume, Disk):
            self.bootVolume = Disk(**as_dict(self.bootVolume))

        if self.gpu is not None and not isinstance(self.gpu, GPU):
            self.gpu = GPU(**as_dict(self.gpu))

        if self.network is not None and not isinstance(self.network, str):
            self.network = str(self.network)

        #self._normalize_inlined_as_dict(slot_name="additionalVolume", slot_type=Disk, key_name="diskSize", keyed=False)

        if self.confidentialComputing is not None and not isinstance(self.confidentialComputing, ConfidentialComputing):
            self.confidentialComputing = ConfidentialComputing(**as_dict(self.confidentialComputing))

        if self.hypervisor is not None and not isinstance(self.hypervisor, Hypervisor):
            self.hypervisor = Hypervisor(**as_dict(self.hypervisor))

        if self.hardwareAssistedVirtualization is not None and not isinstance(self.hardwareAssistedVirtualization, Bool):
            self.hardwareAssistedVirtualization = Bool(self.hardwareAssistedVirtualization)

        if self.hwRngTypeOfFlavor is not None and not isinstance(self.hwRngTypeOfFlavor, RNGTypes):
            self.hwRngTypeOfFlavor = RNGTypes(self.hwRngTypeOfFlavor)

        super().__post_init__(**kwargs)


@dataclass
class ConfidentialComputing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GX["ConfidentialComputing"]
    class_class_curie: ClassVar[str] = "gx:ConfidentialComputing"
    class_name: ClassVar[str] = "ConfidentialComputing"
    class_model_uri: ClassVar[URIRef] = GX.ConfidentialComputing

    technology: str = None
    attestationServiceURI: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.technology):
            self.MissingRequiredField("technology")
        if not isinstance(self.technology, str):
            self.technology = str(self.technology)

        if self.attestationServiceURI is not None and not isinstance(self.attestationServiceURI, URI):
            self.attestationServiceURI = URI(self.attestationServiceURI)

        super().__post_init__(**kwargs)


# Enumerations
class CountryNameAlpha2(EnumDefinitionImpl):

    AF = PermissibleValue(
        text="AF",
        description="Alpha2 code for Afghanistan.")
    EG = PermissibleValue(
        text="EG",
        description="Alpha2 code for Egypt.")
    AX = PermissibleValue(
        text="AX",
        description="Alpha2 code for Aland Islands.")
    AL = PermissibleValue(
        text="AL",
        description="Alpha2 code for Albania.")
    DZ = PermissibleValue(
        text="DZ",
        description="Alpha2 code for Algeria.")
    VI = PermissibleValue(
        text="VI",
        description="Alpha2 code for Virgin Islands (U.S.).")
    UM = PermissibleValue(
        text="UM",
        description="Alpha2 code for United States Minor Outlying Islands (the).")
    AS = PermissibleValue(
        text="AS",
        description="Alpha2 code for American Samoa.")
    AD = PermissibleValue(
        text="AD",
        description="Alpha2 code for Andorra.")
    AO = PermissibleValue(
        text="AO",
        description="Alpha2 code for Angola.")
    AI = PermissibleValue(
        text="AI",
        description="Alpha2 code for Anguilla.")
    AQ = PermissibleValue(
        text="AQ",
        description="Alpha2 code for Antarctica.")
    AG = PermissibleValue(
        text="AG",
        description="Alpha2 code for Antigua and Barbuda.")
    GQ = PermissibleValue(
        text="GQ",
        description="Alpha2 code for Equatorial Guinea.")
    SY = PermissibleValue(
        text="SY",
        description="Alpha2 code for Syrian Arab Republic.")
    AR = PermissibleValue(
        text="AR",
        description="Alpha2 code for Argentina.")
    AM = PermissibleValue(
        text="AM",
        description="Alpha2 code for Armenia.")
    AW = PermissibleValue(
        text="AW",
        description="Alpha2 code for Aruba.")
    AZ = PermissibleValue(
        text="AZ",
        description="Alpha2 code for Azerbaijan.")
    ET = PermissibleValue(
        text="ET",
        description="Alpha2 code for Ethiopia.")
    AU = PermissibleValue(
        text="AU",
        description="Alpha2 code for Australia.")
    BS = PermissibleValue(
        text="BS",
        description="Alpha2 code for Bahamas (the).")
    BH = PermissibleValue(
        text="BH",
        description="Alpha2 code for Bahrain.")
    BD = PermissibleValue(
        text="BD",
        description="Alpha2 code for Bangladesh.")
    BB = PermissibleValue(
        text="BB",
        description="Alpha2 code for Barbados.")
    BE = PermissibleValue(
        text="BE",
        description="Alpha2 code for Belgium.")
    BZ = PermissibleValue(
        text="BZ",
        description="Alpha2 code for Belize.")
    BJ = PermissibleValue(
        text="BJ",
        description="Alpha2 code for Benin.")
    BM = PermissibleValue(
        text="BM",
        description="Alpha2 code for Bermuda.")
    BT = PermissibleValue(
        text="BT",
        description="Alpha2 code for Bhutan.")
    VE = PermissibleValue(
        text="VE",
        description="Alpha2 code for Venezuela (Bolivarian Republic of).")
    BQ = PermissibleValue(
        text="BQ",
        description="Alpha2 code for Bonaire, Sint Eustatius and Saba.")
    BA = PermissibleValue(
        text="BA",
        description="Alpha2 code for Bosnia and Herzegovina.")
    BW = PermissibleValue(
        text="BW",
        description="Alpha2 code for Botswana.")
    BV = PermissibleValue(
        text="BV",
        description="Alpha2 code for Bouvet Island.")
    BR = PermissibleValue(
        text="BR",
        description="Alpha2 code for Brazil.")
    VG = PermissibleValue(
        text="VG",
        description="Alpha2 code for Virgin Islands (British).")
    IO = PermissibleValue(
        text="IO",
        description="Alpha2 code for British Indian Ocean Territory (the).")
    BN = PermissibleValue(
        text="BN",
        description="Alpha2 code for Brunei Darussalam.")
    BG = PermissibleValue(
        text="BG",
        description="Alpha2 code for Bulgaria.")
    BF = PermissibleValue(
        text="BF",
        description="Alpha2 code for Burkina Faso.")
    BI = PermissibleValue(
        text="BI",
        description="Alpha2 code for Burundi.")
    CV = PermissibleValue(
        text="CV",
        description="Alpha2 code for Cabo Verde.")
    CL = PermissibleValue(
        text="CL",
        description="Alpha2 code for Chile.")
    CN = PermissibleValue(
        text="CN",
        description="Alpha2 code for China.")
    CK = PermissibleValue(
        text="CK",
        description="Alpha2 code for Cook Islands (the).")
    CR = PermissibleValue(
        text="CR",
        description="Alpha2 code for Costa Rica.")
    CI = PermissibleValue(
        text="CI",
        description="Alpha2 code for Cote dIvoire.")
    CW = PermissibleValue(
        text="CW",
        description="Alpha2 code for Curacao.")
    DK = PermissibleValue(
        text="DK",
        description="Alpha2 code for Denmark.")
    CD = PermissibleValue(
        text="CD",
        description="Alpha2 code for Congo (the Democratic Republic of the).")
    KP = PermissibleValue(
        text="KP",
        description="Alpha2 code for Korea (the Democratic Peoples Republic of).")
    LA = PermissibleValue(
        text="LA",
        description="Alpha2 code for Lao Peoples Democratic Republic (the).")
    DE = PermissibleValue(
        text="DE",
        description="Alpha2 code for Germany.")
    DM = PermissibleValue(
        text="DM",
        description="Alpha2 code for Dominica.")
    DO = PermissibleValue(
        text="DO",
        description="Alpha2 code for Dominican Republic (the).")
    DJ = PermissibleValue(
        text="DJ",
        description="Alpha2 code for Djibouti.")
    EC = PermissibleValue(
        text="EC",
        description="Alpha2 code for Ecuador.")
    MK = PermissibleValue(
        text="MK",
        description="Alpha2 code for Republic of North Macedonia.")
    SV = PermissibleValue(
        text="SV",
        description="Alpha2 code for El Salvador.")
    ER = PermissibleValue(
        text="ER",
        description="Alpha2 code for Eritrea.")
    EE = PermissibleValue(
        text="EE",
        description="Alpha2 code for Estonia.")
    FK = PermissibleValue(
        text="FK",
        description="Alpha2 code for Falkland Islands (the) [Malvinas].")
    FO = PermissibleValue(
        text="FO",
        description="Alpha2 code for Faroe Islands (the).")
    FJ = PermissibleValue(
        text="FJ",
        description="Alpha2 code for Fiji.")
    FI = PermissibleValue(
        text="FI",
        description="Alpha2 code for Finland.")
    FM = PermissibleValue(
        text="FM",
        description="Alpha2 code for Micronesia (Federated States of).")
    FR = PermissibleValue(
        text="FR",
        description="Alpha2 code for France.")
    TF = PermissibleValue(
        text="TF",
        description="Alpha2 code for French Southern Territories (the).")
    GF = PermissibleValue(
        text="GF",
        description="Alpha2 code for French Guiana.")
    PF = PermissibleValue(
        text="PF",
        description="Alpha2 code for French Polynesia.")
    GA = PermissibleValue(
        text="GA",
        description="Alpha2 code for Gabon.")
    GM = PermissibleValue(
        text="GM",
        description="Alpha2 code for Gambia (the).")
    GE = PermissibleValue(
        text="GE",
        description="Alpha2 code for Georgia.")
    GH = PermissibleValue(
        text="GH",
        description="Alpha2 code for Ghana.")
    GI = PermissibleValue(
        text="GI",
        description="Alpha2 code for Gibraltar.")
    GD = PermissibleValue(
        text="GD",
        description="Alpha2 code for Grenada.")
    GR = PermissibleValue(
        text="GR",
        description="Alpha2 code for Greece.")
    GL = PermissibleValue(
        text="GL",
        description="Alpha2 code for Greenland.")
    GP = PermissibleValue(
        text="GP",
        description="Alpha2 code for Guadeloupe.")
    GU = PermissibleValue(
        text="GU",
        description="Alpha2 code for Guam.")
    GT = PermissibleValue(
        text="GT",
        description="Alpha2 code for Guatemala.")
    GG = PermissibleValue(
        text="GG",
        description="Alpha2 code for Guernsey.")
    GN = PermissibleValue(
        text="GN",
        description="Alpha2 code for Guinea.")
    GW = PermissibleValue(
        text="GW",
        description="Alpha2 code for Guinea-Bissau.")
    GY = PermissibleValue(
        text="GY",
        description="Alpha2 code for Guyana.")
    HT = PermissibleValue(
        text="HT",
        description="Alpha2 code for Haiti.")
    HM = PermissibleValue(
        text="HM",
        description="Alpha2 code for Heard Island and McDonald Islands.")
    HN = PermissibleValue(
        text="HN",
        description="Alpha2 code for Honduras.")
    HK = PermissibleValue(
        text="HK",
        description="Alpha2 code for Hong Kong.")
    IN = PermissibleValue(
        text="IN",
        description="Alpha2 code for India.")
    ID = PermissibleValue(
        text="ID",
        description="Alpha2 code for Indonesia.")
    IM = PermissibleValue(
        text="IM",
        description="Alpha2 code for Isle of Man.")
    IQ = PermissibleValue(
        text="IQ",
        description="Alpha2 code for Iraq.")
    IE = PermissibleValue(
        text="IE",
        description="Alpha2 code for Ireland.")
    IR = PermissibleValue(
        text="IR",
        description="Alpha2 code for Iran (Islamic Republic of).")
    IS = PermissibleValue(
        text="IS",
        description="Alpha2 code for Iceland.")
    IL = PermissibleValue(
        text="IL",
        description="Alpha2 code for Israel.")
    IT = PermissibleValue(
        text="IT",
        description="Alpha2 code for Italy.")
    JM = PermissibleValue(
        text="JM",
        description="Alpha2 code for Jamaica.")
    JP = PermissibleValue(
        text="JP",
        description="Alpha2 code for Japan.")
    YE = PermissibleValue(
        text="YE",
        description="Alpha2 code for Yemen.")
    JE = PermissibleValue(
        text="JE",
        description="Alpha2 code for Jersey.")
    JO = PermissibleValue(
        text="JO",
        description="Alpha2 code for Jordan.")
    KY = PermissibleValue(
        text="KY",
        description="Alpha2 code for Cayman Islands (the).")
    KH = PermissibleValue(
        text="KH",
        description="Alpha2 code for Cambodia.")
    CM = PermissibleValue(
        text="CM",
        description="Alpha2 code for Cameroon.")
    CA = PermissibleValue(
        text="CA",
        description="Alpha2 code for Canada.")
    KZ = PermissibleValue(
        text="KZ",
        description="Alpha2 code for Kazakhstan.")
    QA = PermissibleValue(
        text="QA",
        description="Alpha2 code for Qatar.")
    KE = PermissibleValue(
        text="KE",
        description="Alpha2 code for Kenya.")
    KG = PermissibleValue(
        text="KG",
        description="Alpha2 code for Kyrgyzstan.")
    KI = PermissibleValue(
        text="KI",
        description="Alpha2 code for Kiribati.")
    CC = PermissibleValue(
        text="CC",
        description="Alpha2 code for Cocos (Keeling) Islands (the).")
    CO = PermissibleValue(
        text="CO",
        description="Alpha2 code for Colombia.")
    KM = PermissibleValue(
        text="KM",
        description="Alpha2 code for Comoros (the).")
    CG = PermissibleValue(
        text="CG",
        description="Alpha2 code for Congo (the).")
    HR = PermissibleValue(
        text="HR",
        description="Alpha2 code for Croatia.")
    CU = PermissibleValue(
        text="CU",
        description="Alpha2 code for Cuba.")
    KW = PermissibleValue(
        text="KW",
        description="Alpha2 code for Kuwait.")
    LS = PermissibleValue(
        text="LS",
        description="Alpha2 code for Lesotho.")
    LV = PermissibleValue(
        text="LV",
        description="Alpha2 code for Latvia.")
    LB = PermissibleValue(
        text="LB",
        description="Alpha2 code for Lebanon.")
    LR = PermissibleValue(
        text="LR",
        description="Alpha2 code for Liberia.")
    LY = PermissibleValue(
        text="LY",
        description="Alpha2 code for Libya.")
    LI = PermissibleValue(
        text="LI",
        description="Alpha2 code for Liechtenstein.")
    LT = PermissibleValue(
        text="LT",
        description="Alpha2 code for Lithuania.")
    LU = PermissibleValue(
        text="LU",
        description="Alpha2 code for Luxembourg.")
    MO = PermissibleValue(
        text="MO",
        description="Alpha2 code for Macao.")
    MG = PermissibleValue(
        text="MG",
        description="Alpha2 code for Madagascar.")
    MW = PermissibleValue(
        text="MW",
        description="Alpha2 code for Malawi.")
    MY = PermissibleValue(
        text="MY",
        description="Alpha2 code for Malaysia.")
    MV = PermissibleValue(
        text="MV",
        description="Alpha2 code for Maldives.")
    ML = PermissibleValue(
        text="ML",
        description="Alpha2 code for Mali.")
    MT = PermissibleValue(
        text="MT",
        description="Alpha2 code for Malta.")
    MP = PermissibleValue(
        text="MP",
        description="Alpha2 code for Northern Mariana Islands (the).")
    MA = PermissibleValue(
        text="MA",
        description="Alpha2 code for Morocco.")
    MH = PermissibleValue(
        text="MH",
        description="Alpha2 code for Marshall Islands (the).")
    MQ = PermissibleValue(
        text="MQ",
        description="Alpha2 code for Martinique.")
    MR = PermissibleValue(
        text="MR",
        description="Alpha2 code for Mauritania.")
    MU = PermissibleValue(
        text="MU",
        description="Alpha2 code for Mauritius.")
    YT = PermissibleValue(
        text="YT",
        description="Alpha2 code for Mayotte.")
    MX = PermissibleValue(
        text="MX",
        description="Alpha2 code for Mexico.")
    MC = PermissibleValue(
        text="MC",
        description="Alpha2 code for Monaco.")
    MN = PermissibleValue(
        text="MN",
        description="Alpha2 code for Mongolia.")
    MS = PermissibleValue(
        text="MS",
        description="Alpha2 code for Montserrat.")
    ME = PermissibleValue(
        text="ME",
        description="Alpha2 code for Montenegro.")
    MZ = PermissibleValue(
        text="MZ",
        description="Alpha2 code for Mozambique.")
    MM = PermissibleValue(
        text="MM",
        description="Alpha2 code for Myanmar.")
    NA = PermissibleValue(
        text="NA",
        description="Alpha2 code for Namibia.")
    NR = PermissibleValue(
        text="NR",
        description="Alpha2 code for Nauru.")
    NP = PermissibleValue(
        text="NP",
        description="Alpha2 code for Nepal.")
    NC = PermissibleValue(
        text="NC",
        description="Alpha2 code for New Caledonia.")
    NZ = PermissibleValue(
        text="NZ",
        description="Alpha2 code for New Zealand.")
    NI = PermissibleValue(
        text="NI",
        description="Alpha2 code for Nicaragua.")
    NL = PermissibleValue(
        text="NL",
        description="Alpha2 code for Netherlands (the).")
    NE = PermissibleValue(
        text="NE",
        description="Alpha2 code for Niger (the).")
    NG = PermissibleValue(
        text="NG",
        description="Alpha2 code for Nigeria.")
    NU = PermissibleValue(
        text="NU",
        description="Alpha2 code for Niue.")
    NF = PermissibleValue(
        text="NF",
        description="Alpha2 code for Norfolk Island.")
    OM = PermissibleValue(
        text="OM",
        description="Alpha2 code for Oman.")
    AT = PermissibleValue(
        text="AT",
        description="Alpha2 code for Austria.")
    PK = PermissibleValue(
        text="PK",
        description="Alpha2 code for Pakistan.")
    PW = PermissibleValue(
        text="PW",
        description="Alpha2 code for Palau.")
    PS = PermissibleValue(
        text="PS",
        description="Alpha2 code for Palestine, State of.")
    PA = PermissibleValue(
        text="PA",
        description="Alpha2 code for Panama.")
    PG = PermissibleValue(
        text="PG",
        description="Alpha2 code for Papua New Guinea.")
    PY = PermissibleValue(
        text="PY",
        description="Alpha2 code for Paraguay.")
    PE = PermissibleValue(
        text="PE",
        description="Alpha2 code for Peru.")
    PH = PermissibleValue(
        text="PH",
        description="Alpha2 code for Philippines (the).")
    PN = PermissibleValue(
        text="PN",
        description="Alpha2 code for Pitcairn.")
    BO = PermissibleValue(
        text="BO",
        description="Alpha2 code for Bolivia (Plurinational State of).")
    PL = PermissibleValue(
        text="PL",
        description="Alpha2 code for Poland.")
    PT = PermissibleValue(
        text="PT",
        description="Alpha2 code for Portugal.")
    PR = PermissibleValue(
        text="PR",
        description="Alpha2 code for Puerto Rico.")
    KR = PermissibleValue(
        text="KR",
        description="Alpha2 code for Korea (the Republic of).")
    MD = PermissibleValue(
        text="MD",
        description="Alpha2 code for Moldova (the Republic of).")
    RE = PermissibleValue(
        text="RE",
        description="Alpha2 code for Reunion.")
    RW = PermissibleValue(
        text="RW",
        description="Alpha2 code for Rwanda.")
    RO = PermissibleValue(
        text="RO",
        description="Alpha2 code for Romania.")
    RU = PermissibleValue(
        text="RU",
        description="Alpha2 code for Russian Federation (the).")
    SB = PermissibleValue(
        text="SB",
        description="Alpha2 code for Solomon Islands.")
    ZM = PermissibleValue(
        text="ZM",
        description="Alpha2 code for Zambia.")
    WS = PermissibleValue(
        text="WS",
        description="Alpha2 code for Samoa.")
    SM = PermissibleValue(
        text="SM",
        description="Alpha2 code for San Marino.")
    ST = PermissibleValue(
        text="ST",
        description="Alpha2 code for Sao Tome and Principe.")
    SA = PermissibleValue(
        text="SA",
        description="Alpha2 code for Saudi Arabia.")
    SE = PermissibleValue(
        text="SE",
        description="Alpha2 code for Sweden.")
    CH = PermissibleValue(
        text="CH",
        description="Alpha2 code for Switzerland.")
    SN = PermissibleValue(
        text="SN",
        description="Alpha2 code for Senegal.")
    RS = PermissibleValue(
        text="RS",
        description="Alpha2 code for Serbia.")
    SC = PermissibleValue(
        text="SC",
        description="Alpha2 code for Seychelles.")
    SL = PermissibleValue(
        text="SL",
        description="Alpha2 code for Sierra Leone.")
    ZW = PermissibleValue(
        text="ZW",
        description="Alpha2 code for Zimbabwe.")
    SG = PermissibleValue(
        text="SG",
        description="Alpha2 code for Singapore.")
    SK = PermissibleValue(
        text="SK",
        description="Alpha2 code for Slovakia.")
    SI = PermissibleValue(
        text="SI",
        description="Alpha2 code for Slovenia.")
    SO = PermissibleValue(
        text="SO",
        description="Alpha2 code for Somalia.")
    ES = PermissibleValue(
        text="ES",
        description="Alpha2 code for Spain.")
    LK = PermissibleValue(
        text="LK",
        description="Alpha2 code for Sri Lanka.")
    BL = PermissibleValue(
        text="BL",
        description="Alpha2 code for Saint Barthelemy.")
    SH = PermissibleValue(
        text="SH",
        description="Alpha2 code for Saint Helena, Ascension and Tristan da Cunha.")
    KN = PermissibleValue(
        text="KN",
        description="Alpha2 code for Saint Kitts and Nevis.")
    LC = PermissibleValue(
        text="LC",
        description="Alpha2 code for Saint Lucia.")
    MF = PermissibleValue(
        text="MF",
        description="Alpha2 code for Saint Martin (French part).")
    SX = PermissibleValue(
        text="SX",
        description="Alpha2 code for Sint Maarten (Dutch part).")
    PM = PermissibleValue(
        text="PM",
        description="Alpha2 code for Saint Pierre and Miquelon.")
    VC = PermissibleValue(
        text="VC",
        description="Alpha2 code for Saint Vincent and the Grenadines.")
    ZA = PermissibleValue(
        text="ZA",
        description="Alpha2 code for South Africa.")
    SD = PermissibleValue(
        text="SD",
        description="Alpha2 code for Sudan (the).")
    GS = PermissibleValue(
        text="GS",
        description="Alpha2 code for South Georgia and the South Sandwich Islands.")
    SS = PermissibleValue(
        text="SS",
        description="Alpha2 code for South Sudan.")
    SR = PermissibleValue(
        text="SR",
        description="Alpha2 code for Suriname.")
    SJ = PermissibleValue(
        text="SJ",
        description="Alpha2 code for Svalbard and Jan Mayen.")
    SZ = PermissibleValue(
        text="SZ",
        description="Alpha2 code for Eswatini.")
    TJ = PermissibleValue(
        text="TJ",
        description="Alpha2 code for Tajikistan.")
    TW = PermissibleValue(
        text="TW",
        description="Alpha2 code for Taiwan (Province of China).")
    TH = PermissibleValue(
        text="TH",
        description="Alpha2 code for Thailand.")
    TL = PermissibleValue(
        text="TL",
        description="Alpha2 code for Timor-Leste.")
    TG = PermissibleValue(
        text="TG",
        description="Alpha2 code for Togo.")
    TK = PermissibleValue(
        text="TK",
        description="Alpha2 code for Tokelau.")
    TO = PermissibleValue(
        text="TO",
        description="Alpha2 code for Tonga.")
    TT = PermissibleValue(
        text="TT",
        description="Alpha2 code for Trinidad and Tobago.")
    TD = PermissibleValue(
        text="TD",
        description="Alpha2 code for Chad.")
    CZ = PermissibleValue(
        text="CZ",
        description="Alpha2 code for Czechia.")
    TN = PermissibleValue(
        text="TN",
        description="Alpha2 code for Tunisia.")
    TR = PermissibleValue(
        text="TR",
        description="Alpha2 code for Turkey.")
    TM = PermissibleValue(
        text="TM",
        description="Alpha2 code for Turkmenistan.")
    TC = PermissibleValue(
        text="TC",
        description="Alpha2 code for Turks and Caicos Islands (the).")
    TV = PermissibleValue(
        text="TV",
        description="Alpha2 code for Tuvalu.")
    UG = PermissibleValue(
        text="UG",
        description="Alpha2 code for Uganda.")
    UA = PermissibleValue(
        text="UA",
        description="Alpha2 code for Ukraine.")
    HU = PermissibleValue(
        text="HU",
        description="Alpha2 code for Hungary.")
    UY = PermissibleValue(
        text="UY",
        description="Alpha2 code for Uruguay.")
    UZ = PermissibleValue(
        text="UZ",
        description="Alpha2 code for Uzbekistan.")
    VU = PermissibleValue(
        text="VU",
        description="Alpha2 code for Vanuatu.")
    VA = PermissibleValue(
        text="VA",
        description="Alpha2 code for Holy See (the).")
    AE = PermissibleValue(
        text="AE",
        description="Alpha2 code for United Arab Emirates (the).")
    TZ = PermissibleValue(
        text="TZ",
        description="Alpha2 code for Tanzania, United Republic of.")
    US = PermissibleValue(
        text="US",
        description="Alpha2 code for United States of America (the).")
    GB = PermissibleValue(
        text="GB",
        description="Alpha2 code for United Kingdom of Great Britain and Northern Ireland (the).")
    VN = PermissibleValue(
        text="VN",
        description="Alpha2 code for Viet Nam.")
    WF = PermissibleValue(
        text="WF",
        description="Alpha2 code for Wallis and Futuna.")
    CX = PermissibleValue(
        text="CX",
        description="Alpha2 code for Christmas Island.")
    BY = PermissibleValue(
        text="BY",
        description="Alpha2 code for Belarus.")
    EH = PermissibleValue(
        text="EH",
        description="Alpha2 code for Western Sahara.")
    CF = PermissibleValue(
        text="CF",
        description="Alpha2 code for Central African Republic (the).")
    CY = PermissibleValue(
        text="CY",
        description="Alpha2 code for Cyprus.")

    _defn = EnumDefinition(
        name="CountryNameAlpha2",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "False",
            PermissibleValue(
                text="False",
                description="Alpha2 code for Norway."))

class CountryNameAlpha3(EnumDefinitionImpl):

    AFG = PermissibleValue(
        text="AFG",
        description="Alpha3 code for Afghanistan.")
    ALA = PermissibleValue(
        text="ALA",
        description="Alpha3 code for Aland Islands.")
    ALB = PermissibleValue(
        text="ALB",
        description="Alpha3 code for Albania.")
    DZA = PermissibleValue(
        text="DZA",
        description="Alpha3 code for Algeria.")
    ASM = PermissibleValue(
        text="ASM",
        description="Alpha3 code for American Samoa.")
    AND = PermissibleValue(
        text="AND",
        description="Alpha3 code for Andorra.")
    AGO = PermissibleValue(
        text="AGO",
        description="Alpha3 code for Angola.")
    AIA = PermissibleValue(
        text="AIA",
        description="Alpha3 code for Anguilla.")
    ATA = PermissibleValue(
        text="ATA",
        description="Alpha3 code for Antarctica.")
    ATG = PermissibleValue(
        text="ATG",
        description="Alpha3 code for Antigua and Barbuda.")
    ARG = PermissibleValue(
        text="ARG",
        description="Alpha3 code for Argentina.")
    ARM = PermissibleValue(
        text="ARM",
        description="Alpha3 code for Armenia.")
    ABW = PermissibleValue(
        text="ABW",
        description="Alpha3 code for Aruba.")
    AUS = PermissibleValue(
        text="AUS",
        description="Alpha3 code for Australia.")
    AUT = PermissibleValue(
        text="AUT",
        description="Alpha3 code for Austria.")
    AZE = PermissibleValue(
        text="AZE",
        description="Alpha3 code for Azerbaijan.")
    BHS = PermissibleValue(
        text="BHS",
        description="Alpha3 code for Bahamas (the).")
    BHR = PermissibleValue(
        text="BHR",
        description="Alpha3 code for Bahrain.")
    BGD = PermissibleValue(
        text="BGD",
        description="Alpha3 code for Bangladesh.")
    BRB = PermissibleValue(
        text="BRB",
        description="Alpha3 code for Barbados.")
    BLR = PermissibleValue(
        text="BLR",
        description="Alpha3 code for Belarus.")
    BEL = PermissibleValue(
        text="BEL",
        description="Alpha3 code for Belgium.")
    BLZ = PermissibleValue(
        text="BLZ",
        description="Alpha3 code for Belize.")
    BEN = PermissibleValue(
        text="BEN",
        description="Alpha3 code for Benin.")
    BMU = PermissibleValue(
        text="BMU",
        description="Alpha3 code for Bermuda.")
    BTN = PermissibleValue(
        text="BTN",
        description="Alpha3 code for Bhutan.")
    BOL = PermissibleValue(
        text="BOL",
        description="Alpha3 code for Bolivia (Plurinational State of).")
    BES = PermissibleValue(
        text="BES",
        description="Alpha3 code for Bonaire, Sint Eustatius and Saba.")
    BIH = PermissibleValue(
        text="BIH",
        description="Alpha3 code for Bosnia and Herzegovina.")
    BWA = PermissibleValue(
        text="BWA",
        description="Alpha3 code for Botswana.")
    BVT = PermissibleValue(
        text="BVT",
        description="Alpha3 code for Bouvet Island.")
    BRA = PermissibleValue(
        text="BRA",
        description="Alpha3 code for Brazil.")
    IOT = PermissibleValue(
        text="IOT",
        description="Alpha3 code for British Indian Ocean Territory (the).")
    BRN = PermissibleValue(
        text="BRN",
        description="Alpha3 code for Brunei Darussalam.")
    BGR = PermissibleValue(
        text="BGR",
        description="Alpha3 code for Bulgaria.")
    BFA = PermissibleValue(
        text="BFA",
        description="Alpha3 code for Burkina Faso.")
    BDI = PermissibleValue(
        text="BDI",
        description="Alpha3 code for Burundi.")
    KHM = PermissibleValue(
        text="KHM",
        description="Alpha3 code for Cambodia.")
    CMR = PermissibleValue(
        text="CMR",
        description="Alpha3 code for Cameroon.")
    CAN = PermissibleValue(
        text="CAN",
        description="Alpha3 code for Canada.")
    CPV = PermissibleValue(
        text="CPV",
        description="Alpha3 code for Cabo Verde.")
    CYM = PermissibleValue(
        text="CYM",
        description="Alpha3 code for Cayman Islands (the).")
    CAF = PermissibleValue(
        text="CAF",
        description="Alpha3 code for Central African Republic (the).")
    TCD = PermissibleValue(
        text="TCD",
        description="Alpha3 code for Chad.")
    CHL = PermissibleValue(
        text="CHL",
        description="Alpha3 code for Chile.")
    CHN = PermissibleValue(
        text="CHN",
        description="Alpha3 code for China.")
    CXR = PermissibleValue(
        text="CXR",
        description="Alpha3 code for Christmas Island.")
    CCK = PermissibleValue(
        text="CCK",
        description="Alpha3 code for Cocos (Keeling) Islands (the).")
    COL = PermissibleValue(
        text="COL",
        description="Alpha3 code for Colombia.")
    COM = PermissibleValue(
        text="COM",
        description="Alpha3 code for Comoros (the).")
    COG = PermissibleValue(
        text="COG",
        description="Alpha3 code for Congo (the).")
    COD = PermissibleValue(
        text="COD",
        description="Alpha3 code for Congo (the Democratic Republic of the).")
    COK = PermissibleValue(
        text="COK",
        description="Alpha3 code for Cook Islands (the).")
    CRI = PermissibleValue(
        text="CRI",
        description="Alpha3 code for Costa Rica.")
    CIV = PermissibleValue(
        text="CIV",
        description="Alpha3 code for Cote dIvoire.")
    HRV = PermissibleValue(
        text="HRV",
        description="Alpha3 code for Croatia.")
    CUB = PermissibleValue(
        text="CUB",
        description="Alpha3 code for Cuba.")
    CUW = PermissibleValue(
        text="CUW",
        description="Alpha3 code for Curacao.")
    CYP = PermissibleValue(
        text="CYP",
        description="Alpha3 code for Cyprus.")
    CZE = PermissibleValue(
        text="CZE",
        description="Alpha3 code for Czechia.")
    DNK = PermissibleValue(
        text="DNK",
        description="Alpha3 code for Denmark.")
    DJI = PermissibleValue(
        text="DJI",
        description="Alpha3 code for Djibouti.")
    DMA = PermissibleValue(
        text="DMA",
        description="Alpha3 code for Dominica.")
    DOM = PermissibleValue(
        text="DOM",
        description="Alpha3 code for Dominican Republic (the).")
    ECU = PermissibleValue(
        text="ECU",
        description="Alpha3 code for Ecuador.")
    EGY = PermissibleValue(
        text="EGY",
        description="Alpha3 code for Egypt.")
    SLV = PermissibleValue(
        text="SLV",
        description="Alpha3 code for El Salvador.")
    GNQ = PermissibleValue(
        text="GNQ",
        description="Alpha3 code for Equatorial Guinea.")
    ERI = PermissibleValue(
        text="ERI",
        description="Alpha3 code for Eritrea.")
    EST = PermissibleValue(
        text="EST",
        description="Alpha3 code for Estonia.")
    ETH = PermissibleValue(
        text="ETH",
        description="Alpha3 code for Ethiopia.")
    FLK = PermissibleValue(
        text="FLK",
        description="Alpha3 code for Falkland Islands (the) [Malvinas].")
    FRO = PermissibleValue(
        text="FRO",
        description="Alpha3 code for Faroe Islands (the).")
    FJI = PermissibleValue(
        text="FJI",
        description="Alpha3 code for Fiji.")
    FIN = PermissibleValue(
        text="FIN",
        description="Alpha3 code for Finland.")
    FRA = PermissibleValue(
        text="FRA",
        description="Alpha3 code for France.")
    GUF = PermissibleValue(
        text="GUF",
        description="Alpha3 code for French Guiana.")
    PYF = PermissibleValue(
        text="PYF",
        description="Alpha3 code for French Polynesia.")
    ATF = PermissibleValue(
        text="ATF",
        description="Alpha3 code for French Southern Territories (the).")
    GAB = PermissibleValue(
        text="GAB",
        description="Alpha3 code for Gabon.")
    GMB = PermissibleValue(
        text="GMB",
        description="Alpha3 code for Gambia (the).")
    GEO = PermissibleValue(
        text="GEO",
        description="Alpha3 code for Georgia.")
    DEU = PermissibleValue(
        text="DEU",
        description="Alpha3 code for Germany.")
    GHA = PermissibleValue(
        text="GHA",
        description="Alpha3 code for Ghana.")
    GIB = PermissibleValue(
        text="GIB",
        description="Alpha3 code for Gibraltar.")
    GRC = PermissibleValue(
        text="GRC",
        description="Alpha3 code for Greece.")
    GRL = PermissibleValue(
        text="GRL",
        description="Alpha3 code for Greenland.")
    GRD = PermissibleValue(
        text="GRD",
        description="Alpha3 code for Grenada.")
    GLP = PermissibleValue(
        text="GLP",
        description="Alpha3 code for Guadeloupe.")
    GUM = PermissibleValue(
        text="GUM",
        description="Alpha3 code for Guam.")
    GTM = PermissibleValue(
        text="GTM",
        description="Alpha3 code for Guatemala.")
    GGY = PermissibleValue(
        text="GGY",
        description="Alpha3 code for Guernsey.")
    GIN = PermissibleValue(
        text="GIN",
        description="Alpha3 code for Guinea.")
    GNB = PermissibleValue(
        text="GNB",
        description="Alpha3 code for Guinea-Bissau.")
    GUY = PermissibleValue(
        text="GUY",
        description="Alpha3 code for Guyana.")
    HTI = PermissibleValue(
        text="HTI",
        description="Alpha3 code for Haiti.")
    HMD = PermissibleValue(
        text="HMD",
        description="Alpha3 code for Heard Island and McDonald Islands.")
    VAT = PermissibleValue(
        text="VAT",
        description="Alpha3 code for Holy See (the).")
    HND = PermissibleValue(
        text="HND",
        description="Alpha3 code for Honduras.")
    HKG = PermissibleValue(
        text="HKG",
        description="Alpha3 code for Hong Kong.")
    HUN = PermissibleValue(
        text="HUN",
        description="Alpha3 code for Hungary.")
    ISL = PermissibleValue(
        text="ISL",
        description="Alpha3 code for Iceland.")
    IND = PermissibleValue(
        text="IND",
        description="Alpha3 code for India.")
    IDN = PermissibleValue(
        text="IDN",
        description="Alpha3 code for Indonesia.")
    IRN = PermissibleValue(
        text="IRN",
        description="Alpha3 code for Iran (Islamic Republic of).")
    IRQ = PermissibleValue(
        text="IRQ",
        description="Alpha3 code for Iraq.")
    IRL = PermissibleValue(
        text="IRL",
        description="Alpha3 code for Ireland.")
    IMN = PermissibleValue(
        text="IMN",
        description="Alpha3 code for Isle of Man.")
    ISR = PermissibleValue(
        text="ISR",
        description="Alpha3 code for Israel.")
    ITA = PermissibleValue(
        text="ITA",
        description="Alpha3 code for Italy.")
    JAM = PermissibleValue(
        text="JAM",
        description="Alpha3 code for Jamaica.")
    JPN = PermissibleValue(
        text="JPN",
        description="Alpha3 code for Japan.")
    JEY = PermissibleValue(
        text="JEY",
        description="Alpha3 code for Jersey.")
    JOR = PermissibleValue(
        text="JOR",
        description="Alpha3 code for Jordan.")
    KAZ = PermissibleValue(
        text="KAZ",
        description="Alpha3 code for Kazakhstan.")
    KEN = PermissibleValue(
        text="KEN",
        description="Alpha3 code for Kenya.")
    KIR = PermissibleValue(
        text="KIR",
        description="Alpha3 code for Kiribati.")
    PRK = PermissibleValue(
        text="PRK",
        description="Alpha3 code for Korea (the Democratic Peoples Republic of).")
    KOR = PermissibleValue(
        text="KOR",
        description="Alpha3 code for Korea (the Republic of).")
    KWT = PermissibleValue(
        text="KWT",
        description="Alpha3 code for Kuwait.")
    KGZ = PermissibleValue(
        text="KGZ",
        description="Alpha3 code for Kyrgyzstan.")
    LAO = PermissibleValue(
        text="LAO",
        description="Alpha3 code for Lao Peoples Democratic Republic (the).")
    LVA = PermissibleValue(
        text="LVA",
        description="Alpha3 code for Latvia.")
    LBN = PermissibleValue(
        text="LBN",
        description="Alpha3 code for Lebanon.")
    LSO = PermissibleValue(
        text="LSO",
        description="Alpha3 code for Lesotho.")
    LBR = PermissibleValue(
        text="LBR",
        description="Alpha3 code for Liberia.")
    LBY = PermissibleValue(
        text="LBY",
        description="Alpha3 code for Libya.")
    LIE = PermissibleValue(
        text="LIE",
        description="Alpha3 code for Liechtenstein.")
    LTU = PermissibleValue(
        text="LTU",
        description="Alpha3 code for Lithuania.")
    LUX = PermissibleValue(
        text="LUX",
        description="Alpha3 code for Luxembourg.")
    MAC = PermissibleValue(
        text="MAC",
        description="Alpha3 code for Macao.")
    MKD = PermissibleValue(
        text="MKD",
        description="Alpha3 code for Republic of North Macedonia.")
    MDG = PermissibleValue(
        text="MDG",
        description="Alpha3 code for Madagascar.")
    MWI = PermissibleValue(
        text="MWI",
        description="Alpha3 code for Malawi.")
    MYS = PermissibleValue(
        text="MYS",
        description="Alpha3 code for Malaysia.")
    MDV = PermissibleValue(
        text="MDV",
        description="Alpha3 code for Maldives.")
    MLI = PermissibleValue(
        text="MLI",
        description="Alpha3 code for Mali.")
    MLT = PermissibleValue(
        text="MLT",
        description="Alpha3 code for Malta.")
    MHL = PermissibleValue(
        text="MHL",
        description="Alpha3 code for Marshall Islands (the).")
    MTQ = PermissibleValue(
        text="MTQ",
        description="Alpha3 code for Martinique.")
    MRT = PermissibleValue(
        text="MRT",
        description="Alpha3 code for Mauritania.")
    MUS = PermissibleValue(
        text="MUS",
        description="Alpha3 code for Mauritius.")
    MYT = PermissibleValue(
        text="MYT",
        description="Alpha3 code for Mayotte.")
    MEX = PermissibleValue(
        text="MEX",
        description="Alpha3 code for Mexico.")
    FSM = PermissibleValue(
        text="FSM",
        description="Alpha3 code for Micronesia (Federated States of).")
    MDA = PermissibleValue(
        text="MDA",
        description="Alpha3 code for Moldova (the Republic of).")
    MCO = PermissibleValue(
        text="MCO",
        description="Alpha3 code for Monaco.")
    MNG = PermissibleValue(
        text="MNG",
        description="Alpha3 code for Mongolia.")
    MNE = PermissibleValue(
        text="MNE",
        description="Alpha3 code for Montenegro.")
    MSR = PermissibleValue(
        text="MSR",
        description="Alpha3 code for Montserrat.")
    MAR = PermissibleValue(
        text="MAR",
        description="Alpha3 code for Morocco.")
    MOZ = PermissibleValue(
        text="MOZ",
        description="Alpha3 code for Mozambique.")
    MMR = PermissibleValue(
        text="MMR",
        description="Alpha3 code for Myanmar.")
    NAM = PermissibleValue(
        text="NAM",
        description="Alpha3 code for Namibia.")
    NRU = PermissibleValue(
        text="NRU",
        description="Alpha3 code for Nauru.")
    NPL = PermissibleValue(
        text="NPL",
        description="Alpha3 code for Nepal.")
    NLD = PermissibleValue(
        text="NLD",
        description="Alpha3 code for Netherlands (the).")
    NCL = PermissibleValue(
        text="NCL",
        description="Alpha3 code for New Caledonia.")
    NZL = PermissibleValue(
        text="NZL",
        description="Alpha3 code for New Zealand.")
    NIC = PermissibleValue(
        text="NIC",
        description="Alpha3 code for Nicaragua.")
    NER = PermissibleValue(
        text="NER",
        description="Alpha3 code for Niger (the).")
    NGA = PermissibleValue(
        text="NGA",
        description="Alpha3 code for Nigeria.")
    NIU = PermissibleValue(
        text="NIU",
        description="Alpha3 code for Niue.")
    NFK = PermissibleValue(
        text="NFK",
        description="Alpha3 code for Norfolk Island.")
    MNP = PermissibleValue(
        text="MNP",
        description="Alpha3 code for Northern Mariana Islands (the).")
    NOR = PermissibleValue(
        text="NOR",
        description="Alpha3 code for Norway.")
    OMN = PermissibleValue(
        text="OMN",
        description="Alpha3 code for Oman.")
    PAK = PermissibleValue(
        text="PAK",
        description="Alpha3 code for Pakistan.")
    PLW = PermissibleValue(
        text="PLW",
        description="Alpha3 code for Palau.")
    PSE = PermissibleValue(
        text="PSE",
        description="Alpha3 code for Palestine, State of.")
    PAN = PermissibleValue(
        text="PAN",
        description="Alpha3 code for Panama.")
    PNG = PermissibleValue(
        text="PNG",
        description="Alpha3 code for Papua New Guinea.")
    PRY = PermissibleValue(
        text="PRY",
        description="Alpha3 code for Paraguay.")
    PER = PermissibleValue(
        text="PER",
        description="Alpha3 code for Peru.")
    PHL = PermissibleValue(
        text="PHL",
        description="Alpha3 code for Philippines (the).")
    PCN = PermissibleValue(
        text="PCN",
        description="Alpha3 code forPitcairn.")
    POL = PermissibleValue(
        text="POL",
        description="Alpha3 code for Poland.")
    PRT = PermissibleValue(
        text="PRT",
        description="Alpha3 code for Portugal.")
    PRI = PermissibleValue(
        text="PRI",
        description="Alpha3 code for Puerto Rico.")
    QAT = PermissibleValue(
        text="QAT",
        description="Alpha3 code for Qatar.")
    SRB = PermissibleValue(
        text="SRB",
        description="Alpha3 code for Serbia.")
    REU = PermissibleValue(
        text="REU",
        description="Alpha3 code for Reunion.")
    ROU = PermissibleValue(
        text="ROU",
        description="Alpha3 code for Romania.")
    RUS = PermissibleValue(
        text="RUS",
        description="Alpha3 code for Russian Federation (the).")
    RWA = PermissibleValue(
        text="RWA",
        description="Alpha3 code for Rwanda.")
    BLM = PermissibleValue(
        text="BLM",
        description="Alpha3 code for Saint Barthelemy.")
    SHN = PermissibleValue(
        text="SHN",
        description="Alpha3 code for Saint Helena, Ascension and Tristan da Cunha.")
    KNA = PermissibleValue(
        text="KNA",
        description="Alpha3 code for Saint Kitts and Nevis.")
    LCA = PermissibleValue(
        text="LCA",
        description="Alpha3 code for Saint Lucia.")
    MAF = PermissibleValue(
        text="MAF",
        description="Alpha3 code for Saint Martin (French part).")
    SPM = PermissibleValue(
        text="SPM",
        description="Alpha3 code for Saint Pierre and Miquelon.")
    VCT = PermissibleValue(
        text="VCT",
        description="Alpha3 code for Saint Vincent and the Grenadines.")
    WSM = PermissibleValue(
        text="WSM",
        description="Alpha3 code for Samoa.")
    SMR = PermissibleValue(
        text="SMR",
        description="Alpha3 code for San Marino.")
    STP = PermissibleValue(
        text="STP",
        description="Alpha3 code for Sao Tome and Principe.")
    SAU = PermissibleValue(
        text="SAU",
        description="Alpha3 code for Saudi Arabia.")
    SEN = PermissibleValue(
        text="SEN",
        description="Alpha3 code for Senegal.")
    SYC = PermissibleValue(
        text="SYC",
        description="Alpha3 code for Seychelles.")
    SLE = PermissibleValue(
        text="SLE",
        description="Alpha3 code for Sierra Leone.")
    SGP = PermissibleValue(
        text="SGP",
        description="Alpha3 code for Singapore.")
    SXM = PermissibleValue(
        text="SXM",
        description="Alpha3 code for Sint Maarten (Dutch part).")
    SVK = PermissibleValue(
        text="SVK",
        description="Alpha3 code for Slovakia.")
    SVN = PermissibleValue(
        text="SVN",
        description="Alpha3 code for Slovenia.")
    SLB = PermissibleValue(
        text="SLB",
        description="Alpha3 code for Solomon Islands.")
    SOM = PermissibleValue(
        text="SOM",
        description="Alpha3 code for Somalia.")
    ZAF = PermissibleValue(
        text="ZAF",
        description="Alpha3 code for South Africa.")
    SGS = PermissibleValue(
        text="SGS",
        description="Alpha3 code for South Georgia and the South Sandwich Islands.")
    SSD = PermissibleValue(
        text="SSD",
        description="Alpha3 code for South Sudan.")
    ESP = PermissibleValue(
        text="ESP",
        description="Alpha3 code for Spain.")
    LKA = PermissibleValue(
        text="LKA",
        description="Alpha3 code for Sri Lanka.")
    SDN = PermissibleValue(
        text="SDN",
        description="Alpha3 code for Sudan (the).")
    SUR = PermissibleValue(
        text="SUR",
        description="Alpha3 code for Suriname.")
    SJM = PermissibleValue(
        text="SJM",
        description="Alpha3 code for Svalbard and Jan Mayen.")
    SWZ = PermissibleValue(
        text="SWZ",
        description="Alpha3 code for Eswatini.")
    SWE = PermissibleValue(
        text="SWE",
        description="Alpha3 code for Sweden.")
    CHE = PermissibleValue(
        text="CHE",
        description="Alpha3 code for Switzerland.")
    SYR = PermissibleValue(
        text="SYR",
        description="Alpha3 code for Syrian Arab Republic.")
    TWN = PermissibleValue(
        text="TWN",
        description="Alpha3 code for Taiwan (Province of China).")
    TJK = PermissibleValue(
        text="TJK",
        description="Alpha3 code for Tajikistan.")
    TZA = PermissibleValue(
        text="TZA",
        description="Alpha3 code for Tanzania, United Republic of.")
    THA = PermissibleValue(
        text="THA",
        description="Alpha3 code for Thailand.")
    TLS = PermissibleValue(
        text="TLS",
        description="Alpha3 code for Timor-Leste.")
    TGO = PermissibleValue(
        text="TGO",
        description="Alpha3 code for Togo.")
    TKL = PermissibleValue(
        text="TKL",
        description="Alpha3 code for Tokelau.")
    TON = PermissibleValue(
        text="TON",
        description="Alpha3 code for Tonga.")
    TTO = PermissibleValue(
        text="TTO",
        description="Alpha3 code for Trinidad and Tobago.")
    TUN = PermissibleValue(
        text="TUN",
        description="Alpha3 code for Tunisia.")
    TUR = PermissibleValue(
        text="TUR",
        description="Alpha3 code for Turkey.")
    XTX = PermissibleValue(
        text="XTX",
        description="Alpha3 code for Turkish Republic of northern Cyprus.")
    TKM = PermissibleValue(
        text="TKM",
        description="Alpha3 code for Turkmenistan.")
    TCA = PermissibleValue(
        text="TCA",
        description="Alpha3 code for Turks and Caicos Islands (the).")
    TUV = PermissibleValue(
        text="TUV",
        description="Alpha3 code for Tuvalu.")
    UGA = PermissibleValue(
        text="UGA",
        description="Alpha3 code for Uganda.")
    UKR = PermissibleValue(
        text="UKR",
        description="Alpha3 code for Ukraine.")
    ARE = PermissibleValue(
        text="ARE",
        description="Alpha3 code for United Arab Emirates (the).")
    GBR = PermissibleValue(
        text="GBR",
        description="Alpha3 code for United Kingdom of Great Britain and Northern Ireland (the).")
    USA = PermissibleValue(
        text="USA",
        description="Alpha3 code for United States of America (the).")
    UMI = PermissibleValue(
        text="UMI",
        description="Alpha3 code for United States Minor Outlying Islands (the).")
    URY = PermissibleValue(
        text="URY",
        description="Alpha3 code for Uruguay.")
    UZB = PermissibleValue(
        text="UZB",
        description="Alpha3 code for Uzbekistan.")
    VUT = PermissibleValue(
        text="VUT",
        description="Alpha3 code for Vanuatu.")
    VEN = PermissibleValue(
        text="VEN",
        description="Alpha3 code for Venezuela (Bolivarian Republic of).")
    VNM = PermissibleValue(
        text="VNM",
        description="Alpha3 code for Viet Nam.")
    VGB = PermissibleValue(
        text="VGB",
        description="Alpha3 code for Virgin Islands (British).")
    VIR = PermissibleValue(
        text="VIR",
        description="Alpha3 code for Virgin Islands (U.S.).")
    WLF = PermissibleValue(
        text="WLF",
        description="Alpha3 code for Wallis and Futuna.")
    ESH = PermissibleValue(
        text="ESH",
        description="Alpha3 code for Western Sahara.")
    YEM = PermissibleValue(
        text="YEM",
        description="Alpha3 code for Yemen.")
    ZMB = PermissibleValue(
        text="ZMB",
        description="Alpha3 code for Zambia.")
    ZWE = PermissibleValue(
        text="ZWE",
        description="Alpha3 code for Zimbabwe.")
    XKX = PermissibleValue(
        text="XKX",
        description="Alpha3 code for Kosovo.")

    _defn = EnumDefinition(
        name="CountryNameAlpha3",
    )

class CountryNameNumeric(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CountryNameNumeric",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "4",
            PermissibleValue(
                text="4",
                description="Numeric code for Afghanistan."))
        setattr(cls, "818",
            PermissibleValue(
                text="818",
                description="Numeric code for Egypt."))
        setattr(cls, "248",
            PermissibleValue(
                text="248",
                description="Numeric code for Aland Islands."))
        setattr(cls, "008",
            PermissibleValue(
                text="008",
                description="Numeric code for Albania."))
        setattr(cls, "10",
            PermissibleValue(
                text="10",
                description="Numeric code for Algeria."))
        setattr(cls, "850",
            PermissibleValue(
                text="850",
                description="Numeric code for Virgin Islands (U.S.)."))
        setattr(cls, "581",
            PermissibleValue(
                text="581",
                description="Numeric code for United States Minor Outlying Islands (the)."))
        setattr(cls, "14",
            PermissibleValue(
                text="14",
                description="Numeric code for American Samoa."))
        setattr(cls, "16",
            PermissibleValue(
                text="16",
                description="Numeric code for Andorra."))
        setattr(cls, "20",
            PermissibleValue(
                text="20",
                description="Numeric code for Angola."))
        setattr(cls, "660",
            PermissibleValue(
                text="660",
                description="Numeric code for Anguilla."))
        setattr(cls, "8",
            PermissibleValue(
                text="8",
                description="Numeric code for Antarctica."))
        setattr(cls, "028",
            PermissibleValue(
                text="028",
                description="Numeric code for Antigua and Barbuda."))
        setattr(cls, "226",
            PermissibleValue(
                text="226",
                description="Numeric code for Equatorial Guinea."))
        setattr(cls, "760",
            PermissibleValue(
                text="760",
                description="Numeric code for Syrian Arab Republic."))
        setattr(cls, "26",
            PermissibleValue(
                text="26",
                description="Numeric code for Argentina."))
        setattr(cls, "41",
            PermissibleValue(
                text="41",
                description="Numeric code for Armenia."))
        setattr(cls, "231",
            PermissibleValue(
                text="231",
                description="Numeric code for Ethiopia."))
        setattr(cls, "30",
            PermissibleValue(
                text="30",
                description="Numeric code for Australia."))
        setattr(cls, "36",
            PermissibleValue(
                text="36",
                description="Numeric code for Bahamas (the)."))
        setattr(cls, "048",
            PermissibleValue(
                text="048",
                description="Numeric code for Bahrain."))
        setattr(cls, "40",
            PermissibleValue(
                text="40",
                description="Numeric code for Bangladesh."))
        setattr(cls, "42",
            PermissibleValue(
                text="42",
                description="Numeric code for Barbados."))
        setattr(cls, "46",
            PermissibleValue(
                text="46",
                description="Numeric code forBelgium."))
        setattr(cls, "084",
            PermissibleValue(
                text="084",
                description="Numeric code for Belize."))
        setattr(cls, "204",
            PermissibleValue(
                text="204",
                description="Numeric code for Benin."))
        setattr(cls, "48",
            PermissibleValue(
                text="48",
                description="Numeric code for Bermuda."))
        setattr(cls, "52",
            PermissibleValue(
                text="52",
                description="Numeric code for Bhutan."))
        setattr(cls, "58",
            PermissibleValue(
                text="58",
                description="Numeric code for Botswana."))
        setattr(cls, "60",
            PermissibleValue(
                text="60",
                description="Numeric code for Bouvet Island."))
        setattr(cls, "62",
            PermissibleValue(
                text="62",
                description="Numeric code for Brazil."))
        setattr(cls, "092",
            PermissibleValue(
                text="092",
                description="Numeric code for Virgin Islands (British)."))
        setattr(cls, "086",
            PermissibleValue(
                text="086",
                description="Numeric code for British Indian Ocean Territory (the)."))
        setattr(cls, "854",
            PermissibleValue(
                text="854",
                description="Numeric code for Burkina Faso."))
        setattr(cls, "108",
            PermissibleValue(
                text="108",
                description="Numeric code for Burundi."))
        setattr(cls, "132",
            PermissibleValue(
                text="132",
                description="Numeric code for Cabo Verde."))
        setattr(cls, "152",
            PermissibleValue(
                text="152",
                description="Numeric code for Chile."))
        setattr(cls, "156",
            PermissibleValue(
                text="156",
                description="Numeric code for China."))
        setattr(cls, "184",
            PermissibleValue(
                text="184",
                description="Numeric code for Cook Islands (the)."))
        setattr(cls, "188",
            PermissibleValue(
                text="188",
                description="Numeric code for Costa Rica."))
        setattr(cls, "384",
            PermissibleValue(
                text="384",
                description="Numeric code for Cote dIvoire."))
        setattr(cls, "531",
            PermissibleValue(
                text="531",
                description="Numeric code for Curacao."))
        setattr(cls, "208",
            PermissibleValue(
                text="208",
                description="Numeric code for Denmark."))
        setattr(cls, "180",
            PermissibleValue(
                text="180",
                description="Numeric code for Congo (the Democratic Republic of the)."))
        setattr(cls, "408",
            PermissibleValue(
                text="408",
                description="Numeric code for Korea (the Democratic Peoples Republic of)."))
        setattr(cls, "418",
            PermissibleValue(
                text="418",
                description="Numeric code for Lao Peoples Democratic Republic (the)."))
        setattr(cls, "276",
            PermissibleValue(
                text="276",
                description="Numeric code for Germany."))
        setattr(cls, "212",
            PermissibleValue(
                text="212",
                description="Numeric code for Dominica."))
        setattr(cls, "214",
            PermissibleValue(
                text="214",
                description="Numeric code for Dominican Republic (the)."))
        setattr(cls, "262",
            PermissibleValue(
                text="262",
                description="Numeric code for Djibouti."))
        setattr(cls, "218",
            PermissibleValue(
                text="218",
                description="Numeric code for Ecuador."))
        setattr(cls, "807",
            PermissibleValue(
                text="807",
                description="Numeric code for Republic of North Macedonia."))
        setattr(cls, "222",
            PermissibleValue(
                text="222",
                description="Numeric code for El Salvador."))
        setattr(cls, "232",
            PermissibleValue(
                text="232",
                description="Numeric code for Eritrea."))
        setattr(cls, "233",
            PermissibleValue(
                text="233",
                description="Numeric code for Estonia."))
        setattr(cls, "238",
            PermissibleValue(
                text="238",
                description="Numeric code for Falkland Islands (the) [Malvinas]."))
        setattr(cls, "234",
            PermissibleValue(
                text="234",
                description="Numeric code for Faroe Islands (the)."))
        setattr(cls, "242",
            PermissibleValue(
                text="242",
                description="Numeric code for Fiji."))
        setattr(cls, "246",
            PermissibleValue(
                text="246",
                description="Numeric code for Finland."))
        setattr(cls, "583",
            PermissibleValue(
                text="583",
                description="Numeric code for Micronesia (Federated States of)."))
        setattr(cls, "250",
            PermissibleValue(
                text="250",
                description="Numeric code for France."))
        setattr(cls, "260",
            PermissibleValue(
                text="260",
                description="Numeric code for French Southern Territories (the)."))
        setattr(cls, "254",
            PermissibleValue(
                text="254",
                description="Numeric code for French Guiana."))
        setattr(cls, "258",
            PermissibleValue(
                text="258",
                description="Numeric code for French Polynesia."))
        setattr(cls, "266",
            PermissibleValue(
                text="266",
                description="Numeric code for Gabon."))
        setattr(cls, "270",
            PermissibleValue(
                text="270",
                description="Numeric code for Gambia (the)."))
        setattr(cls, "268",
            PermissibleValue(
                text="268",
                description="Numeric code for Georgia."))
        setattr(cls, "288",
            PermissibleValue(
                text="288",
                description="Numeric code for Ghana."))
        setattr(cls, "292",
            PermissibleValue(
                text="292",
                description="Numeric code for Gibraltar."))
        setattr(cls, "308",
            PermissibleValue(
                text="308",
                description="Numeric code for Grenada."))
        setattr(cls, "300",
            PermissibleValue(
                text="300",
                description="Numeric code for Greece."))
        setattr(cls, "304",
            PermissibleValue(
                text="304",
                description="Numeric code for Greenland."))
        setattr(cls, "312",
            PermissibleValue(
                text="312",
                description="Numeric code for Guadeloupe."))
        setattr(cls, "316",
            PermissibleValue(
                text="316",
                description="Numeric code for Guam."))
        setattr(cls, "320",
            PermissibleValue(
                text="320",
                description="Numeric code for Guatemala."))
        setattr(cls, "831",
            PermissibleValue(
                text="831",
                description="Numeric code for Guernsey."))
        setattr(cls, "324",
            PermissibleValue(
                text="324",
                description="Numeric code for Guinea."))
        setattr(cls, "624",
            PermissibleValue(
                text="624",
                description="Numeric code for Guinea-Bissau."))
        setattr(cls, "328",
            PermissibleValue(
                text="328",
                description="Numeric code for Guyana."))
        setattr(cls, "332",
            PermissibleValue(
                text="332",
                description="Numeric code for Haiti."))
        setattr(cls, "334",
            PermissibleValue(
                text="334",
                description="Numeric code for Heard Island and McDonald Islands."))
        setattr(cls, "340",
            PermissibleValue(
                text="340",
                description="Numeric code for Honduras."))
        setattr(cls, "344",
            PermissibleValue(
                text="344",
                description="Numeric code for Hong Kong."))
        setattr(cls, "356",
            PermissibleValue(
                text="356",
                description="Numeric code for India."))
        setattr(cls, "360",
            PermissibleValue(
                text="360",
                description="Numeric code for Indonesia."))
        setattr(cls, "833",
            PermissibleValue(
                text="833",
                description="Numeric code for Isle of Man."))
        setattr(cls, "368",
            PermissibleValue(
                text="368",
                description="Numeric code for Iraq."))
        setattr(cls, "372",
            PermissibleValue(
                text="372",
                description="Numeric code for Ireland."))
        setattr(cls, "364",
            PermissibleValue(
                text="364",
                description="Numeric code for Iran (Islamic Republic of)."))
        setattr(cls, "352",
            PermissibleValue(
                text="352",
                description="Numeric code for Iceland."))
        setattr(cls, "376",
            PermissibleValue(
                text="376",
                description="Numeric code for Israel."))
        setattr(cls, "380",
            PermissibleValue(
                text="380",
                description="Numeric code for Italy."))
        setattr(cls, "388",
            PermissibleValue(
                text="388",
                description="Numeric code for Jamaica."))
        setattr(cls, "392",
            PermissibleValue(
                text="392",
                description="Numeric code for Japan."))
        setattr(cls, "887",
            PermissibleValue(
                text="887",
                description="Numeric code for Yemen."))
        setattr(cls, "832",
            PermissibleValue(
                text="832",
                description="Numeric code for Jersey."))
        setattr(cls, "400",
            PermissibleValue(
                text="400",
                description="Numeric code for Jordan."))
        setattr(cls, "136",
            PermissibleValue(
                text="136",
                description="Numeric code for Cayman Islands (the)."))
        setattr(cls, "116",
            PermissibleValue(
                text="116",
                description="Numeric code for Cambodia."))
        setattr(cls, "120",
            PermissibleValue(
                text="120",
                description="Numeric code for Cameroon."))
        setattr(cls, "124",
            PermissibleValue(
                text="124",
                description="Numeric code for Canada."))
        setattr(cls, "398",
            PermissibleValue(
                text="398",
                description="Numeric code for Kazakhstan."))
        setattr(cls, "634",
            PermissibleValue(
                text="634",
                description="Numeric code for Qatar."))
        setattr(cls, "404",
            PermissibleValue(
                text="404",
                description="Numeric code for Kenya."))
        setattr(cls, "417",
            PermissibleValue(
                text="417",
                description="Numeric code for Kyrgyzstan."))
        setattr(cls, "296",
            PermissibleValue(
                text="296",
                description="Numeric code for Kiribati."))
        setattr(cls, "166",
            PermissibleValue(
                text="166",
                description="Numeric code for Cocos (Keeling) Islands (the)."))
        setattr(cls, "170",
            PermissibleValue(
                text="170",
                description="Numeric code for Colombia."))
        setattr(cls, "174",
            PermissibleValue(
                text="174",
                description="Numeric code for Comoros (the)."))
        setattr(cls, "178",
            PermissibleValue(
                text="178",
                description="Numeric code for Congo (the)."))
        setattr(cls, "191",
            PermissibleValue(
                text="191",
                description="Numeric code for Croatia."))
        setattr(cls, "192",
            PermissibleValue(
                text="192",
                description="Numeric code for Cuba."))
        setattr(cls, "414",
            PermissibleValue(
                text="414",
                description="Numeric code for Kuwait."))
        setattr(cls, "426",
            PermissibleValue(
                text="426",
                description="Numeric code for Lesotho."))
        setattr(cls, "428",
            PermissibleValue(
                text="428",
                description="Numeric code for Latvia."))
        setattr(cls, "422",
            PermissibleValue(
                text="422",
                description="Numeric code for Lebanon."))
        setattr(cls, "430",
            PermissibleValue(
                text="430",
                description="Numeric code for Liberia."))
        setattr(cls, "434",
            PermissibleValue(
                text="434",
                description="Numeric code for Libya."))
        setattr(cls, "438",
            PermissibleValue(
                text="438",
                description="Numeric code for Liechtenstein."))
        setattr(cls, "440",
            PermissibleValue(
                text="440",
                description="Numeric code for Lithuania."))
        setattr(cls, "442",
            PermissibleValue(
                text="442",
                description="Numeric code for Luxembourg."))
        setattr(cls, "446",
            PermissibleValue(
                text="446",
                description="Numeric code for Macao."))
        setattr(cls, "450",
            PermissibleValue(
                text="450",
                description="Numeric code for Madagascar."))
        setattr(cls, "454",
            PermissibleValue(
                text="454",
                description="Numeric code for Malawi."))
        setattr(cls, "458",
            PermissibleValue(
                text="458",
                description="Numeric code for Malaysia."))
        setattr(cls, "462",
            PermissibleValue(
                text="462",
                description="Numeric code for Maldives."))
        setattr(cls, "466",
            PermissibleValue(
                text="466",
                description="Numeric code for Mali."))
        setattr(cls, "470",
            PermissibleValue(
                text="470",
                description="Numeric code for Malta    ."))
        setattr(cls, "580",
            PermissibleValue(
                text="580",
                description="Numeric code for Northern Mariana Islands (the)."))
        setattr(cls, "504",
            PermissibleValue(
                text="504",
                description="Numeric code for Morocco."))
        setattr(cls, "584",
            PermissibleValue(
                text="584",
                description="Numeric code for Marshall Islands (the)."))
        setattr(cls, "474",
            PermissibleValue(
                text="474",
                description="Numeric code for Martinique."))
        setattr(cls, "478",
            PermissibleValue(
                text="478",
                description="Numeric code for Mauritania."))
        setattr(cls, "480",
            PermissibleValue(
                text="480",
                description="Numeric code for Mauritius."))
        setattr(cls, "175",
            PermissibleValue(
                text="175",
                description="Numeric code for Mayotte."))
        setattr(cls, "484",
            PermissibleValue(
                text="484",
                description="Numeric code for Mexico."))
        setattr(cls, "492",
            PermissibleValue(
                text="492",
                description="Numeric code for Monaco."))
        setattr(cls, "496",
            PermissibleValue(
                text="496",
                description="Numeric code for Mongolia."))
        setattr(cls, "500",
            PermissibleValue(
                text="500",
                description="Numeric code for Montserrat."))
        setattr(cls, "499",
            PermissibleValue(
                text="499",
                description="Numeric code for Montenegro."))
        setattr(cls, "508",
            PermissibleValue(
                text="508",
                description="Numeric code for Mozambique."))
        setattr(cls, "104",
            PermissibleValue(
                text="104",
                description="Numeric code for Myanmar."))
        setattr(cls, "516",
            PermissibleValue(
                text="516",
                description="Numeric code for Namibia."))
        setattr(cls, "520",
            PermissibleValue(
                text="520",
                description="Numeric code for Nauru."))
        setattr(cls, "524",
            PermissibleValue(
                text="524",
                description="Numeric code for Nepal."))
        setattr(cls, "540",
            PermissibleValue(
                text="540",
                description="Numeric code for New Caledonia."))
        setattr(cls, "554",
            PermissibleValue(
                text="554",
                description="Numeric code for New Zealand."))
        setattr(cls, "558",
            PermissibleValue(
                text="558",
                description="Numeric code for Nicaragua."))
        setattr(cls, "528",
            PermissibleValue(
                text="528",
                description="Numeric code for Netherlands (the)."))
        setattr(cls, "562",
            PermissibleValue(
                text="562",
                description="Numeric code for Niger (the)."))
        setattr(cls, "566",
            PermissibleValue(
                text="566",
                description="Numeric code for Nigeria."))
        setattr(cls, "570",
            PermissibleValue(
                text="570",
                description="Numeric code for Niue."))
        setattr(cls, "574",
            PermissibleValue(
                text="574",
                description="Numeric code for Norfolk Island."))
        setattr(cls, "578",
            PermissibleValue(
                text="578",
                description="Numeric code for Norway."))
        setattr(cls, "512",
            PermissibleValue(
                text="512",
                description="Numeric code for Oman."))
        setattr(cls, "32",
            PermissibleValue(
                text="32",
                description="Numeric code for Austria."))
        setattr(cls, "586",
            PermissibleValue(
                text="586",
                description="Numeric code for Pakistan."))
        setattr(cls, "585",
            PermissibleValue(
                text="585",
                description="Numeric code for Palau."))
        setattr(cls, "275",
            PermissibleValue(
                text="275",
                description="Numeric code for Palestine, State of."))
        setattr(cls, "591",
            PermissibleValue(
                text="591",
                description="Numeric code for Panama."))
        setattr(cls, "598",
            PermissibleValue(
                text="598",
                description="Numeric code for Papua New Guinea."))
        setattr(cls, "600",
            PermissibleValue(
                text="600",
                description="Numeric code for Paraguay."))
        setattr(cls, "604",
            PermissibleValue(
                text="604",
                description="Numeric code for Peru."))
        setattr(cls, "608",
            PermissibleValue(
                text="608",
                description="Numeric code for Philippines (the)."))
        setattr(cls, "612",
            PermissibleValue(
                text="612",
                description="Numeric code for Pitcairn."))
        setattr(cls, "068",
            PermissibleValue(
                text="068",
                description="Numeric code for Bolivia (Plurinational State of)."))
        setattr(cls, "616",
            PermissibleValue(
                text="616",
                description="Numeric code for Poland."))
        setattr(cls, "620",
            PermissibleValue(
                text="620",
                description="Numeric code for Portugal."))
        setattr(cls, "630",
            PermissibleValue(
                text="630",
                description="Numeric code for Puerto Rico."))
        setattr(cls, "410",
            PermissibleValue(
                text="410",
                description="Numeric code for Korea (the Republic of)."))
        setattr(cls, "498",
            PermissibleValue(
                text="498",
                description="Numeric code for Moldova (the Republic of)."))
        setattr(cls, "638",
            PermissibleValue(
                text="638",
                description="Numeric code for Reunion."))
        setattr(cls, "646",
            PermissibleValue(
                text="646",
                description="Numeric code for Rwanda."))
        setattr(cls, "642",
            PermissibleValue(
                text="642",
                description="Numeric code for Romania."))
        setattr(cls, "643",
            PermissibleValue(
                text="643",
                description="Numeric code for Russian Federation (the)."))
        setattr(cls, "090",
            PermissibleValue(
                text="090",
                description="Numeric code for Solomon Islands."))
        setattr(cls, "894",
            PermissibleValue(
                text="894",
                description="Numeric code for Zambia."))
        setattr(cls, "882",
            PermissibleValue(
                text="882",
                description="Numeric code for Samoa."))
        setattr(cls, "674",
            PermissibleValue(
                text="674",
                description="Numeric code for San Marino."))
        setattr(cls, "678",
            PermissibleValue(
                text="678",
                description="Numeric code for Sao Tome and Principe."))
        setattr(cls, "682",
            PermissibleValue(
                text="682",
                description="Numeric code for Saudi Arabia."))
        setattr(cls, "752",
            PermissibleValue(
                text="752",
                description="Numeric code for Sweden."))
        setattr(cls, "756",
            PermissibleValue(
                text="756",
                description="Numeric code for Switzerland."))
        setattr(cls, "686",
            PermissibleValue(
                text="686",
                description="Numeric code for Senegal."))
        setattr(cls, "688",
            PermissibleValue(
                text="688",
                description="Numeric code for Serbia."))
        setattr(cls, "690",
            PermissibleValue(
                text="690",
                description="Numeric code for Seychelles."))
        setattr(cls, "694",
            PermissibleValue(
                text="694",
                description="Numeric code for Sierra Leone."))
        setattr(cls, "716",
            PermissibleValue(
                text="716",
                description="Numeric code for Zimbabwe."))
        setattr(cls, "702",
            PermissibleValue(
                text="702",
                description="Numeric code for Singapore."))
        setattr(cls, "703",
            PermissibleValue(
                text="703",
                description="Numeric code for Slovakia."))
        setattr(cls, "705",
            PermissibleValue(
                text="705",
                description="Numeric code for Slovenia."))
        setattr(cls, "706",
            PermissibleValue(
                text="706",
                description="Numeric code for Somalia."))
        setattr(cls, "724",
            PermissibleValue(
                text="724",
                description="Numeric code for Spain."))
        setattr(cls, "144",
            PermissibleValue(
                text="144",
                description="Numeric code for Sri Lanka."))
        setattr(cls, "652",
            PermissibleValue(
                text="652",
                description="Numeric code for Saint Barthelemy."))
        setattr(cls, "654",
            PermissibleValue(
                text="654",
                description="Numeric code for Saint Helena, Ascension and Tristan da Cunha."))
        setattr(cls, "659",
            PermissibleValue(
                text="659",
                description="Numeric code for Saint Kitts and Nevis."))
        setattr(cls, "662",
            PermissibleValue(
                text="662",
                description="Numeric code for Saint Lucia."))
        setattr(cls, "663",
            PermissibleValue(
                text="663",
                description="Numeric code for Saint Martin (French part)."))
        setattr(cls, "534",
            PermissibleValue(
                text="534",
                description="Numeric code for Sint Maarten (Dutch part)."))
        setattr(cls, "666",
            PermissibleValue(
                text="666",
                description="Numeric code for Saint Pierre and Miquelon."))
        setattr(cls, "670",
            PermissibleValue(
                text="670",
                description="Numeric code for Saint Vincent and the Grenadines."))
        setattr(cls, "710",
            PermissibleValue(
                text="710",
                description="Numeric code for South Africa."))
        setattr(cls, "729",
            PermissibleValue(
                text="729",
                description="Numeric code forSudan (the)."))
        setattr(cls, "239",
            PermissibleValue(
                text="239",
                description="Numeric code for South Georgia and the South Sandwich Islands."))
        setattr(cls, "728",
            PermissibleValue(
                text="728",
                description="Numeric code for South Sudan."))
        setattr(cls, "740",
            PermissibleValue(
                text="740",
                description="Numeric code for Suriname."))
        setattr(cls, "744",
            PermissibleValue(
                text="744",
                description="Numeric code for Svalbard and Jan Mayen."))
        setattr(cls, "748",
            PermissibleValue(
                text="748",
                description="Numeric code for Eswatini."))
        setattr(cls, "762",
            PermissibleValue(
                text="762",
                description="Numeric code for Tajikistan."))
        setattr(cls, "158",
            PermissibleValue(
                text="158",
                description="Numeric code for Taiwan (Province of China)."))
        setattr(cls, "764",
            PermissibleValue(
                text="764",
                description="Numeric code for Thailand."))
        setattr(cls, "626",
            PermissibleValue(
                text="626",
                description="Numeric code for Timor-Leste."))
        setattr(cls, "768",
            PermissibleValue(
                text="768",
                description="Numeric code for Togo."))
        setattr(cls, "772",
            PermissibleValue(
                text="772",
                description="Numeric code for Tokelau."))
        setattr(cls, "776",
            PermissibleValue(
                text="776",
                description="Numeric code for Tonga."))
        setattr(cls, "780",
            PermissibleValue(
                text="780",
                description="Numeric code for Trinidad and Tobago."))
        setattr(cls, "148",
            PermissibleValue(
                text="148",
                description="Numeric code for Chad."))
        setattr(cls, "203",
            PermissibleValue(
                text="203",
                description="Numeric code for Czechia."))
        setattr(cls, "788",
            PermissibleValue(
                text="788",
                description="Numeric code for Tunisia."))
        setattr(cls, "792",
            PermissibleValue(
                text="792",
                description="Numeric code for Turkey."))
        setattr(cls, "795",
            PermissibleValue(
                text="795",
                description="Numeric code for Turkmenistan."))
        setattr(cls, "796",
            PermissibleValue(
                text="796",
                description="Numeric code for Turks and Caicos Islands (the)."))
        setattr(cls, "798",
            PermissibleValue(
                text="798",
                description="Numeric code for Tuvalu."))
        setattr(cls, "800",
            PermissibleValue(
                text="800",
                description="Numeric code for Uganda."))
        setattr(cls, "804",
            PermissibleValue(
                text="804",
                description="Numeric code for Ukraine."))
        setattr(cls, "348",
            PermissibleValue(
                text="348",
                description="Numeric code for Hungary."))
        setattr(cls, "858",
            PermissibleValue(
                text="858",
                description="Numeric code for Uruguay."))
        setattr(cls, "860",
            PermissibleValue(
                text="860",
                description="Numeric code for Uzbekistan."))
        setattr(cls, "548",
            PermissibleValue(
                text="548",
                description="Numeric code for Vanuatu."))
        setattr(cls, "336",
            PermissibleValue(
                text="336",
                description="Numeric code for Holy See (the)."))
        setattr(cls, "784",
            PermissibleValue(
                text="784",
                description="Numeric code for United Arab Emirates (the)."))
        setattr(cls, "834",
            PermissibleValue(
                text="834",
                description="Numeric code for Tanzania, United Republic of."))
        setattr(cls, "840",
            PermissibleValue(
                text="840",
                description="Numeric code for United States of America (the)."))
        setattr(cls, "826",
            PermissibleValue(
                text="826",
                description="Numeric code for United Kingdom of Great Britain and Northern Ireland (the)."))
        setattr(cls, "704",
            PermissibleValue(
                text="704",
                description="Numeric code for Viet Nam."))
        setattr(cls, "876",
            PermissibleValue(
                text="876",
                description="Numeric code for Wallis and Futuna."))
        setattr(cls, "162",
            PermissibleValue(
                text="162",
                description="Numeric code for Christmas Island."))
        setattr(cls, "112",
            PermissibleValue(
                text="112",
                description="Numeric code for Belarus."))
        setattr(cls, "732",
            PermissibleValue(
                text="732",
                description="Numeric code for Western Sahara."))
        setattr(cls, "140",
            PermissibleValue(
                text="140",
                description="Numeric code for Central African Republic (the)."))
        setattr(cls, "196",
            PermissibleValue(
                text="196",
                description="Numeric code for Cyprus."))

class Architectures(EnumDefinitionImpl):

    Other = PermissibleValue(
        text="Other",
        description="CPU architecture not specified above.")

    _defn = EnumDefinition(
        name="Architectures",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "x86-32",
            PermissibleValue(
                text="x86-32",
                description="32 bit version of x86 architecture."))
        setattr(cls, "x86-64",
            PermissibleValue(
                text="x86-64",
                description="64 bit version of x86 architecture."))
        setattr(cls, "AArch-32",
            PermissibleValue(
                text="AArch-32",
                description="32-bit version of ARM architecture."))
        setattr(cls, "AArch-64",
            PermissibleValue(
                text="AArch-64",
                description="64-bit version of ARM architecture."))
        setattr(cls, "RISC-V",
            PermissibleValue(
                text="RISC-V",
                description="Architecture based on open standard instruction set (ISA)."))

class EncryptionAlgorithm(EnumDefinitionImpl):

    RSA = PermissibleValue(
        text="RSA",
        description="""Algorithm for encryption based on public key cryptography (asymmetric cryptography), which uses two keys (public and private) for encoding and sending messages and data.""")
    AES = PermissibleValue(
        text="AES",
        description="""(Advanced Encryption Standard) Algorithm for encryption based on symmetric cryptography (secret key cryptography) that works over group of bits of fixed length (blocks).""")
    Blowfish = PermissibleValue(
        text="Blowfish",
        description="""Symmetric-key block cipher algorithm for encryption that includes advanced functionalities aimed to improve DES algorithm.""")
    Twofish = PermissibleValue(
        text="Twofish",
        description="Evolution of the Symmetric-key block cipher Blowfish algorithm.")
    SDA = PermissibleValue(
        text="SDA",
        description="""(Static Data Authentication) is a digital signature scheme that works with asymmetric cryptography.""")
    other = PermissibleValue(
        text="other",
        description="Algorithm for encryption not further described.")

    _defn = EnumDefinition(
        name="EncryptionAlgorithm",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3DES",
            PermissibleValue(
                text="3DES",
                description="""(Triple Data Encryption Algorithm) Symmetric-key block cipher algorithm for encryption, which applies three times the DES (Data Encryption Standard) algorithm to each single data block."""))

class ChecksumAlgorithm(EnumDefinitionImpl):

    md5 = PermissibleValue(
        text="md5",
        description="""(Message Digest Method 5) Algorithm that generates a 128-bit digest, represented as 32-digit hexadecimal numbers, regardless the length of the input string.""")
    blake2 = PermissibleValue(
        text="blake2",
        description="""Improved version of the sha-3 algorithm Blake, optimized for 64-bit platforms, that generates digests of size between 1 and 64 bytes (Blake2b) or up to 32 bytes (Blake2s).""")
    blake3 = PermissibleValue(
        text="blake3",
        description="""Evolution of Bao and Blake2, although in contrast to these, doesn't offer different variants depending on the architectures, but just a single algorithm.""")
    other = PermissibleValue(
        text="other",
        description="Algorithm to calculate checksum not further described.")

    _defn = EnumDefinition(
        name="ChecksumAlgorithm",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sha-1",
            PermissibleValue(
                text="sha-1",
                description="""(Secure Hash Algorithm 1) Algorithm that generates a 160-bit digest, typically represented as 40-digit hexadecimal numbers, regardless the length of the input string."""))
        setattr(cls, "sha-256",
            PermissibleValue(
                text="sha-256",
                description="""Cryptographic algorithm that produces a fixed-length, 256-bit (32-byte) hash value. The input text should be less than 264 bits length. The algorithm is irreversible by design."""))
        setattr(cls, "sha-384",
            PermissibleValue(
                text="sha-384",
                description="""This variant converts text of any length into a fixed-size string. Each output produces a hash of 384 bits."""))
        setattr(cls, "sha-512",
            PermissibleValue(
                text="sha-512",
                description="""This variant converts text of any length into a fixed-size string. Each output produces a hash of 512 bits (64 bytes)."""))
        setattr(cls, "sha-3",
            PermissibleValue(
                text="sha-3",
                description="""Advanced version of the sha function, based on a sponge function approach, that generates an output bit stream of a desired length (56, 64, 96 or 128-digit hexadecimal numbers) depending of the sha-3 function version used."""))
        setattr(cls, "ripemd-160",
            PermissibleValue(
                text="ripemd-160",
                description="""RIPEMD-160 is a hash function from the RIPEMD (RIPE Message Digest) family that generates 160-bit hashes represented as 40-digit hexadecimal numbers."""))

class KeyManagement(EnumDefinitionImpl):

    BYOK = PermissibleValue(
        text="BYOK",
        description="bring-your-own-key: Keys created by user and stored in key manager of cloud")
    HYOK = PermissibleValue(
        text="HYOK",
        description="hold-your-own-key Key created by user and kept by user")
    managed = PermissibleValue(
        text="managed",
        description="managed: Keys are created by and stored in key manager of cloud.")

    _defn = EnumDefinition(
        name="KeyManagement",
    )

class SignatureAlgorithm(EnumDefinitionImpl):

    DSA = PermissibleValue(
        text="DSA",
        description="""DSA (Digital Signature Algorithm) is an asymmetric algorithm for signing information proposed by the NIST (National Institute of Standards and Technology).""")
    KCDSA = PermissibleValue(
        text="KCDSA",
        description="""(Korean Certificate-based Digital Signature Algorithm), created by the Korea Internet & Security Agency (KISA), is similar to the DSA algorithm and can produce and output from 128 to 256 bits, in 32-bit increments.""")
    Schnorr = PermissibleValue(
        text="Schnorr",
        description="""Similar to ECDSA scheme was described by Claus Schnorr, is a well-known algorithm due to its simplicity and efficiency that generates short signatures.""")
    ECDSA = PermissibleValue(
        text="ECDSA",
        description="""ECDSA (Elliptic Curve Digital Signature Algorithm) is an improved variant of the DSA algorithm which uses keys derived from elliptic curve cryptography.""")
    ECKDSA = PermissibleValue(
        text="ECKDSA",
        description="Elliptic Curve variant of the KCDSA algorithm.")
    ECGDSA = PermissibleValue(
        text="ECGDSA",
        description="(Elliptic Curve German Digital Signature Algorithm), variant of the ECDSA algorithm.")
    other = PermissibleValue(
        text="other",
        description="Algorithm for digital signatures not further described.")

    _defn = EnumDefinition(
        name="SignatureAlgorithm",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RSA-Signature",
            PermissibleValue(
                text="RSA-Signature",
                description="""RSA is a cryptographic system based on public key that can be used both for signing and encryption purposes."""))
        setattr(cls, "EC Schnorr",
            PermissibleValue(
                text="EC Schnorr",
                description="Elliptic Curve Based Schnorr signatura algorithm."))

class DiskType(EnumDefinitionImpl):

    other = PermissibleValue(
        text="other",
        description="Storage device no further described.")

    _defn = EnumDefinition(
        name="DiskType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "local HDD",
            PermissibleValue(
                text="local HDD",
                description="""A hard disk drive is a storage device that uses an electro-mechanical system to store and retrieve digital data."""))
        setattr(cls, "local SSD",
            PermissibleValue(
                text="local SSD",
                description="""A SDD hard disk is a storage device that relies on flash memory technology, integrated circuits and solid-state electronics to store data."""))
        setattr(cls, "magnetic hard drive",
            PermissibleValue(
                text="magnetic hard drive",
                description="""Storage device that uses rotating magnetic disks (platters) to read and write data into the hard drive."""))
        setattr(cls, "hybrid hard drive",
            PermissibleValue(
                text="hybrid hard drive",
                description="""Storage device that combines both platters and flash memory, so increases both storage capabilities and storage capacity."""))
        setattr(cls, "shared network storage",
            PermissibleValue(
                text="shared network storage",
                description="""The information is stored in a central resource that is accessible to multiple users or data systems."""))

class DiskBusType(EnumDefinitionImpl):

    SATA = PermissibleValue(
        text="SATA",
        description="""The SATA (Serial Advanced Technology Attachment) interface connects the storage device to the computer using serial signaling technology.""")
    PATA = PermissibleValue(
        text="PATA",
        description="""Based on parallel signaling technology, the Parallel Advanced Technology Attachment (also known as IDE) interface can be used in old systems, PATA cable is usually flat and features 40-pin connectors on each side.""")
    SCSI = PermissibleValue(
        text="SCSI",
        description="""Small Computer System Interface, uses a system interface that is a standard for connecting peripheral devices such as printers, scanners, and others.""")
    SAS = PermissibleValue(
        text="SAS",
        description="""The Serial Attached SCSI interface provides more performance than SCSI interfaces, and it is usually convenient for environments that require high-performance data transfer.""")
    NVMe = PermissibleValue(
        text="NVMe",
        description="""The Non-volatile Memory Express interface is designed to address tasks that require high-performance computing environments.""")
    other = PermissibleValue(
        text="other",
        description="Disk controller no further described.")

    _defn = EnumDefinition(
        name="DiskBusType",
    )

class GPUInterconnetionTypes(EnumDefinitionImpl):

    NVLink = PermissibleValue(text="NVLink")
    RoCE2 = PermissibleValue(text="RoCE2")
    other = PermissibleValue(text="other")
    none = PermissibleValue(text="none")

    _defn = EnumDefinition(
        name="GPUInterconnetionTypes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Xe Link",
            PermissibleValue(text="Xe Link"))
        setattr(cls, "Infinity Fabric",
            PermissibleValue(text="Infinity Fabric"))

class UpdateFrequency(EnumDefinitionImpl):
    """
    Possible values for image's update frequency.
    """
    yearly = PermissibleValue(
        text="yearly",
        description="Image will be updated at least once per year.")
    quarterly = PermissibleValue(
        text="quarterly",
        description="Image will be updated at least once per quarter.")
    monthly = PermissibleValue(
        text="monthly",
        description="Image will be updated at least once per month.")
    weekly = PermissibleValue(
        text="weekly",
        description="Image will be updated at least once per week.")
    daily = PermissibleValue(
        text="daily",
        description="Image will be updated at least once per day.")
    critical_bug = PermissibleValue(
        text="critical_bug",
        description="Image will be updated for critical bugs only.")
    never = PermissibleValue(
        text="never",
        description="Image will never be updated.")

    _defn = EnumDefinition(
        name="UpdateFrequency",
        description="Possible values for image's update frequency.",
    )

class Validity1(EnumDefinitionImpl):
    """
    Possible values for definition of image's validity after upgrading to a new version.
    """
    none = PermissibleValue(
        text="none",
        description="No information are given.")
    notice = PermissibleValue(
        text="notice",
        description="Outdated version of the image will remain valid until a deprecation notice will be published.")

    _defn = EnumDefinition(
        name="Validity1",
        description="Possible values for definition of image's validity after upgrading to a new version.",
    )

class Validity2(EnumDefinitionImpl):
    """
    Possible values for definition of image's validity after upgrading to a new version.
    """
    forever = PermissibleValue(
        text="forever",
        description="Outdated version of the image will remain valid for as long as the cloud operates.")

    _defn = EnumDefinition(
        name="Validity2",
        description="Possible values for definition of image's validity after upgrading to a new version.",
    )

class GaiaXTermsAndConditions(EnumDefinitionImpl):
    """
    SHA256 check sum of Gaia-X Terms and Conditions: 'The PARTICIPANT signing Gaia-X credentials agrees as follows: -
    to update its Gaia-X credentials about any changes, be it technical, organizational, or legal - especially but not
    limited to contractual in regards to the indicated attributes present in the Gaia-X credentials.
    The keypair used to sign Gaia-X credentials will be revoked where Gaia-X Association becomes aware of any
    inaccurate statements in regards to the claims which result in a non-compliance with the Trust Framework and
    policy rules defined in the Policy Rules and Labelling Document (PRLD).'
    """
    _defn = EnumDefinition(
        name="GaiaXTermsAndConditions",
        description="""SHA256 check sum of Gaia-X Terms and Conditions: 'The PARTICIPANT signing Gaia-X credentials agrees as follows: - to update its Gaia-X credentials about any changes, be it technical, organizational, or legal - especially but not limited to contractual in regards to the indicated attributes present in the Gaia-X credentials.
The keypair used to sign Gaia-X credentials will be revoked where Gaia-X Association becomes aware of any inaccurate statements in regards to the claims which result in a non-compliance with the Trust Framework and policy rules defined in the Policy Rules and Labelling Document (PRLD).'""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "4bd7554097444c960292b4726c2efa1373485e8a5565d94d41195214c5e0ceb3",
            PermissibleValue(text="4bd7554097444c960292b4726c2efa1373485e8a5565d94d41195214c5e0ceb3"))

class MemoryClasses(EnumDefinitionImpl):

    SDRAM = PermissibleValue(
        text="SDRAM",
        description="Synchronous DRAM, improves performance in data transfer actions through its pins.")
    DDR4 = PermissibleValue(
        text="DDR4",
        description="""Fourth generation of the synchronous dynamic random-access memory interface, improves speed and efficiency in data transfer actions.""")
    DDR5 = PermissibleValue(
        text="DDR5",
        description="""Fifth generation of the synchronous dynamic random-access memory interface, planned to reduce power consumption.""")
    GDDR5 = PermissibleValue(
        text="GDDR5",
        description="""Type of memory that is also based on the DDR standard, but designed specifically to be used in graphic cards.""")
    GDDR6 = PermissibleValue(
        text="GDDR6",
        description="Evolution of GDDR5 memory, designed for high-performance computing.")
    other = PermissibleValue(
        text="other",
        description="Memory class no further described.")

    _defn = EnumDefinition(
        name="MemoryClasses",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DDR SDRAM",
            PermissibleValue(
                text="DDR SDRAM",
                description="SDRAM evolution with twice the data transmission frequency."))
        setattr(cls, "ECC DRAM",
            PermissibleValue(
                text="ECC DRAM",
                description="This type of DRAM memory can find and even fix corrupted data."))

class MemoryRanks(EnumDefinitionImpl):

    other = PermissibleValue(
        text="other",
        description="Memory rank no further described.")

    _defn = EnumDefinition(
        name="MemoryRanks",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1R RDIMM",
            PermissibleValue(
                text="1R RDIMM",
                description="""(Registered DIMM) A single-rank (1R) memory module contains one set of DRAM chips that is accessed during writing/reading operations."""))
        setattr(cls, "2R RDIMM",
            PermissibleValue(
                text="2R RDIMM",
                description="""(Registered DIMM) A dual-rank (2R) memory module contains two sets of DRAM chips that are accessed during writing/reading operations."""))
        setattr(cls, "4R LRDIMM",
            PermissibleValue(
                text="4R LRDIMM",
                description="""(Load Reduced DIMM) A quad-rank (4R) memory module contains four sets of DRAM chips that are accessed during writing/reading operations."""))

class PXEDiskType(EnumDefinitionImpl):

    WINPE = PermissibleValue(text="WINPE")
    ISO = PermissibleValue(text="ISO")

    _defn = EnumDefinition(
        name="PXEDiskType",
    )

class SPDX(EnumDefinitionImpl):

    Glide = PermissibleValue(
        text="Glide",
        description="Visit https://spdx.org/licenses/Glide.html for complete details of 3dfx Glide License")
    Abstyles = PermissibleValue(
        text="Abstyles",
        description="Visit https://spdx.org/licenses/Abstyles.html for complete details of Abstyles License")
    AMPAS = PermissibleValue(
        text="AMPAS",
        description="""Visit https://spdx.org/licenses/AMPAS.html for complete details of Academy of Motion Picture Arts and Sciences BSD""")
    APAFML = PermissibleValue(
        text="APAFML",
        description="""Visit https://spdx.org/licenses/APAFML.html for complete details of Adobe Postscript AFM License""")
    Afmparse = PermissibleValue(
        text="Afmparse",
        description="Visit https://spdx.org/licenses/Afmparse.html for complete details of Afmparse License")
    Aladdin = PermissibleValue(
        text="Aladdin",
        description="""Visit https://spdx.org/licenses/Aladdin.html for complete details of Aladdin Free Public License""")
    ADSL = PermissibleValue(
        text="ADSL",
        description="""Visit https://spdx.org/licenses/ADSL.html for complete details of Amazon Digital Services License""")
    AMDPLPA = PermissibleValue(
        text="AMDPLPA",
        description="Visit https://spdx.org/licenses/AMDPLPA.html for complete details of AMD's plpa_map.c License")
    AML = PermissibleValue(
        text="AML",
        description="Visit https://spdx.org/licenses/AML.html for complete details of Apple MIT License")
    AAL = PermissibleValue(
        text="AAL",
        description="Visit https://spdx.org/licenses/AAL.html for complete details of Attribution Assurance License")
    Baekmuk = PermissibleValue(
        text="Baekmuk",
        description="Visit https://spdx.org/licenses/Baekmuk.html for complete details of Baekmuk License")
    Bahyph = PermissibleValue(
        text="Bahyph",
        description="Visit https://spdx.org/licenses/Bahyph.html for complete details of Bahyph License")
    Barr = PermissibleValue(
        text="Barr",
        description="Visit https://spdx.org/licenses/Barr.html for complete details of Barr License")
    Beerware = PermissibleValue(
        text="Beerware",
        description="Visit https://spdx.org/licenses/Beerware.html for complete details of Beerware License")
    Borceux = PermissibleValue(
        text="Borceux",
        description="Visit https://spdx.org/licenses/Borceux.html for complete details of Borceux license")
    Caldera = PermissibleValue(
        text="Caldera",
        description="Visit https://spdx.org/licenses/Caldera.html for complete details of Caldera License")
    CFITSIO = PermissibleValue(
        text="CFITSIO",
        description="Visit https://spdx.org/licenses/CFITSIO.html for complete details of CFITSIO License")
    checkmk = PermissibleValue(
        text="checkmk",
        description="Visit https://spdx.org/licenses/checkmk.html for complete details of Checkmk License")
    ClArtistic = PermissibleValue(
        text="ClArtistic",
        description="""Visit https://spdx.org/licenses/ClArtistic.html for complete details of Clarified Artistic License""")
    Clips = PermissibleValue(
        text="Clips",
        description="Visit https://spdx.org/licenses/Clips.html for complete details of Clips License")
    LOOP = PermissibleValue(
        text="LOOP",
        description="Visit https://spdx.org/licenses/LOOP.html for complete details of Common Lisp LOOP License")
    Cronyx = PermissibleValue(
        text="Cronyx",
        description="Visit https://spdx.org/licenses/Cronyx.html for complete details of Cronyx License")
    Crossword = PermissibleValue(
        text="Crossword",
        description="Visit https://spdx.org/licenses/Crossword.html for complete details of Crossword License")
    CrystalStacker = PermissibleValue(
        text="CrystalStacker",
        description="""Visit https://spdx.org/licenses/CrystalStacker.html for complete details of CrystalStacker License""")
    Cube = PermissibleValue(
        text="Cube",
        description="Visit https://spdx.org/licenses/Cube.html for complete details of Cube License")
    curl = PermissibleValue(
        text="curl",
        description="Visit https://spdx.org/licenses/curl.html for complete details of curl License")
    dtoa = PermissibleValue(
        text="dtoa",
        description="Visit https://spdx.org/licenses/dtoa.html for complete details of David M. Gay dtoa License")
    diffmark = PermissibleValue(
        text="diffmark",
        description="Visit https://spdx.org/licenses/diffmark.html for complete details of diffmark license")
    WTFPL = PermissibleValue(
        text="WTFPL",
        description="""Visit https://spdx.org/licenses/WTFPL.html for complete details of Do What The F*ck You Want To Public License""")
    DOC = PermissibleValue(
        text="DOC",
        description="Visit https://spdx.org/licenses/DOC.html for complete details of DOC License")
    Dotseqn = PermissibleValue(
        text="Dotseqn",
        description="Visit https://spdx.org/licenses/Dotseqn.html for complete details of Dotseqn License")
    DSDP = PermissibleValue(
        text="DSDP",
        description="Visit https://spdx.org/licenses/DSDP.html for complete details of DSDP License")
    dvipdfm = PermissibleValue(
        text="dvipdfm",
        description="Visit https://spdx.org/licenses/dvipdfm.html for complete details of dvipdfm License")
    eGenix = PermissibleValue(
        text="eGenix",
        description="""Visit https://spdx.org/licenses/eGenix.html for complete details of eGenix.com Public License 1.1.0""")
    Entessa = PermissibleValue(
        text="Entessa",
        description="""Visit https://spdx.org/licenses/Entessa.html for complete details of Entessa Public License v1.0""")
    EPICS = PermissibleValue(
        text="EPICS",
        description="Visit https://spdx.org/licenses/EPICS.html for complete details of EPICS Open License")
    EUDatagrid = PermissibleValue(
        text="EUDatagrid",
        description="""Visit https://spdx.org/licenses/EUDatagrid.html for complete details of EU DataGrid Software License""")
    Eurosym = PermissibleValue(
        text="Eurosym",
        description="Visit https://spdx.org/licenses/Eurosym.html for complete details of Eurosym License")
    Fair = PermissibleValue(
        text="Fair",
        description="Visit https://spdx.org/licenses/Fair.html for complete details of Fair License")
    FreeImage = PermissibleValue(
        text="FreeImage",
        description="""Visit https://spdx.org/licenses/FreeImage.html for complete details of FreeImage Public License v1.0""")
    FTL = PermissibleValue(
        text="FTL",
        description="Visit https://spdx.org/licenses/FTL.html for complete details of Freetype Project License")
    FSFAP = PermissibleValue(
        text="FSFAP",
        description="Visit https://spdx.org/licenses/FSFAP.html for complete details of FSF All Permissive License")
    FSFUL = PermissibleValue(
        text="FSFUL",
        description="Visit https://spdx.org/licenses/FSFUL.html for complete details of FSF Unlimited License")
    FSFULLRWD = PermissibleValue(
        text="FSFULLRWD",
        description="""Visit https://spdx.org/licenses/FSFULLRWD.html for complete details of FSF Unlimited License (With License Retention and Warranty Disclaimer)""")
    FSFULLR = PermissibleValue(
        text="FSFULLR",
        description="""Visit https://spdx.org/licenses/FSFULLR.html for complete details of FSF Unlimited License (with License Retention)""")
    Furuseth = PermissibleValue(
        text="Furuseth",
        description="Visit https://spdx.org/licenses/Furuseth.html for complete details of Furuseth License")
    FBM = PermissibleValue(
        text="FBM",
        description="Visit https://spdx.org/licenses/FBM.html for complete details of Fuzzy Bitmap License")
    fwlw = PermissibleValue(
        text="fwlw",
        description="Visit https://spdx.org/licenses/fwlw.html for complete details of fwlw License")
    GD = PermissibleValue(
        text="GD",
        description="Visit https://spdx.org/licenses/GD.html for complete details of GD License")
    Giftware = PermissibleValue(
        text="Giftware",
        description="Visit https://spdx.org/licenses/Giftware.html for complete details of Giftware License")
    GL2PS = PermissibleValue(
        text="GL2PS",
        description="Visit https://spdx.org/licenses/GL2PS.html for complete details of GL2PS License")
    Glulxe = PermissibleValue(
        text="Glulxe",
        description="Visit https://spdx.org/licenses/Glulxe.html for complete details of Glulxe License")
    gnuplot = PermissibleValue(
        text="gnuplot",
        description="Visit https://spdx.org/licenses/gnuplot.html for complete details of gnuplot License")
    GLWTPL = PermissibleValue(
        text="GLWTPL",
        description="""Visit https://spdx.org/licenses/GLWTPL.html for complete details of Good Luck With That Public License""")
    HaskellReport = PermissibleValue(
        text="HaskellReport",
        description="""Visit https://spdx.org/licenses/HaskellReport.html for complete details of Haskell Language Report License""")
    HPND = PermissibleValue(
        text="HPND",
        description="""Visit https://spdx.org/licenses/HPND.html for complete details of Historical Permission Notice and Disclaimer""")
    HTMLTIDY = PermissibleValue(
        text="HTMLTIDY",
        description="Visit https://spdx.org/licenses/HTMLTIDY.html for complete details of HTML Tidy License")
    ICU = PermissibleValue(
        text="ICU",
        description="Visit https://spdx.org/licenses/ICU.html for complete details of ICU License")
    ImageMagick = PermissibleValue(
        text="ImageMagick",
        description="Visit https://spdx.org/licenses/ImageMagick.html for complete details of ImageMagick License")
    iMatix = PermissibleValue(
        text="iMatix",
        description="""Visit https://spdx.org/licenses/iMatix.html for complete details of iMatix Standard Function Library Agreement""")
    Imlib2 = PermissibleValue(
        text="Imlib2",
        description="Visit https://spdx.org/licenses/Imlib2.html for complete details of Imlib2 License")
    IJG = PermissibleValue(
        text="IJG",
        description="""Visit https://spdx.org/licenses/IJG.html for complete details of Independent JPEG Group License""")
    Intel = PermissibleValue(
        text="Intel",
        description="Visit https://spdx.org/licenses/Intel.html for complete details of Intel Open Source License")
    IPA = PermissibleValue(
        text="IPA",
        description="Visit https://spdx.org/licenses/IPA.html for complete details of IPA Font License")
    ISC = PermissibleValue(
        text="ISC",
        description="Visit https://spdx.org/licenses/ISC.html for complete details of ISC License")
    Jam = PermissibleValue(
        text="Jam",
        description="Visit https://spdx.org/licenses/Jam.html for complete details of Jam License")
    JPNIC = PermissibleValue(
        text="JPNIC",
        description="""Visit https://spdx.org/licenses/JPNIC.html for complete details of Japan Network Information Center License""")
    JSON = PermissibleValue(
        text="JSON",
        description="Visit https://spdx.org/licenses/JSON.html for complete details of JSON License")
    Kastrup = PermissibleValue(
        text="Kastrup",
        description="Visit https://spdx.org/licenses/Kastrup.html for complete details of Kastrup License")
    Kazlib = PermissibleValue(
        text="Kazlib",
        description="Visit https://spdx.org/licenses/Kazlib.html for complete details of Kazlib License")
    Latex2e = PermissibleValue(
        text="Latex2e",
        description="Visit https://spdx.org/licenses/Latex2e.html for complete details of Latex2e License")
    Leptonica = PermissibleValue(
        text="Leptonica",
        description="Visit https://spdx.org/licenses/Leptonica.html for complete details of Leptonica License")
    LGPLLR = PermissibleValue(
        text="LGPLLR",
        description="""Visit https://spdx.org/licenses/LGPLLR.html for complete details of Lesser General Public License For Linguistic Resources""")
    Libpng = PermissibleValue(
        text="Libpng",
        description="Visit https://spdx.org/licenses/Libpng.html for complete details of libpng License")
    libtiff = PermissibleValue(
        text="libtiff",
        description="Visit https://spdx.org/licenses/libtiff.html for complete details of libtiff License")
    lsof = PermissibleValue(
        text="lsof",
        description="Visit https://spdx.org/licenses/lsof.html for complete details of lsof License")
    magaz = PermissibleValue(
        text="magaz",
        description="Visit https://spdx.org/licenses/magaz.html for complete details of magaz License")
    MakeIndex = PermissibleValue(
        text="MakeIndex",
        description="Visit https://spdx.org/licenses/MakeIndex.html for complete details of MakeIndex License")
    MTLL = PermissibleValue(
        text="MTLL",
        description="""Visit https://spdx.org/licenses/MTLL.html for complete details of Matrix Template Library License""")
    metamail = PermissibleValue(
        text="metamail",
        description="Visit https://spdx.org/licenses/metamail.html for complete details of metamail License")
    Minpack = PermissibleValue(
        text="Minpack",
        description="Visit https://spdx.org/licenses/Minpack.html for complete details of Minpack License")
    MITNFA = PermissibleValue(
        text="MITNFA",
        description="""Visit https://spdx.org/licenses/MITNFA.html for complete details of MIT +no-false-attribs license""")
    MIT = PermissibleValue(
        text="MIT",
        description="Visit https://spdx.org/licenses/MIT.html for complete details of MIT License")
    MMIXware = PermissibleValue(
        text="MMIXware",
        description="Visit https://spdx.org/licenses/MMIXware.html for complete details of MMIXware License")
    Motosoto = PermissibleValue(
        text="Motosoto",
        description="Visit https://spdx.org/licenses/Motosoto.html for complete details of Motosoto License")
    mpich2 = PermissibleValue(
        text="mpich2",
        description="Visit https://spdx.org/licenses/mpich2.html for complete details of mpich2 License")
    mplus = PermissibleValue(
        text="mplus",
        description="Visit https://spdx.org/licenses/mplus.html for complete details of mplus Font License")
    Multics = PermissibleValue(
        text="Multics",
        description="Visit https://spdx.org/licenses/Multics.html for complete details of Multics License")
    Mup = PermissibleValue(
        text="Mup",
        description="Visit https://spdx.org/licenses/Mup.html for complete details of Mup License")
    Naumen = PermissibleValue(
        text="Naumen",
        description="Visit https://spdx.org/licenses/Naumen.html for complete details of Naumen Public License")
    NetCDF = PermissibleValue(
        text="NetCDF",
        description="Visit https://spdx.org/licenses/NetCDF.html for complete details of NetCDF license")
    NGPL = PermissibleValue(
        text="NGPL",
        description="""Visit https://spdx.org/licenses/NGPL.html for complete details of Nethack General Public License""")
    NOSL = PermissibleValue(
        text="NOSL",
        description="Visit https://spdx.org/licenses/NOSL.html for complete details of Netizen Open Source License")
    Newsletr = PermissibleValue(
        text="Newsletr",
        description="Visit https://spdx.org/licenses/Newsletr.html for complete details of Newsletr License")
    NLPL = PermissibleValue(
        text="NLPL",
        description="Visit https://spdx.org/licenses/NLPL.html for complete details of No Limit Public License")
    Nokia = PermissibleValue(
        text="Nokia",
        description="Visit https://spdx.org/licenses/Nokia.html for complete details of Nokia Open Source License")
    Noweb = PermissibleValue(
        text="Noweb",
        description="Visit https://spdx.org/licenses/Noweb.html for complete details of Noweb License")
    NRL = PermissibleValue(
        text="NRL",
        description="Visit https://spdx.org/licenses/NRL.html for complete details of NRL License")
    NTP = PermissibleValue(
        text="NTP",
        description="Visit https://spdx.org/licenses/NTP.html for complete details of NTP License")
    OFFIS = PermissibleValue(
        text="OFFIS",
        description="Visit https://spdx.org/licenses/OFFIS.html for complete details of OFFIS License")
    OGTSL = PermissibleValue(
        text="OGTSL",
        description="""Visit https://spdx.org/licenses/OGTSL.html for complete details of Open Group Test Suite License""")
    OML = PermissibleValue(
        text="OML",
        description="Visit https://spdx.org/licenses/OML.html for complete details of Open Market License")
    OpenSSL = PermissibleValue(
        text="OpenSSL",
        description="Visit https://spdx.org/licenses/OpenSSL.html for complete details of OpenSSL License")
    PADL = PermissibleValue(
        text="PADL",
        description="Visit https://spdx.org/licenses/PADL.html for complete details of PADL License")
    Plexus = PermissibleValue(
        text="Plexus",
        description="Visit https://spdx.org/licenses/Plexus.html for complete details of Plexus Classworlds License")
    pnmstitch = PermissibleValue(
        text="pnmstitch",
        description="Visit https://spdx.org/licenses/pnmstitch.html for complete details of pnmstitch License")
    PostgreSQL = PermissibleValue(
        text="PostgreSQL",
        description="Visit https://spdx.org/licenses/PostgreSQL.html for complete details of PostgreSQL License")
    psfrag = PermissibleValue(
        text="psfrag",
        description="Visit https://spdx.org/licenses/psfrag.html for complete details of psfrag License")
    psutils = PermissibleValue(
        text="psutils",
        description="Visit https://spdx.org/licenses/psutils.html for complete details of psutils License")
    Qhull = PermissibleValue(
        text="Qhull",
        description="Visit https://spdx.org/licenses/Qhull.html for complete details of Qhull License")
    Rdisc = PermissibleValue(
        text="Rdisc",
        description="Visit https://spdx.org/licenses/Rdisc.html for complete details of Rdisc License")
    RSCPL = PermissibleValue(
        text="RSCPL",
        description="""Visit https://spdx.org/licenses/RSCPL.html for complete details of Ricoh Source Code Public License""")
    Ruby = PermissibleValue(
        text="Ruby",
        description="Visit https://spdx.org/licenses/Ruby.html for complete details of Ruby License")
    Saxpath = PermissibleValue(
        text="Saxpath",
        description="Visit https://spdx.org/licenses/Saxpath.html for complete details of Saxpath License")
    SCEA = PermissibleValue(
        text="SCEA",
        description="Visit https://spdx.org/licenses/SCEA.html for complete details of SCEA Shared Source License")
    SchemeReport = PermissibleValue(
        text="SchemeReport",
        description="""Visit https://spdx.org/licenses/SchemeReport.html for complete details of Scheme Language Report License""")
    SWL = PermissibleValue(
        text="SWL",
        description="""Visit https://spdx.org/licenses/SWL.html for complete details of Scheme Widget Library (SWL) Software License Agreement""")
    SMPPL = PermissibleValue(
        text="SMPPL",
        description="""Visit https://spdx.org/licenses/SMPPL.html for complete details of Secure Messaging Protocol Public License""")
    Sendmail = PermissibleValue(
        text="Sendmail",
        description="Visit https://spdx.org/licenses/Sendmail.html for complete details of Sendmail License")
    SGP4 = PermissibleValue(
        text="SGP4",
        description="Visit https://spdx.org/licenses/SGP4.html for complete details of SGP4 Permission Notice")
    SL = PermissibleValue(
        text="SL",
        description="Visit https://spdx.org/licenses/SL.html for complete details of SL License")
    Sleepycat = PermissibleValue(
        text="Sleepycat",
        description="Visit https://spdx.org/licenses/Sleepycat.html for complete details of Sleepycat License")
    SNIA = PermissibleValue(
        text="SNIA",
        description="Visit https://spdx.org/licenses/SNIA.html for complete details of SNIA Public License 1.1")
    snprintf = PermissibleValue(
        text="snprintf",
        description="Visit https://spdx.org/licenses/snprintf.html for complete details of snprintf License")
    Soundex = PermissibleValue(
        text="Soundex",
        description="Visit https://spdx.org/licenses/Soundex.html for complete details of Soundex License")
    blessing = PermissibleValue(
        text="blessing",
        description="Visit https://spdx.org/licenses/blessing.html for complete details of SQLite Blessing")
    SMLNJ = PermissibleValue(
        text="SMLNJ",
        description="""Visit https://spdx.org/licenses/SMLNJ.html for complete details of Standard ML of New Jersey License""")
    SISSL = PermissibleValue(
        text="SISSL",
        description="""Visit https://spdx.org/licenses/SISSL.html for complete details of Sun Industry Standards Source License v1.1""")
    SunPro = PermissibleValue(
        text="SunPro",
        description="Visit https://spdx.org/licenses/SunPro.html for complete details of SunPro License")
    swrule = PermissibleValue(
        text="swrule",
        description="Visit https://spdx.org/licenses/swrule.html for complete details of swrule License")
    Symlinks = PermissibleValue(
        text="Symlinks",
        description="Visit https://spdx.org/licenses/Symlinks.html for complete details of Symlinks License")
    TCL = PermissibleValue(
        text="TCL",
        description="Visit https://spdx.org/licenses/TCL.html for complete details of TCL/TK License")
    TermReadKey = PermissibleValue(
        text="TermReadKey",
        description="Visit https://spdx.org/licenses/TermReadKey.html for complete details of TermReadKey License")
    TTWL = PermissibleValue(
        text="TTWL",
        description="Visit https://spdx.org/licenses/TTWL.html for complete details of Text-Tabs+Wrap License")
    MirOS = PermissibleValue(
        text="MirOS",
        description="Visit https://spdx.org/licenses/MirOS.html for complete details of The MirOS Licence")
    Unlicense = PermissibleValue(
        text="Unlicense",
        description="Visit https://spdx.org/licenses/Unlicense.html for complete details of The Unlicense")
    TPDL = PermissibleValue(
        text="TPDL",
        description="Visit https://spdx.org/licenses/TPDL.html for complete details of Time::ParseDate License")
    TMate = PermissibleValue(
        text="TMate",
        description="Visit https://spdx.org/licenses/TMate.html for complete details of TMate Open Source License")
    TOSL = PermissibleValue(
        text="TOSL",
        description="Visit https://spdx.org/licenses/TOSL.html for complete details of Trusster Open Source License")
    TTYP0 = PermissibleValue(
        text="TTYP0",
        description="Visit https://spdx.org/licenses/TTYP0.html for complete details of TTYP0 License")
    UCAR = PermissibleValue(
        text="UCAR",
        description="Visit https://spdx.org/licenses/UCAR.html for complete details of UCAR License")
    ulem = PermissibleValue(
        text="ulem",
        description="Visit https://spdx.org/licenses/ulem.html for complete details of ulem License")
    NCSA = PermissibleValue(
        text="NCSA",
        description="""Visit https://spdx.org/licenses/NCSA.html for complete details of University of Illinois/NCSA Open Source License""")
    UnixCrypt = PermissibleValue(
        text="UnixCrypt",
        description="Visit https://spdx.org/licenses/UnixCrypt.html for complete details of UnixCrypt License")
    Vim = PermissibleValue(
        text="Vim",
        description="Visit https://spdx.org/licenses/Vim.html for complete details of Vim License")
    VOSTROM = PermissibleValue(
        text="VOSTROM",
        description="""Visit https://spdx.org/licenses/VOSTROM.html for complete details of VOSTROM Public License for Open Source""")
    W3C = PermissibleValue(
        text="W3C",
        description="""Visit https://spdx.org/licenses/W3C.html for complete details of W3C Software Notice and License (2002-12-31)""")
    w3m = PermissibleValue(
        text="w3m",
        description="Visit https://spdx.org/licenses/w3m.html for complete details of w3m License")
    Wsuipa = PermissibleValue(
        text="Wsuipa",
        description="Visit https://spdx.org/licenses/Wsuipa.html for complete details of Wsuipa License")
    Xnet = PermissibleValue(
        text="Xnet",
        description="Visit https://spdx.org/licenses/Xnet.html for complete details of X.Net License")
    X11 = PermissibleValue(
        text="X11",
        description="Visit https://spdx.org/licenses/X11.html for complete details of X11 License")
    Xerox = PermissibleValue(
        text="Xerox",
        description="Visit https://spdx.org/licenses/Xerox.html for complete details of Xerox License")
    Xfig = PermissibleValue(
        text="Xfig",
        description="Visit https://spdx.org/licenses/Xfig.html for complete details of Xfig License")
    xinetd = PermissibleValue(
        text="xinetd",
        description="Visit https://spdx.org/licenses/xinetd.html for complete details of xinetd License")
    xlock = PermissibleValue(
        text="xlock",
        description="Visit https://spdx.org/licenses/xlock.html for complete details of xlock License")
    xpp = PermissibleValue(
        text="xpp",
        description="Visit https://spdx.org/licenses/xpp.html for complete details of XPP License")
    XSkat = PermissibleValue(
        text="XSkat",
        description="Visit https://spdx.org/licenses/XSkat.html for complete details of XSkat License")
    Zed = PermissibleValue(
        text="Zed",
        description="Visit https://spdx.org/licenses/Zed.html for complete details of Zed License")
    Zeeff = PermissibleValue(
        text="Zeeff",
        description="Visit https://spdx.org/licenses/Zeeff.html for complete details of Zeeff License")
    Zlib = PermissibleValue(
        text="Zlib",
        description="Visit https://spdx.org/licenses/Zlib.html for complete details of zlib License")

    _defn = EnumDefinition(
        name="SPDX",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "AFL-1.1",
            PermissibleValue(
                text="AFL-1.1",
                description="""Visit https://spdx.org/licenses/AFL-1.1.html for complete details of Academic Free License v1.1"""))
        setattr(cls, "AFL-1.2",
            PermissibleValue(
                text="AFL-1.2",
                description="""Visit https://spdx.org/licenses/AFL-1.2.html for complete details of Academic Free License v1.2"""))
        setattr(cls, "AFL-2.0",
            PermissibleValue(
                text="AFL-2.0",
                description="""Visit https://spdx.org/licenses/AFL-2.0.html for complete details of Academic Free License v2.0"""))
        setattr(cls, "AFL-2.1",
            PermissibleValue(
                text="AFL-2.1",
                description="""Visit https://spdx.org/licenses/AFL-2.1.html for complete details of Academic Free License v2.1"""))
        setattr(cls, "AFL-3.0",
            PermissibleValue(
                text="AFL-3.0",
                description="""Visit https://spdx.org/licenses/AFL-3.0.html for complete details of Academic Free License v3.0"""))
        setattr(cls, "AdaCore-doc",
            PermissibleValue(
                text="AdaCore-doc",
                description="""Visit https://spdx.org/licenses/AdaCore-doc.html for complete details of AdaCore Doc License"""))
        setattr(cls, "APL-1.0",
            PermissibleValue(
                text="APL-1.0",
                description="""Visit https://spdx.org/licenses/APL-1.0.html for complete details of Adaptive Public License 1.0"""))
        setattr(cls, "Adobe-Glyph",
            PermissibleValue(
                text="Adobe-Glyph",
                description="""Visit https://spdx.org/licenses/Adobe-Glyph.html for complete details of Adobe Glyph List License"""))
        setattr(cls, "Adobe-2006",
            PermissibleValue(
                text="Adobe-2006",
                description="""Visit https://spdx.org/licenses/Adobe-2006.html for complete details of Adobe Systems Incorporated Source Code License Agreement"""))
        setattr(cls, "Adobe-Utopia",
            PermissibleValue(
                text="Adobe-Utopia",
                description="""Visit https://spdx.org/licenses/Adobe-Utopia.html for complete details of Adobe Utopia Font License"""))
        setattr(cls, "AGPL-1.0-only",
            PermissibleValue(
                text="AGPL-1.0-only",
                description="""Visit https://spdx.org/licenses/AGPL-1.0-only.html for complete details of Affero General Public License v1.0 only"""))
        setattr(cls, "AGPL-1.0-or-later",
            PermissibleValue(
                text="AGPL-1.0-or-later",
                description="""Visit https://spdx.org/licenses/AGPL-1.0-or-later.html for complete details of Affero General Public License v1.0 or later"""))
        setattr(cls, "ANTLR-PD",
            PermissibleValue(
                text="ANTLR-PD",
                description="""Visit https://spdx.org/licenses/ANTLR-PD.html for complete details of ANTLR Software Rights Notice"""))
        setattr(cls, "ANTLR-PD-fallback",
            PermissibleValue(
                text="ANTLR-PD-fallback",
                description="""Visit https://spdx.org/licenses/ANTLR-PD-fallback.html for complete details of ANTLR Software Rights Notice with license fallback"""))
        setattr(cls, "Apache-1.0",
            PermissibleValue(
                text="Apache-1.0",
                description="""Visit https://spdx.org/licenses/Apache-1.0.html for complete details of Apache License 1.0"""))
        setattr(cls, "Apache-1.1",
            PermissibleValue(
                text="Apache-1.1",
                description="""Visit https://spdx.org/licenses/Apache-1.1.html for complete details of Apache License 1.1"""))
        setattr(cls, "Apache-2.0",
            PermissibleValue(
                text="Apache-2.0",
                description="""Visit https://spdx.org/licenses/Apache-2.0.html for complete details of Apache License 2.0"""))
        setattr(cls, "App-s2p",
            PermissibleValue(
                text="App-s2p",
                description="Visit https://spdx.org/licenses/App-s2p.html for complete details of App::s2p License"))
        setattr(cls, "APSL-1.0",
            PermissibleValue(
                text="APSL-1.0",
                description="""Visit https://spdx.org/licenses/APSL-1.0.html for complete details of Apple Public Source License 1.0"""))
        setattr(cls, "APSL-1.1",
            PermissibleValue(
                text="APSL-1.1",
                description="""Visit https://spdx.org/licenses/APSL-1.1.html for complete details of Apple Public Source License 1.1"""))
        setattr(cls, "APSL-1.2",
            PermissibleValue(
                text="APSL-1.2",
                description="""Visit https://spdx.org/licenses/APSL-1.2.html for complete details of Apple Public Source License 1.2"""))
        setattr(cls, "APSL-2.0",
            PermissibleValue(
                text="APSL-2.0",
                description="""Visit https://spdx.org/licenses/APSL-2.0.html for complete details of Apple Public Source License 2.0"""))
        setattr(cls, "Arphic-1999",
            PermissibleValue(
                text="Arphic-1999",
                description="""Visit https://spdx.org/licenses/Arphic-1999.html for complete details of Arphic Public License"""))
        setattr(cls, "Artistic-1.0",
            PermissibleValue(
                text="Artistic-1.0",
                description="""Visit https://spdx.org/licenses/Artistic-1.0.html for complete details of Artistic License 1.0"""))
        setattr(cls, "Artistic-1.0-Perl",
            PermissibleValue(
                text="Artistic-1.0-Perl",
                description="""Visit https://spdx.org/licenses/Artistic-1.0-Perl.html for complete details of Artistic License 1.0 (Perl)"""))
        setattr(cls, "Artistic-1.0-cl8",
            PermissibleValue(
                text="Artistic-1.0-cl8",
                description="""Visit https://spdx.org/licenses/Artistic-1.0-cl8.html for complete details of Artistic License 1.0 w/clause 8"""))
        setattr(cls, "Artistic-2.0",
            PermissibleValue(
                text="Artistic-2.0",
                description="""Visit https://spdx.org/licenses/Artistic-2.0.html for complete details of Artistic License 2.0"""))
        setattr(cls, "ASWF-Digital-Assets-1.1",
            PermissibleValue(
                text="ASWF-Digital-Assets-1.1",
                description="""Visit https://spdx.org/licenses/ASWF-Digital-Assets-1.1.html for complete details of ASWF Digital Assets License 1.1"""))
        setattr(cls, "ASWF-Digital-Assets-1.0",
            PermissibleValue(
                text="ASWF-Digital-Assets-1.0",
                description="""Visit https://spdx.org/licenses/ASWF-Digital-Assets-1.0.html for complete details of ASWF Digital Assets License version 1.0"""))
        setattr(cls, "Bitstream-Charter",
            PermissibleValue(
                text="Bitstream-Charter",
                description="""Visit https://spdx.org/licenses/Bitstream-Charter.html for complete details of Bitstream Charter Font License"""))
        setattr(cls, "Bitstream-Vera",
            PermissibleValue(
                text="Bitstream-Vera",
                description="""Visit https://spdx.org/licenses/Bitstream-Vera.html for complete details of Bitstream Vera Font License"""))
        setattr(cls, "BitTorrent-1.0",
            PermissibleValue(
                text="BitTorrent-1.0",
                description="""Visit https://spdx.org/licenses/BitTorrent-1.0.html for complete details of BitTorrent Open Source License v1.0"""))
        setattr(cls, "BitTorrent-1.1",
            PermissibleValue(
                text="BitTorrent-1.1",
                description="""Visit https://spdx.org/licenses/BitTorrent-1.1.html for complete details of BitTorrent Open Source License v1.1"""))
        setattr(cls, "BlueOak-1.0.0",
            PermissibleValue(
                text="BlueOak-1.0.0",
                description="""Visit https://spdx.org/licenses/BlueOak-1.0.0.html for complete details of Blue Oak Model License 1.0.0"""))
        setattr(cls, "Boehm-GC",
            PermissibleValue(
                text="Boehm-GC",
                description="""Visit https://spdx.org/licenses/Boehm-GC.html for complete details of Boehm-Demers-Weiser GC License"""))
        setattr(cls, "BSL-1.0",
            PermissibleValue(
                text="BSL-1.0",
                description="""Visit https://spdx.org/licenses/BSL-1.0.html for complete details of Boost Software License 1.0"""))
        setattr(cls, "Brian-Gladman-3-Clause",
            PermissibleValue(
                text="Brian-Gladman-3-Clause",
                description="""Visit https://spdx.org/licenses/Brian-Gladman-3-Clause.html for complete details of Brian Gladman 3-Clause License"""))
        setattr(cls, "BSD-1-Clause",
            PermissibleValue(
                text="BSD-1-Clause",
                description="""Visit https://spdx.org/licenses/BSD-1-Clause.html for complete details of BSD 1-Clause License"""))
        setattr(cls, "BSD-2-Clause",
            PermissibleValue(
                text="BSD-2-Clause",
                description="""Visit https://spdx.org/licenses/BSD-2-Clause.html for complete details of BSD 2-Clause 'Simplified' License"""))
        setattr(cls, "BSD-2-Clause-Views",
            PermissibleValue(
                text="BSD-2-Clause-Views",
                description="""Visit https://spdx.org/licenses/BSD-2-Clause-Views.html for complete details of BSD 2-Clause with views sentence"""))
        setattr(cls, "BSD-3-Clause",
            PermissibleValue(
                text="BSD-3-Clause",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause.html for complete details of BSD 3-Clause 'New' or 'Revised' License"""))
        setattr(cls, "BSD-3-Clause-Clear",
            PermissibleValue(
                text="BSD-3-Clause-Clear",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-Clear.html for complete details of BSD 3-Clause Clear License"""))
        setattr(cls, "BSD-3-Clause-flex",
            PermissibleValue(
                text="BSD-3-Clause-flex",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-flex.html for complete details of BSD 3-Clause Flex variant"""))
        setattr(cls, "BSD-3-Clause-Modification",
            PermissibleValue(
                text="BSD-3-Clause-Modification",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-Modification.html for complete details of BSD 3-Clause Modification"""))
        setattr(cls, "BSD-3-Clause-No-Military-License",
            PermissibleValue(
                text="BSD-3-Clause-No-Military-License",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-No-Military-License.html for complete details of BSD 3-Clause No Military License"""))
        setattr(cls, "BSD-3-Clause-No-Nuclear-License",
            PermissibleValue(
                text="BSD-3-Clause-No-Nuclear-License",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License.html for complete details of BSD 3-Clause No Nuclear License"""))
        setattr(cls, "BSD-3-Clause-No-Nuclear-License-2014",
            PermissibleValue(
                text="BSD-3-Clause-No-Nuclear-License-2014",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License-2014.html for complete details of BSD 3-Clause No Nuclear License 2014"""))
        setattr(cls, "BSD-3-Clause-No-Nuclear-Warranty",
            PermissibleValue(
                text="BSD-3-Clause-No-Nuclear-Warranty",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-Warranty.html for complete details of BSD 3-Clause No Nuclear Warranty"""))
        setattr(cls, "BSD-3-Clause-Open-MPI",
            PermissibleValue(
                text="BSD-3-Clause-Open-MPI",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-Open-MPI.html for complete details of BSD 3-Clause Open MPI variant"""))
        setattr(cls, "BSD-3-Clause-Sun",
            PermissibleValue(
                text="BSD-3-Clause-Sun",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-Sun.html for complete details of BSD 3-Clause Sun Microsystems"""))
        setattr(cls, "BSD-4-Clause-Shortened",
            PermissibleValue(
                text="BSD-4-Clause-Shortened",
                description="""Visit https://spdx.org/licenses/BSD-4-Clause-Shortened.html for complete details of BSD 4 Clause Shortened"""))
        setattr(cls, "BSD-4-Clause",
            PermissibleValue(
                text="BSD-4-Clause",
                description="""Visit https://spdx.org/licenses/BSD-4-Clause.html for complete details of BSD 4-Clause 'Original' or 'Old' License"""))
        setattr(cls, "BSD-4.3RENO",
            PermissibleValue(
                text="BSD-4.3RENO",
                description="""Visit https://spdx.org/licenses/BSD-4.3RENO.html for complete details of BSD 4.3 RENO License"""))
        setattr(cls, "BSD-4.3TAHOE",
            PermissibleValue(
                text="BSD-4.3TAHOE",
                description="""Visit https://spdx.org/licenses/BSD-4.3TAHOE.html for complete details of BSD 4.3 TAHOE License"""))
        setattr(cls, "BSD-Advertising-Acknowledgement",
            PermissibleValue(
                text="BSD-Advertising-Acknowledgement",
                description="""Visit https://spdx.org/licenses/BSD-Advertising-Acknowledgement.html for complete details of BSD Advertising Acknowledgement License"""))
        setattr(cls, "BSD-Protection",
            PermissibleValue(
                text="BSD-Protection",
                description="""Visit https://spdx.org/licenses/BSD-Protection.html for complete details of BSD Protection License"""))
        setattr(cls, "BSD-Source-Code",
            PermissibleValue(
                text="BSD-Source-Code",
                description="""Visit https://spdx.org/licenses/BSD-Source-Code.html for complete details of BSD Source Code Attribution"""))
        setattr(cls, "BSD-3-Clause-Attribution",
            PermissibleValue(
                text="BSD-3-Clause-Attribution",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-Attribution.html for complete details of BSD with attribution"""))
        setattr(cls, "BSD-Attribution-HPND-disclaimer",
            PermissibleValue(
                text="BSD-Attribution-HPND-disclaimer",
                description="""Visit https://spdx.org/licenses/BSD-Attribution-HPND-disclaimer.html for complete details of BSD with Attribution and HPND disclaimer"""))
        setattr(cls, "0BSD",
            PermissibleValue(
                text="0BSD",
                description="""Visit https://spdx.org/licenses/0BSD.html for complete details of BSD Zero Clause License"""))
        setattr(cls, "BSD-2-Clause-Patent",
            PermissibleValue(
                text="BSD-2-Clause-Patent",
                description="""Visit https://spdx.org/licenses/BSD-2-Clause-Patent.html for complete details of BSD-2-Clause Plus Patent License"""))
        setattr(cls, "BSD-4-Clause-UC",
            PermissibleValue(
                text="BSD-4-Clause-UC",
                description="""Visit https://spdx.org/licenses/BSD-4-Clause-UC.html for complete details of BSD-4-Clause (University of California-Specific)"""))
        setattr(cls, "BSD-Inferno-Nettverk",
            PermissibleValue(
                text="BSD-Inferno-Nettverk",
                description="""Visit https://spdx.org/licenses/BSD-Inferno-Nettverk.html for complete details of BSD-Inferno-Nettverk"""))
        setattr(cls, "BUSL-1.1",
            PermissibleValue(
                text="BUSL-1.1",
                description="""Visit https://spdx.org/licenses/BUSL-1.1.html for complete details of Business Source License 1.1"""))
        setattr(cls, "bzip2-1.0.6",
            PermissibleValue(
                text="bzip2-1.0.6",
                description="""Visit https://spdx.org/licenses/bzip2-1.0.6.html for complete details of bzip2 and libbzip2 License v1.0.6"""))
        setattr(cls, "CECILL-1.0",
            PermissibleValue(
                text="CECILL-1.0",
                description="""Visit https://spdx.org/licenses/CECILL-1.0.html for complete details of CeCILL Free Software License Agreement v1.0"""))
        setattr(cls, "CECILL-1.1",
            PermissibleValue(
                text="CECILL-1.1",
                description="""Visit https://spdx.org/licenses/CECILL-1.1.html for complete details of CeCILL Free Software License Agreement v1.1"""))
        setattr(cls, "CECILL-2.0",
            PermissibleValue(
                text="CECILL-2.0",
                description="""Visit https://spdx.org/licenses/CECILL-2.0.html for complete details of CeCILL Free Software License Agreement v2.0"""))
        setattr(cls, "CECILL-2.1",
            PermissibleValue(
                text="CECILL-2.1",
                description="""Visit https://spdx.org/licenses/CECILL-2.1.html for complete details of CeCILL Free Software License Agreement v2.1"""))
        setattr(cls, "CECILL-B",
            PermissibleValue(
                text="CECILL-B",
                description="""Visit https://spdx.org/licenses/CECILL-B.html for complete details of CeCILL-B Free Software License Agreement"""))
        setattr(cls, "CECILL-C",
            PermissibleValue(
                text="CECILL-C",
                description="""Visit https://spdx.org/licenses/CECILL-C.html for complete details of CeCILL-C Free Software License Agreement"""))
        setattr(cls, "CERN-OHL-1.1",
            PermissibleValue(
                text="CERN-OHL-1.1",
                description="""Visit https://spdx.org/licenses/CERN-OHL-1.1.html for complete details of CERN Open Hardware Licence v1.1"""))
        setattr(cls, "CERN-OHL-1.2",
            PermissibleValue(
                text="CERN-OHL-1.2",
                description="""Visit https://spdx.org/licenses/CERN-OHL-1.2.html for complete details of CERN Open Hardware Licence v1.2"""))
        setattr(cls, "CERN-OHL-P-2.0",
            PermissibleValue(
                text="CERN-OHL-P-2.0",
                description="""Visit https://spdx.org/licenses/CERN-OHL-P-2.0.html for complete details of CERN Open Hardware Licence Version 2 - Permissive"""))
        setattr(cls, "CERN-OHL-S-2.0",
            PermissibleValue(
                text="CERN-OHL-S-2.0",
                description="""Visit https://spdx.org/licenses/CERN-OHL-S-2.0.html for complete details of CERN Open Hardware Licence Version 2 - Strongly Reciprocal"""))
        setattr(cls, "CERN-OHL-W-2.0",
            PermissibleValue(
                text="CERN-OHL-W-2.0",
                description="""Visit https://spdx.org/licenses/CERN-OHL-W-2.0.html for complete details of CERN Open Hardware Licence Version 2 - Weakly Reciprocal"""))
        setattr(cls, "check-cvs",
            PermissibleValue(
                text="check-cvs",
                description="""Visit https://spdx.org/licenses/check-cvs.html for complete details of check-cvs License"""))
        setattr(cls, "MIT-CMU",
            PermissibleValue(
                text="MIT-CMU",
                description="Visit https://spdx.org/licenses/MIT-CMU.html for complete details of CMU License"))
        setattr(cls, "CMU-Mach",
            PermissibleValue(
                text="CMU-Mach",
                description="Visit https://spdx.org/licenses/CMU-Mach.html for complete details of CMU Mach License"))
        setattr(cls, "CNRI-Jython",
            PermissibleValue(
                text="CNRI-Jython",
                description="""Visit https://spdx.org/licenses/CNRI-Jython.html for complete details of CNRI Jython License"""))
        setattr(cls, "CNRI-Python",
            PermissibleValue(
                text="CNRI-Python",
                description="""Visit https://spdx.org/licenses/CNRI-Python.html for complete details of CNRI Python License"""))
        setattr(cls, "CNRI-Python-GPL-Compatible",
            PermissibleValue(
                text="CNRI-Python-GPL-Compatible",
                description="""Visit https://spdx.org/licenses/CNRI-Python-GPL-Compatible.html for complete details of CNRI Python Open Source GPL Compatible License Agreement"""))
        setattr(cls, "CPOL-1.02",
            PermissibleValue(
                text="CPOL-1.02",
                description="""Visit https://spdx.org/licenses/CPOL-1.02.html for complete details of Code Project Open License 1.02"""))
        setattr(cls, "CDDL-1.0",
            PermissibleValue(
                text="CDDL-1.0",
                description="""Visit https://spdx.org/licenses/CDDL-1.0.html for complete details of Common Development and Distribution License 1.0"""))
        setattr(cls, "CDDL-1.1",
            PermissibleValue(
                text="CDDL-1.1",
                description="""Visit https://spdx.org/licenses/CDDL-1.1.html for complete details of Common Development and Distribution License 1.1"""))
        setattr(cls, "CDL-1.0",
            PermissibleValue(
                text="CDL-1.0",
                description="""Visit https://spdx.org/licenses/CDL-1.0.html for complete details of Common Documentation License 1.0"""))
        setattr(cls, "CPAL-1.0",
            PermissibleValue(
                text="CPAL-1.0",
                description="""Visit https://spdx.org/licenses/CPAL-1.0.html for complete details of Common Public Attribution License 1.0"""))
        setattr(cls, "CPL-1.0",
            PermissibleValue(
                text="CPL-1.0",
                description="""Visit https://spdx.org/licenses/CPL-1.0.html for complete details of Common Public License 1.0"""))
        setattr(cls, "CDLA-Permissive-1.0",
            PermissibleValue(
                text="CDLA-Permissive-1.0",
                description="""Visit https://spdx.org/licenses/CDLA-Permissive-1.0.html for complete details of Community Data License Agreement Permissive 1.0"""))
        setattr(cls, "CDLA-Permissive-2.0",
            PermissibleValue(
                text="CDLA-Permissive-2.0",
                description="""Visit https://spdx.org/licenses/CDLA-Permissive-2.0.html for complete details of Community Data License Agreement Permissive 2.0"""))
        setattr(cls, "CDLA-Sharing-1.0",
            PermissibleValue(
                text="CDLA-Sharing-1.0",
                description="""Visit https://spdx.org/licenses/CDLA-Sharing-1.0.html for complete details of Community Data License Agreement Sharing 1.0"""))
        setattr(cls, "Community-Spec-1.0",
            PermissibleValue(
                text="Community-Spec-1.0",
                description="""Visit https://spdx.org/licenses/Community-Spec-1.0.html for complete details of Community Specification License 1.0"""))
        setattr(cls, "C-UDA-1.0",
            PermissibleValue(
                text="C-UDA-1.0",
                description="""Visit https://spdx.org/licenses/C-UDA-1.0.html for complete details of Computational Use of Data Agreement v1.0"""))
        setattr(cls, "CATOSL-1.1",
            PermissibleValue(
                text="CATOSL-1.1",
                description="""Visit https://spdx.org/licenses/CATOSL-1.1.html for complete details of Computer Associates Trusted Open Source License 1.1"""))
        setattr(cls, "Condor-1.1",
            PermissibleValue(
                text="Condor-1.1",
                description="""Visit https://spdx.org/licenses/Condor-1.1.html for complete details of Condor Public License v1.1"""))
        setattr(cls, "COIL-1.0",
            PermissibleValue(
                text="COIL-1.0",
                description="""Visit https://spdx.org/licenses/COIL-1.0.html for complete details of Copyfree Open Innovation License"""))
        setattr(cls, "copyleft-next-0.3.0",
            PermissibleValue(
                text="copyleft-next-0.3.0",
                description="""Visit https://spdx.org/licenses/copyleft-next-0.3.0.html for complete details of copyleft-next 0.3.0"""))
        setattr(cls, "copyleft-next-0.3.1",
            PermissibleValue(
                text="copyleft-next-0.3.1",
                description="""Visit https://spdx.org/licenses/copyleft-next-0.3.1.html for complete details of copyleft-next 0.3.1"""))
        setattr(cls, "Cornell-Lossless-JPEG",
            PermissibleValue(
                text="Cornell-Lossless-JPEG",
                description="""Visit https://spdx.org/licenses/Cornell-Lossless-JPEG.html for complete details of Cornell Lossless JPEG License"""))
        setattr(cls, "CC-BY-1.0",
            PermissibleValue(
                text="CC-BY-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-1.0.html for complete details of Creative Commons Attribution 1.0 Generic"""))
        setattr(cls, "CC-BY-2.0",
            PermissibleValue(
                text="CC-BY-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-2.0.html for complete details of Creative Commons Attribution 2.0 Generic"""))
        setattr(cls, "CC-BY-2.5-AU",
            PermissibleValue(
                text="CC-BY-2.5-AU",
                description="""Visit https://spdx.org/licenses/CC-BY-2.5-AU.html for complete details of Creative Commons Attribution 2.5 Australia"""))
        setattr(cls, "CC-BY-2.5",
            PermissibleValue(
                text="CC-BY-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-2.5.html for complete details of Creative Commons Attribution 2.5 Generic"""))
        setattr(cls, "CC-BY-3.0-AT",
            PermissibleValue(
                text="CC-BY-3.0-AT",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0-AT.html for complete details of Creative Commons Attribution 3.0 Austria"""))
        setattr(cls, "CC-BY-3.0-DE",
            PermissibleValue(
                text="CC-BY-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0-DE.html for complete details of Creative Commons Attribution 3.0 Germany"""))
        setattr(cls, "CC-BY-3.0-IGO",
            PermissibleValue(
                text="CC-BY-3.0-IGO",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0-IGO.html for complete details of Creative Commons Attribution 3.0 IGO"""))
        setattr(cls, "CC-BY-3.0-NL",
            PermissibleValue(
                text="CC-BY-3.0-NL",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0-NL.html for complete details of Creative Commons Attribution 3.0 Netherlands"""))
        setattr(cls, "CC-BY-3.0-US",
            PermissibleValue(
                text="CC-BY-3.0-US",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0-US.html for complete details of Creative Commons Attribution 3.0 United States"""))
        setattr(cls, "CC-BY-3.0",
            PermissibleValue(
                text="CC-BY-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-3.0.html for complete details of Creative Commons Attribution 3.0 Unported"""))
        setattr(cls, "CC-BY-4.0",
            PermissibleValue(
                text="CC-BY-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-4.0.html for complete details of Creative Commons Attribution 4.0 International"""))
        setattr(cls, "CC-BY-ND-1.0",
            PermissibleValue(
                text="CC-BY-ND-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-1.0.html for complete details of Creative Commons Attribution No Derivatives 1.0 Generic"""))
        setattr(cls, "CC-BY-ND-2.0",
            PermissibleValue(
                text="CC-BY-ND-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-2.0.html for complete details of Creative Commons Attribution No Derivatives 2.0 Generic"""))
        setattr(cls, "CC-BY-ND-2.5",
            PermissibleValue(
                text="CC-BY-ND-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-2.5.html for complete details of Creative Commons Attribution No Derivatives 2.5 Generic"""))
        setattr(cls, "CC-BY-ND-3.0-DE",
            PermissibleValue(
                text="CC-BY-ND-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-3.0-DE.html for complete details of Creative Commons Attribution No Derivatives 3.0 Germany"""))
        setattr(cls, "CC-BY-ND-3.0",
            PermissibleValue(
                text="CC-BY-ND-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-3.0.html for complete details of Creative Commons Attribution No Derivatives 3.0 Unported"""))
        setattr(cls, "CC-BY-ND-4.0",
            PermissibleValue(
                text="CC-BY-ND-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-ND-4.0.html for complete details of Creative Commons Attribution No Derivatives 4.0 International"""))
        setattr(cls, "CC-BY-NC-1.0",
            PermissibleValue(
                text="CC-BY-NC-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-1.0.html for complete details of Creative Commons Attribution Non Commercial 1.0 Generic"""))
        setattr(cls, "CC-BY-NC-2.0",
            PermissibleValue(
                text="CC-BY-NC-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-2.0.html for complete details of Creative Commons Attribution Non Commercial 2.0 Generic"""))
        setattr(cls, "CC-BY-NC-2.5",
            PermissibleValue(
                text="CC-BY-NC-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-2.5.html for complete details of Creative Commons Attribution Non Commercial 2.5 Generic"""))
        setattr(cls, "CC-BY-NC-3.0-DE",
            PermissibleValue(
                text="CC-BY-NC-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-3.0-DE.html for complete details of Creative Commons Attribution Non Commercial 3.0 Germany"""))
        setattr(cls, "CC-BY-NC-3.0",
            PermissibleValue(
                text="CC-BY-NC-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-3.0.html for complete details of Creative Commons Attribution Non Commercial 3.0 Unported"""))
        setattr(cls, "CC-BY-NC-4.0",
            PermissibleValue(
                text="CC-BY-NC-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-4.0.html for complete details of Creative Commons Attribution Non Commercial 4.0 International"""))
        setattr(cls, "CC-BY-NC-ND-1.0",
            PermissibleValue(
                text="CC-BY-NC-ND-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-1.0.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic"""))
        setattr(cls, "CC-BY-NC-ND-2.0",
            PermissibleValue(
                text="CC-BY-NC-ND-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-2.0.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic"""))
        setattr(cls, "CC-BY-NC-ND-2.5",
            PermissibleValue(
                text="CC-BY-NC-ND-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-2.5.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic"""))
        setattr(cls, "CC-BY-NC-ND-3.0-DE",
            PermissibleValue(
                text="CC-BY-NC-ND-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-3.0-DE.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany"""))
        setattr(cls, "CC-BY-NC-ND-3.0-IGO",
            PermissibleValue(
                text="CC-BY-NC-ND-3.0-IGO",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-3.0-IGO.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO"""))
        setattr(cls, "CC-BY-NC-ND-3.0",
            PermissibleValue(
                text="CC-BY-NC-ND-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-3.0.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported"""))
        setattr(cls, "CC-BY-NC-ND-4.0",
            PermissibleValue(
                text="CC-BY-NC-ND-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-ND-4.0.html for complete details of Creative Commons Attribution Non Commercial No Derivatives 4.0 International"""))
        setattr(cls, "CC-BY-NC-SA-1.0",
            PermissibleValue(
                text="CC-BY-NC-SA-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-1.0.html for complete details of Creative Commons Attribution Non Commercial Share Alike 1.0 Generic"""))
        setattr(cls, "CC-BY-NC-SA-2.0-UK",
            PermissibleValue(
                text="CC-BY-NC-SA-2.0-UK",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-2.0-UK.html for complete details of Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales"""))
        setattr(cls, "CC-BY-NC-SA-2.0",
            PermissibleValue(
                text="CC-BY-NC-SA-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-2.0.html for complete details of Creative Commons Attribution Non Commercial Share Alike 2.0 Generic"""))
        setattr(cls, "CC-BY-NC-SA-2.0-DE",
            PermissibleValue(
                text="CC-BY-NC-SA-2.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-2.0-DE.html for complete details of Creative Commons Attribution Non Commercial Share Alike 2.0 Germany"""))
        setattr(cls, "CC-BY-NC-SA-2.5",
            PermissibleValue(
                text="CC-BY-NC-SA-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-2.5.html for complete details of Creative Commons Attribution Non Commercial Share Alike 2.5 Generic"""))
        setattr(cls, "CC-BY-NC-SA-3.0-DE",
            PermissibleValue(
                text="CC-BY-NC-SA-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-3.0-DE.html for complete details of Creative Commons Attribution Non Commercial Share Alike 3.0 Germany"""))
        setattr(cls, "CC-BY-NC-SA-3.0-IGO",
            PermissibleValue(
                text="CC-BY-NC-SA-3.0-IGO",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-3.0-IGO.html for complete details of Creative Commons Attribution Non Commercial Share Alike 3.0 IGO"""))
        setattr(cls, "CC-BY-NC-SA-3.0",
            PermissibleValue(
                text="CC-BY-NC-SA-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-3.0.html for complete details of Creative Commons Attribution Non Commercial Share Alike 3.0 Unported"""))
        setattr(cls, "CC-BY-NC-SA-4.0",
            PermissibleValue(
                text="CC-BY-NC-SA-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-4.0.html for complete details of Creative Commons Attribution Non Commercial Share Alike 4.0 International"""))
        setattr(cls, "CC-BY-SA-1.0",
            PermissibleValue(
                text="CC-BY-SA-1.0",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-1.0.html for complete details of Creative Commons Attribution Share Alike 1.0 Generic"""))
        setattr(cls, "CC-BY-SA-2.0-UK",
            PermissibleValue(
                text="CC-BY-SA-2.0-UK",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-2.0-UK.html for complete details of Creative Commons Attribution Share Alike 2.0 England and Wales"""))
        setattr(cls, "CC-BY-SA-2.0",
            PermissibleValue(
                text="CC-BY-SA-2.0",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-2.0.html for complete details of Creative Commons Attribution Share Alike 2.0 Generic"""))
        setattr(cls, "CC-BY-SA-2.1-JP",
            PermissibleValue(
                text="CC-BY-SA-2.1-JP",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-2.1-JP.html for complete details of Creative Commons Attribution Share Alike 2.1 Japan"""))
        setattr(cls, "CC-BY-SA-2.5",
            PermissibleValue(
                text="CC-BY-SA-2.5",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-2.5.html for complete details of Creative Commons Attribution Share Alike 2.5 Generic"""))
        setattr(cls, "CC-BY-SA-3.0-AT",
            PermissibleValue(
                text="CC-BY-SA-3.0-AT",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-3.0-AT.html for complete details of Creative Commons Attribution Share Alike 3.0 Austria"""))
        setattr(cls, "CC-BY-SA-3.0-DE",
            PermissibleValue(
                text="CC-BY-SA-3.0-DE",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-3.0-DE.html for complete details of Creative Commons Attribution Share Alike 3.0 Germany"""))
        setattr(cls, "CC-BY-SA-3.0",
            PermissibleValue(
                text="CC-BY-SA-3.0",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-3.0.html for complete details of Creative Commons Attribution Share Alike 3.0 Unported"""))
        setattr(cls, "CC-BY-SA-4.0",
            PermissibleValue(
                text="CC-BY-SA-4.0",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-4.0.html for complete details of Creative Commons Attribution Share Alike 4.0 International"""))
        setattr(cls, "CC-BY-NC-SA-2.0-FR",
            PermissibleValue(
                text="CC-BY-NC-SA-2.0-FR",
                description="""Visit https://spdx.org/licenses/CC-BY-NC-SA-2.0-FR.html for complete details of Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France"""))
        setattr(cls, "CC-BY-SA-3.0-IGO",
            PermissibleValue(
                text="CC-BY-SA-3.0-IGO",
                description="""Visit https://spdx.org/licenses/CC-BY-SA-3.0-IGO.html for complete details of Creative Commons Attribution-ShareAlike 3.0 IGO"""))
        setattr(cls, "CC-PDDC",
            PermissibleValue(
                text="CC-PDDC",
                description="""Visit https://spdx.org/licenses/CC-PDDC.html for complete details of Creative Commons Public Domain Dedication and Certification"""))
        setattr(cls, "CC0-1.0",
            PermissibleValue(
                text="CC0-1.0",
                description="""Visit https://spdx.org/licenses/CC0-1.0.html for complete details of Creative Commons Zero v1.0 Universal"""))
        setattr(cls, "CAL-1.0",
            PermissibleValue(
                text="CAL-1.0",
                description="""Visit https://spdx.org/licenses/CAL-1.0.html for complete details of Cryptographic Autonomy License 1.0"""))
        setattr(cls, "CAL-1.0-Combined-Work-Exception",
            PermissibleValue(
                text="CAL-1.0-Combined-Work-Exception",
                description="""Visit https://spdx.org/licenses/CAL-1.0-Combined-Work-Exception.html for complete details of Cryptographic Autonomy License 1.0 (Combined Work Exception)"""))
        setattr(cls, "CUA-OPL-1.0",
            PermissibleValue(
                text="CUA-OPL-1.0",
                description="""Visit https://spdx.org/licenses/CUA-OPL-1.0.html for complete details of CUA Office Public License v1.0"""))
        setattr(cls, "DL-DE-BY-2.0",
            PermissibleValue(
                text="DL-DE-BY-2.0",
                description="""Visit https://spdx.org/licenses/DL-DE-BY-2.0.html for complete details of Data licence Germany attribution version 2.0"""))
        setattr(cls, "DL-DE-ZERO-2.0",
            PermissibleValue(
                text="DL-DE-ZERO-2.0",
                description="""Visit https://spdx.org/licenses/DL-DE-ZERO-2.0.html for complete details of Data licence Germany zero version 2.0"""))
        setattr(cls, "DRL-1.0",
            PermissibleValue(
                text="DRL-1.0",
                description="""Visit https://spdx.org/licenses/DRL-1.0.html for complete details of Detection Rule License 1.0"""))
        setattr(cls, "D-FSL-1.0",
            PermissibleValue(
                text="D-FSL-1.0",
                description="""Visit https://spdx.org/licenses/D-FSL-1.0.html for complete details of Deutsche Freie Software Lizenz"""))
        setattr(cls, "EPL-1.0",
            PermissibleValue(
                text="EPL-1.0",
                description="""Visit https://spdx.org/licenses/EPL-1.0.html for complete details of Eclipse Public License 1.0"""))
        setattr(cls, "EPL-2.0",
            PermissibleValue(
                text="EPL-2.0",
                description="""Visit https://spdx.org/licenses/EPL-2.0.html for complete details of Eclipse Public License 2.0"""))
        setattr(cls, "ECL-1.0",
            PermissibleValue(
                text="ECL-1.0",
                description="""Visit https://spdx.org/licenses/ECL-1.0.html for complete details of Educational Community License v1.0"""))
        setattr(cls, "ECL-2.0",
            PermissibleValue(
                text="ECL-2.0",
                description="""Visit https://spdx.org/licenses/ECL-2.0.html for complete details of Educational Community License v2.0"""))
        setattr(cls, "EFL-1.0",
            PermissibleValue(
                text="EFL-1.0",
                description="""Visit https://spdx.org/licenses/EFL-1.0.html for complete details of Eiffel Forum License v1.0"""))
        setattr(cls, "EFL-2.0",
            PermissibleValue(
                text="EFL-2.0",
                description="""Visit https://spdx.org/licenses/EFL-2.0.html for complete details of Eiffel Forum License v2.0"""))
        setattr(cls, "Elastic-2.0",
            PermissibleValue(
                text="Elastic-2.0",
                description="""Visit https://spdx.org/licenses/Elastic-2.0.html for complete details of Elastic License 2.0"""))
        setattr(cls, "MIT-advertising",
            PermissibleValue(
                text="MIT-advertising",
                description="""Visit https://spdx.org/licenses/MIT-advertising.html for complete details of Enlightenment License (e16)"""))
        setattr(cls, "MIT-enna",
            PermissibleValue(
                text="MIT-enna",
                description="Visit https://spdx.org/licenses/MIT-enna.html for complete details of enna License"))
        setattr(cls, "ErlPL-1.1",
            PermissibleValue(
                text="ErlPL-1.1",
                description="""Visit https://spdx.org/licenses/ErlPL-1.1.html for complete details of Erlang Public License v1.1"""))
        setattr(cls, "etalab-2.0",
            PermissibleValue(
                text="etalab-2.0",
                description="""Visit https://spdx.org/licenses/etalab-2.0.html for complete details of Etalab Open License 2.0"""))
        setattr(cls, "EUPL-1.0",
            PermissibleValue(
                text="EUPL-1.0",
                description="""Visit https://spdx.org/licenses/EUPL-1.0.html for complete details of European Union Public License 1.0"""))
        setattr(cls, "EUPL-1.1",
            PermissibleValue(
                text="EUPL-1.1",
                description="""Visit https://spdx.org/licenses/EUPL-1.1.html for complete details of European Union Public License 1.1"""))
        setattr(cls, "EUPL-1.2",
            PermissibleValue(
                text="EUPL-1.2",
                description="""Visit https://spdx.org/licenses/EUPL-1.2.html for complete details of European Union Public License 1.2"""))
        setattr(cls, "MIT-feh",
            PermissibleValue(
                text="MIT-feh",
                description="Visit https://spdx.org/licenses/MIT-feh.html for complete details of feh License"))
        setattr(cls, "Ferguson-Twofish",
            PermissibleValue(
                text="Ferguson-Twofish",
                description="""Visit https://spdx.org/licenses/Ferguson-Twofish.html for complete details of Ferguson Twofish License"""))
        setattr(cls, "Frameworx-1.0",
            PermissibleValue(
                text="Frameworx-1.0",
                description="""Visit https://spdx.org/licenses/Frameworx-1.0.html for complete details of Frameworx Open License 1.0"""))
        setattr(cls, "FDK-AAC",
            PermissibleValue(
                text="FDK-AAC",
                description="""Visit https://spdx.org/licenses/FDK-AAC.html for complete details of Fraunhofer FDK AAC Codec Library"""))
        setattr(cls, "FreeBSD-DOC",
            PermissibleValue(
                text="FreeBSD-DOC",
                description="""Visit https://spdx.org/licenses/FreeBSD-DOC.html for complete details of FreeBSD Documentation License"""))
        setattr(cls, "AGPL-3.0-only",
            PermissibleValue(
                text="AGPL-3.0-only",
                description="""Visit https://spdx.org/licenses/AGPL-3.0-only.html for complete details of GNU Affero General Public License v3.0 only"""))
        setattr(cls, "AGPL-3.0-or-later",
            PermissibleValue(
                text="AGPL-3.0-or-later",
                description="""Visit https://spdx.org/licenses/AGPL-3.0-or-later.html for complete details of GNU Affero General Public License v3.0 or later"""))
        setattr(cls, "GFDL-1.1-only",
            PermissibleValue(
                text="GFDL-1.1-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-only.html for complete details of GNU Free Documentation License v1.1 only"""))
        setattr(cls, "GFDL-1.1-invariants-only",
            PermissibleValue(
                text="GFDL-1.1-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-invariants-only.html for complete details of GNU Free Documentation License v1.1 only - invariants"""))
        setattr(cls, "GFDL-1.1-no-invariants-only",
            PermissibleValue(
                text="GFDL-1.1-no-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-no-invariants-only.html for complete details of GNU Free Documentation License v1.1 only - no invariants"""))
        setattr(cls, "GFDL-1.1-or-later",
            PermissibleValue(
                text="GFDL-1.1-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-or-later.html for complete details of GNU Free Documentation License v1.1 or later"""))
        setattr(cls, "GFDL-1.1-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.1-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-invariants-or-later.html for complete details of GNU Free Documentation License v1.1 or later - invariants"""))
        setattr(cls, "GFDL-1.1-no-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.1-no-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.1-no-invariants-or-later.html for complete details of GNU Free Documentation License v1.1 or later - no invariants"""))
        setattr(cls, "GFDL-1.2-only",
            PermissibleValue(
                text="GFDL-1.2-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-only.html for complete details of GNU Free Documentation License v1.2 only"""))
        setattr(cls, "GFDL-1.2-invariants-only",
            PermissibleValue(
                text="GFDL-1.2-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-invariants-only.html for complete details of GNU Free Documentation License v1.2 only - invariants"""))
        setattr(cls, "GFDL-1.2-no-invariants-only",
            PermissibleValue(
                text="GFDL-1.2-no-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-no-invariants-only.html for complete details of GNU Free Documentation License v1.2 only - no invariants"""))
        setattr(cls, "GFDL-1.2-or-later",
            PermissibleValue(
                text="GFDL-1.2-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-or-later.html for complete details of GNU Free Documentation License v1.2 or later"""))
        setattr(cls, "GFDL-1.2-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.2-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-invariants-or-later.html for complete details of GNU Free Documentation License v1.2 or later - invariants"""))
        setattr(cls, "GFDL-1.2-no-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.2-no-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.2-no-invariants-or-later.html for complete details of GNU Free Documentation License v1.2 or later - no invariants"""))
        setattr(cls, "GFDL-1.3-only",
            PermissibleValue(
                text="GFDL-1.3-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-only.html for complete details of GNU Free Documentation License v1.3 only"""))
        setattr(cls, "GFDL-1.3-invariants-only",
            PermissibleValue(
                text="GFDL-1.3-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-invariants-only.html for complete details of GNU Free Documentation License v1.3 only - invariants"""))
        setattr(cls, "GFDL-1.3-no-invariants-only",
            PermissibleValue(
                text="GFDL-1.3-no-invariants-only",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-no-invariants-only.html for complete details of GNU Free Documentation License v1.3 only - no invariants"""))
        setattr(cls, "GFDL-1.3-or-later",
            PermissibleValue(
                text="GFDL-1.3-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-or-later.html for complete details of GNU Free Documentation License v1.3 or later"""))
        setattr(cls, "GFDL-1.3-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.3-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-invariants-or-later.html for complete details of GNU Free Documentation License v1.3 or later - invariants"""))
        setattr(cls, "GFDL-1.3-no-invariants-or-later",
            PermissibleValue(
                text="GFDL-1.3-no-invariants-or-later",
                description="""Visit https://spdx.org/licenses/GFDL-1.3-no-invariants-or-later.html for complete details of GNU Free Documentation License v1.3 or later - no invariants"""))
        setattr(cls, "GPL-1.0-only",
            PermissibleValue(
                text="GPL-1.0-only",
                description="""Visit https://spdx.org/licenses/GPL-1.0-only.html for complete details of GNU General Public License v1.0 only"""))
        setattr(cls, "GPL-1.0-or-later",
            PermissibleValue(
                text="GPL-1.0-or-later",
                description="""Visit https://spdx.org/licenses/GPL-1.0-or-later.html for complete details of GNU General Public License v1.0 or later"""))
        setattr(cls, "GPL-2.0-only",
            PermissibleValue(
                text="GPL-2.0-only",
                description="""Visit https://spdx.org/licenses/GPL-2.0-only.html for complete details of GNU General Public License v2.0 only"""))
        setattr(cls, "GPL-2.0-or-later",
            PermissibleValue(
                text="GPL-2.0-or-later",
                description="""Visit https://spdx.org/licenses/GPL-2.0-or-later.html for complete details of GNU General Public License v2.0 or later"""))
        setattr(cls, "GPL-3.0-only",
            PermissibleValue(
                text="GPL-3.0-only",
                description="""Visit https://spdx.org/licenses/GPL-3.0-only.html for complete details of GNU General Public License v3.0 only"""))
        setattr(cls, "GPL-3.0-or-later",
            PermissibleValue(
                text="GPL-3.0-or-later",
                description="""Visit https://spdx.org/licenses/GPL-3.0-or-later.html for complete details of GNU General Public License v3.0 or later"""))
        setattr(cls, "LGPL-2.1-only",
            PermissibleValue(
                text="LGPL-2.1-only",
                description="""Visit https://spdx.org/licenses/LGPL-2.1-only.html for complete details of GNU Lesser General Public License v2.1 only"""))
        setattr(cls, "LGPL-2.1-or-later",
            PermissibleValue(
                text="LGPL-2.1-or-later",
                description="""Visit https://spdx.org/licenses/LGPL-2.1-or-later.html for complete details of GNU Lesser General Public License v2.1 or later"""))
        setattr(cls, "LGPL-3.0-only",
            PermissibleValue(
                text="LGPL-3.0-only",
                description="""Visit https://spdx.org/licenses/LGPL-3.0-only.html for complete details of GNU Lesser General Public License v3.0 only"""))
        setattr(cls, "LGPL-3.0-or-later",
            PermissibleValue(
                text="LGPL-3.0-or-later",
                description="""Visit https://spdx.org/licenses/LGPL-3.0-or-later.html for complete details of GNU Lesser General Public License v3.0 or later"""))
        setattr(cls, "LGPL-2.0-only",
            PermissibleValue(
                text="LGPL-2.0-only",
                description="""Visit https://spdx.org/licenses/LGPL-2.0-only.html for complete details of GNU Library General Public License v2 only"""))
        setattr(cls, "LGPL-2.0-or-later",
            PermissibleValue(
                text="LGPL-2.0-or-later",
                description="""Visit https://spdx.org/licenses/LGPL-2.0-or-later.html for complete details of GNU Library General Public License v2 or later"""))
        setattr(cls, "Graphics-Gems",
            PermissibleValue(
                text="Graphics-Gems",
                description="""Visit https://spdx.org/licenses/Graphics-Gems.html for complete details of Graphics Gems License"""))
        setattr(cls, "gSOAP-1.3b",
            PermissibleValue(
                text="gSOAP-1.3b",
                description="""Visit https://spdx.org/licenses/gSOAP-1.3b.html for complete details of gSOAP Public License v1.3b"""))
        setattr(cls, "HP-1986",
            PermissibleValue(
                text="HP-1986",
                description="""Visit https://spdx.org/licenses/HP-1986.html for complete details of Hewlett-Packard 1986 License"""))
        setattr(cls, "HP-1989",
            PermissibleValue(
                text="HP-1989",
                description="""Visit https://spdx.org/licenses/HP-1989.html for complete details of Hewlett-Packard 1989 License"""))
        setattr(cls, "BSD-3-Clause-HP",
            PermissibleValue(
                text="BSD-3-Clause-HP",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-HP.html for complete details of Hewlett-Packard BSD variant license"""))
        setattr(cls, "Hippocratic-2.1",
            PermissibleValue(
                text="Hippocratic-2.1",
                description="""Visit https://spdx.org/licenses/Hippocratic-2.1.html for complete details of Hippocratic License 2.1"""))
        setattr(cls, "HPND-DEC",
            PermissibleValue(
                text="HPND-DEC",
                description="""Visit https://spdx.org/licenses/HPND-DEC.html for complete details of Historical Permission Notice and Disclaimer - DEC variant"""))
        setattr(cls, "HPND-doc-sell",
            PermissibleValue(
                text="HPND-doc-sell",
                description="""Visit https://spdx.org/licenses/HPND-doc-sell.html for complete details of Historical Permission Notice and Disclaimer - documentation sell variant"""))
        setattr(cls, "HPND-doc",
            PermissibleValue(
                text="HPND-doc",
                description="""Visit https://spdx.org/licenses/HPND-doc.html for complete details of Historical Permission Notice and Disclaimer - documentation variant"""))
        setattr(cls, "HPND-Markus-Kuhn",
            PermissibleValue(
                text="HPND-Markus-Kuhn",
                description="""Visit https://spdx.org/licenses/HPND-Markus-Kuhn.html for complete details of Historical Permission Notice and Disclaimer - Markus Kuhn variant"""))
        setattr(cls, "HPND-Pbmplus",
            PermissibleValue(
                text="HPND-Pbmplus",
                description="""Visit https://spdx.org/licenses/HPND-Pbmplus.html for complete details of Historical Permission Notice and Disclaimer - Pbmplus variant"""))
        setattr(cls, "HPND-sell-regexpr",
            PermissibleValue(
                text="HPND-sell-regexpr",
                description="""Visit https://spdx.org/licenses/HPND-sell-regexpr.html for complete details of Historical Permission Notice and Disclaimer - sell regexpr variant"""))
        setattr(cls, "HPND-sell-variant",
            PermissibleValue(
                text="HPND-sell-variant",
                description="""Visit https://spdx.org/licenses/HPND-sell-variant.html for complete details of Historical Permission Notice and Disclaimer - sell variant"""))
        setattr(cls, "HPND-UC",
            PermissibleValue(
                text="HPND-UC",
                description="""Visit https://spdx.org/licenses/HPND-UC.html for complete details of Historical Permission Notice and Disclaimer - University of California variant"""))
        setattr(cls, "HPND-sell-variant-MIT-disclaimer",
            PermissibleValue(
                text="HPND-sell-variant-MIT-disclaimer",
                description="""Visit https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer.html for complete details of HPND sell variant with MIT disclaimer"""))
        setattr(cls, "HPND-export-US",
            PermissibleValue(
                text="HPND-export-US",
                description="""Visit https://spdx.org/licenses/HPND-export-US.html for complete details of HPND with US Government export control warning"""))
        setattr(cls, "HPND-export-US-modify",
            PermissibleValue(
                text="HPND-export-US-modify",
                description="""Visit https://spdx.org/licenses/HPND-export-US-modify.html for complete details of HPND with US Government export control warning and modification rqmt"""))
        setattr(cls, "IBM-pibs",
            PermissibleValue(
                text="IBM-pibs",
                description="""Visit https://spdx.org/licenses/IBM-pibs.html for complete details of IBM PowerPC Initialization and Boot Software"""))
        setattr(cls, "IPL-1.0",
            PermissibleValue(
                text="IPL-1.0",
                description="""Visit https://spdx.org/licenses/IPL-1.0.html for complete details of IBM Public License v1.0"""))
        setattr(cls, "IEC-Code-Components-EULA",
            PermissibleValue(
                text="IEC-Code-Components-EULA",
                description="""Visit https://spdx.org/licenses/IEC-Code-Components-EULA.html for complete details of IEC Code Components End-user licence agreement"""))
        setattr(cls, "IJG-short",
            PermissibleValue(
                text="IJG-short",
                description="""Visit https://spdx.org/licenses/IJG-short.html for complete details of Independent JPEG Group License - short"""))
        setattr(cls, "Info-ZIP",
            PermissibleValue(
                text="Info-ZIP",
                description="Visit https://spdx.org/licenses/Info-ZIP.html for complete details of Info-ZIP License"))
        setattr(cls, "Inner-Net-2.0",
            PermissibleValue(
                text="Inner-Net-2.0",
                description="""Visit https://spdx.org/licenses/Inner-Net-2.0.html for complete details of Inner Net License v2.0"""))
        setattr(cls, "Intel-ACPI",
            PermissibleValue(
                text="Intel-ACPI",
                description="""Visit https://spdx.org/licenses/Intel-ACPI.html for complete details of Intel ACPI Software License Agreement"""))
        setattr(cls, "Interbase-1.0",
            PermissibleValue(
                text="Interbase-1.0",
                description="""Visit https://spdx.org/licenses/Interbase-1.0.html for complete details of Interbase Public License v1.0"""))
        setattr(cls, "JasPer-2.0",
            PermissibleValue(
                text="JasPer-2.0",
                description="Visit https://spdx.org/licenses/JasPer-2.0.html for complete details of JasPer License"))
        setattr(cls, "JPL-image",
            PermissibleValue(
                text="JPL-image",
                description="""Visit https://spdx.org/licenses/JPL-image.html for complete details of JPL Image Use Policy"""))
        setattr(cls, "Knuth-CTAN",
            PermissibleValue(
                text="Knuth-CTAN",
                description="""Visit https://spdx.org/licenses/Knuth-CTAN.html for complete details of Knuth CTAN License"""))
        setattr(cls, "LPPL-1.0",
            PermissibleValue(
                text="LPPL-1.0",
                description="""Visit https://spdx.org/licenses/LPPL-1.0.html for complete details of LaTeX Project Public License v1.0"""))
        setattr(cls, "LPPL-1.1",
            PermissibleValue(
                text="LPPL-1.1",
                description="""Visit https://spdx.org/licenses/LPPL-1.1.html for complete details of LaTeX Project Public License v1.1"""))
        setattr(cls, "LPPL-1.2",
            PermissibleValue(
                text="LPPL-1.2",
                description="""Visit https://spdx.org/licenses/LPPL-1.2.html for complete details of LaTeX Project Public License v1.2"""))
        setattr(cls, "LPPL-1.3a",
            PermissibleValue(
                text="LPPL-1.3a",
                description="""Visit https://spdx.org/licenses/LPPL-1.3a.html for complete details of LaTeX Project Public License v1.3a"""))
        setattr(cls, "LPPL-1.3c",
            PermissibleValue(
                text="LPPL-1.3c",
                description="""Visit https://spdx.org/licenses/LPPL-1.3c.html for complete details of LaTeX Project Public License v1.3c"""))
        setattr(cls, "Latex2e-translated-notice",
            PermissibleValue(
                text="Latex2e-translated-notice",
                description="""Visit https://spdx.org/licenses/Latex2e-translated-notice.html for complete details of Latex2e with translated notice permission"""))
        setattr(cls, "BSD-3-Clause-LBNL",
            PermissibleValue(
                text="BSD-3-Clause-LBNL",
                description="""Visit https://spdx.org/licenses/BSD-3-Clause-LBNL.html for complete details of Lawrence Berkeley National Labs BSD variant license"""))
        setattr(cls, "libselinux-1.0",
            PermissibleValue(
                text="libselinux-1.0",
                description="""Visit https://spdx.org/licenses/libselinux-1.0.html for complete details of libselinux public domain notice"""))
        setattr(cls, "libutil-David-Nugent",
            PermissibleValue(
                text="libutil-David-Nugent",
                description="""Visit https://spdx.org/licenses/libutil-David-Nugent.html for complete details of libutil David Nugent License"""))
        setattr(cls, "LAL-1.2",
            PermissibleValue(
                text="LAL-1.2",
                description="""Visit https://spdx.org/licenses/LAL-1.2.html for complete details of Licence Art Libre 1.2"""))
        setattr(cls, "LAL-1.3",
            PermissibleValue(
                text="LAL-1.3",
                description="""Visit https://spdx.org/licenses/LAL-1.3.html for complete details of Licence Art Libre 1.3"""))
        setattr(cls, "LiLiQ-P-1.1",
            PermissibleValue(
                text="LiLiQ-P-1.1",
                description="""Visit https://spdx.org/licenses/LiLiQ-P-1.1.html for complete details of Licence Libre du Quebec Permissive version 1.1"""))
        setattr(cls, "LiLiQ-Rplus-1.1",
            PermissibleValue(
                text="LiLiQ-Rplus-1.1",
                description="""Visit https://spdx.org/licenses/LiLiQ-Rplus-1.1.html for complete details of Licence Libre du Quebec Reciprocite forte version 1.1"""))
        setattr(cls, "LiLiQ-R-1.1",
            PermissibleValue(
                text="LiLiQ-R-1.1",
                description="""Visit https://spdx.org/licenses/LiLiQ-R-1.1.html for complete details of Licence Libre du Quebec Reciprocite version 1.1"""))
        setattr(cls, "Linux-OpenIB",
            PermissibleValue(
                text="Linux-OpenIB",
                description="""Visit https://spdx.org/licenses/Linux-OpenIB.html for complete details of Linux Kernel Variant of OpenIB.org license"""))
        setattr(cls, "Linux-man-pages-1-para",
            PermissibleValue(
                text="Linux-man-pages-1-para",
                description="""Visit https://spdx.org/licenses/Linux-man-pages-1-para.html for complete details of Linux man-pages 1 paragraph"""))
        setattr(cls, "Linux-man-pages-copyleft",
            PermissibleValue(
                text="Linux-man-pages-copyleft",
                description="""Visit https://spdx.org/licenses/Linux-man-pages-copyleft.html for complete details of Linux man-pages Copyleft"""))
        setattr(cls, "Linux-man-pages-copyleft-2-para",
            PermissibleValue(
                text="Linux-man-pages-copyleft-2-para",
                description="""Visit https://spdx.org/licenses/Linux-man-pages-copyleft-2-para.html for complete details of Linux man-pages Copyleft - 2 paragraphs"""))
        setattr(cls, "Linux-man-pages-copyleft-var",
            PermissibleValue(
                text="Linux-man-pages-copyleft-var",
                description="""Visit https://spdx.org/licenses/Linux-man-pages-copyleft-var.html for complete details of Linux man-pages Copyleft Variant"""))
        setattr(cls, "LPL-1.02",
            PermissibleValue(
                text="LPL-1.02",
                description="""Visit https://spdx.org/licenses/LPL-1.02.html for complete details of Lucent Public License v1.02"""))
        setattr(cls, "LPL-1.0",
            PermissibleValue(
                text="LPL-1.0",
                description="""Visit https://spdx.org/licenses/LPL-1.0.html for complete details of Lucent Public License Version 1.0"""))
        setattr(cls, "Lucida-Bitmap-Fonts",
            PermissibleValue(
                text="Lucida-Bitmap-Fonts",
                description="""Visit https://spdx.org/licenses/Lucida-Bitmap-Fonts.html for complete details of Lucida Bitmap Fonts License"""))
        setattr(cls, "LZMA-SDK-9.11-to-9.20",
            PermissibleValue(
                text="LZMA-SDK-9.11-to-9.20",
                description="""Visit https://spdx.org/licenses/LZMA-SDK-9.11-to-9.20.html for complete details of LZMA SDK License (versions 9.11 to 9.20)"""))
        setattr(cls, "LZMA-SDK-9.22",
            PermissibleValue(
                text="LZMA-SDK-9.22",
                description="""Visit https://spdx.org/licenses/LZMA-SDK-9.22.html for complete details of LZMA SDK License (versions 9.22 and beyond)"""))
        setattr(cls, "Martin-Birgmeier",
            PermissibleValue(
                text="Martin-Birgmeier",
                description="""Visit https://spdx.org/licenses/Martin-Birgmeier.html for complete details of Martin Birgmeier License"""))
        setattr(cls, "McPhee-slideshow",
            PermissibleValue(
                text="McPhee-slideshow",
                description="""Visit https://spdx.org/licenses/McPhee-slideshow.html for complete details of McPhee Slideshow License"""))
        setattr(cls, "MS-LPL",
            PermissibleValue(
                text="MS-LPL",
                description="""Visit https://spdx.org/licenses/MS-LPL.html for complete details of Microsoft Limited Public License"""))
        setattr(cls, "MS-PL",
            PermissibleValue(
                text="MS-PL",
                description="""Visit https://spdx.org/licenses/MS-PL.html for complete details of Microsoft Public License"""))
        setattr(cls, "MS-RL",
            PermissibleValue(
                text="MS-RL",
                description="""Visit https://spdx.org/licenses/MS-RL.html for complete details of Microsoft Reciprocal License"""))
        setattr(cls, "MIT-Festival",
            PermissibleValue(
                text="MIT-Festival",
                description="""Visit https://spdx.org/licenses/MIT-Festival.html for complete details of MIT Festival Variant"""))
        setattr(cls, "MIT-Modern-Variant",
            PermissibleValue(
                text="MIT-Modern-Variant",
                description="""Visit https://spdx.org/licenses/MIT-Modern-Variant.html for complete details of MIT License Modern Variant"""))
        setattr(cls, "MIT-0",
            PermissibleValue(
                text="MIT-0",
                description="Visit https://spdx.org/licenses/MIT-0.html for complete details of MIT No Attribution"))
        setattr(cls, "MIT-open-group",
            PermissibleValue(
                text="MIT-open-group",
                description="""Visit https://spdx.org/licenses/MIT-open-group.html for complete details of MIT Open Group variant"""))
        setattr(cls, "MIT-testregex",
            PermissibleValue(
                text="MIT-testregex",
                description="""Visit https://spdx.org/licenses/MIT-testregex.html for complete details of MIT testregex Variant"""))
        setattr(cls, "MIT-Wu",
            PermissibleValue(
                text="MIT-Wu",
                description="Visit https://spdx.org/licenses/MIT-Wu.html for complete details of MIT Tom Wu Variant"))
        setattr(cls, "MPL-1.0",
            PermissibleValue(
                text="MPL-1.0",
                description="""Visit https://spdx.org/licenses/MPL-1.0.html for complete details of Mozilla Public License 1.0"""))
        setattr(cls, "MPL-1.1",
            PermissibleValue(
                text="MPL-1.1",
                description="""Visit https://spdx.org/licenses/MPL-1.1.html for complete details of Mozilla Public License 1.1"""))
        setattr(cls, "MPL-2.0",
            PermissibleValue(
                text="MPL-2.0",
                description="""Visit https://spdx.org/licenses/MPL-2.0.html for complete details of Mozilla Public License 2.0"""))
        setattr(cls, "MPL-2.0-no-copyleft-exception",
            PermissibleValue(
                text="MPL-2.0-no-copyleft-exception",
                description="""Visit https://spdx.org/licenses/MPL-2.0-no-copyleft-exception.html for complete details of Mozilla Public License 2.0 (no copyleft exception)"""))
        setattr(cls, "MPEG-SSG",
            PermissibleValue(
                text="MPEG-SSG",
                description="""Visit https://spdx.org/licenses/MPEG-SSG.html for complete details of MPEG Software Simulation"""))
        setattr(cls, "mpi-permissive",
            PermissibleValue(
                text="mpi-permissive",
                description="""Visit https://spdx.org/licenses/mpi-permissive.html for complete details of mpi Permissive License"""))
        setattr(cls, "MulanPSL-1.0",
            PermissibleValue(
                text="MulanPSL-1.0",
                description="""Visit https://spdx.org/licenses/MulanPSL-1.0.html for complete details of Mulan Permissive Software License, Version 1"""))
        setattr(cls, "MulanPSL-2.0",
            PermissibleValue(
                text="MulanPSL-2.0",
                description="""Visit https://spdx.org/licenses/MulanPSL-2.0.html for complete details of Mulan Permissive Software License, Version 2"""))
        setattr(cls, "NAIST-2003",
            PermissibleValue(
                text="NAIST-2003",
                description="""Visit https://spdx.org/licenses/NAIST-2003.html for complete details of Nara Institute of Science and Technology License (2003)"""))
        setattr(cls, "NASA-1.3",
            PermissibleValue(
                text="NASA-1.3",
                description="""Visit https://spdx.org/licenses/NASA-1.3.html for complete details of NASA Open Source Agreement 1.3"""))
        setattr(cls, "NBPL-1.0",
            PermissibleValue(
                text="NBPL-1.0",
                description="""Visit https://spdx.org/licenses/NBPL-1.0.html for complete details of Net Boolean Public License v1"""))
        setattr(cls, "Net-SNMP",
            PermissibleValue(
                text="Net-SNMP",
                description="Visit https://spdx.org/licenses/Net-SNMP.html for complete details of Net-SNMP License"))
        setattr(cls, "NPL-1.0",
            PermissibleValue(
                text="NPL-1.0",
                description="""Visit https://spdx.org/licenses/NPL-1.0.html for complete details of Netscape Public License v1.0"""))
        setattr(cls, "NPL-1.1",
            PermissibleValue(
                text="NPL-1.1",
                description="""Visit https://spdx.org/licenses/NPL-1.1.html for complete details of Netscape Public License v1.1"""))
        setattr(cls, "NICTA-1.0",
            PermissibleValue(
                text="NICTA-1.0",
                description="""Visit https://spdx.org/licenses/NICTA-1.0.html for complete details of NICTA Public Software License, Version 1.0"""))
        setattr(cls, "NIST-PD",
            PermissibleValue(
                text="NIST-PD",
                description="""Visit https://spdx.org/licenses/NIST-PD.html for complete details of NIST Public Domain Notice"""))
        setattr(cls, "NIST-PD-fallback",
            PermissibleValue(
                text="NIST-PD-fallback",
                description="""Visit https://spdx.org/licenses/NIST-PD-fallback.html for complete details of NIST Public Domain Notice with license fallback"""))
        setattr(cls, "NIST-Software",
            PermissibleValue(
                text="NIST-Software",
                description="""Visit https://spdx.org/licenses/NIST-Software.html for complete details of NIST Software License"""))
        setattr(cls, "NCGL-UK-2.0",
            PermissibleValue(
                text="NCGL-UK-2.0",
                description="""Visit https://spdx.org/licenses/NCGL-UK-2.0.html for complete details of Non-Commercial Government Licence"""))
        setattr(cls, "NPOSL-3.0",
            PermissibleValue(
                text="NPOSL-3.0",
                description="""Visit https://spdx.org/licenses/NPOSL-3.0.html for complete details of Non-Profit Open Software License 3.0"""))
        setattr(cls, "NLOD-1.0",
            PermissibleValue(
                text="NLOD-1.0",
                description="""Visit https://spdx.org/licenses/NLOD-1.0.html for complete details of Norwegian Licence for Open Government Data (NLOD) 1.0"""))
        setattr(cls, "NLOD-2.0",
            PermissibleValue(
                text="NLOD-2.0",
                description="""Visit https://spdx.org/licenses/NLOD-2.0.html for complete details of Norwegian Licence for Open Government Data (NLOD) 2.0"""))
        setattr(cls, "NTP-0",
            PermissibleValue(
                text="NTP-0",
                description="Visit https://spdx.org/licenses/NTP-0.html for complete details of NTP No Attribution"))
        setattr(cls, "OCLC-2.0",
            PermissibleValue(
                text="OCLC-2.0",
                description="""Visit https://spdx.org/licenses/OCLC-2.0.html for complete details of OCLC Research Public License 2.0"""))
        setattr(cls, "OGC-1.0",
            PermissibleValue(
                text="OGC-1.0",
                description="""Visit https://spdx.org/licenses/OGC-1.0.html for complete details of OGC Software License, Version 1.0"""))
        setattr(cls, "OCCT-PL",
            PermissibleValue(
                text="OCCT-PL",
                description="""Visit https://spdx.org/licenses/OCCT-PL.html for complete details of Open CASCADE Technology Public License"""))
        setattr(cls, "ODC-By-1.0",
            PermissibleValue(
                text="ODC-By-1.0",
                description="""Visit https://spdx.org/licenses/ODC-By-1.0.html for complete details of Open Data Commons Attribution License v1.0"""))
        setattr(cls, "ODbL-1.0",
            PermissibleValue(
                text="ODbL-1.0",
                description="""Visit https://spdx.org/licenses/ODbL-1.0.html for complete details of Open Data Commons Open Database License v1.0"""))
        setattr(cls, "PDDL-1.0",
            PermissibleValue(
                text="PDDL-1.0",
                description="""Visit https://spdx.org/licenses/PDDL-1.0.html for complete details of Open Data Commons Public Domain Dedication License 1.0"""))
        setattr(cls, "OGL-Canada-2.0",
            PermissibleValue(
                text="OGL-Canada-2.0",
                description="""Visit https://spdx.org/licenses/OGL-Canada-2.0.html for complete details of Open Government Licence - Canada"""))
        setattr(cls, "OGL-UK-1.0",
            PermissibleValue(
                text="OGL-UK-1.0",
                description="""Visit https://spdx.org/licenses/OGL-UK-1.0.html for complete details of Open Government Licence v1.0"""))
        setattr(cls, "OGL-UK-2.0",
            PermissibleValue(
                text="OGL-UK-2.0",
                description="""Visit https://spdx.org/licenses/OGL-UK-2.0.html for complete details of Open Government Licence v2.0"""))
        setattr(cls, "OGL-UK-3.0",
            PermissibleValue(
                text="OGL-UK-3.0",
                description="""Visit https://spdx.org/licenses/OGL-UK-3.0.html for complete details of Open Government Licence v3.0"""))
        setattr(cls, "OLDAP-2.2.2",
            PermissibleValue(
                text="OLDAP-2.2.2",
                description="""Visit https://spdx.org/licenses/OLDAP-2.2.2.html for complete details of Open LDAP Public License 2.2.2"""))
        setattr(cls, "OLDAP-1.1",
            PermissibleValue(
                text="OLDAP-1.1",
                description="""Visit https://spdx.org/licenses/OLDAP-1.1.html for complete details of Open LDAP Public License v1.1"""))
        setattr(cls, "OLDAP-1.2",
            PermissibleValue(
                text="OLDAP-1.2",
                description="""Visit https://spdx.org/licenses/OLDAP-1.2.html for complete details of Open LDAP Public License v1.2"""))
        setattr(cls, "OLDAP-1.3",
            PermissibleValue(
                text="OLDAP-1.3",
                description="""Visit https://spdx.org/licenses/OLDAP-1.3.html for complete details of Open LDAP Public License v1.3"""))
        setattr(cls, "OLDAP-1.4",
            PermissibleValue(
                text="OLDAP-1.4",
                description="""Visit https://spdx.org/licenses/OLDAP-1.4.html for complete details of Open LDAP Public License v1.4"""))
        setattr(cls, "OLDAP-2.0",
            PermissibleValue(
                text="OLDAP-2.0",
                description="""Visit https://spdx.org/licenses/OLDAP-2.0.html for complete details of Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)"""))
        setattr(cls, "OLDAP-2.0.1",
            PermissibleValue(
                text="OLDAP-2.0.1",
                description="""Visit https://spdx.org/licenses/OLDAP-2.0.1.html for complete details of Open LDAP Public License v2.0.1"""))
        setattr(cls, "OLDAP-2.1",
            PermissibleValue(
                text="OLDAP-2.1",
                description="""Visit https://spdx.org/licenses/OLDAP-2.1.html for complete details of Open LDAP Public License v2.1"""))
        setattr(cls, "OLDAP-2.2",
            PermissibleValue(
                text="OLDAP-2.2",
                description="""Visit https://spdx.org/licenses/OLDAP-2.2.html for complete details of Open LDAP Public License v2.2"""))
        setattr(cls, "OLDAP-2.2.1",
            PermissibleValue(
                text="OLDAP-2.2.1",
                description="""Visit https://spdx.org/licenses/OLDAP-2.2.1.html for complete details of Open LDAP Public License v2.2.1"""))
        setattr(cls, "OLDAP-2.3",
            PermissibleValue(
                text="OLDAP-2.3",
                description="""Visit https://spdx.org/licenses/OLDAP-2.3.html for complete details of Open LDAP Public License v2.3"""))
        setattr(cls, "OLDAP-2.4",
            PermissibleValue(
                text="OLDAP-2.4",
                description="""Visit https://spdx.org/licenses/OLDAP-2.4.html for complete details of Open LDAP Public License v2.4"""))
        setattr(cls, "OLDAP-2.5",
            PermissibleValue(
                text="OLDAP-2.5",
                description="""Visit https://spdx.org/licenses/OLDAP-2.5.html for complete details of Open LDAP Public License v2.5"""))
        setattr(cls, "OLDAP-2.6",
            PermissibleValue(
                text="OLDAP-2.6",
                description="""Visit https://spdx.org/licenses/OLDAP-2.6.html for complete details of Open LDAP Public License v2.6"""))
        setattr(cls, "OLDAP-2.7",
            PermissibleValue(
                text="OLDAP-2.7",
                description="""Visit https://spdx.org/licenses/OLDAP-2.7.html for complete details of Open LDAP Public License v2.7"""))
        setattr(cls, "OLDAP-2.8",
            PermissibleValue(
                text="OLDAP-2.8",
                description="""Visit https://spdx.org/licenses/OLDAP-2.8.html for complete details of Open LDAP Public License v2.8"""))
        setattr(cls, "OLFL-1.3",
            PermissibleValue(
                text="OLFL-1.3",
                description="""Visit https://spdx.org/licenses/OLFL-1.3.html for complete details of Open Logistics Foundation License Version 1.3"""))
        setattr(cls, "OPL-1.0",
            PermissibleValue(
                text="OPL-1.0",
                description="""Visit https://spdx.org/licenses/OPL-1.0.html for complete details of Open Public License v1.0"""))
        setattr(cls, "OPUBL-1.0",
            PermissibleValue(
                text="OPUBL-1.0",
                description="""Visit https://spdx.org/licenses/OPUBL-1.0.html for complete details of Open Publication License v1.0"""))
        setattr(cls, "OSL-1.0",
            PermissibleValue(
                text="OSL-1.0",
                description="""Visit https://spdx.org/licenses/OSL-1.0.html for complete details of Open Software License 1.0"""))
        setattr(cls, "OSL-1.1",
            PermissibleValue(
                text="OSL-1.1",
                description="""Visit https://spdx.org/licenses/OSL-1.1.html for complete details of Open Software License 1.1"""))
        setattr(cls, "OSL-2.0",
            PermissibleValue(
                text="OSL-2.0",
                description="""Visit https://spdx.org/licenses/OSL-2.0.html for complete details of Open Software License 2.0"""))
        setattr(cls, "OSL-2.1",
            PermissibleValue(
                text="OSL-2.1",
                description="""Visit https://spdx.org/licenses/OSL-2.1.html for complete details of Open Software License 2.1"""))
        setattr(cls, "OSL-3.0",
            PermissibleValue(
                text="OSL-3.0",
                description="""Visit https://spdx.org/licenses/OSL-3.0.html for complete details of Open Software License 3.0"""))
        setattr(cls, "O-UDA-1.0",
            PermissibleValue(
                text="O-UDA-1.0",
                description="""Visit https://spdx.org/licenses/O-UDA-1.0.html for complete details of Open Use of Data Agreement v1.0"""))
        setattr(cls, "OpenPBS-2.3",
            PermissibleValue(
                text="OpenPBS-2.3",
                description="""Visit https://spdx.org/licenses/OpenPBS-2.3.html for complete details of OpenPBS v2.3 Software License"""))
        setattr(cls, "OSET-PL-2.1",
            PermissibleValue(
                text="OSET-PL-2.1",
                description="""Visit https://spdx.org/licenses/OSET-PL-2.1.html for complete details of OSET Public License version 2.1"""))
        setattr(cls, "PHP-3.0",
            PermissibleValue(
                text="PHP-3.0",
                description="Visit https://spdx.org/licenses/PHP-3.0.html for complete details of PHP License v3.0"))
        setattr(cls, "PHP-3.01",
            PermissibleValue(
                text="PHP-3.01",
                description="""Visit https://spdx.org/licenses/PHP-3.01.html for complete details of PHP License v3.01"""))
        setattr(cls, "libpng-2.0",
            PermissibleValue(
                text="libpng-2.0",
                description="""Visit https://spdx.org/licenses/libpng-2.0.html for complete details of PNG Reference Library version 2"""))
        setattr(cls, "PolyForm-Noncommercial-1.0.0",
            PermissibleValue(
                text="PolyForm-Noncommercial-1.0.0",
                description="""Visit https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html for complete details of PolyForm Noncommercial License 1.0.0"""))
        setattr(cls, "PolyForm-Small-Business-1.0.0",
            PermissibleValue(
                text="PolyForm-Small-Business-1.0.0",
                description="""Visit https://spdx.org/licenses/PolyForm-Small-Business-1.0.0.html for complete details of PolyForm Small Business License 1.0.0"""))
        setattr(cls, "python-ldap",
            PermissibleValue(
                text="python-ldap",
                description="""Visit https://spdx.org/licenses/python-ldap.html for complete details of Python ldap License"""))
        setattr(cls, "Python-2.0",
            PermissibleValue(
                text="Python-2.0",
                description="""Visit https://spdx.org/licenses/Python-2.0.html for complete details of Python License 2.0"""))
        setattr(cls, "Python-2.0.1",
            PermissibleValue(
                text="Python-2.0.1",
                description="""Visit https://spdx.org/licenses/Python-2.0.1.html for complete details of Python License 2.0.1"""))
        setattr(cls, "PSF-2.0",
            PermissibleValue(
                text="PSF-2.0",
                description="""Visit https://spdx.org/licenses/PSF-2.0.html for complete details of Python Software Foundation License 2.0"""))
        setattr(cls, "QPL-1.0",
            PermissibleValue(
                text="QPL-1.0",
                description="""Visit https://spdx.org/licenses/QPL-1.0.html for complete details of Q Public License 1.0"""))
        setattr(cls, "QPL-1.0-INRIA-2004",
            PermissibleValue(
                text="QPL-1.0-INRIA-2004",
                description="""Visit https://spdx.org/licenses/QPL-1.0-INRIA-2004.html for complete details of Q Public License 1.0 - INRIA 2004 variant"""))
        setattr(cls, "RPSL-1.0",
            PermissibleValue(
                text="RPSL-1.0",
                description="""Visit https://spdx.org/licenses/RPSL-1.0.html for complete details of RealNetworks Public Source License v1.0"""))
        setattr(cls, "RPL-1.1",
            PermissibleValue(
                text="RPL-1.1",
                description="""Visit https://spdx.org/licenses/RPL-1.1.html for complete details of Reciprocal Public License 1.1"""))
        setattr(cls, "RPL-1.5",
            PermissibleValue(
                text="RPL-1.5",
                description="""Visit https://spdx.org/licenses/RPL-1.5.html for complete details of Reciprocal Public License 1.5"""))
        setattr(cls, "RHeCos-1.1",
            PermissibleValue(
                text="RHeCos-1.1",
                description="""Visit https://spdx.org/licenses/RHeCos-1.1.html for complete details of Red Hat eCos Public License v1.1"""))
        setattr(cls, "RSA-MD",
            PermissibleValue(
                text="RSA-MD",
                description="""Visit https://spdx.org/licenses/RSA-MD.html for complete details of RSA Message-Digest License"""))
        setattr(cls, "SAX-PD",
            PermissibleValue(
                text="SAX-PD",
                description="""Visit https://spdx.org/licenses/SAX-PD.html for complete details of Sax Public Domain Notice"""))
        setattr(cls, "Sendmail-8.23",
            PermissibleValue(
                text="Sendmail-8.23",
                description="""Visit https://spdx.org/licenses/Sendmail-8.23.html for complete details of Sendmail License 8.23"""))
        setattr(cls, "SSPL-1.0",
            PermissibleValue(
                text="SSPL-1.0",
                description="""Visit https://spdx.org/licenses/SSPL-1.0.html for complete details of Server Side Public License, v 1"""))
        setattr(cls, "SGI-B-1.0",
            PermissibleValue(
                text="SGI-B-1.0",
                description="""Visit https://spdx.org/licenses/SGI-B-1.0.html for complete details of SGI Free Software License B v1.0"""))
        setattr(cls, "SGI-B-1.1",
            PermissibleValue(
                text="SGI-B-1.1",
                description="""Visit https://spdx.org/licenses/SGI-B-1.1.html for complete details of SGI Free Software License B v1.1"""))
        setattr(cls, "SGI-B-2.0",
            PermissibleValue(
                text="SGI-B-2.0",
                description="""Visit https://spdx.org/licenses/SGI-B-2.0.html for complete details of SGI Free Software License B v2.0"""))
        setattr(cls, "SGI-OpenGL",
            PermissibleValue(
                text="SGI-OpenGL",
                description="""Visit https://spdx.org/licenses/SGI-OpenGL.html for complete details of SGI OpenGL License"""))
        setattr(cls, "OFL-1.0",
            PermissibleValue(
                text="OFL-1.0",
                description="""Visit https://spdx.org/licenses/OFL-1.0.html for complete details of SIL Open Font License 1.0"""))
        setattr(cls, "OFL-1.0-no-RFN",
            PermissibleValue(
                text="OFL-1.0-no-RFN",
                description="""Visit https://spdx.org/licenses/OFL-1.0-no-RFN.html for complete details of SIL Open Font License 1.0 with no Reserved Font Name"""))
        setattr(cls, "OFL-1.0-RFN",
            PermissibleValue(
                text="OFL-1.0-RFN",
                description="""Visit https://spdx.org/licenses/OFL-1.0-RFN.html for complete details of SIL Open Font License 1.0 with Reserved Font Name"""))
        setattr(cls, "OFL-1.1",
            PermissibleValue(
                text="OFL-1.1",
                description="""Visit https://spdx.org/licenses/OFL-1.1.html for complete details of SIL Open Font License 1.1"""))
        setattr(cls, "OFL-1.1-no-RFN",
            PermissibleValue(
                text="OFL-1.1-no-RFN",
                description="""Visit https://spdx.org/licenses/OFL-1.1-no-RFN.html for complete details of SIL Open Font License 1.1 with no Reserved Font Name"""))
        setattr(cls, "OFL-1.1-RFN",
            PermissibleValue(
                text="OFL-1.1-RFN",
                description="""Visit https://spdx.org/licenses/OFL-1.1-RFN.html for complete details of SIL Open Font License 1.1 with Reserved Font Name"""))
        setattr(cls, "SimPL-2.0",
            PermissibleValue(
                text="SimPL-2.0",
                description="""Visit https://spdx.org/licenses/SimPL-2.0.html for complete details of Simple Public License 2.0"""))
        setattr(cls, "SHL-0.5",
            PermissibleValue(
                text="SHL-0.5",
                description="""Visit https://spdx.org/licenses/SHL-0.5.html for complete details of Solderpad Hardware License v0.5"""))
        setattr(cls, "SHL-0.51",
            PermissibleValue(
                text="SHL-0.51",
                description="""Visit https://spdx.org/licenses/SHL-0.51.html for complete details of Solderpad Hardware License, Version 0.51"""))
        setattr(cls, "Spencer-86",
            PermissibleValue(
                text="Spencer-86",
                description="""Visit https://spdx.org/licenses/Spencer-86.html for complete details of Spencer License 86"""))
        setattr(cls, "Spencer-94",
            PermissibleValue(
                text="Spencer-94",
                description="""Visit https://spdx.org/licenses/Spencer-94.html for complete details of Spencer License 94"""))
        setattr(cls, "Spencer-99",
            PermissibleValue(
                text="Spencer-99",
                description="""Visit https://spdx.org/licenses/Spencer-99.html for complete details of Spencer License 99"""))
        setattr(cls, "SSH-OpenSSH",
            PermissibleValue(
                text="SSH-OpenSSH",
                description="""Visit https://spdx.org/licenses/SSH-OpenSSH.html for complete details of SSH OpenSSH license"""))
        setattr(cls, "SSH-short",
            PermissibleValue(
                text="SSH-short",
                description="""Visit https://spdx.org/licenses/SSH-short.html for complete details of SSH short notice"""))
        setattr(cls, "ssh-keyscan",
            PermissibleValue(
                text="ssh-keyscan",
                description="""Visit https://spdx.org/licenses/ssh-keyscan.html for complete details of ssh-keyscan License"""))
        setattr(cls, "SugarCRM-1.1.3",
            PermissibleValue(
                text="SugarCRM-1.1.3",
                description="""Visit https://spdx.org/licenses/SugarCRM-1.1.3.html for complete details of SugarCRM Public License v1.1.3"""))
        setattr(cls, "SISSL-1.2",
            PermissibleValue(
                text="SISSL-1.2",
                description="""Visit https://spdx.org/licenses/SISSL-1.2.html for complete details of Sun Industry Standards Source License v1.2"""))
        setattr(cls, "SPL-1.0",
            PermissibleValue(
                text="SPL-1.0",
                description="""Visit https://spdx.org/licenses/SPL-1.0.html for complete details of Sun Public License v1.0"""))
        setattr(cls, "Watcom-1.0",
            PermissibleValue(
                text="Watcom-1.0",
                description="""Visit https://spdx.org/licenses/Watcom-1.0.html for complete details of Sybase Open Watcom Public License 1.0"""))
        setattr(cls, "BSD-Systemics",
            PermissibleValue(
                text="BSD-Systemics",
                description="""Visit https://spdx.org/licenses/BSD-Systemics.html for complete details of Systemics BSD variant license"""))
        setattr(cls, "OGDL-Taiwan-1.0",
            PermissibleValue(
                text="OGDL-Taiwan-1.0",
                description="""Visit https://spdx.org/licenses/OGDL-Taiwan-1.0.html for complete details of Taiwan Open Government Data License, version 1.0"""))
        setattr(cls, "TAPR-OHL-1.0",
            PermissibleValue(
                text="TAPR-OHL-1.0",
                description="""Visit https://spdx.org/licenses/TAPR-OHL-1.0.html for complete details of TAPR Open Hardware License v1.0"""))
        setattr(cls, "TCP-wrappers",
            PermissibleValue(
                text="TCP-wrappers",
                description="""Visit https://spdx.org/licenses/TCP-wrappers.html for complete details of TCP Wrappers License"""))
        setattr(cls, "TU-Berlin-1.0",
            PermissibleValue(
                text="TU-Berlin-1.0",
                description="""Visit https://spdx.org/licenses/TU-Berlin-1.0.html for complete details of Technische Universitaet Berlin License 1.0"""))
        setattr(cls, "TU-Berlin-2.0",
            PermissibleValue(
                text="TU-Berlin-2.0",
                description="""Visit https://spdx.org/licenses/TU-Berlin-2.0.html for complete details of Technische Universitaet Berlin License 2.0"""))
        setattr(cls, "Parity-6.0.0",
            PermissibleValue(
                text="Parity-6.0.0",
                description="""Visit https://spdx.org/licenses/Parity-6.0.0.html for complete details of The Parity Public License 6.0.0"""))
        setattr(cls, "Parity-7.0.0",
            PermissibleValue(
                text="Parity-7.0.0",
                description="""Visit https://spdx.org/licenses/Parity-7.0.0.html for complete details of The Parity Public License 7.0.0"""))
        setattr(cls, "TPL-1.0",
            PermissibleValue(
                text="TPL-1.0",
                description="""Visit https://spdx.org/licenses/TPL-1.0.html for complete details of THOR Public License 1.0"""))
        setattr(cls, "TORQUE-1.1",
            PermissibleValue(
                text="TORQUE-1.1",
                description="""Visit https://spdx.org/licenses/TORQUE-1.1.html for complete details of TORQUE v2.5+ Software License v1.1"""))
        setattr(cls, "Unicode-DFS-2015",
            PermissibleValue(
                text="Unicode-DFS-2015",
                description="""Visit https://spdx.org/licenses/Unicode-DFS-2015.html for complete details of Unicode License Agreement - Data Files and Software (2015)"""))
        setattr(cls, "Unicode-DFS-2016",
            PermissibleValue(
                text="Unicode-DFS-2016",
                description="""Visit https://spdx.org/licenses/Unicode-DFS-2016.html for complete details of Unicode License Agreement - Data Files and Software (2016)"""))
        setattr(cls, "Unicode-TOU",
            PermissibleValue(
                text="Unicode-TOU",
                description="""Visit https://spdx.org/licenses/Unicode-TOU.html for complete details of Unicode Terms of Use"""))
        setattr(cls, "OPL-UK-3.0",
            PermissibleValue(
                text="OPL-UK-3.0",
                description="""Visit https://spdx.org/licenses/OPL-UK-3.0.html for complete details of United Kingdom Open Parliament Licence v3.0"""))
        setattr(cls, "UPL-1.0",
            PermissibleValue(
                text="UPL-1.0",
                description="""Visit https://spdx.org/licenses/UPL-1.0.html for complete details of Universal Permissive License v1.0"""))
        setattr(cls, "UCL-1.0",
            PermissibleValue(
                text="UCL-1.0",
                description="""Visit https://spdx.org/licenses/UCL-1.0.html for complete details of Upstream Compatibility License v1.0"""))
        setattr(cls, "URT-RLE",
            PermissibleValue(
                text="URT-RLE",
                description="""Visit https://spdx.org/licenses/URT-RLE.html for complete details of Utah Raster Toolkit Run Length Encoded License"""))
        setattr(cls, "VSL-1.0",
            PermissibleValue(
                text="VSL-1.0",
                description="""Visit https://spdx.org/licenses/VSL-1.0.html for complete details of Vovida Software License v1.0"""))
        setattr(cls, "W3C-20150513",
            PermissibleValue(
                text="W3C-20150513",
                description="""Visit https://spdx.org/licenses/W3C-20150513.html for complete details of W3C Software Notice and Document License (2015-05-13)"""))
        setattr(cls, "W3C-19980720",
            PermissibleValue(
                text="W3C-19980720",
                description="""Visit https://spdx.org/licenses/W3C-19980720.html for complete details of W3C Software Notice and License (1998-07-20)"""))
        setattr(cls, "Widget-Workshop",
            PermissibleValue(
                text="Widget-Workshop",
                description="""Visit https://spdx.org/licenses/Widget-Workshop.html for complete details of Widget Workshop License"""))
        setattr(cls, "X11-distribute-modifications-variant",
            PermissibleValue(
                text="X11-distribute-modifications-variant",
                description="""Visit https://spdx.org/licenses/X11-distribute-modifications-variant.html for complete details of X11 License Distribution Modification Variant"""))
        setattr(cls, "Xdebug-1.03",
            PermissibleValue(
                text="Xdebug-1.03",
                description="""Visit https://spdx.org/licenses/Xdebug-1.03.html for complete details of Xdebug License v 1.03"""))
        setattr(cls, "XFree86-1.1",
            PermissibleValue(
                text="XFree86-1.1",
                description="""Visit https://spdx.org/licenses/XFree86-1.1.html for complete details of XFree86 License 1.1"""))
        setattr(cls, "YPL-1.0",
            PermissibleValue(
                text="YPL-1.0",
                description="""Visit https://spdx.org/licenses/YPL-1.0.html for complete details of Yahoo! Public License v1.0"""))
        setattr(cls, "YPL-1.1",
            PermissibleValue(
                text="YPL-1.1",
                description="""Visit https://spdx.org/licenses/YPL-1.1.html for complete details of Yahoo! Public License v1.1"""))
        setattr(cls, "Zend-2.0",
            PermissibleValue(
                text="Zend-2.0",
                description="""Visit https://spdx.org/licenses/Zend-2.0.html for complete details of Zend License v2.0"""))
        setattr(cls, "Zimbra-1.3",
            PermissibleValue(
                text="Zimbra-1.3",
                description="""Visit https://spdx.org/licenses/Zimbra-1.3.html for complete details of Zimbra Public License v1.3"""))
        setattr(cls, "Zimbra-1.4",
            PermissibleValue(
                text="Zimbra-1.4",
                description="""Visit https://spdx.org/licenses/Zimbra-1.4.html for complete details of Zimbra Public License v1.4"""))
        setattr(cls, "zlib-acknowledgement",
            PermissibleValue(
                text="zlib-acknowledgement",
                description="""Visit https://spdx.org/licenses/zlib-acknowledgement.html for complete details of zlib/libpng License with Acknowledgement"""))
        setattr(cls, "ZPL-1.1",
            PermissibleValue(
                text="ZPL-1.1",
                description="""Visit https://spdx.org/licenses/ZPL-1.1.html for complete details of Zope Public License 1.1"""))
        setattr(cls, "ZPL-2.0",
            PermissibleValue(
                text="ZPL-2.0",
                description="""Visit https://spdx.org/licenses/ZPL-2.0.html for complete details of Zope Public License 2.0"""))
        setattr(cls, "ZPL-2.1",
            PermissibleValue(
                text="ZPL-2.1",
                description="""Visit https://spdx.org/licenses/ZPL-2.1.html for complete details of Zope Public License 2.1"""))

class OSDistribution(EnumDefinitionImpl):
    """
    Possible values for operating system distribution.
    """
    Debian = PermissibleValue(text="Debian")
    Fedora = PermissibleValue(text="Fedora")
    FreeBSD = PermissibleValue(text="FreeBSD")
    Mandrakelinux = PermissibleValue(text="Mandrakelinux")
    NetBSD = PermissibleValue(text="NetBSD")
    OpenBSD = PermissibleValue(text="OpenBSD")
    OpenSolaris = PermissibleValue(text="OpenSolaris")
    openSUSE = PermissibleValue(text="openSUSE")
    Ubuntu = PermissibleValue(text="Ubuntu")
    CirrOS = PermissibleValue(text="CirrOS")
    AlmaLinux = PermissibleValue(text="AlmaLinux")
    others = PermissibleValue(text="others")

    _defn = EnumDefinition(
        name="OSDistribution",
        description="Possible values for operating system distribution.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Alpine Linux",
            PermissibleValue(text="Alpine Linux"))
        setattr(cls, "Arch Linux",
            PermissibleValue(text="Arch Linux"))
        setattr(cls, "CentOS Linux",
            PermissibleValue(text="CentOS Linux"))
        setattr(cls, "Gentoo Linux",
            PermissibleValue(text="Gentoo Linux"))
        setattr(cls, "Mandriva Linux",
            PermissibleValue(text="Mandriva Linux"))
        setattr(cls, "Mandriva Enterprise Server",
            PermissibleValue(text="Mandriva Enterprise Server"))
        setattr(cls, "MS-DOS",
            PermissibleValue(text="MS-DOS"))
        setattr(cls, "Novell NetWare",
            PermissibleValue(text="Novell NetWare"))
        setattr(cls, "Rocky Linux",
            PermissibleValue(text="Rocky Linux"))
        setattr(cls, "Red Hat Enterprise Linux",
            PermissibleValue(text="Red Hat Enterprise Linux"))
        setattr(cls, "SUSE Linux Enterprise Server",
            PermissibleValue(text="SUSE Linux Enterprise Server"))
        setattr(cls, "Microsoft Windows",
            PermissibleValue(text="Microsoft Windows"))

class HypervisorType(EnumDefinitionImpl):
    """
    Possible values for hypervisor types.
    """
    quemu = PermissibleValue(text="quemu")
    KVM = PermissibleValue(text="KVM")
    Xen = PermissibleValue(text="Xen")
    ESXi = PermissibleValue(text="ESXi")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="HypervisorType",
        description="Possible values for hypervisor types.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hyper-V",
            PermissibleValue(text="Hyper-V"))
        setattr(cls, "Cloud Hypervisor",
            PermissibleValue(text="Cloud Hypervisor"))

class PersonalDataProtectionRegime(EnumDefinitionImpl):

    GDPR2016 = PermissibleValue(
        text="GDPR2016",
        description="General Data Protection Regulation / EEA.")
    LGPD2019 = PermissibleValue(
        text="LGPD2019",
        description="General Personal Data Protection Law (Lei Geral de Prote��o de Dados Pessoais) / BRA.")
    PDPA2012 = PermissibleValue(
        text="PDPA2012",
        description="Personal Data Protection Act 2012 / SGP.")
    CCPA2018 = PermissibleValue(
        text="CCPA2018",
        description="California Consumer Privacy Act / US-CA.")
    VCDPA2021 = PermissibleValue(
        text="VCDPA2021",
        description="Virginia Consumer Data Protection Act / US-VA.")

    _defn = EnumDefinition(
        name="PersonalDataProtectionRegime",
    )

class RequestTypes(EnumDefinitionImpl):

    API = PermissibleValue(text="API")
    email = PermissibleValue(text="email")
    webform = PermissibleValue(text="webform")
    unregisteredLetter = PermissibleValue(text="unregisteredLetter")
    registeredLetter = PermissibleValue(text="registeredLetter")
    supportCenter = PermissibleValue(text="supportCenter")

    _defn = EnumDefinition(
        name="RequestTypes",
    )

class AccessTypes(EnumDefinitionImpl):

    digital = PermissibleValue(
        text="digital",
        description="Access via digital service, such as e-mail or web form.")
    physical = PermissibleValue(
        text="physical",
        description="Access via physical medium, such as letter or physical appointment.")

    _defn = EnumDefinition(
        name="AccessTypes",
    )

class MIMETypes(EnumDefinitionImpl):

    calendar = PermissibleValue(text="calendar")
    cql = PermissibleValue(text="cql")
    css = PermissibleValue(text="css")
    csv = PermissibleValue(text="csv")
    dns = PermissibleValue(text="dns")
    encaprtp = PermissibleValue(text="encaprtp")
    enriched = PermissibleValue(text="enriched")
    example = PermissibleValue(text="example")
    fhirpath = PermissibleValue(text="fhirpath")
    flexfec = PermissibleValue(text="flexfec")
    fwdred = PermissibleValue(text="fwdred")
    gff3 = PermissibleValue(text="gff3")
    hl7v2 = PermissibleValue(text="hl7v2")
    html = PermissibleValue(text="html")
    javascript = PermissibleValue(text="javascript")
    markdown = PermissibleValue(text="markdown")
    mizar = PermissibleValue(text="mizar")
    n3 = PermissibleValue(text="n3")
    parameters = PermissibleValue(text="parameters")
    parityfec = PermissibleValue(text="parityfec")
    plain = PermissibleValue(text="plain")
    RED = PermissibleValue(text="RED")
    richtext = PermissibleValue(text="richtext")
    rtf = PermissibleValue(text="rtf")
    rtploopback = PermissibleValue(text="rtploopback")
    rtx = PermissibleValue(text="rtx")
    SGML = PermissibleValue(text="SGML")
    shacl = PermissibleValue(text="shacl")
    shex = PermissibleValue(text="shex")
    spdx = PermissibleValue(text="spdx")
    strings = PermissibleValue(text="strings")
    t140 = PermissibleValue(text="t140")
    troff = PermissibleValue(text="troff")
    turtle = PermissibleValue(text="turtle")
    ulpfec = PermissibleValue(text="ulpfec")
    vcard = PermissibleValue(text="vcard")
    vtt = PermissibleValue(text="vtt")
    wgsl = PermissibleValue(text="wgsl")
    xml = PermissibleValue(text="xml")
    A2L = PermissibleValue(text="A2L")
    activemessage = PermissibleValue(text="activemessage")
    AML = PermissibleValue(text="AML")
    applefile = PermissibleValue(text="applefile")
    ATF = PermissibleValue(text="ATF")
    ATFX = PermissibleValue(text="ATFX")
    atomicmail = PermissibleValue(text="atomicmail")
    ATXML = PermissibleValue(text="ATXML")
    cbor = PermissibleValue(text="cbor")
    cccex = PermissibleValue(text="cccex")
    cdni = PermissibleValue(text="cdni")
    CEA = PermissibleValue(text="CEA")
    cfw = PermissibleValue(text="cfw")
    clr = PermissibleValue(text="clr")
    cms = PermissibleValue(text="cms")
    commonground = PermissibleValue(text="commonground")
    cose = PermissibleValue(text="cose")
    csrattrs = PermissibleValue(text="csrattrs")
    cwl = PermissibleValue(text="cwl")
    cwt = PermissibleValue(text="cwt")
    cybercash = PermissibleValue(text="cybercash")
    dashdelta = PermissibleValue(text="dashdelta")
    DCD = PermissibleValue(text="DCD")
    dicom = PermissibleValue(text="dicom")
    DII = PermissibleValue(text="DII")
    DIT = PermissibleValue(text="DIT")
    dvcs = PermissibleValue(text="dvcs")
    EDIFACT = PermissibleValue(text="EDIFACT")
    efi = PermissibleValue(text="efi")
    eshop = PermissibleValue(text="eshop")
    exi = PermissibleValue(text="exi")
    express = PermissibleValue(text="express")
    fastinfoset = PermissibleValue(text="fastinfoset")
    fastsoap = PermissibleValue(text="fastsoap")
    fdf = PermissibleValue(text="fdf")
    fits = PermissibleValue(text="fits")
    gzip = PermissibleValue(text="gzip")
    H224 = PermissibleValue(text="H224")
    http = PermissibleValue(text="http")
    hyperstudio = PermissibleValue(text="hyperstudio")
    iges = PermissibleValue(text="iges")
    index = PermissibleValue(text="index")
    IOTP = PermissibleValue(text="IOTP")
    ipfix = PermissibleValue(text="ipfix")
    ipp = PermissibleValue(text="ipp")
    ISUP = PermissibleValue(text="ISUP")
    jose = PermissibleValue(text="jose")
    json = PermissibleValue(text="json")
    jwt = PermissibleValue(text="jwt")
    linkset = PermissibleValue(text="linkset")
    LXF = PermissibleValue(text="LXF")
    macwriteii = PermissibleValue(text="macwriteii")
    marc = PermissibleValue(text="marc")
    mathematica = PermissibleValue(text="mathematica")
    mbox = PermissibleValue(text="mbox")
    MF4 = PermissibleValue(text="MF4")
    mikey = PermissibleValue(text="mikey")
    mipc = PermissibleValue(text="mipc")
    mp21 = PermissibleValue(text="mp21")
    mp4 = PermissibleValue(text="mp4")
    msword = PermissibleValue(text="msword")
    mxf = PermissibleValue(text="mxf")
    nasdata = PermissibleValue(text="nasdata")
    node = PermissibleValue(text="node")
    nss = PermissibleValue(text="nss")
    ODA = PermissibleValue(text="ODA")
    ODX = PermissibleValue(text="ODX")
    ogg = PermissibleValue(text="ogg")
    oscore = PermissibleValue(text="oscore")
    oxps = PermissibleValue(text="oxps")
    p21 = PermissibleValue(text="p21")
    passport = PermissibleValue(text="passport")
    pdf = PermissibleValue(text="pdf")
    PDX = PermissibleValue(text="PDX")
    pkcs10 = PermissibleValue(text="pkcs10")
    pkcs8 = PermissibleValue(text="pkcs8")
    pkcs12 = PermissibleValue(text="pkcs12")
    pkixcmp = PermissibleValue(text="pkixcmp")
    postscript = PermissibleValue(text="postscript")
    QSIG = PermissibleValue(text="QSIG")
    raptorfec = PermissibleValue(text="raptorfec")
    riscos = PermissibleValue(text="riscos")
    sbe = PermissibleValue(text="sbe")
    sdp = PermissibleValue(text="sdp")
    sieve = PermissibleValue(text="sieve")
    simpleSymbolContainer = PermissibleValue(text="simpleSymbolContainer")
    sipc = PermissibleValue(text="sipc")
    slate = PermissibleValue(text="slate")
    smpte336m = PermissibleValue(text="smpte336m")
    sql = PermissibleValue(text="sql")
    srgs = PermissibleValue(text="srgs")
    TETRA_ISI = PermissibleValue(text="TETRA_ISI")
    tnauthlist = PermissibleValue(text="tnauthlist")
    trig = PermissibleValue(text="trig")
    tzif = PermissibleValue(text="tzif")
    vemmi = PermissibleValue(text="vemmi")
    wasm = PermissibleValue(text="wasm")
    widget = PermissibleValue(text="widget")
    wita = PermissibleValue(text="wita")
    xfdf = PermissibleValue(text="xfdf")
    yaml = PermissibleValue(text="yaml")
    yang = PermissibleValue(text="yang")
    zip = PermissibleValue(text="zip")
    zlib = PermissibleValue(text="zlib")
    zstd = PermissibleValue(text="zstd")

    _defn = EnumDefinition(
        name="MIMETypes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1d-interleaved-parityfec",
            PermissibleValue(text="1d-interleaved-parityfec"))
        setattr(cls, "cache-manifest",
            PermissibleValue(text="cache-manifest"))
        setattr(cls, "cql-expression",
            PermissibleValue(text="cql-expression"))
        setattr(cls, "cql-identifier",
            PermissibleValue(text="cql-identifier"))
        setattr(cls, "csv-schema",
            PermissibleValue(text="csv-schema"))
        setattr(cls, "directory - DEPRECATED by RFC6350",
            PermissibleValue(text="directory - DEPRECATED by RFC6350"))
        setattr(cls, "ecmascript (OBSOLETED in favor of text/javascript)",
            PermissibleValue(text="ecmascript (OBSOLETED in favor of text/javascript)"))
        setattr(cls, "grammar-ref-list",
            PermissibleValue(text="grammar-ref-list"))
        setattr(cls, "jcr-cnd",
            PermissibleValue(text="jcr-cnd"))
        setattr(cls, "provenance-notation",
            PermissibleValue(text="provenance-notation"))
        setattr(cls, "prs.fallenstein.rst",
            PermissibleValue(text="prs.fallenstein.rst"))
        setattr(cls, "prs.lines.tag",
            PermissibleValue(text="prs.lines.tag"))
        setattr(cls, "prs.prop.logic",
            PermissibleValue(text="prs.prop.logic"))
        setattr(cls, "rfc822-headers",
            PermissibleValue(text="rfc822-headers"))
        setattr(cls, "rtp-enc-aescm128",
            PermissibleValue(text="rtp-enc-aescm128"))
        setattr(cls, "tab-separated-values",
            PermissibleValue(text="tab-separated-values"))
        setattr(cls, "uri-list",
            PermissibleValue(text="uri-list"))
        setattr(cls, "vnd.a",
            PermissibleValue(text="vnd.a"))
        setattr(cls, "vnd.abc",
            PermissibleValue(text="vnd.abc"))
        setattr(cls, "vnd.ascii-art",
            PermissibleValue(text="vnd.ascii-art"))
        setattr(cls, "vnd.curl",
            PermissibleValue(text="vnd.curl"))
        setattr(cls, "vnd.debian.copyright",
            PermissibleValue(text="vnd.debian.copyright"))
        setattr(cls, "vnd.DMClientScript",
            PermissibleValue(text="vnd.DMClientScript"))
        setattr(cls, "vnd.dvb.subtitle",
            PermissibleValue(text="vnd.dvb.subtitle"))
        setattr(cls, "vnd.esmertec.theme-descriptor",
            PermissibleValue(text="vnd.esmertec.theme-descriptor"))
        setattr(cls, "vnd.exchangeable",
            PermissibleValue(text="vnd.exchangeable"))
        setattr(cls, "vnd.familysearch.gedcom",
            PermissibleValue(text="vnd.familysearch.gedcom"))
        setattr(cls, "vnd.ficlab.flt",
            PermissibleValue(text="vnd.ficlab.flt"))
        setattr(cls, "vnd.fly",
            PermissibleValue(text="vnd.fly"))
        setattr(cls, "vnd.fmi.flexstor",
            PermissibleValue(text="vnd.fmi.flexstor"))
        setattr(cls, "vnd.gml",
            PermissibleValue(text="vnd.gml"))
        setattr(cls, "vnd.graphviz",
            PermissibleValue(text="vnd.graphviz"))
        setattr(cls, "vnd.hans",
            PermissibleValue(text="vnd.hans"))
        setattr(cls, "vnd.hgl",
            PermissibleValue(text="vnd.hgl"))
        setattr(cls, "vnd.in3d.3dml",
            PermissibleValue(text="vnd.in3d.3dml"))
        setattr(cls, "vnd.in3d.spot",
            PermissibleValue(text="vnd.in3d.spot"))
        setattr(cls, "vnd.IPTC.NewsML",
            PermissibleValue(text="vnd.IPTC.NewsML"))
        setattr(cls, "vnd.IPTC.NITF",
            PermissibleValue(text="vnd.IPTC.NITF"))
        setattr(cls, "vnd.latex-z",
            PermissibleValue(text="vnd.latex-z"))
        setattr(cls, "vnd.motorola.reflex",
            PermissibleValue(text="vnd.motorola.reflex"))
        setattr(cls, "vnd.ms-mediapackage",
            PermissibleValue(text="vnd.ms-mediapackage"))
        setattr(cls, "vnd.net2phone.commcenter.command",
            PermissibleValue(text="vnd.net2phone.commcenter.command"))
        setattr(cls, "vnd.radisys.msml-basic-layout",
            PermissibleValue(text="vnd.radisys.msml-basic-layout"))
        setattr(cls, "vnd.senx.warpscript",
            PermissibleValue(text="vnd.senx.warpscript"))
        setattr(cls, "vnd.si.uricatalogue",
            PermissibleValue(text="vnd.si.uricatalogue"))
        setattr(cls, "vnd.sun.j2me.app-descriptor",
            PermissibleValue(text="vnd.sun.j2me.app-descriptor"))
        setattr(cls, "vnd.sosi",
            PermissibleValue(text="vnd.sosi"))
        setattr(cls, "vnd.trolltech.linguist",
            PermissibleValue(text="vnd.trolltech.linguist"))
        setattr(cls, "vnd.wap.si",
            PermissibleValue(text="vnd.wap.si"))
        setattr(cls, "vnd.wap.sl",
            PermissibleValue(text="vnd.wap.sl"))
        setattr(cls, "vnd.wap.wml",
            PermissibleValue(text="vnd.wap.wml"))
        setattr(cls, "vnd.wap.wmlscript",
            PermissibleValue(text="vnd.wap.wmlscript"))
        setattr(cls, "xml-external-parsed-entity",
            PermissibleValue(text="xml-external-parsed-entity"))
        setattr(cls, "3gpdash-qoe-report+xml",
            PermissibleValue(text="3gpdash-qoe-report+xml"))
        setattr(cls, "3gppHal+json",
            PermissibleValue(text="3gppHal+json"))
        setattr(cls, "3gppHalForms+json",
            PermissibleValue(text="3gppHalForms+json"))
        setattr(cls, "3gpp-ims+xml",
            PermissibleValue(text="3gpp-ims+xml"))
        setattr(cls, "ace+cbor",
            PermissibleValue(text="ace+cbor"))
        setattr(cls, "ace+json",
            PermissibleValue(text="ace+json"))
        setattr(cls, "activity+json",
            PermissibleValue(text="activity+json"))
        setattr(cls, "aif+cbor",
            PermissibleValue(text="aif+cbor"))
        setattr(cls, "aif+json",
            PermissibleValue(text="aif+json"))
        setattr(cls, "alto-cdni+json",
            PermissibleValue(text="alto-cdni+json"))
        setattr(cls, "alto-cdnifilter+json",
            PermissibleValue(text="alto-cdnifilter+json"))
        setattr(cls, "alto-costmap+json",
            PermissibleValue(text="alto-costmap+json"))
        setattr(cls, "alto-costmapfilter+json",
            PermissibleValue(text="alto-costmapfilter+json"))
        setattr(cls, "alto-directory+json",
            PermissibleValue(text="alto-directory+json"))
        setattr(cls, "alto-endpointprop+json",
            PermissibleValue(text="alto-endpointprop+json"))
        setattr(cls, "alto-endpointpropparams+json",
            PermissibleValue(text="alto-endpointpropparams+json"))
        setattr(cls, "alto-endpointcost+json",
            PermissibleValue(text="alto-endpointcost+json"))
        setattr(cls, "alto-endpointcostparams+json",
            PermissibleValue(text="alto-endpointcostparams+json"))
        setattr(cls, "alto-error+json",
            PermissibleValue(text="alto-error+json"))
        setattr(cls, "alto-networkmapfilter+json",
            PermissibleValue(text="alto-networkmapfilter+json"))
        setattr(cls, "alto-networkmap+json",
            PermissibleValue(text="alto-networkmap+json"))
        setattr(cls, "alto-propmap+json",
            PermissibleValue(text="alto-propmap+json"))
        setattr(cls, "alto-propmapparams+json",
            PermissibleValue(text="alto-propmapparams+json"))
        setattr(cls, "alto-updatestreamcontrol+json",
            PermissibleValue(text="alto-updatestreamcontrol+json"))
        setattr(cls, "alto-updatestreamparams+json",
            PermissibleValue(text="alto-updatestreamparams+json"))
        setattr(cls, "andrew-inset",
            PermissibleValue(text="andrew-inset"))
        setattr(cls, "at+jwt",
            PermissibleValue(text="at+jwt"))
        setattr(cls, "atom+xml",
            PermissibleValue(text="atom+xml"))
        setattr(cls, "atomcat+xml",
            PermissibleValue(text="atomcat+xml"))
        setattr(cls, "atomdeleted+xml",
            PermissibleValue(text="atomdeleted+xml"))
        setattr(cls, "atomsvc+xml",
            PermissibleValue(text="atomsvc+xml"))
        setattr(cls, "atsc-dwd+xml",
            PermissibleValue(text="atsc-dwd+xml"))
        setattr(cls, "atsc-dynamic-event-message",
            PermissibleValue(text="atsc-dynamic-event-message"))
        setattr(cls, "atsc-held+xml",
            PermissibleValue(text="atsc-held+xml"))
        setattr(cls, "atsc-rdt+json",
            PermissibleValue(text="atsc-rdt+json"))
        setattr(cls, "atsc-rsat+xml",
            PermissibleValue(text="atsc-rsat+xml"))
        setattr(cls, "auth-policy+xml",
            PermissibleValue(text="auth-policy+xml"))
        setattr(cls, "automationml-aml+xml",
            PermissibleValue(text="automationml-aml+xml"))
        setattr(cls, "automationml-amlx+zip",
            PermissibleValue(text="automationml-amlx+zip"))
        setattr(cls, "bacnet-xdd+zip",
            PermissibleValue(text="bacnet-xdd+zip"))
        setattr(cls, "batch-SMTP",
            PermissibleValue(text="batch-SMTP"))
        setattr(cls, "beep+xml",
            PermissibleValue(text="beep+xml"))
        setattr(cls, "calendar+json",
            PermissibleValue(text="calendar+json"))
        setattr(cls, "calendar+xml",
            PermissibleValue(text="calendar+xml"))
        setattr(cls, "call-completion",
            PermissibleValue(text="call-completion"))
        setattr(cls, "CALS-1840",
            PermissibleValue(text="CALS-1840"))
        setattr(cls, "captive+json",
            PermissibleValue(text="captive+json"))
        setattr(cls, "cbor-seq",
            PermissibleValue(text="cbor-seq"))
        setattr(cls, "ccmp+xml",
            PermissibleValue(text="ccmp+xml"))
        setattr(cls, "ccxml+xml",
            PermissibleValue(text="ccxml+xml"))
        setattr(cls, "cda+xml",
            PermissibleValue(text="cda+xml"))
        setattr(cls, "CDFX+XML",
            PermissibleValue(text="CDFX+XML"))
        setattr(cls, "cdmi-capability",
            PermissibleValue(text="cdmi-capability"))
        setattr(cls, "cdmi-container",
            PermissibleValue(text="cdmi-container"))
        setattr(cls, "cdmi-domain",
            PermissibleValue(text="cdmi-domain"))
        setattr(cls, "cdmi-object",
            PermissibleValue(text="cdmi-object"))
        setattr(cls, "cdmi-queue",
            PermissibleValue(text="cdmi-queue"))
        setattr(cls, "cea-2018+xml",
            PermissibleValue(text="cea-2018+xml"))
        setattr(cls, "cellml+xml",
            PermissibleValue(text="cellml+xml"))
        setattr(cls, "cid-edhoc+cbor-seq",
            PermissibleValue(text="cid-edhoc+cbor-seq"))
        setattr(cls, "city+json",
            PermissibleValue(text="city+json"))
        setattr(cls, "clue_info+xml",
            PermissibleValue(text="clue_info+xml"))
        setattr(cls, "clue+xml",
            PermissibleValue(text="clue+xml"))
        setattr(cls, "cnrp+xml",
            PermissibleValue(text="cnrp+xml"))
        setattr(cls, "coap-group+json",
            PermissibleValue(text="coap-group+json"))
        setattr(cls, "coap-payload",
            PermissibleValue(text="coap-payload"))
        setattr(cls, "concise-problem-details+cbor",
            PermissibleValue(text="concise-problem-details+cbor"))
        setattr(cls, "conference-info+xml",
            PermissibleValue(text="conference-info+xml"))
        setattr(cls, "cpl+xml",
            PermissibleValue(text="cpl+xml"))
        setattr(cls, "cose-key",
            PermissibleValue(text="cose-key"))
        setattr(cls, "cose-key-set",
            PermissibleValue(text="cose-key-set"))
        setattr(cls, "cose-x509",
            PermissibleValue(text="cose-x509"))
        setattr(cls, "csta+xml",
            PermissibleValue(text="csta+xml"))
        setattr(cls, "CSTAdata+xml",
            PermissibleValue(text="CSTAdata+xml"))
        setattr(cls, "csvm+json",
            PermissibleValue(text="csvm+json"))
        setattr(cls, "cwl+json",
            PermissibleValue(text="cwl+json"))
        setattr(cls, "dash+xml",
            PermissibleValue(text="dash+xml"))
        setattr(cls, "dash-patch+xml",
            PermissibleValue(text="dash-patch+xml"))
        setattr(cls, "davmount+xml",
            PermissibleValue(text="davmount+xml"))
        setattr(cls, "dca-rft",
            PermissibleValue(text="dca-rft"))
        setattr(cls, "dec-dx",
            PermissibleValue(text="dec-dx"))
        setattr(cls, "dialog-info+xml",
            PermissibleValue(text="dialog-info+xml"))
        setattr(cls, "dicom+json",
            PermissibleValue(text="dicom+json"))
        setattr(cls, "dicom+xml",
            PermissibleValue(text="dicom+xml"))
        setattr(cls, "dns+json",
            PermissibleValue(text="dns+json"))
        setattr(cls, "dns-message",
            PermissibleValue(text="dns-message"))
        setattr(cls, "dots+cbor",
            PermissibleValue(text="dots+cbor"))
        setattr(cls, "dpop+jwt",
            PermissibleValue(text="dpop+jwt"))
        setattr(cls, "dskpp+xml",
            PermissibleValue(text="dskpp+xml"))
        setattr(cls, "dssc+der",
            PermissibleValue(text="dssc+der"))
        setattr(cls, "dssc+xml",
            PermissibleValue(text="dssc+xml"))
        setattr(cls, "edhoc+cbor-seq",
            PermissibleValue(text="edhoc+cbor-seq"))
        setattr(cls, "EDI-consent",
            PermissibleValue(text="EDI-consent"))
        setattr(cls, "EDI-X12",
            PermissibleValue(text="EDI-X12"))
        setattr(cls, "elm+json",
            PermissibleValue(text="elm+json"))
        setattr(cls, "elm+xml",
            PermissibleValue(text="elm+xml"))
        setattr(cls, "EmergencyCallData.cap+xml",
            PermissibleValue(text="EmergencyCallData.cap+xml"))
        setattr(cls, "EmergencyCallData.Comment+xml",
            PermissibleValue(text="EmergencyCallData.Comment+xml"))
        setattr(cls, "EmergencyCallData.Control+xml",
            PermissibleValue(text="EmergencyCallData.Control+xml"))
        setattr(cls, "EmergencyCallData.DeviceInfo+xml",
            PermissibleValue(text="EmergencyCallData.DeviceInfo+xml"))
        setattr(cls, "EmergencyCallData.eCall.MSD",
            PermissibleValue(text="EmergencyCallData.eCall.MSD"))
        setattr(cls, "EmergencyCallData.LegacyESN+json",
            PermissibleValue(text="EmergencyCallData.LegacyESN+json"))
        setattr(cls, "EmergencyCallData.ProviderInfo+xml",
            PermissibleValue(text="EmergencyCallData.ProviderInfo+xml"))
        setattr(cls, "EmergencyCallData.ServiceInfo+xml",
            PermissibleValue(text="EmergencyCallData.ServiceInfo+xml"))
        setattr(cls, "EmergencyCallData.SubscriberInfo+xml",
            PermissibleValue(text="EmergencyCallData.SubscriberInfo+xml"))
        setattr(cls, "EmergencyCallData.VEDS+xml",
            PermissibleValue(text="EmergencyCallData.VEDS+xml"))
        setattr(cls, "emma+xml",
            PermissibleValue(text="emma+xml"))
        setattr(cls, "emotionml+xml",
            PermissibleValue(text="emotionml+xml"))
        setattr(cls, "epp+xml",
            PermissibleValue(text="epp+xml"))
        setattr(cls, "epub+zip",
            PermissibleValue(text="epub+zip"))
        setattr(cls, "expect-ct-report+json",
            PermissibleValue(text="expect-ct-report+json"))
        setattr(cls, "fdt+xml",
            PermissibleValue(text="fdt+xml"))
        setattr(cls, "fhir+json",
            PermissibleValue(text="fhir+json"))
        setattr(cls, "fhir+xml",
            PermissibleValue(text="fhir+xml"))
        setattr(cls, "font-sfnt - DEPRECATED in favor of font/sfnt",
            PermissibleValue(text="font-sfnt - DEPRECATED in favor of font/sfnt"))
        setattr(cls, "font-tdpfr",
            PermissibleValue(text="font-tdpfr"))
        setattr(cls, "font-woff - DEPRECATED in favor of font/woff",
            PermissibleValue(text="font-woff - DEPRECATED in favor of font/woff"))
        setattr(cls, "framework-attributes+xml",
            PermissibleValue(text="framework-attributes+xml"))
        setattr(cls, "geo+json",
            PermissibleValue(text="geo+json"))
        setattr(cls, "geo+json-seq",
            PermissibleValue(text="geo+json-seq"))
        setattr(cls, "geopackage+sqlite3",
            PermissibleValue(text="geopackage+sqlite3"))
        setattr(cls, "geoxacml+xml",
            PermissibleValue(text="geoxacml+xml"))
        setattr(cls, "gltf-buffer",
            PermissibleValue(text="gltf-buffer"))
        setattr(cls, "gml+xml",
            PermissibleValue(text="gml+xml"))
        setattr(cls, "held+xml",
            PermissibleValue(text="held+xml"))
        setattr(cls, "hl7v2+xml",
            PermissibleValue(text="hl7v2+xml"))
        setattr(cls, "ibe-key-request+xml",
            PermissibleValue(text="ibe-key-request+xml"))
        setattr(cls, "ibe-pkg-reply+xml",
            PermissibleValue(text="ibe-pkg-reply+xml"))
        setattr(cls, "ibe-pp-data",
            PermissibleValue(text="ibe-pp-data"))
        setattr(cls, "im-iscomposing+xml",
            PermissibleValue(text="im-iscomposing+xml"))
        setattr(cls, "index.cmd",
            PermissibleValue(text="index.cmd"))
        setattr(cls, "index.obj",
            PermissibleValue(text="index.obj"))
        setattr(cls, "index.response",
            PermissibleValue(text="index.response"))
        setattr(cls, "index.vnd",
            PermissibleValue(text="index.vnd"))
        setattr(cls, "inkml+xml",
            PermissibleValue(text="inkml+xml"))
        setattr(cls, "its+xml",
            PermissibleValue(text="its+xml"))
        setattr(cls, "java-archive",
            PermissibleValue(text="java-archive"))
        setattr(cls, "javascript (OBSOLETED in favor of text/javascript)",
            PermissibleValue(text="javascript (OBSOLETED in favor of text/javascript)"))
        setattr(cls, "jf2feed+json",
            PermissibleValue(text="jf2feed+json"))
        setattr(cls, "jose+json",
            PermissibleValue(text="jose+json"))
        setattr(cls, "jrd+json",
            PermissibleValue(text="jrd+json"))
        setattr(cls, "jscalendar+json",
            PermissibleValue(text="jscalendar+json"))
        setattr(cls, "json-patch+json",
            PermissibleValue(text="json-patch+json"))
        setattr(cls, "json-seq",
            PermissibleValue(text="json-seq"))
        setattr(cls, "jwk+json",
            PermissibleValue(text="jwk+json"))
        setattr(cls, "jwk-set+json",
            PermissibleValue(text="jwk-set+json"))
        setattr(cls, "kpml-request+xml",
            PermissibleValue(text="kpml-request+xml"))
        setattr(cls, "kpml-response+xml",
            PermissibleValue(text="kpml-response+xml"))
        setattr(cls, "ld+json",
            PermissibleValue(text="ld+json"))
        setattr(cls, "lgr+xml",
            PermissibleValue(text="lgr+xml"))
        setattr(cls, "link-format",
            PermissibleValue(text="link-format"))
        setattr(cls, "linkset+json",
            PermissibleValue(text="linkset+json"))
        setattr(cls, "load-control+xml",
            PermissibleValue(text="load-control+xml"))
        setattr(cls, "logout+jwt",
            PermissibleValue(text="logout+jwt"))
        setattr(cls, "lost+xml",
            PermissibleValue(text="lost+xml"))
        setattr(cls, "lostsync+xml",
            PermissibleValue(text="lostsync+xml"))
        setattr(cls, "lpf+zip",
            PermissibleValue(text="lpf+zip"))
        setattr(cls, "mac-binhex40",
            PermissibleValue(text="mac-binhex40"))
        setattr(cls, "mads+xml",
            PermissibleValue(text="mads+xml"))
        setattr(cls, "manifest+json",
            PermissibleValue(text="manifest+json"))
        setattr(cls, "marcxml+xml",
            PermissibleValue(text="marcxml+xml"))
        setattr(cls, "mathml+xml",
            PermissibleValue(text="mathml+xml"))
        setattr(cls, "mathml-content+xml",
            PermissibleValue(text="mathml-content+xml"))
        setattr(cls, "mathml-presentation+xml",
            PermissibleValue(text="mathml-presentation+xml"))
        setattr(cls, "mbms-associated-procedure-description+xml",
            PermissibleValue(text="mbms-associated-procedure-description+xml"))
        setattr(cls, "mbms-deregister+xml",
            PermissibleValue(text="mbms-deregister+xml"))
        setattr(cls, "mbms-envelope+xml",
            PermissibleValue(text="mbms-envelope+xml"))
        setattr(cls, "mbms-msk-response+xml",
            PermissibleValue(text="mbms-msk-response+xml"))
        setattr(cls, "mbms-msk+xml",
            PermissibleValue(text="mbms-msk+xml"))
        setattr(cls, "mbms-protection-description+xml",
            PermissibleValue(text="mbms-protection-description+xml"))
        setattr(cls, "mbms-reception-report+xml",
            PermissibleValue(text="mbms-reception-report+xml"))
        setattr(cls, "mbms-register-response+xml",
            PermissibleValue(text="mbms-register-response+xml"))
        setattr(cls, "mbms-register+xml",
            PermissibleValue(text="mbms-register+xml"))
        setattr(cls, "mbms-schedule+xml",
            PermissibleValue(text="mbms-schedule+xml"))
        setattr(cls, "mbms-user-service-description+xml",
            PermissibleValue(text="mbms-user-service-description+xml"))
        setattr(cls, "media_control+xml",
            PermissibleValue(text="media_control+xml"))
        setattr(cls, "media-policy-dataset+xml",
            PermissibleValue(text="media-policy-dataset+xml"))
        setattr(cls, "mediaservercontrol+xml",
            PermissibleValue(text="mediaservercontrol+xml"))
        setattr(cls, "merge-patch+json",
            PermissibleValue(text="merge-patch+json"))
        setattr(cls, "metalink4+xml",
            PermissibleValue(text="metalink4+xml"))
        setattr(cls, "mets+xml",
            PermissibleValue(text="mets+xml"))
        setattr(cls, "missing-blocks+cbor-seq",
            PermissibleValue(text="missing-blocks+cbor-seq"))
        setattr(cls, "mmt-aei+xml",
            PermissibleValue(text="mmt-aei+xml"))
        setattr(cls, "mmt-usd+xml",
            PermissibleValue(text="mmt-usd+xml"))
        setattr(cls, "mods+xml",
            PermissibleValue(text="mods+xml"))
        setattr(cls, "moss-keys",
            PermissibleValue(text="moss-keys"))
        setattr(cls, "moss-signature",
            PermissibleValue(text="moss-signature"))
        setattr(cls, "mosskey-data",
            PermissibleValue(text="mosskey-data"))
        setattr(cls, "mosskey-request",
            PermissibleValue(text="mosskey-request"))
        setattr(cls, "mpeg4-generic",
            PermissibleValue(text="mpeg4-generic"))
        setattr(cls, "mpeg4-iod",
            PermissibleValue(text="mpeg4-iod"))
        setattr(cls, "mpeg4-iod-xmt",
            PermissibleValue(text="mpeg4-iod-xmt"))
        setattr(cls, "mrb-consumer+xml",
            PermissibleValue(text="mrb-consumer+xml"))
        setattr(cls, "mrb-publish+xml",
            PermissibleValue(text="mrb-publish+xml"))
        setattr(cls, "msc-ivr+xml",
            PermissibleValue(text="msc-ivr+xml"))
        setattr(cls, "msc-mixer+xml",
            PermissibleValue(text="msc-mixer+xml"))
        setattr(cls, "mud+json",
            PermissibleValue(text="mud+json"))
        setattr(cls, "multipart-core",
            PermissibleValue(text="multipart-core"))
        setattr(cls, "n-quads",
            PermissibleValue(text="n-quads"))
        setattr(cls, "n-triples",
            PermissibleValue(text="n-triples"))
        setattr(cls, "news-checkgroups",
            PermissibleValue(text="news-checkgroups"))
        setattr(cls, "news-groupinfo",
            PermissibleValue(text="news-groupinfo"))
        setattr(cls, "news-transmission",
            PermissibleValue(text="news-transmission"))
        setattr(cls, "nlsml+xml",
            PermissibleValue(text="nlsml+xml"))
        setattr(cls, "oauth-authz-req+jwt",
            PermissibleValue(text="oauth-authz-req+jwt"))
        setattr(cls, "oblivious-dns-message",
            PermissibleValue(text="oblivious-dns-message"))
        setattr(cls, "ocsp-request",
            PermissibleValue(text="ocsp-request"))
        setattr(cls, "ocsp-response",
            PermissibleValue(text="ocsp-response"))
        setattr(cls, "octet-stream",
            PermissibleValue(text="octet-stream"))
        setattr(cls, "odm+xml",
            PermissibleValue(text="odm+xml"))
        setattr(cls, "oebps-package+xml",
            PermissibleValue(text="oebps-package+xml"))
        setattr(cls, "ohttp-keys",
            PermissibleValue(text="ohttp-keys"))
        setattr(cls, "opc-nodeset+xml",
            PermissibleValue(text="opc-nodeset+xml"))
        setattr(cls, "p21+zip",
            PermissibleValue(text="p21+zip"))
        setattr(cls, "p2p-overlay+xml",
            PermissibleValue(text="p2p-overlay+xml"))
        setattr(cls, "patch-ops-error+xml",
            PermissibleValue(text="patch-ops-error+xml"))
        setattr(cls, "pem-certificate-chain",
            PermissibleValue(text="pem-certificate-chain"))
        setattr(cls, "pgp-encrypted",
            PermissibleValue(text="pgp-encrypted"))
        setattr(cls, "pgp-keys",
            PermissibleValue(text="pgp-keys"))
        setattr(cls, "pgp-signature",
            PermissibleValue(text="pgp-signature"))
        setattr(cls, "pidf-diff+xml",
            PermissibleValue(text="pidf-diff+xml"))
        setattr(cls, "pidf+xml",
            PermissibleValue(text="pidf+xml"))
        setattr(cls, "pkcs7-mime",
            PermissibleValue(text="pkcs7-mime"))
        setattr(cls, "pkcs7-signature",
            PermissibleValue(text="pkcs7-signature"))
        setattr(cls, "pkcs8-encrypted",
            PermissibleValue(text="pkcs8-encrypted"))
        setattr(cls, "pkix-attr-cert",
            PermissibleValue(text="pkix-attr-cert"))
        setattr(cls, "pkix-cert",
            PermissibleValue(text="pkix-cert"))
        setattr(cls, "pkix-crl",
            PermissibleValue(text="pkix-crl"))
        setattr(cls, "pkix-pkipath",
            PermissibleValue(text="pkix-pkipath"))
        setattr(cls, "pls+xml",
            PermissibleValue(text="pls+xml"))
        setattr(cls, "poc-settings+xml",
            PermissibleValue(text="poc-settings+xml"))
        setattr(cls, "ppsp-tracker+json",
            PermissibleValue(text="ppsp-tracker+json"))
        setattr(cls, "problem+json",
            PermissibleValue(text="problem+json"))
        setattr(cls, "problem+xml",
            PermissibleValue(text="problem+xml"))
        setattr(cls, "provenance+xml",
            PermissibleValue(text="provenance+xml"))
        setattr(cls, "prs.alvestrand.titrax-sheet",
            PermissibleValue(text="prs.alvestrand.titrax-sheet"))
        setattr(cls, "prs.cww",
            PermissibleValue(text="prs.cww"))
        setattr(cls, "prs.cyn",
            PermissibleValue(text="prs.cyn"))
        setattr(cls, "prs.hpub+zip",
            PermissibleValue(text="prs.hpub+zip"))
        setattr(cls, "prs.implied-document+xml",
            PermissibleValue(text="prs.implied-document+xml"))
        setattr(cls, "prs.implied-executable",
            PermissibleValue(text="prs.implied-executable"))
        setattr(cls, "prs.implied-structure",
            PermissibleValue(text="prs.implied-structure"))
        setattr(cls, "prs.nprend",
            PermissibleValue(text="prs.nprend"))
        setattr(cls, "prs.plucker",
            PermissibleValue(text="prs.plucker"))
        setattr(cls, "prs.rdf-xml-crypt",
            PermissibleValue(text="prs.rdf-xml-crypt"))
        setattr(cls, "prs.vcfbzip2",
            PermissibleValue(text="prs.vcfbzip2"))
        setattr(cls, "prs.xsf+xml",
            PermissibleValue(text="prs.xsf+xml"))
        setattr(cls, "pskc+xml",
            PermissibleValue(text="pskc+xml"))
        setattr(cls, "pvd+json",
            PermissibleValue(text="pvd+json"))
        setattr(cls, "rdf+xml",
            PermissibleValue(text="rdf+xml"))
        setattr(cls, "route-apd+xml",
            PermissibleValue(text="route-apd+xml"))
        setattr(cls, "route-s-tsid+xml",
            PermissibleValue(text="route-s-tsid+xml"))
        setattr(cls, "route-usd+xml",
            PermissibleValue(text="route-usd+xml"))
        setattr(cls, "rdap+json",
            PermissibleValue(text="rdap+json"))
        setattr(cls, "reginfo+xml",
            PermissibleValue(text="reginfo+xml"))
        setattr(cls, "relax-ng-compact-syntax",
            PermissibleValue(text="relax-ng-compact-syntax"))
        setattr(cls, "remote-printing (OBSOLETE)",
            PermissibleValue(text="remote-printing (OBSOLETE)"))
        setattr(cls, "reputon+json",
            PermissibleValue(text="reputon+json"))
        setattr(cls, "resource-lists-diff+xml",
            PermissibleValue(text="resource-lists-diff+xml"))
        setattr(cls, "resource-lists+xml",
            PermissibleValue(text="resource-lists+xml"))
        setattr(cls, "rfc+xml",
            PermissibleValue(text="rfc+xml"))
        setattr(cls, "rlmi+xml",
            PermissibleValue(text="rlmi+xml"))
        setattr(cls, "rls-services+xml",
            PermissibleValue(text="rls-services+xml"))
        setattr(cls, "rpki-checklist",
            PermissibleValue(text="rpki-checklist"))
        setattr(cls, "rpki-ghostbusters",
            PermissibleValue(text="rpki-ghostbusters"))
        setattr(cls, "rpki-manifest",
            PermissibleValue(text="rpki-manifest"))
        setattr(cls, "rpki-publication",
            PermissibleValue(text="rpki-publication"))
        setattr(cls, "rpki-roa",
            PermissibleValue(text="rpki-roa"))
        setattr(cls, "rpki-updown",
            PermissibleValue(text="rpki-updown"))
        setattr(cls, "samlassertion+xml",
            PermissibleValue(text="samlassertion+xml"))
        setattr(cls, "samlmetadata+xml",
            PermissibleValue(text="samlmetadata+xml"))
        setattr(cls, "sarif-external-properties+json",
            PermissibleValue(text="sarif-external-properties+json"))
        setattr(cls, "sarif+json",
            PermissibleValue(text="sarif+json"))
        setattr(cls, "sbml+xml",
            PermissibleValue(text="sbml+xml"))
        setattr(cls, "scaip+xml",
            PermissibleValue(text="scaip+xml"))
        setattr(cls, "scim+json",
            PermissibleValue(text="scim+json"))
        setattr(cls, "scvp-cv-request",
            PermissibleValue(text="scvp-cv-request"))
        setattr(cls, "scvp-cv-response",
            PermissibleValue(text="scvp-cv-response"))
        setattr(cls, "scvp-vp-request",
            PermissibleValue(text="scvp-vp-request"))
        setattr(cls, "scvp-vp-response",
            PermissibleValue(text="scvp-vp-response"))
        setattr(cls, "secevent+jwt",
            PermissibleValue(text="secevent+jwt"))
        setattr(cls, "senml-etch+cbor",
            PermissibleValue(text="senml-etch+cbor"))
        setattr(cls, "senml-etch+json",
            PermissibleValue(text="senml-etch+json"))
        setattr(cls, "senml-exi",
            PermissibleValue(text="senml-exi"))
        setattr(cls, "senml+cbor",
            PermissibleValue(text="senml+cbor"))
        setattr(cls, "senml+json",
            PermissibleValue(text="senml+json"))
        setattr(cls, "senml+xml",
            PermissibleValue(text="senml+xml"))
        setattr(cls, "sensml-exi",
            PermissibleValue(text="sensml-exi"))
        setattr(cls, "sensml+cbor",
            PermissibleValue(text="sensml+cbor"))
        setattr(cls, "sensml+json",
            PermissibleValue(text="sensml+json"))
        setattr(cls, "sensml+xml",
            PermissibleValue(text="sensml+xml"))
        setattr(cls, "sep-exi",
            PermissibleValue(text="sep-exi"))
        setattr(cls, "sep+xml",
            PermissibleValue(text="sep+xml"))
        setattr(cls, "session-info",
            PermissibleValue(text="session-info"))
        setattr(cls, "set-payment",
            PermissibleValue(text="set-payment"))
        setattr(cls, "set-payment-initiation",
            PermissibleValue(text="set-payment-initiation"))
        setattr(cls, "set-registration",
            PermissibleValue(text="set-registration"))
        setattr(cls, "set-registration-initiation",
            PermissibleValue(text="set-registration-initiation"))
        setattr(cls, "sgml-open-catalog",
            PermissibleValue(text="sgml-open-catalog"))
        setattr(cls, "shf+xml",
            PermissibleValue(text="shf+xml"))
        setattr(cls, "simple-filter+xml",
            PermissibleValue(text="simple-filter+xml"))
        setattr(cls, "simple-message-summary",
            PermissibleValue(text="simple-message-summary"))
        setattr(cls, "smil (OBSOLETED in favor of application/smil+xml)",
            PermissibleValue(text="smil (OBSOLETED in favor of application/smil+xml)"))
        setattr(cls, "smil+xml",
            PermissibleValue(text="smil+xml"))
        setattr(cls, "soap+fastinfoset",
            PermissibleValue(text="soap+fastinfoset"))
        setattr(cls, "soap+xml",
            PermissibleValue(text="soap+xml"))
        setattr(cls, "sparql-query",
            PermissibleValue(text="sparql-query"))
        setattr(cls, "spdx+json",
            PermissibleValue(text="spdx+json"))
        setattr(cls, "sparql-results+xml",
            PermissibleValue(text="sparql-results+xml"))
        setattr(cls, "spirits-event+xml",
            PermissibleValue(text="spirits-event+xml"))
        setattr(cls, "srgs+xml",
            PermissibleValue(text="srgs+xml"))
        setattr(cls, "sru+xml",
            PermissibleValue(text="sru+xml"))
        setattr(cls, "ssml+xml",
            PermissibleValue(text="ssml+xml"))
        setattr(cls, "stix+json",
            PermissibleValue(text="stix+json"))
        setattr(cls, "swid+cbor",
            PermissibleValue(text="swid+cbor"))
        setattr(cls, "swid+xml",
            PermissibleValue(text="swid+xml"))
        setattr(cls, "tamp-apex-update",
            PermissibleValue(text="tamp-apex-update"))
        setattr(cls, "tamp-apex-update-confirm",
            PermissibleValue(text="tamp-apex-update-confirm"))
        setattr(cls, "tamp-community-update",
            PermissibleValue(text="tamp-community-update"))
        setattr(cls, "tamp-community-update-confirm",
            PermissibleValue(text="tamp-community-update-confirm"))
        setattr(cls, "tamp-error",
            PermissibleValue(text="tamp-error"))
        setattr(cls, "tamp-sequence-adjust",
            PermissibleValue(text="tamp-sequence-adjust"))
        setattr(cls, "tamp-sequence-adjust-confirm",
            PermissibleValue(text="tamp-sequence-adjust-confirm"))
        setattr(cls, "tamp-status-query",
            PermissibleValue(text="tamp-status-query"))
        setattr(cls, "tamp-status-response",
            PermissibleValue(text="tamp-status-response"))
        setattr(cls, "tamp-update",
            PermissibleValue(text="tamp-update"))
        setattr(cls, "tamp-update-confirm",
            PermissibleValue(text="tamp-update-confirm"))
        setattr(cls, "taxii+json",
            PermissibleValue(text="taxii+json"))
        setattr(cls, "td+json",
            PermissibleValue(text="td+json"))
        setattr(cls, "tei+xml",
            PermissibleValue(text="tei+xml"))
        setattr(cls, "thraud+xml",
            PermissibleValue(text="thraud+xml"))
        setattr(cls, "timestamp-query",
            PermissibleValue(text="timestamp-query"))
        setattr(cls, "timestamp-reply",
            PermissibleValue(text="timestamp-reply"))
        setattr(cls, "timestamped-data",
            PermissibleValue(text="timestamped-data"))
        setattr(cls, "tlsrpt+gzip",
            PermissibleValue(text="tlsrpt+gzip"))
        setattr(cls, "tlsrpt+json",
            PermissibleValue(text="tlsrpt+json"))
        setattr(cls, "tm+json",
            PermissibleValue(text="tm+json"))
        setattr(cls, "token-introspection+jwt",
            PermissibleValue(text="token-introspection+jwt"))
        setattr(cls, "trickle-ice-sdpfrag",
            PermissibleValue(text="trickle-ice-sdpfrag"))
        setattr(cls, "ttml+xml",
            PermissibleValue(text="ttml+xml"))
        setattr(cls, "tve-trigger",
            PermissibleValue(text="tve-trigger"))
        setattr(cls, "tzif-leap",
            PermissibleValue(text="tzif-leap"))
        setattr(cls, "urc-grpsheet+xml",
            PermissibleValue(text="urc-grpsheet+xml"))
        setattr(cls, "urc-ressheet+xml",
            PermissibleValue(text="urc-ressheet+xml"))
        setattr(cls, "urc-targetdesc+xml",
            PermissibleValue(text="urc-targetdesc+xml"))
        setattr(cls, "urc-uisocketdesc+xml",
            PermissibleValue(text="urc-uisocketdesc+xml"))
        setattr(cls, "vcard+json",
            PermissibleValue(text="vcard+json"))
        setattr(cls, "vcard+xml",
            PermissibleValue(text="vcard+xml"))
        setattr(cls, "vnd.1000minds.decision-model+xml",
            PermissibleValue(text="vnd.1000minds.decision-model+xml"))
        setattr(cls, "vnd.1ob",
            PermissibleValue(text="vnd.1ob"))
        setattr(cls, "vnd.3gpp.5gnas",
            PermissibleValue(text="vnd.3gpp.5gnas"))
        setattr(cls, "vnd.3gpp.access-transfer-events+xml",
            PermissibleValue(text="vnd.3gpp.access-transfer-events+xml"))
        setattr(cls, "vnd.3gpp.bsf+xml",
            PermissibleValue(text="vnd.3gpp.bsf+xml"))
        setattr(cls, "vnd.3gpp.crs+xml",
            PermissibleValue(text="vnd.3gpp.crs+xml"))
        setattr(cls, "vnd.3gpp.current-location-discovery+xml",
            PermissibleValue(text="vnd.3gpp.current-location-discovery+xml"))
        setattr(cls, "vnd.3gpp.GMOP+xml",
            PermissibleValue(text="vnd.3gpp.GMOP+xml"))
        setattr(cls, "vnd.3gpp.gtpc",
            PermissibleValue(text="vnd.3gpp.gtpc"))
        setattr(cls, "vnd.3gpp.interworking-data",
            PermissibleValue(text="vnd.3gpp.interworking-data"))
        setattr(cls, "vnd.3gpp.lpp",
            PermissibleValue(text="vnd.3gpp.lpp"))
        setattr(cls, "vnd.3gpp.mc-signalling-ear",
            PermissibleValue(text="vnd.3gpp.mc-signalling-ear"))
        setattr(cls, "vnd.3gpp.mcdata-affiliation-command+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-affiliation-command+xml"))
        setattr(cls, "vnd.3gpp.mcdata-info+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-info+xml"))
        setattr(cls, "vnd.3gpp.mcdata-msgstore-ctrl-request+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-msgstore-ctrl-request+xml"))
        setattr(cls, "vnd.3gpp.mcdata-payload",
            PermissibleValue(text="vnd.3gpp.mcdata-payload"))
        setattr(cls, "vnd.3gpp.mcdata-regroup+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-regroup+xml"))
        setattr(cls, "vnd.3gpp.mcdata-service-config+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-service-config+xml"))
        setattr(cls, "vnd.3gpp.mcdata-signalling",
            PermissibleValue(text="vnd.3gpp.mcdata-signalling"))
        setattr(cls, "vnd.3gpp.mcdata-ue-config+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-ue-config+xml"))
        setattr(cls, "vnd.3gpp.mcdata-user-profile+xml",
            PermissibleValue(text="vnd.3gpp.mcdata-user-profile+xml"))
        setattr(cls, "vnd.3gpp.mcptt-affiliation-command+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-affiliation-command+xml"))
        setattr(cls, "vnd.3gpp.mcptt-floor-request+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-floor-request+xml"))
        setattr(cls, "vnd.3gpp.mcptt-info+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-info+xml"))
        setattr(cls, "vnd.3gpp.mcptt-location-info+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-location-info+xml"))
        setattr(cls, "vnd.3gpp.mcptt-mbms-usage-info+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-mbms-usage-info+xml"))
        setattr(cls, "vnd.3gpp.mcptt-regroup+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-regroup+xml"))
        setattr(cls, "vnd.3gpp.mcptt-service-config+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-service-config+xml"))
        setattr(cls, "vnd.3gpp.mcptt-signed+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-signed+xml"))
        setattr(cls, "vnd.3gpp.mcptt-ue-config+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-ue-config+xml"))
        setattr(cls, "vnd.3gpp.mcptt-ue-init-config+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-ue-init-config+xml"))
        setattr(cls, "vnd.3gpp.mcptt-user-profile+xml",
            PermissibleValue(text="vnd.3gpp.mcptt-user-profile+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-affiliation-command+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-affiliation-command+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-affiliation-info+xml (OBSOLETED in favor of application/vnd.3gpp.mcvideo-info+xml)",
            PermissibleValue(text="vnd.3gpp.mcvideo-affiliation-info+xml (OBSOLETED in favor of application/vnd.3gpp.mcvideo-info+xml)"))
        setattr(cls, "vnd.3gpp.mcvideo-info+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-info+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-location-info+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-location-info+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-mbms-usage-info+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-mbms-usage-info+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-regroup+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-regroup+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-service-config+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-service-config+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-transmission-request+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-transmission-request+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-ue-config+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-ue-config+xml"))
        setattr(cls, "vnd.3gpp.mcvideo-user-profile+xml",
            PermissibleValue(text="vnd.3gpp.mcvideo-user-profile+xml"))
        setattr(cls, "vnd.3gpp.mid-call+xml",
            PermissibleValue(text="vnd.3gpp.mid-call+xml"))
        setattr(cls, "vnd.3gpp.ngap",
            PermissibleValue(text="vnd.3gpp.ngap"))
        setattr(cls, "vnd.3gpp.pfcp",
            PermissibleValue(text="vnd.3gpp.pfcp"))
        setattr(cls, "vnd.3gpp.pic-bw-large",
            PermissibleValue(text="vnd.3gpp.pic-bw-large"))
        setattr(cls, "vnd.3gpp.pic-bw-small",
            PermissibleValue(text="vnd.3gpp.pic-bw-small"))
        setattr(cls, "vnd.3gpp.pic-bw-var",
            PermissibleValue(text="vnd.3gpp.pic-bw-var"))
        setattr(cls, "vnd.3gpp-prose-pc3a+xml",
            PermissibleValue(text="vnd.3gpp-prose-pc3a+xml"))
        setattr(cls, "vnd.3gpp-prose-pc3ach+xml",
            PermissibleValue(text="vnd.3gpp-prose-pc3ach+xml"))
        setattr(cls, "vnd.3gpp-prose-pc3ch+xml",
            PermissibleValue(text="vnd.3gpp-prose-pc3ch+xml"))
        setattr(cls, "vnd.3gpp-prose-pc8+xml",
            PermissibleValue(text="vnd.3gpp-prose-pc8+xml"))
        setattr(cls, "vnd.3gpp-prose+xml",
            PermissibleValue(text="vnd.3gpp-prose+xml"))
        setattr(cls, "vnd.3gpp.s1ap",
            PermissibleValue(text="vnd.3gpp.s1ap"))
        setattr(cls, "vnd.3gpp.seal-group-doc+xml",
            PermissibleValue(text="vnd.3gpp.seal-group-doc+xml"))
        setattr(cls, "vnd.3gpp.seal-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-info+xml"))
        setattr(cls, "vnd.3gpp.seal-location-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-location-info+xml"))
        setattr(cls, "vnd.3gpp.seal-mbms-usage-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-mbms-usage-info+xml"))
        setattr(cls, "vnd.3gpp.seal-network-QoS-management-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-network-QoS-management-info+xml"))
        setattr(cls, "vnd.3gpp.seal-ue-config-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-ue-config-info+xml"))
        setattr(cls, "vnd.3gpp.seal-unicast-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-unicast-info+xml"))
        setattr(cls, "vnd.3gpp.seal-user-profile-info+xml",
            PermissibleValue(text="vnd.3gpp.seal-user-profile-info+xml"))
        setattr(cls, "vnd.3gpp.sms",
            PermissibleValue(text="vnd.3gpp.sms"))
        setattr(cls, "vnd.3gpp.sms+xml",
            PermissibleValue(text="vnd.3gpp.sms+xml"))
        setattr(cls, "vnd.3gpp.srvcc-ext+xml",
            PermissibleValue(text="vnd.3gpp.srvcc-ext+xml"))
        setattr(cls, "vnd.3gpp.SRVCC-info+xml",
            PermissibleValue(text="vnd.3gpp.SRVCC-info+xml"))
        setattr(cls, "vnd.3gpp.state-and-event-info+xml",
            PermissibleValue(text="vnd.3gpp.state-and-event-info+xml"))
        setattr(cls, "vnd.3gpp.ussd+xml",
            PermissibleValue(text="vnd.3gpp.ussd+xml"))
        setattr(cls, "vnd.3gpp.vae-info+xml",
            PermissibleValue(text="vnd.3gpp.vae-info+xml"))
        setattr(cls, "vnd.3gpp-v2x-local-service-information",
            PermissibleValue(text="vnd.3gpp-v2x-local-service-information"))
        setattr(cls, "vnd.3gpp2.bcmcsinfo+xml",
            PermissibleValue(text="vnd.3gpp2.bcmcsinfo+xml"))
        setattr(cls, "vnd.3gpp2.sms",
            PermissibleValue(text="vnd.3gpp2.sms"))
        setattr(cls, "vnd.3gpp2.tcap",
            PermissibleValue(text="vnd.3gpp2.tcap"))
        setattr(cls, "vnd.3gpp.v2x",
            PermissibleValue(text="vnd.3gpp.v2x"))
        setattr(cls, "vnd.3lightssoftware.imagescal",
            PermissibleValue(text="vnd.3lightssoftware.imagescal"))
        setattr(cls, "vnd.3M.Post-it-Notes",
            PermissibleValue(text="vnd.3M.Post-it-Notes"))
        setattr(cls, "vnd.accpac.simply.aso",
            PermissibleValue(text="vnd.accpac.simply.aso"))
        setattr(cls, "vnd.accpac.simply.imp",
            PermissibleValue(text="vnd.accpac.simply.imp"))
        setattr(cls, "vnd.acm.addressxfer+json",
            PermissibleValue(text="vnd.acm.addressxfer+json"))
        setattr(cls, "vnd.acm.chatbot+json",
            PermissibleValue(text="vnd.acm.chatbot+json"))
        setattr(cls, "vnd.acucobol",
            PermissibleValue(text="vnd.acucobol"))
        setattr(cls, "vnd.acucorp",
            PermissibleValue(text="vnd.acucorp"))
        setattr(cls, "vnd.adobe.flash.movie",
            PermissibleValue(text="vnd.adobe.flash.movie"))
        setattr(cls, "vnd.adobe.formscentral.fcdt",
            PermissibleValue(text="vnd.adobe.formscentral.fcdt"))
        setattr(cls, "vnd.adobe.fxp",
            PermissibleValue(text="vnd.adobe.fxp"))
        setattr(cls, "vnd.adobe.partial-upload",
            PermissibleValue(text="vnd.adobe.partial-upload"))
        setattr(cls, "vnd.adobe.xdp+xml",
            PermissibleValue(text="vnd.adobe.xdp+xml"))
        setattr(cls, "vnd.aether.imp",
            PermissibleValue(text="vnd.aether.imp"))
        setattr(cls, "vnd.afpc.afplinedata",
            PermissibleValue(text="vnd.afpc.afplinedata"))
        setattr(cls, "vnd.afpc.afplinedata-pagedef",
            PermissibleValue(text="vnd.afpc.afplinedata-pagedef"))
        setattr(cls, "vnd.afpc.cmoca-cmresource",
            PermissibleValue(text="vnd.afpc.cmoca-cmresource"))
        setattr(cls, "vnd.afpc.foca-charset",
            PermissibleValue(text="vnd.afpc.foca-charset"))
        setattr(cls, "vnd.afpc.foca-codedfont",
            PermissibleValue(text="vnd.afpc.foca-codedfont"))
        setattr(cls, "vnd.afpc.foca-codepage",
            PermissibleValue(text="vnd.afpc.foca-codepage"))
        setattr(cls, "vnd.afpc.modca",
            PermissibleValue(text="vnd.afpc.modca"))
        setattr(cls, "vnd.afpc.modca-cmtable",
            PermissibleValue(text="vnd.afpc.modca-cmtable"))
        setattr(cls, "vnd.afpc.modca-formdef",
            PermissibleValue(text="vnd.afpc.modca-formdef"))
        setattr(cls, "vnd.afpc.modca-mediummap",
            PermissibleValue(text="vnd.afpc.modca-mediummap"))
        setattr(cls, "vnd.afpc.modca-objectcontainer",
            PermissibleValue(text="vnd.afpc.modca-objectcontainer"))
        setattr(cls, "vnd.afpc.modca-overlay",
            PermissibleValue(text="vnd.afpc.modca-overlay"))
        setattr(cls, "vnd.afpc.modca-pagesegment",
            PermissibleValue(text="vnd.afpc.modca-pagesegment"))
        setattr(cls, "vnd.age",
            PermissibleValue(text="vnd.age"))
        setattr(cls, "vnd.ah-barcode",
            PermissibleValue(text="vnd.ah-barcode"))
        setattr(cls, "vnd.ahead.space",
            PermissibleValue(text="vnd.ahead.space"))
        setattr(cls, "vnd.airzip.filesecure.azf",
            PermissibleValue(text="vnd.airzip.filesecure.azf"))
        setattr(cls, "vnd.airzip.filesecure.azs",
            PermissibleValue(text="vnd.airzip.filesecure.azs"))
        setattr(cls, "vnd.amadeus+json",
            PermissibleValue(text="vnd.amadeus+json"))
        setattr(cls, "vnd.amazon.mobi8-ebook",
            PermissibleValue(text="vnd.amazon.mobi8-ebook"))
        setattr(cls, "vnd.americandynamics.acc",
            PermissibleValue(text="vnd.americandynamics.acc"))
        setattr(cls, "vnd.amiga.ami",
            PermissibleValue(text="vnd.amiga.ami"))
        setattr(cls, "vnd.amundsen.maze+xml",
            PermissibleValue(text="vnd.amundsen.maze+xml"))
        setattr(cls, "vnd.android.ota",
            PermissibleValue(text="vnd.android.ota"))
        setattr(cls, "vnd.anki",
            PermissibleValue(text="vnd.anki"))
        setattr(cls, "vnd.anser-web-certificate-issue-initiation",
            PermissibleValue(text="vnd.anser-web-certificate-issue-initiation"))
        setattr(cls, "vnd.antix.game-component",
            PermissibleValue(text="vnd.antix.game-component"))
        setattr(cls, "vnd.apache.arrow.file",
            PermissibleValue(text="vnd.apache.arrow.file"))
        setattr(cls, "vnd.apache.arrow.stream",
            PermissibleValue(text="vnd.apache.arrow.stream"))
        setattr(cls, "vnd.apache.thrift.binary",
            PermissibleValue(text="vnd.apache.thrift.binary"))
        setattr(cls, "vnd.apache.thrift.compact",
            PermissibleValue(text="vnd.apache.thrift.compact"))
        setattr(cls, "vnd.apache.thrift.json",
            PermissibleValue(text="vnd.apache.thrift.json"))
        setattr(cls, "vnd.apexlang",
            PermissibleValue(text="vnd.apexlang"))
        setattr(cls, "vnd.api+json",
            PermissibleValue(text="vnd.api+json"))
        setattr(cls, "vnd.aplextor.warrp+json",
            PermissibleValue(text="vnd.aplextor.warrp+json"))
        setattr(cls, "vnd.apothekende.reservation+json",
            PermissibleValue(text="vnd.apothekende.reservation+json"))
        setattr(cls, "vnd.apple.installer+xml",
            PermissibleValue(text="vnd.apple.installer+xml"))
        setattr(cls, "vnd.apple.keynote",
            PermissibleValue(text="vnd.apple.keynote"))
        setattr(cls, "vnd.apple.mpegurl",
            PermissibleValue(text="vnd.apple.mpegurl"))
        setattr(cls, "vnd.apple.numbers",
            PermissibleValue(text="vnd.apple.numbers"))
        setattr(cls, "vnd.apple.pages",
            PermissibleValue(text="vnd.apple.pages"))
        setattr(cls, "vnd.arastra.swi (OBSOLETED in favor of application/vnd.aristanetworks.swi)",
            PermissibleValue(text="vnd.arastra.swi (OBSOLETED in favor of application/vnd.aristanetworks.swi)"))
        setattr(cls, "vnd.aristanetworks.swi",
            PermissibleValue(text="vnd.aristanetworks.swi"))
        setattr(cls, "vnd.artisan+json",
            PermissibleValue(text="vnd.artisan+json"))
        setattr(cls, "vnd.artsquare",
            PermissibleValue(text="vnd.artsquare"))
        setattr(cls, "vnd.astraea-software.iota",
            PermissibleValue(text="vnd.astraea-software.iota"))
        setattr(cls, "vnd.audiograph",
            PermissibleValue(text="vnd.audiograph"))
        setattr(cls, "vnd.autopackage",
            PermissibleValue(text="vnd.autopackage"))
        setattr(cls, "vnd.avalon+json",
            PermissibleValue(text="vnd.avalon+json"))
        setattr(cls, "vnd.avistar+xml",
            PermissibleValue(text="vnd.avistar+xml"))
        setattr(cls, "vnd.balsamiq.bmml+xml",
            PermissibleValue(text="vnd.balsamiq.bmml+xml"))
        setattr(cls, "vnd.banana-accounting",
            PermissibleValue(text="vnd.banana-accounting"))
        setattr(cls, "vnd.bbf.usp.error",
            PermissibleValue(text="vnd.bbf.usp.error"))
        setattr(cls, "vnd.bbf.usp.msg",
            PermissibleValue(text="vnd.bbf.usp.msg"))
        setattr(cls, "vnd.bbf.usp.msg+json",
            PermissibleValue(text="vnd.bbf.usp.msg+json"))
        setattr(cls, "vnd.balsamiq.bmpr",
            PermissibleValue(text="vnd.balsamiq.bmpr"))
        setattr(cls, "vnd.bekitzur-stech+json",
            PermissibleValue(text="vnd.bekitzur-stech+json"))
        setattr(cls, "vnd.belightsoft.lhzd+zip",
            PermissibleValue(text="vnd.belightsoft.lhzd+zip"))
        setattr(cls, "vnd.belightsoft.lhzl+zip",
            PermissibleValue(text="vnd.belightsoft.lhzl+zip"))
        setattr(cls, "vnd.bint.med-content",
            PermissibleValue(text="vnd.bint.med-content"))
        setattr(cls, "vnd.biopax.rdf+xml",
            PermissibleValue(text="vnd.biopax.rdf+xml"))
        setattr(cls, "vnd.blink-idb-value-wrapper",
            PermissibleValue(text="vnd.blink-idb-value-wrapper"))
        setattr(cls, "vnd.blueice.multipass",
            PermissibleValue(text="vnd.blueice.multipass"))
        setattr(cls, "vnd.bluetooth.ep.oob",
            PermissibleValue(text="vnd.bluetooth.ep.oob"))
        setattr(cls, "vnd.bluetooth.le.oob",
            PermissibleValue(text="vnd.bluetooth.le.oob"))
        setattr(cls, "vnd.bmi",
            PermissibleValue(text="vnd.bmi"))
        setattr(cls, "vnd.bpf",
            PermissibleValue(text="vnd.bpf"))
        setattr(cls, "vnd.bpf3",
            PermissibleValue(text="vnd.bpf3"))
        setattr(cls, "vnd.businessobjects",
            PermissibleValue(text="vnd.businessobjects"))
        setattr(cls, "vnd.byu.uapi+json",
            PermissibleValue(text="vnd.byu.uapi+json"))
        setattr(cls, "vnd.cab-jscript",
            PermissibleValue(text="vnd.cab-jscript"))
        setattr(cls, "vnd.canon-cpdl",
            PermissibleValue(text="vnd.canon-cpdl"))
        setattr(cls, "vnd.canon-lips",
            PermissibleValue(text="vnd.canon-lips"))
        setattr(cls, "vnd.capasystems-pg+json",
            PermissibleValue(text="vnd.capasystems-pg+json"))
        setattr(cls, "vnd.cendio.thinlinc.clientconf",
            PermissibleValue(text="vnd.cendio.thinlinc.clientconf"))
        setattr(cls, "vnd.century-systems.tcp_stream",
            PermissibleValue(text="vnd.century-systems.tcp_stream"))
        setattr(cls, "vnd.chemdraw+xml",
            PermissibleValue(text="vnd.chemdraw+xml"))
        setattr(cls, "vnd.chess-pgn",
            PermissibleValue(text="vnd.chess-pgn"))
        setattr(cls, "vnd.chipnuts.karaoke-mmd",
            PermissibleValue(text="vnd.chipnuts.karaoke-mmd"))
        setattr(cls, "vnd.ciedi",
            PermissibleValue(text="vnd.ciedi"))
        setattr(cls, "vnd.cinderella",
            PermissibleValue(text="vnd.cinderella"))
        setattr(cls, "vnd.cirpack.isdn-ext",
            PermissibleValue(text="vnd.cirpack.isdn-ext"))
        setattr(cls, "vnd.citationstyles.style+xml",
            PermissibleValue(text="vnd.citationstyles.style+xml"))
        setattr(cls, "vnd.claymore",
            PermissibleValue(text="vnd.claymore"))
        setattr(cls, "vnd.cloanto.rp9",
            PermissibleValue(text="vnd.cloanto.rp9"))
        setattr(cls, "vnd.clonk.c4group",
            PermissibleValue(text="vnd.clonk.c4group"))
        setattr(cls, "vnd.cluetrust.cartomobile-config",
            PermissibleValue(text="vnd.cluetrust.cartomobile-config"))
        setattr(cls, "vnd.cluetrust.cartomobile-config-pkg",
            PermissibleValue(text="vnd.cluetrust.cartomobile-config-pkg"))
        setattr(cls, "vnd.cncf.helm.chart.content.v1.tar+gzip",
            PermissibleValue(text="vnd.cncf.helm.chart.content.v1.tar+gzip"))
        setattr(cls, "vnd.cncf.helm.chart.provenance.v1.prov",
            PermissibleValue(text="vnd.cncf.helm.chart.provenance.v1.prov"))
        setattr(cls, "vnd.cncf.helm.config.v1+json",
            PermissibleValue(text="vnd.cncf.helm.config.v1+json"))
        setattr(cls, "vnd.coffeescript",
            PermissibleValue(text="vnd.coffeescript"))
        setattr(cls, "vnd.collabio.xodocuments.document",
            PermissibleValue(text="vnd.collabio.xodocuments.document"))
        setattr(cls, "vnd.collabio.xodocuments.document-template",
            PermissibleValue(text="vnd.collabio.xodocuments.document-template"))
        setattr(cls, "vnd.collabio.xodocuments.presentation",
            PermissibleValue(text="vnd.collabio.xodocuments.presentation"))
        setattr(cls, "vnd.collabio.xodocuments.presentation-template",
            PermissibleValue(text="vnd.collabio.xodocuments.presentation-template"))
        setattr(cls, "vnd.collabio.xodocuments.spreadsheet",
            PermissibleValue(text="vnd.collabio.xodocuments.spreadsheet"))
        setattr(cls, "vnd.collabio.xodocuments.spreadsheet-template",
            PermissibleValue(text="vnd.collabio.xodocuments.spreadsheet-template"))
        setattr(cls, "vnd.collection.doc+json",
            PermissibleValue(text="vnd.collection.doc+json"))
        setattr(cls, "vnd.collection+json",
            PermissibleValue(text="vnd.collection+json"))
        setattr(cls, "vnd.collection.next+json",
            PermissibleValue(text="vnd.collection.next+json"))
        setattr(cls, "vnd.comicbook-rar",
            PermissibleValue(text="vnd.comicbook-rar"))
        setattr(cls, "vnd.comicbook+zip",
            PermissibleValue(text="vnd.comicbook+zip"))
        setattr(cls, "vnd.commerce-battelle",
            PermissibleValue(text="vnd.commerce-battelle"))
        setattr(cls, "vnd.commonspace",
            PermissibleValue(text="vnd.commonspace"))
        setattr(cls, "vnd.coreos.ignition+json",
            PermissibleValue(text="vnd.coreos.ignition+json"))
        setattr(cls, "vnd.cosmocaller",
            PermissibleValue(text="vnd.cosmocaller"))
        setattr(cls, "vnd.contact.cmsg",
            PermissibleValue(text="vnd.contact.cmsg"))
        setattr(cls, "vnd.crick.clicker",
            PermissibleValue(text="vnd.crick.clicker"))
        setattr(cls, "vnd.crick.clicker.keyboard",
            PermissibleValue(text="vnd.crick.clicker.keyboard"))
        setattr(cls, "vnd.crick.clicker.palette",
            PermissibleValue(text="vnd.crick.clicker.palette"))
        setattr(cls, "vnd.crick.clicker.template",
            PermissibleValue(text="vnd.crick.clicker.template"))
        setattr(cls, "vnd.crick.clicker.wordbank",
            PermissibleValue(text="vnd.crick.clicker.wordbank"))
        setattr(cls, "vnd.criticaltools.wbs+xml",
            PermissibleValue(text="vnd.criticaltools.wbs+xml"))
        setattr(cls, "vnd.cryptii.pipe+json",
            PermissibleValue(text="vnd.cryptii.pipe+json"))
        setattr(cls, "vnd.crypto-shade-file",
            PermissibleValue(text="vnd.crypto-shade-file"))
        setattr(cls, "vnd.cryptomator.encrypted",
            PermissibleValue(text="vnd.cryptomator.encrypted"))
        setattr(cls, "vnd.cryptomator.vault",
            PermissibleValue(text="vnd.cryptomator.vault"))
        setattr(cls, "vnd.ctc-posml",
            PermissibleValue(text="vnd.ctc-posml"))
        setattr(cls, "vnd.ctct.ws+xml",
            PermissibleValue(text="vnd.ctct.ws+xml"))
        setattr(cls, "vnd.cups-pdf",
            PermissibleValue(text="vnd.cups-pdf"))
        setattr(cls, "vnd.cups-postscript",
            PermissibleValue(text="vnd.cups-postscript"))
        setattr(cls, "vnd.cups-ppd",
            PermissibleValue(text="vnd.cups-ppd"))
        setattr(cls, "vnd.cups-raster",
            PermissibleValue(text="vnd.cups-raster"))
        setattr(cls, "vnd.cups-raw",
            PermissibleValue(text="vnd.cups-raw"))
        setattr(cls, "vnd.cyan.dean.root+xml",
            PermissibleValue(text="vnd.cyan.dean.root+xml"))
        setattr(cls, "vnd.cybank",
            PermissibleValue(text="vnd.cybank"))
        setattr(cls, "vnd.cyclonedx+json",
            PermissibleValue(text="vnd.cyclonedx+json"))
        setattr(cls, "vnd.cyclonedx+xml",
            PermissibleValue(text="vnd.cyclonedx+xml"))
        setattr(cls, "vnd.d2l.coursepackage1p0+zip",
            PermissibleValue(text="vnd.d2l.coursepackage1p0+zip"))
        setattr(cls, "vnd.d3m-dataset",
            PermissibleValue(text="vnd.d3m-dataset"))
        setattr(cls, "vnd.d3m-problem",
            PermissibleValue(text="vnd.d3m-problem"))
        setattr(cls, "vnd.dart",
            PermissibleValue(text="vnd.dart"))
        setattr(cls, "vnd.data-vision.rdz",
            PermissibleValue(text="vnd.data-vision.rdz"))
        setattr(cls, "vnd.datalog",
            PermissibleValue(text="vnd.datalog"))
        setattr(cls, "vnd.datapackage+json",
            PermissibleValue(text="vnd.datapackage+json"))
        setattr(cls, "vnd.dataresource+json",
            PermissibleValue(text="vnd.dataresource+json"))
        setattr(cls, "vnd.dbf",
            PermissibleValue(text="vnd.dbf"))
        setattr(cls, "vnd.debian.binary-package",
            PermissibleValue(text="vnd.debian.binary-package"))
        setattr(cls, "vnd.dece.data",
            PermissibleValue(text="vnd.dece.data"))
        setattr(cls, "vnd.dece.ttml+xml",
            PermissibleValue(text="vnd.dece.ttml+xml"))
        setattr(cls, "vnd.dece.unspecified",
            PermissibleValue(text="vnd.dece.unspecified"))
        setattr(cls, "vnd.dece.zip",
            PermissibleValue(text="vnd.dece.zip"))
        setattr(cls, "vnd.denovo.fcselayout-link",
            PermissibleValue(text="vnd.denovo.fcselayout-link"))
        setattr(cls, "vnd.desmume.movie",
            PermissibleValue(text="vnd.desmume.movie"))
        setattr(cls, "vnd.dir-bi.plate-dl-nosuffix",
            PermissibleValue(text="vnd.dir-bi.plate-dl-nosuffix"))
        setattr(cls, "vnd.dm.delegation+xml",
            PermissibleValue(text="vnd.dm.delegation+xml"))
        setattr(cls, "vnd.dna",
            PermissibleValue(text="vnd.dna"))
        setattr(cls, "vnd.document+json",
            PermissibleValue(text="vnd.document+json"))
        setattr(cls, "vnd.dolby.mobile.1",
            PermissibleValue(text="vnd.dolby.mobile.1"))
        setattr(cls, "vnd.dolby.mobile.2",
            PermissibleValue(text="vnd.dolby.mobile.2"))
        setattr(cls, "vnd.doremir.scorecloud-binary-document",
            PermissibleValue(text="vnd.doremir.scorecloud-binary-document"))
        setattr(cls, "vnd.dpgraph",
            PermissibleValue(text="vnd.dpgraph"))
        setattr(cls, "vnd.dreamfactory",
            PermissibleValue(text="vnd.dreamfactory"))
        setattr(cls, "vnd.drive+json",
            PermissibleValue(text="vnd.drive+json"))
        setattr(cls, "vnd.dtg.local",
            PermissibleValue(text="vnd.dtg.local"))
        setattr(cls, "vnd.dtg.local.flash",
            PermissibleValue(text="vnd.dtg.local.flash"))
        setattr(cls, "vnd.dtg.local.html",
            PermissibleValue(text="vnd.dtg.local.html"))
        setattr(cls, "vnd.dvb.ait",
            PermissibleValue(text="vnd.dvb.ait"))
        setattr(cls, "vnd.dvb.dvbisl+xml",
            PermissibleValue(text="vnd.dvb.dvbisl+xml"))
        setattr(cls, "vnd.dvb.dvbj",
            PermissibleValue(text="vnd.dvb.dvbj"))
        setattr(cls, "vnd.dvb.esgcontainer",
            PermissibleValue(text="vnd.dvb.esgcontainer"))
        setattr(cls, "vnd.dvb.ipdcdftnotifaccess",
            PermissibleValue(text="vnd.dvb.ipdcdftnotifaccess"))
        setattr(cls, "vnd.dvb.ipdcesgaccess",
            PermissibleValue(text="vnd.dvb.ipdcesgaccess"))
        setattr(cls, "vnd.dvb.ipdcesgaccess2",
            PermissibleValue(text="vnd.dvb.ipdcesgaccess2"))
        setattr(cls, "vnd.dvb.ipdcesgpdd",
            PermissibleValue(text="vnd.dvb.ipdcesgpdd"))
        setattr(cls, "vnd.dvb.ipdcroaming",
            PermissibleValue(text="vnd.dvb.ipdcroaming"))
        setattr(cls, "vnd.dvb.iptv.alfec-base",
            PermissibleValue(text="vnd.dvb.iptv.alfec-base"))
        setattr(cls, "vnd.dvb.iptv.alfec-enhancement",
            PermissibleValue(text="vnd.dvb.iptv.alfec-enhancement"))
        setattr(cls, "vnd.dvb.notif-aggregate-root+xml",
            PermissibleValue(text="vnd.dvb.notif-aggregate-root+xml"))
        setattr(cls, "vnd.dvb.notif-container+xml",
            PermissibleValue(text="vnd.dvb.notif-container+xml"))
        setattr(cls, "vnd.dvb.notif-generic+xml",
            PermissibleValue(text="vnd.dvb.notif-generic+xml"))
        setattr(cls, "vnd.dvb.notif-ia-msglist+xml",
            PermissibleValue(text="vnd.dvb.notif-ia-msglist+xml"))
        setattr(cls, "vnd.dvb.notif-ia-registration-request+xml",
            PermissibleValue(text="vnd.dvb.notif-ia-registration-request+xml"))
        setattr(cls, "vnd.dvb.notif-ia-registration-response+xml",
            PermissibleValue(text="vnd.dvb.notif-ia-registration-response+xml"))
        setattr(cls, "vnd.dvb.notif-init+xml",
            PermissibleValue(text="vnd.dvb.notif-init+xml"))
        setattr(cls, "vnd.dvb.pfr",
            PermissibleValue(text="vnd.dvb.pfr"))
        setattr(cls, "vnd.dvb.service",
            PermissibleValue(text="vnd.dvb.service"))
        setattr(cls, "vnd.dxr",
            PermissibleValue(text="vnd.dxr"))
        setattr(cls, "vnd.dynageo",
            PermissibleValue(text="vnd.dynageo"))
        setattr(cls, "vnd.dzr",
            PermissibleValue(text="vnd.dzr"))
        setattr(cls, "vnd.easykaraoke.cdgdownload",
            PermissibleValue(text="vnd.easykaraoke.cdgdownload"))
        setattr(cls, "vnd.ecip.rlp",
            PermissibleValue(text="vnd.ecip.rlp"))
        setattr(cls, "vnd.ecdis-update",
            PermissibleValue(text="vnd.ecdis-update"))
        setattr(cls, "vnd.eclipse.ditto+json",
            PermissibleValue(text="vnd.eclipse.ditto+json"))
        setattr(cls, "vnd.ecowin.chart",
            PermissibleValue(text="vnd.ecowin.chart"))
        setattr(cls, "vnd.ecowin.filerequest",
            PermissibleValue(text="vnd.ecowin.filerequest"))
        setattr(cls, "vnd.ecowin.fileupdate",
            PermissibleValue(text="vnd.ecowin.fileupdate"))
        setattr(cls, "vnd.ecowin.series",
            PermissibleValue(text="vnd.ecowin.series"))
        setattr(cls, "vnd.ecowin.seriesrequest",
            PermissibleValue(text="vnd.ecowin.seriesrequest"))
        setattr(cls, "vnd.ecowin.seriesupdate",
            PermissibleValue(text="vnd.ecowin.seriesupdate"))
        setattr(cls, "vnd.efi.img",
            PermissibleValue(text="vnd.efi.img"))
        setattr(cls, "vnd.efi.iso",
            PermissibleValue(text="vnd.efi.iso"))
        setattr(cls, "vnd.eln+zip",
            PermissibleValue(text="vnd.eln+zip"))
        setattr(cls, "vnd.emclient.accessrequest+xml",
            PermissibleValue(text="vnd.emclient.accessrequest+xml"))
        setattr(cls, "vnd.enliven",
            PermissibleValue(text="vnd.enliven"))
        setattr(cls, "vnd.enphase.envoy",
            PermissibleValue(text="vnd.enphase.envoy"))
        setattr(cls, "vnd.eprints.data+xml",
            PermissibleValue(text="vnd.eprints.data+xml"))
        setattr(cls, "vnd.epson.esf",
            PermissibleValue(text="vnd.epson.esf"))
        setattr(cls, "vnd.epson.msf",
            PermissibleValue(text="vnd.epson.msf"))
        setattr(cls, "vnd.epson.quickanime",
            PermissibleValue(text="vnd.epson.quickanime"))
        setattr(cls, "vnd.epson.salt",
            PermissibleValue(text="vnd.epson.salt"))
        setattr(cls, "vnd.epson.ssf",
            PermissibleValue(text="vnd.epson.ssf"))
        setattr(cls, "vnd.ericsson.quickcall",
            PermissibleValue(text="vnd.ericsson.quickcall"))
        setattr(cls, "vnd.espass-espass+zip",
            PermissibleValue(text="vnd.espass-espass+zip"))
        setattr(cls, "vnd.eszigno3+xml",
            PermissibleValue(text="vnd.eszigno3+xml"))
        setattr(cls, "vnd.etsi.aoc+xml",
            PermissibleValue(text="vnd.etsi.aoc+xml"))
        setattr(cls, "vnd.etsi.asic-s+zip",
            PermissibleValue(text="vnd.etsi.asic-s+zip"))
        setattr(cls, "vnd.etsi.asic-e+zip",
            PermissibleValue(text="vnd.etsi.asic-e+zip"))
        setattr(cls, "vnd.etsi.cug+xml",
            PermissibleValue(text="vnd.etsi.cug+xml"))
        setattr(cls, "vnd.etsi.iptvcommand+xml",
            PermissibleValue(text="vnd.etsi.iptvcommand+xml"))
        setattr(cls, "vnd.etsi.iptvdiscovery+xml",
            PermissibleValue(text="vnd.etsi.iptvdiscovery+xml"))
        setattr(cls, "vnd.etsi.iptvprofile+xml",
            PermissibleValue(text="vnd.etsi.iptvprofile+xml"))
        setattr(cls, "vnd.etsi.iptvsad-bc+xml",
            PermissibleValue(text="vnd.etsi.iptvsad-bc+xml"))
        setattr(cls, "vnd.etsi.iptvsad-cod+xml",
            PermissibleValue(text="vnd.etsi.iptvsad-cod+xml"))
        setattr(cls, "vnd.etsi.iptvsad-npvr+xml",
            PermissibleValue(text="vnd.etsi.iptvsad-npvr+xml"))
        setattr(cls, "vnd.etsi.iptvservice+xml",
            PermissibleValue(text="vnd.etsi.iptvservice+xml"))
        setattr(cls, "vnd.etsi.iptvsync+xml",
            PermissibleValue(text="vnd.etsi.iptvsync+xml"))
        setattr(cls, "vnd.etsi.iptvueprofile+xml",
            PermissibleValue(text="vnd.etsi.iptvueprofile+xml"))
        setattr(cls, "vnd.etsi.mcid+xml",
            PermissibleValue(text="vnd.etsi.mcid+xml"))
        setattr(cls, "vnd.etsi.mheg5",
            PermissibleValue(text="vnd.etsi.mheg5"))
        setattr(cls, "vnd.etsi.overload-control-policy-dataset+xml",
            PermissibleValue(text="vnd.etsi.overload-control-policy-dataset+xml"))
        setattr(cls, "vnd.etsi.pstn+xml",
            PermissibleValue(text="vnd.etsi.pstn+xml"))
        setattr(cls, "vnd.etsi.sci+xml",
            PermissibleValue(text="vnd.etsi.sci+xml"))
        setattr(cls, "vnd.etsi.simservs+xml",
            PermissibleValue(text="vnd.etsi.simservs+xml"))
        setattr(cls, "vnd.etsi.timestamp-token",
            PermissibleValue(text="vnd.etsi.timestamp-token"))
        setattr(cls, "vnd.etsi.tsl+xml",
            PermissibleValue(text="vnd.etsi.tsl+xml"))
        setattr(cls, "vnd.etsi.tsl.der",
            PermissibleValue(text="vnd.etsi.tsl.der"))
        setattr(cls, "vnd.eu.kasparian.car+json",
            PermissibleValue(text="vnd.eu.kasparian.car+json"))
        setattr(cls, "vnd.eudora.data",
            PermissibleValue(text="vnd.eudora.data"))
        setattr(cls, "vnd.evolv.ecig.profile",
            PermissibleValue(text="vnd.evolv.ecig.profile"))
        setattr(cls, "vnd.evolv.ecig.settings",
            PermissibleValue(text="vnd.evolv.ecig.settings"))
        setattr(cls, "vnd.evolv.ecig.theme",
            PermissibleValue(text="vnd.evolv.ecig.theme"))
        setattr(cls, "vnd.exstream-empower+zip",
            PermissibleValue(text="vnd.exstream-empower+zip"))
        setattr(cls, "vnd.exstream-package",
            PermissibleValue(text="vnd.exstream-package"))
        setattr(cls, "vnd.ezpix-album",
            PermissibleValue(text="vnd.ezpix-album"))
        setattr(cls, "vnd.ezpix-package",
            PermissibleValue(text="vnd.ezpix-package"))
        setattr(cls, "vnd.f-secure.mobile",
            PermissibleValue(text="vnd.f-secure.mobile"))
        setattr(cls, "vnd.fastcopy-disk-image",
            PermissibleValue(text="vnd.fastcopy-disk-image"))
        setattr(cls, "vnd.familysearch.gedcom+zip",
            PermissibleValue(text="vnd.familysearch.gedcom+zip"))
        setattr(cls, "vnd.fdsn.mseed",
            PermissibleValue(text="vnd.fdsn.mseed"))
        setattr(cls, "vnd.fdsn.seed",
            PermissibleValue(text="vnd.fdsn.seed"))
        setattr(cls, "vnd.ffsns",
            PermissibleValue(text="vnd.ffsns"))
        setattr(cls, "vnd.ficlab.flb+zip",
            PermissibleValue(text="vnd.ficlab.flb+zip"))
        setattr(cls, "vnd.filmit.zfc",
            PermissibleValue(text="vnd.filmit.zfc"))
        setattr(cls, "vnd.fints",
            PermissibleValue(text="vnd.fints"))
        setattr(cls, "vnd.firemonkeys.cloudcell",
            PermissibleValue(text="vnd.firemonkeys.cloudcell"))
        setattr(cls, "vnd.FloGraphIt",
            PermissibleValue(text="vnd.FloGraphIt"))
        setattr(cls, "vnd.fluxtime.clip",
            PermissibleValue(text="vnd.fluxtime.clip"))
        setattr(cls, "vnd.font-fontforge-sfd",
            PermissibleValue(text="vnd.font-fontforge-sfd"))
        setattr(cls, "vnd.framemaker",
            PermissibleValue(text="vnd.framemaker"))
        setattr(cls, "vnd.freelog.comic",
            PermissibleValue(text="vnd.freelog.comic"))
        setattr(cls, "vnd.frogans.fnc (OBSOLETE)",
            PermissibleValue(text="vnd.frogans.fnc (OBSOLETE)"))
        setattr(cls, "vnd.frogans.ltf (OBSOLETE)",
            PermissibleValue(text="vnd.frogans.ltf (OBSOLETE)"))
        setattr(cls, "vnd.fsc.weblaunch",
            PermissibleValue(text="vnd.fsc.weblaunch"))
        setattr(cls, "vnd.fujifilm.fb.docuworks",
            PermissibleValue(text="vnd.fujifilm.fb.docuworks"))
        setattr(cls, "vnd.fujifilm.fb.docuworks.binder",
            PermissibleValue(text="vnd.fujifilm.fb.docuworks.binder"))
        setattr(cls, "vnd.fujifilm.fb.docuworks.container",
            PermissibleValue(text="vnd.fujifilm.fb.docuworks.container"))
        setattr(cls, "vnd.fujifilm.fb.jfi+xml",
            PermissibleValue(text="vnd.fujifilm.fb.jfi+xml"))
        setattr(cls, "vnd.fujitsu.oasys",
            PermissibleValue(text="vnd.fujitsu.oasys"))
        setattr(cls, "vnd.fujitsu.oasys2",
            PermissibleValue(text="vnd.fujitsu.oasys2"))
        setattr(cls, "vnd.fujitsu.oasys3",
            PermissibleValue(text="vnd.fujitsu.oasys3"))
        setattr(cls, "vnd.fujitsu.oasysgp",
            PermissibleValue(text="vnd.fujitsu.oasysgp"))
        setattr(cls, "vnd.fujitsu.oasysprs",
            PermissibleValue(text="vnd.fujitsu.oasysprs"))
        setattr(cls, "vnd.fujixerox.ART4",
            PermissibleValue(text="vnd.fujixerox.ART4"))
        setattr(cls, "vnd.fujixerox.ART-EX",
            PermissibleValue(text="vnd.fujixerox.ART-EX"))
        setattr(cls, "vnd.fujixerox.ddd",
            PermissibleValue(text="vnd.fujixerox.ddd"))
        setattr(cls, "vnd.fujixerox.docuworks",
            PermissibleValue(text="vnd.fujixerox.docuworks"))
        setattr(cls, "vnd.fujixerox.docuworks.binder",
            PermissibleValue(text="vnd.fujixerox.docuworks.binder"))
        setattr(cls, "vnd.fujixerox.docuworks.container",
            PermissibleValue(text="vnd.fujixerox.docuworks.container"))
        setattr(cls, "vnd.fujixerox.HBPL",
            PermissibleValue(text="vnd.fujixerox.HBPL"))
        setattr(cls, "vnd.fut-misnet",
            PermissibleValue(text="vnd.fut-misnet"))
        setattr(cls, "vnd.futoin+cbor",
            PermissibleValue(text="vnd.futoin+cbor"))
        setattr(cls, "vnd.futoin+json",
            PermissibleValue(text="vnd.futoin+json"))
        setattr(cls, "vnd.fuzzysheet",
            PermissibleValue(text="vnd.fuzzysheet"))
        setattr(cls, "vnd.genomatix.tuxedo",
            PermissibleValue(text="vnd.genomatix.tuxedo"))
        setattr(cls, "vnd.genozip",
            PermissibleValue(text="vnd.genozip"))
        setattr(cls, "vnd.gentics.grd+json",
            PermissibleValue(text="vnd.gentics.grd+json"))
        setattr(cls, "vnd.gentoo.catmetadata+xml",
            PermissibleValue(text="vnd.gentoo.catmetadata+xml"))
        setattr(cls, "vnd.gentoo.ebuild",
            PermissibleValue(text="vnd.gentoo.ebuild"))
        setattr(cls, "vnd.gentoo.eclass",
            PermissibleValue(text="vnd.gentoo.eclass"))
        setattr(cls, "vnd.gentoo.gpkg",
            PermissibleValue(text="vnd.gentoo.gpkg"))
        setattr(cls, "vnd.gentoo.manifest",
            PermissibleValue(text="vnd.gentoo.manifest"))
        setattr(cls, "vnd.gentoo.xpak",
            PermissibleValue(text="vnd.gentoo.xpak"))
        setattr(cls, "vnd.gentoo.pkgmetadata+xml",
            PermissibleValue(text="vnd.gentoo.pkgmetadata+xml"))
        setattr(cls, "vnd.geo+json (OBSOLETED by [RFC7946] in favor of application/geo+json)",
            PermissibleValue(text="vnd.geo+json (OBSOLETED by [RFC7946] in favor of application/geo+json)"))
        setattr(cls, "vnd.geocube+xml (OBSOLETED by request)",
            PermissibleValue(text="vnd.geocube+xml (OBSOLETED by request)"))
        setattr(cls, "vnd.geogebra.file",
            PermissibleValue(text="vnd.geogebra.file"))
        setattr(cls, "vnd.geogebra.slides",
            PermissibleValue(text="vnd.geogebra.slides"))
        setattr(cls, "vnd.geogebra.tool",
            PermissibleValue(text="vnd.geogebra.tool"))
        setattr(cls, "vnd.geometry-explorer",
            PermissibleValue(text="vnd.geometry-explorer"))
        setattr(cls, "vnd.geonext",
            PermissibleValue(text="vnd.geonext"))
        setattr(cls, "vnd.geoplan",
            PermissibleValue(text="vnd.geoplan"))
        setattr(cls, "vnd.geospace",
            PermissibleValue(text="vnd.geospace"))
        setattr(cls, "vnd.gerber",
            PermissibleValue(text="vnd.gerber"))
        setattr(cls, "vnd.globalplatform.card-content-mgt",
            PermissibleValue(text="vnd.globalplatform.card-content-mgt"))
        setattr(cls, "vnd.globalplatform.card-content-mgt-response",
            PermissibleValue(text="vnd.globalplatform.card-content-mgt-response"))
        setattr(cls, "vnd.gmx - DEPRECATED",
            PermissibleValue(text="vnd.gmx - DEPRECATED"))
        setattr(cls, "vnd.gnu.taler.exchange+json",
            PermissibleValue(text="vnd.gnu.taler.exchange+json"))
        setattr(cls, "vnd.gnu.taler.merchant+json",
            PermissibleValue(text="vnd.gnu.taler.merchant+json"))
        setattr(cls, "vnd.google-earth.kml+xml",
            PermissibleValue(text="vnd.google-earth.kml+xml"))
        setattr(cls, "vnd.google-earth.kmz",
            PermissibleValue(text="vnd.google-earth.kmz"))
        setattr(cls, "vnd.gov.sk.e-form+xml",
            PermissibleValue(text="vnd.gov.sk.e-form+xml"))
        setattr(cls, "vnd.gov.sk.e-form+zip",
            PermissibleValue(text="vnd.gov.sk.e-form+zip"))
        setattr(cls, "vnd.gov.sk.xmldatacontainer+xml",
            PermissibleValue(text="vnd.gov.sk.xmldatacontainer+xml"))
        setattr(cls, "vnd.gpxsee.map+xml",
            PermissibleValue(text="vnd.gpxsee.map+xml"))
        setattr(cls, "vnd.grafeq",
            PermissibleValue(text="vnd.grafeq"))
        setattr(cls, "vnd.gridmp",
            PermissibleValue(text="vnd.gridmp"))
        setattr(cls, "vnd.groove-account",
            PermissibleValue(text="vnd.groove-account"))
        setattr(cls, "vnd.groove-help",
            PermissibleValue(text="vnd.groove-help"))
        setattr(cls, "vnd.groove-identity-message",
            PermissibleValue(text="vnd.groove-identity-message"))
        setattr(cls, "vnd.groove-injector",
            PermissibleValue(text="vnd.groove-injector"))
        setattr(cls, "vnd.groove-tool-message",
            PermissibleValue(text="vnd.groove-tool-message"))
        setattr(cls, "vnd.groove-tool-template",
            PermissibleValue(text="vnd.groove-tool-template"))
        setattr(cls, "vnd.groove-vcard",
            PermissibleValue(text="vnd.groove-vcard"))
        setattr(cls, "vnd.hal+json",
            PermissibleValue(text="vnd.hal+json"))
        setattr(cls, "vnd.hal+xml",
            PermissibleValue(text="vnd.hal+xml"))
        setattr(cls, "vnd.HandHeld-Entertainment+xml",
            PermissibleValue(text="vnd.HandHeld-Entertainment+xml"))
        setattr(cls, "vnd.hbci",
            PermissibleValue(text="vnd.hbci"))
        setattr(cls, "vnd.hc+json",
            PermissibleValue(text="vnd.hc+json"))
        setattr(cls, "vnd.hcl-bireports",
            PermissibleValue(text="vnd.hcl-bireports"))
        setattr(cls, "vnd.hdt",
            PermissibleValue(text="vnd.hdt"))
        setattr(cls, "vnd.heroku+json",
            PermissibleValue(text="vnd.heroku+json"))
        setattr(cls, "vnd.hhe.lesson-player",
            PermissibleValue(text="vnd.hhe.lesson-player"))
        setattr(cls, "vnd.hp-HPGL",
            PermissibleValue(text="vnd.hp-HPGL"))
        setattr(cls, "vnd.hp-hpid",
            PermissibleValue(text="vnd.hp-hpid"))
        setattr(cls, "vnd.hp-hps",
            PermissibleValue(text="vnd.hp-hps"))
        setattr(cls, "vnd.hp-jlyt",
            PermissibleValue(text="vnd.hp-jlyt"))
        setattr(cls, "vnd.hp-PCL",
            PermissibleValue(text="vnd.hp-PCL"))
        setattr(cls, "vnd.hp-PCLXL",
            PermissibleValue(text="vnd.hp-PCLXL"))
        setattr(cls, "vnd.hsl",
            PermissibleValue(text="vnd.hsl"))
        setattr(cls, "vnd.httphone",
            PermissibleValue(text="vnd.httphone"))
        setattr(cls, "vnd.hydrostatix.sof-data",
            PermissibleValue(text="vnd.hydrostatix.sof-data"))
        setattr(cls, "vnd.hyper-item+json",
            PermissibleValue(text="vnd.hyper-item+json"))
        setattr(cls, "vnd.hyper+json",
            PermissibleValue(text="vnd.hyper+json"))
        setattr(cls, "vnd.hyperdrive+json",
            PermissibleValue(text="vnd.hyperdrive+json"))
        setattr(cls, "vnd.hzn-3d-crossword",
            PermissibleValue(text="vnd.hzn-3d-crossword"))
        setattr(cls, "vnd.ibm.afplinedata (OBSOLETED in favor of vnd.afpc.afplinedata)",
            PermissibleValue(text="vnd.ibm.afplinedata (OBSOLETED in favor of vnd.afpc.afplinedata)"))
        setattr(cls, "vnd.ibm.electronic-media",
            PermissibleValue(text="vnd.ibm.electronic-media"))
        setattr(cls, "vnd.ibm.MiniPay",
            PermissibleValue(text="vnd.ibm.MiniPay"))
        setattr(cls, "vnd.ibm.modcap (OBSOLETED in favor of application/vnd.afpc.modca)",
            PermissibleValue(text="vnd.ibm.modcap (OBSOLETED in favor of application/vnd.afpc.modca)"))
        setattr(cls, "vnd.ibm.rights-management",
            PermissibleValue(text="vnd.ibm.rights-management"))
        setattr(cls, "vnd.ibm.secure-container",
            PermissibleValue(text="vnd.ibm.secure-container"))
        setattr(cls, "vnd.iccprofile",
            PermissibleValue(text="vnd.iccprofile"))
        setattr(cls, "vnd.ieee.1905",
            PermissibleValue(text="vnd.ieee.1905"))
        setattr(cls, "vnd.igloader",
            PermissibleValue(text="vnd.igloader"))
        setattr(cls, "vnd.imagemeter.folder+zip",
            PermissibleValue(text="vnd.imagemeter.folder+zip"))
        setattr(cls, "vnd.imagemeter.image+zip",
            PermissibleValue(text="vnd.imagemeter.image+zip"))
        setattr(cls, "vnd.immervision-ivp",
            PermissibleValue(text="vnd.immervision-ivp"))
        setattr(cls, "vnd.immervision-ivu",
            PermissibleValue(text="vnd.immervision-ivu"))
        setattr(cls, "vnd.ims.imsccv1p1",
            PermissibleValue(text="vnd.ims.imsccv1p1"))
        setattr(cls, "vnd.ims.imsccv1p2",
            PermissibleValue(text="vnd.ims.imsccv1p2"))
        setattr(cls, "vnd.ims.imsccv1p3",
            PermissibleValue(text="vnd.ims.imsccv1p3"))
        setattr(cls, "vnd.ims.lis.v2.result+json",
            PermissibleValue(text="vnd.ims.lis.v2.result+json"))
        setattr(cls, "vnd.ims.lti.v2.toolconsumerprofile+json",
            PermissibleValue(text="vnd.ims.lti.v2.toolconsumerprofile+json"))
        setattr(cls, "vnd.ims.lti.v2.toolproxy.id+json",
            PermissibleValue(text="vnd.ims.lti.v2.toolproxy.id+json"))
        setattr(cls, "vnd.ims.lti.v2.toolproxy+json",
            PermissibleValue(text="vnd.ims.lti.v2.toolproxy+json"))
        setattr(cls, "vnd.ims.lti.v2.toolsettings+json",
            PermissibleValue(text="vnd.ims.lti.v2.toolsettings+json"))
        setattr(cls, "vnd.ims.lti.v2.toolsettings.simple+json",
            PermissibleValue(text="vnd.ims.lti.v2.toolsettings.simple+json"))
        setattr(cls, "vnd.informedcontrol.rms+xml",
            PermissibleValue(text="vnd.informedcontrol.rms+xml"))
        setattr(cls, "vnd.infotech.project",
            PermissibleValue(text="vnd.infotech.project"))
        setattr(cls, "vnd.infotech.project+xml",
            PermissibleValue(text="vnd.infotech.project+xml"))
        setattr(cls, "vnd.informix-visionary (OBSOLETED in favor of application/vnd.visionary)",
            PermissibleValue(text="vnd.informix-visionary (OBSOLETED in favor of application/vnd.visionary)"))
        setattr(cls, "vnd.innopath.wamp.notification",
            PermissibleValue(text="vnd.innopath.wamp.notification"))
        setattr(cls, "vnd.insors.igm",
            PermissibleValue(text="vnd.insors.igm"))
        setattr(cls, "vnd.intercon.formnet",
            PermissibleValue(text="vnd.intercon.formnet"))
        setattr(cls, "vnd.intergeo",
            PermissibleValue(text="vnd.intergeo"))
        setattr(cls, "vnd.intertrust.digibox",
            PermissibleValue(text="vnd.intertrust.digibox"))
        setattr(cls, "vnd.intertrust.nncp",
            PermissibleValue(text="vnd.intertrust.nncp"))
        setattr(cls, "vnd.intu.qbo",
            PermissibleValue(text="vnd.intu.qbo"))
        setattr(cls, "vnd.intu.qfx",
            PermissibleValue(text="vnd.intu.qfx"))
        setattr(cls, "vnd.ipfs.ipns-record",
            PermissibleValue(text="vnd.ipfs.ipns-record"))
        setattr(cls, "vnd.ipld.car",
            PermissibleValue(text="vnd.ipld.car"))
        setattr(cls, "vnd.ipld.dag-cbor",
            PermissibleValue(text="vnd.ipld.dag-cbor"))
        setattr(cls, "vnd.ipld.dag-json",
            PermissibleValue(text="vnd.ipld.dag-json"))
        setattr(cls, "vnd.ipld.raw",
            PermissibleValue(text="vnd.ipld.raw"))
        setattr(cls, "vnd.iptc.g2.catalogitem+xml",
            PermissibleValue(text="vnd.iptc.g2.catalogitem+xml"))
        setattr(cls, "vnd.iptc.g2.conceptitem+xml",
            PermissibleValue(text="vnd.iptc.g2.conceptitem+xml"))
        setattr(cls, "vnd.iptc.g2.knowledgeitem+xml",
            PermissibleValue(text="vnd.iptc.g2.knowledgeitem+xml"))
        setattr(cls, "vnd.iptc.g2.newsitem+xml",
            PermissibleValue(text="vnd.iptc.g2.newsitem+xml"))
        setattr(cls, "vnd.iptc.g2.newsmessage+xml",
            PermissibleValue(text="vnd.iptc.g2.newsmessage+xml"))
        setattr(cls, "vnd.iptc.g2.packageitem+xml",
            PermissibleValue(text="vnd.iptc.g2.packageitem+xml"))
        setattr(cls, "vnd.iptc.g2.planningitem+xml",
            PermissibleValue(text="vnd.iptc.g2.planningitem+xml"))
        setattr(cls, "vnd.ipunplugged.rcprofile",
            PermissibleValue(text="vnd.ipunplugged.rcprofile"))
        setattr(cls, "vnd.irepository.package+xml",
            PermissibleValue(text="vnd.irepository.package+xml"))
        setattr(cls, "vnd.is-xpr",
            PermissibleValue(text="vnd.is-xpr"))
        setattr(cls, "vnd.isac.fcs",
            PermissibleValue(text="vnd.isac.fcs"))
        setattr(cls, "vnd.jam",
            PermissibleValue(text="vnd.jam"))
        setattr(cls, "vnd.iso11783-10+zip",
            PermissibleValue(text="vnd.iso11783-10+zip"))
        setattr(cls, "vnd.japannet-directory-service",
            PermissibleValue(text="vnd.japannet-directory-service"))
        setattr(cls, "vnd.japannet-jpnstore-wakeup",
            PermissibleValue(text="vnd.japannet-jpnstore-wakeup"))
        setattr(cls, "vnd.japannet-payment-wakeup",
            PermissibleValue(text="vnd.japannet-payment-wakeup"))
        setattr(cls, "vnd.japannet-registration",
            PermissibleValue(text="vnd.japannet-registration"))
        setattr(cls, "vnd.japannet-registration-wakeup",
            PermissibleValue(text="vnd.japannet-registration-wakeup"))
        setattr(cls, "vnd.japannet-setstore-wakeup",
            PermissibleValue(text="vnd.japannet-setstore-wakeup"))
        setattr(cls, "vnd.japannet-verification",
            PermissibleValue(text="vnd.japannet-verification"))
        setattr(cls, "vnd.japannet-verification-wakeup",
            PermissibleValue(text="vnd.japannet-verification-wakeup"))
        setattr(cls, "vnd.jcp.javame.midlet-rms",
            PermissibleValue(text="vnd.jcp.javame.midlet-rms"))
        setattr(cls, "vnd.jisp",
            PermissibleValue(text="vnd.jisp"))
        setattr(cls, "vnd.joost.joda-archive",
            PermissibleValue(text="vnd.joost.joda-archive"))
        setattr(cls, "vnd.jsk.isdn-ngn",
            PermissibleValue(text="vnd.jsk.isdn-ngn"))
        setattr(cls, "vnd.kahootz",
            PermissibleValue(text="vnd.kahootz"))
        setattr(cls, "vnd.kde.karbon",
            PermissibleValue(text="vnd.kde.karbon"))
        setattr(cls, "vnd.kde.kchart",
            PermissibleValue(text="vnd.kde.kchart"))
        setattr(cls, "vnd.kde.kformula",
            PermissibleValue(text="vnd.kde.kformula"))
        setattr(cls, "vnd.kde.kivio",
            PermissibleValue(text="vnd.kde.kivio"))
        setattr(cls, "vnd.kde.kontour",
            PermissibleValue(text="vnd.kde.kontour"))
        setattr(cls, "vnd.kde.kpresenter",
            PermissibleValue(text="vnd.kde.kpresenter"))
        setattr(cls, "vnd.kde.kspread",
            PermissibleValue(text="vnd.kde.kspread"))
        setattr(cls, "vnd.kde.kword",
            PermissibleValue(text="vnd.kde.kword"))
        setattr(cls, "vnd.kenameaapp",
            PermissibleValue(text="vnd.kenameaapp"))
        setattr(cls, "vnd.kidspiration",
            PermissibleValue(text="vnd.kidspiration"))
        setattr(cls, "vnd.Kinar",
            PermissibleValue(text="vnd.Kinar"))
        setattr(cls, "vnd.koan",
            PermissibleValue(text="vnd.koan"))
        setattr(cls, "vnd.kodak-descriptor",
            PermissibleValue(text="vnd.kodak-descriptor"))
        setattr(cls, "vnd.las",
            PermissibleValue(text="vnd.las"))
        setattr(cls, "vnd.las.las+json",
            PermissibleValue(text="vnd.las.las+json"))
        setattr(cls, "vnd.las.las+xml",
            PermissibleValue(text="vnd.las.las+xml"))
        setattr(cls, "vnd.laszip",
            PermissibleValue(text="vnd.laszip"))
        setattr(cls, "vnd.leap+json",
            PermissibleValue(text="vnd.leap+json"))
        setattr(cls, "vnd.liberty-request+xml",
            PermissibleValue(text="vnd.liberty-request+xml"))
        setattr(cls, "vnd.llamagraphics.life-balance.desktop",
            PermissibleValue(text="vnd.llamagraphics.life-balance.desktop"))
        setattr(cls, "vnd.llamagraphics.life-balance.exchange+xml",
            PermissibleValue(text="vnd.llamagraphics.life-balance.exchange+xml"))
        setattr(cls, "vnd.logipipe.circuit+zip",
            PermissibleValue(text="vnd.logipipe.circuit+zip"))
        setattr(cls, "vnd.loom",
            PermissibleValue(text="vnd.loom"))
        setattr(cls, "vnd.lotus-1-2-3",
            PermissibleValue(text="vnd.lotus-1-2-3"))
        setattr(cls, "vnd.lotus-approach",
            PermissibleValue(text="vnd.lotus-approach"))
        setattr(cls, "vnd.lotus-freelance",
            PermissibleValue(text="vnd.lotus-freelance"))
        setattr(cls, "vnd.lotus-notes",
            PermissibleValue(text="vnd.lotus-notes"))
        setattr(cls, "vnd.lotus-organizer",
            PermissibleValue(text="vnd.lotus-organizer"))
        setattr(cls, "vnd.lotus-screencam",
            PermissibleValue(text="vnd.lotus-screencam"))
        setattr(cls, "vnd.lotus-wordpro",
            PermissibleValue(text="vnd.lotus-wordpro"))
        setattr(cls, "vnd.macports.portpkg",
            PermissibleValue(text="vnd.macports.portpkg"))
        setattr(cls, "vnd.mapbox-vector-tile",
            PermissibleValue(text="vnd.mapbox-vector-tile"))
        setattr(cls, "vnd.marlin.drm.actiontoken+xml",
            PermissibleValue(text="vnd.marlin.drm.actiontoken+xml"))
        setattr(cls, "vnd.marlin.drm.conftoken+xml",
            PermissibleValue(text="vnd.marlin.drm.conftoken+xml"))
        setattr(cls, "vnd.marlin.drm.license+xml",
            PermissibleValue(text="vnd.marlin.drm.license+xml"))
        setattr(cls, "vnd.marlin.drm.mdcf",
            PermissibleValue(text="vnd.marlin.drm.mdcf"))
        setattr(cls, "vnd.mason+json",
            PermissibleValue(text="vnd.mason+json"))
        setattr(cls, "vnd.maxar.archive.3tz+zip",
            PermissibleValue(text="vnd.maxar.archive.3tz+zip"))
        setattr(cls, "vnd.maxmind.maxmind-db",
            PermissibleValue(text="vnd.maxmind.maxmind-db"))
        setattr(cls, "vnd.mcd",
            PermissibleValue(text="vnd.mcd"))
        setattr(cls, "vnd.mdl",
            PermissibleValue(text="vnd.mdl"))
        setattr(cls, "vnd.mdl-mbsdf",
            PermissibleValue(text="vnd.mdl-mbsdf"))
        setattr(cls, "vnd.medcalcdata",
            PermissibleValue(text="vnd.medcalcdata"))
        setattr(cls, "vnd.mediastation.cdkey",
            PermissibleValue(text="vnd.mediastation.cdkey"))
        setattr(cls, "vnd.medicalholodeck.recordxr",
            PermissibleValue(text="vnd.medicalholodeck.recordxr"))
        setattr(cls, "vnd.meridian-slingshot",
            PermissibleValue(text="vnd.meridian-slingshot"))
        setattr(cls, "vnd.mermaid",
            PermissibleValue(text="vnd.mermaid"))
        setattr(cls, "vnd.MFER",
            PermissibleValue(text="vnd.MFER"))
        setattr(cls, "vnd.mfmp",
            PermissibleValue(text="vnd.mfmp"))
        setattr(cls, "vnd.micro+json",
            PermissibleValue(text="vnd.micro+json"))
        setattr(cls, "vnd.micrografx.flo",
            PermissibleValue(text="vnd.micrografx.flo"))
        setattr(cls, "vnd.micrografx.igx",
            PermissibleValue(text="vnd.micrografx.igx"))
        setattr(cls, "vnd.microsoft.portable-executable",
            PermissibleValue(text="vnd.microsoft.portable-executable"))
        setattr(cls, "vnd.microsoft.windows.thumbnail-cache",
            PermissibleValue(text="vnd.microsoft.windows.thumbnail-cache"))
        setattr(cls, "vnd.miele+json",
            PermissibleValue(text="vnd.miele+json"))
        setattr(cls, "vnd.mif",
            PermissibleValue(text="vnd.mif"))
        setattr(cls, "vnd.minisoft-hp3000-save",
            PermissibleValue(text="vnd.minisoft-hp3000-save"))
        setattr(cls, "vnd.mitsubishi.misty-guard.trustweb",
            PermissibleValue(text="vnd.mitsubishi.misty-guard.trustweb"))
        setattr(cls, "vnd.Mobius.DAF",
            PermissibleValue(text="vnd.Mobius.DAF"))
        setattr(cls, "vnd.Mobius.DIS",
            PermissibleValue(text="vnd.Mobius.DIS"))
        setattr(cls, "vnd.Mobius.MBK",
            PermissibleValue(text="vnd.Mobius.MBK"))
        setattr(cls, "vnd.Mobius.MQY",
            PermissibleValue(text="vnd.Mobius.MQY"))
        setattr(cls, "vnd.Mobius.MSL",
            PermissibleValue(text="vnd.Mobius.MSL"))
        setattr(cls, "vnd.Mobius.PLC",
            PermissibleValue(text="vnd.Mobius.PLC"))
        setattr(cls, "vnd.Mobius.TXF",
            PermissibleValue(text="vnd.Mobius.TXF"))
        setattr(cls, "vnd.modl",
            PermissibleValue(text="vnd.modl"))
        setattr(cls, "vnd.mophun.application",
            PermissibleValue(text="vnd.mophun.application"))
        setattr(cls, "vnd.mophun.certificate",
            PermissibleValue(text="vnd.mophun.certificate"))
        setattr(cls, "vnd.motorola.flexsuite",
            PermissibleValue(text="vnd.motorola.flexsuite"))
        setattr(cls, "vnd.motorola.flexsuite.adsi",
            PermissibleValue(text="vnd.motorola.flexsuite.adsi"))
        setattr(cls, "vnd.motorola.flexsuite.fis",
            PermissibleValue(text="vnd.motorola.flexsuite.fis"))
        setattr(cls, "vnd.motorola.flexsuite.gotap",
            PermissibleValue(text="vnd.motorola.flexsuite.gotap"))
        setattr(cls, "vnd.motorola.flexsuite.kmr",
            PermissibleValue(text="vnd.motorola.flexsuite.kmr"))
        setattr(cls, "vnd.motorola.flexsuite.ttc",
            PermissibleValue(text="vnd.motorola.flexsuite.ttc"))
        setattr(cls, "vnd.motorola.flexsuite.wem",
            PermissibleValue(text="vnd.motorola.flexsuite.wem"))
        setattr(cls, "vnd.motorola.iprm",
            PermissibleValue(text="vnd.motorola.iprm"))
        setattr(cls, "vnd.mozilla.xul+xml",
            PermissibleValue(text="vnd.mozilla.xul+xml"))
        setattr(cls, "vnd.ms-artgalry",
            PermissibleValue(text="vnd.ms-artgalry"))
        setattr(cls, "vnd.ms-asf",
            PermissibleValue(text="vnd.ms-asf"))
        setattr(cls, "vnd.ms-cab-compressed",
            PermissibleValue(text="vnd.ms-cab-compressed"))
        setattr(cls, "vnd.ms-3mfdocument",
            PermissibleValue(text="vnd.ms-3mfdocument"))
        setattr(cls, "vnd.ms-excel",
            PermissibleValue(text="vnd.ms-excel"))
        setattr(cls, "vnd.ms-excel.addin.macroEnabled.12",
            PermissibleValue(text="vnd.ms-excel.addin.macroEnabled.12"))
        setattr(cls, "vnd.ms-excel.sheet.binary.macroEnabled.12",
            PermissibleValue(text="vnd.ms-excel.sheet.binary.macroEnabled.12"))
        setattr(cls, "vnd.ms-excel.sheet.macroEnabled.12",
            PermissibleValue(text="vnd.ms-excel.sheet.macroEnabled.12"))
        setattr(cls, "vnd.ms-excel.template.macroEnabled.12",
            PermissibleValue(text="vnd.ms-excel.template.macroEnabled.12"))
        setattr(cls, "vnd.ms-fontobject",
            PermissibleValue(text="vnd.ms-fontobject"))
        setattr(cls, "vnd.ms-htmlhelp",
            PermissibleValue(text="vnd.ms-htmlhelp"))
        setattr(cls, "vnd.ms-ims",
            PermissibleValue(text="vnd.ms-ims"))
        setattr(cls, "vnd.ms-lrm",
            PermissibleValue(text="vnd.ms-lrm"))
        setattr(cls, "vnd.ms-office.activeX+xml",
            PermissibleValue(text="vnd.ms-office.activeX+xml"))
        setattr(cls, "vnd.ms-officetheme",
            PermissibleValue(text="vnd.ms-officetheme"))
        setattr(cls, "vnd.ms-playready.initiator+xml",
            PermissibleValue(text="vnd.ms-playready.initiator+xml"))
        setattr(cls, "vnd.ms-powerpoint",
            PermissibleValue(text="vnd.ms-powerpoint"))
        setattr(cls, "vnd.ms-powerpoint.addin.macroEnabled.12",
            PermissibleValue(text="vnd.ms-powerpoint.addin.macroEnabled.12"))
        setattr(cls, "vnd.ms-powerpoint.presentation.macroEnabled.12",
            PermissibleValue(text="vnd.ms-powerpoint.presentation.macroEnabled.12"))
        setattr(cls, "vnd.ms-powerpoint.slide.macroEnabled.12",
            PermissibleValue(text="vnd.ms-powerpoint.slide.macroEnabled.12"))
        setattr(cls, "vnd.ms-powerpoint.slideshow.macroEnabled.12",
            PermissibleValue(text="vnd.ms-powerpoint.slideshow.macroEnabled.12"))
        setattr(cls, "vnd.ms-powerpoint.template.macroEnabled.12",
            PermissibleValue(text="vnd.ms-powerpoint.template.macroEnabled.12"))
        setattr(cls, "vnd.ms-PrintDeviceCapabilities+xml",
            PermissibleValue(text="vnd.ms-PrintDeviceCapabilities+xml"))
        setattr(cls, "vnd.ms-PrintSchemaTicket+xml",
            PermissibleValue(text="vnd.ms-PrintSchemaTicket+xml"))
        setattr(cls, "vnd.ms-project",
            PermissibleValue(text="vnd.ms-project"))
        setattr(cls, "vnd.ms-tnef",
            PermissibleValue(text="vnd.ms-tnef"))
        setattr(cls, "vnd.ms-windows.devicepairing",
            PermissibleValue(text="vnd.ms-windows.devicepairing"))
        setattr(cls, "vnd.ms-windows.nwprinting.oob",
            PermissibleValue(text="vnd.ms-windows.nwprinting.oob"))
        setattr(cls, "vnd.ms-windows.printerpairing",
            PermissibleValue(text="vnd.ms-windows.printerpairing"))
        setattr(cls, "vnd.ms-windows.wsd.oob",
            PermissibleValue(text="vnd.ms-windows.wsd.oob"))
        setattr(cls, "vnd.ms-wmdrm.lic-chlg-req",
            PermissibleValue(text="vnd.ms-wmdrm.lic-chlg-req"))
        setattr(cls, "vnd.ms-wmdrm.lic-resp",
            PermissibleValue(text="vnd.ms-wmdrm.lic-resp"))
        setattr(cls, "vnd.ms-wmdrm.meter-chlg-req",
            PermissibleValue(text="vnd.ms-wmdrm.meter-chlg-req"))
        setattr(cls, "vnd.ms-wmdrm.meter-resp",
            PermissibleValue(text="vnd.ms-wmdrm.meter-resp"))
        setattr(cls, "vnd.ms-word.document.macroEnabled.12",
            PermissibleValue(text="vnd.ms-word.document.macroEnabled.12"))
        setattr(cls, "vnd.ms-word.template.macroEnabled.12",
            PermissibleValue(text="vnd.ms-word.template.macroEnabled.12"))
        setattr(cls, "vnd.ms-works",
            PermissibleValue(text="vnd.ms-works"))
        setattr(cls, "vnd.ms-wpl",
            PermissibleValue(text="vnd.ms-wpl"))
        setattr(cls, "vnd.ms-xpsdocument",
            PermissibleValue(text="vnd.ms-xpsdocument"))
        setattr(cls, "vnd.msa-disk-image",
            PermissibleValue(text="vnd.msa-disk-image"))
        setattr(cls, "vnd.mseq",
            PermissibleValue(text="vnd.mseq"))
        setattr(cls, "vnd.msign",
            PermissibleValue(text="vnd.msign"))
        setattr(cls, "vnd.multiad.creator",
            PermissibleValue(text="vnd.multiad.creator"))
        setattr(cls, "vnd.multiad.creator.cif",
            PermissibleValue(text="vnd.multiad.creator.cif"))
        setattr(cls, "vnd.musician",
            PermissibleValue(text="vnd.musician"))
        setattr(cls, "vnd.music-niff",
            PermissibleValue(text="vnd.music-niff"))
        setattr(cls, "vnd.muvee.style",
            PermissibleValue(text="vnd.muvee.style"))
        setattr(cls, "vnd.mynfc",
            PermissibleValue(text="vnd.mynfc"))
        setattr(cls, "vnd.nacamar.ybrid+json",
            PermissibleValue(text="vnd.nacamar.ybrid+json"))
        setattr(cls, "vnd.ncd.control",
            PermissibleValue(text="vnd.ncd.control"))
        setattr(cls, "vnd.ncd.reference",
            PermissibleValue(text="vnd.ncd.reference"))
        setattr(cls, "vnd.nearst.inv+json",
            PermissibleValue(text="vnd.nearst.inv+json"))
        setattr(cls, "vnd.nebumind.line",
            PermissibleValue(text="vnd.nebumind.line"))
        setattr(cls, "vnd.nervana",
            PermissibleValue(text="vnd.nervana"))
        setattr(cls, "vnd.netfpx",
            PermissibleValue(text="vnd.netfpx"))
        setattr(cls, "vnd.neurolanguage.nlu",
            PermissibleValue(text="vnd.neurolanguage.nlu"))
        setattr(cls, "vnd.nimn",
            PermissibleValue(text="vnd.nimn"))
        setattr(cls, "vnd.nintendo.snes.rom",
            PermissibleValue(text="vnd.nintendo.snes.rom"))
        setattr(cls, "vnd.nintendo.nitro.rom",
            PermissibleValue(text="vnd.nintendo.nitro.rom"))
        setattr(cls, "vnd.nitf",
            PermissibleValue(text="vnd.nitf"))
        setattr(cls, "vnd.noblenet-directory",
            PermissibleValue(text="vnd.noblenet-directory"))
        setattr(cls, "vnd.noblenet-sealer",
            PermissibleValue(text="vnd.noblenet-sealer"))
        setattr(cls, "vnd.noblenet-web",
            PermissibleValue(text="vnd.noblenet-web"))
        setattr(cls, "vnd.nokia.catalogs",
            PermissibleValue(text="vnd.nokia.catalogs"))
        setattr(cls, "vnd.nokia.conml+wbxml",
            PermissibleValue(text="vnd.nokia.conml+wbxml"))
        setattr(cls, "vnd.nokia.conml+xml",
            PermissibleValue(text="vnd.nokia.conml+xml"))
        setattr(cls, "vnd.nokia.iptv.config+xml",
            PermissibleValue(text="vnd.nokia.iptv.config+xml"))
        setattr(cls, "vnd.nokia.iSDS-radio-presets",
            PermissibleValue(text="vnd.nokia.iSDS-radio-presets"))
        setattr(cls, "vnd.nokia.landmark+wbxml",
            PermissibleValue(text="vnd.nokia.landmark+wbxml"))
        setattr(cls, "vnd.nokia.landmark+xml",
            PermissibleValue(text="vnd.nokia.landmark+xml"))
        setattr(cls, "vnd.nokia.landmarkcollection+xml",
            PermissibleValue(text="vnd.nokia.landmarkcollection+xml"))
        setattr(cls, "vnd.nokia.ncd",
            PermissibleValue(text="vnd.nokia.ncd"))
        setattr(cls, "vnd.nokia.n-gage.ac+xml",
            PermissibleValue(text="vnd.nokia.n-gage.ac+xml"))
        setattr(cls, "vnd.nokia.n-gage.data",
            PermissibleValue(text="vnd.nokia.n-gage.data"))
        setattr(cls, "vnd.nokia.n-gage.symbian.install (OBSOLETE",
            PermissibleValue(text="vnd.nokia.n-gage.symbian.install (OBSOLETE"))
        setattr(cls, "vnd.nokia.pcd+wbxml",
            PermissibleValue(text="vnd.nokia.pcd+wbxml"))
        setattr(cls, "vnd.nokia.pcd+xml",
            PermissibleValue(text="vnd.nokia.pcd+xml"))
        setattr(cls, "vnd.nokia.radio-preset",
            PermissibleValue(text="vnd.nokia.radio-preset"))
        setattr(cls, "vnd.nokia.radio-presets",
            PermissibleValue(text="vnd.nokia.radio-presets"))
        setattr(cls, "vnd.novadigm.EDM",
            PermissibleValue(text="vnd.novadigm.EDM"))
        setattr(cls, "vnd.novadigm.EDX",
            PermissibleValue(text="vnd.novadigm.EDX"))
        setattr(cls, "vnd.novadigm.EXT",
            PermissibleValue(text="vnd.novadigm.EXT"))
        setattr(cls, "vnd.ntt-local.content-share",
            PermissibleValue(text="vnd.ntt-local.content-share"))
        setattr(cls, "vnd.ntt-local.file-transfer",
            PermissibleValue(text="vnd.ntt-local.file-transfer"))
        setattr(cls, "vnd.ntt-local.ogw_remote-access",
            PermissibleValue(text="vnd.ntt-local.ogw_remote-access"))
        setattr(cls, "vnd.ntt-local.sip-ta_remote",
            PermissibleValue(text="vnd.ntt-local.sip-ta_remote"))
        setattr(cls, "vnd.ntt-local.sip-ta_tcp_stream",
            PermissibleValue(text="vnd.ntt-local.sip-ta_tcp_stream"))
        setattr(cls, "vnd.oasis.opendocument.base",
            PermissibleValue(text="vnd.oasis.opendocument.base"))
        setattr(cls, "vnd.oasis.opendocument.chart",
            PermissibleValue(text="vnd.oasis.opendocument.chart"))
        setattr(cls, "vnd.oasis.opendocument.chart-template",
            PermissibleValue(text="vnd.oasis.opendocument.chart-template"))
        setattr(cls, "vnd.oasis.opendocument.database (OBSOLETED in favor of application/vnd.oasis.opendocument.base)",
            PermissibleValue(text="vnd.oasis.opendocument.database (OBSOLETED in favor of application/vnd.oasis.opendocument.base)"))
        setattr(cls, "vnd.oasis.opendocument.formula",
            PermissibleValue(text="vnd.oasis.opendocument.formula"))
        setattr(cls, "vnd.oasis.opendocument.formula-template",
            PermissibleValue(text="vnd.oasis.opendocument.formula-template"))
        setattr(cls, "vnd.oasis.opendocument.graphics",
            PermissibleValue(text="vnd.oasis.opendocument.graphics"))
        setattr(cls, "vnd.oasis.opendocument.graphics-template",
            PermissibleValue(text="vnd.oasis.opendocument.graphics-template"))
        setattr(cls, "vnd.oasis.opendocument.image",
            PermissibleValue(text="vnd.oasis.opendocument.image"))
        setattr(cls, "vnd.oasis.opendocument.image-template",
            PermissibleValue(text="vnd.oasis.opendocument.image-template"))
        setattr(cls, "vnd.oasis.opendocument.presentation",
            PermissibleValue(text="vnd.oasis.opendocument.presentation"))
        setattr(cls, "vnd.oasis.opendocument.presentation-template",
            PermissibleValue(text="vnd.oasis.opendocument.presentation-template"))
        setattr(cls, "vnd.oasis.opendocument.spreadsheet",
            PermissibleValue(text="vnd.oasis.opendocument.spreadsheet"))
        setattr(cls, "vnd.oasis.opendocument.spreadsheet-template",
            PermissibleValue(text="vnd.oasis.opendocument.spreadsheet-template"))
        setattr(cls, "vnd.oasis.opendocument.text",
            PermissibleValue(text="vnd.oasis.opendocument.text"))
        setattr(cls, "vnd.oasis.opendocument.text-master",
            PermissibleValue(text="vnd.oasis.opendocument.text-master"))
        setattr(cls, "vnd.oasis.opendocument.text-master-template",
            PermissibleValue(text="vnd.oasis.opendocument.text-master-template"))
        setattr(cls, "vnd.oasis.opendocument.text-template",
            PermissibleValue(text="vnd.oasis.opendocument.text-template"))
        setattr(cls, "vnd.oasis.opendocument.text-web",
            PermissibleValue(text="vnd.oasis.opendocument.text-web"))
        setattr(cls, "vnd.obn",
            PermissibleValue(text="vnd.obn"))
        setattr(cls, "vnd.ocf+cbor",
            PermissibleValue(text="vnd.ocf+cbor"))
        setattr(cls, "vnd.oci.image.manifest.v1+json",
            PermissibleValue(text="vnd.oci.image.manifest.v1+json"))
        setattr(cls, "vnd.oftn.l10n+json",
            PermissibleValue(text="vnd.oftn.l10n+json"))
        setattr(cls, "vnd.oipf.contentaccessdownload+xml",
            PermissibleValue(text="vnd.oipf.contentaccessdownload+xml"))
        setattr(cls, "vnd.oipf.contentaccessstreaming+xml",
            PermissibleValue(text="vnd.oipf.contentaccessstreaming+xml"))
        setattr(cls, "vnd.oipf.cspg-hexbinary",
            PermissibleValue(text="vnd.oipf.cspg-hexbinary"))
        setattr(cls, "vnd.oipf.dae.svg+xml",
            PermissibleValue(text="vnd.oipf.dae.svg+xml"))
        setattr(cls, "vnd.oipf.dae.xhtml+xml",
            PermissibleValue(text="vnd.oipf.dae.xhtml+xml"))
        setattr(cls, "vnd.oipf.mippvcontrolmessage+xml",
            PermissibleValue(text="vnd.oipf.mippvcontrolmessage+xml"))
        setattr(cls, "vnd.oipf.pae.gem",
            PermissibleValue(text="vnd.oipf.pae.gem"))
        setattr(cls, "vnd.oipf.spdiscovery+xml",
            PermissibleValue(text="vnd.oipf.spdiscovery+xml"))
        setattr(cls, "vnd.oipf.spdlist+xml",
            PermissibleValue(text="vnd.oipf.spdlist+xml"))
        setattr(cls, "vnd.oipf.ueprofile+xml",
            PermissibleValue(text="vnd.oipf.ueprofile+xml"))
        setattr(cls, "vnd.oipf.userprofile+xml",
            PermissibleValue(text="vnd.oipf.userprofile+xml"))
        setattr(cls, "vnd.olpc-sugar",
            PermissibleValue(text="vnd.olpc-sugar"))
        setattr(cls, "vnd.oma.bcast.associated-procedure-parameter+xml",
            PermissibleValue(text="vnd.oma.bcast.associated-procedure-parameter+xml"))
        setattr(cls, "vnd.oma.bcast.drm-trigger+xml",
            PermissibleValue(text="vnd.oma.bcast.drm-trigger+xml"))
        setattr(cls, "vnd.oma.bcast.imd+xml",
            PermissibleValue(text="vnd.oma.bcast.imd+xml"))
        setattr(cls, "vnd.oma.bcast.ltkm",
            PermissibleValue(text="vnd.oma.bcast.ltkm"))
        setattr(cls, "vnd.oma.bcast.notification+xml",
            PermissibleValue(text="vnd.oma.bcast.notification+xml"))
        setattr(cls, "vnd.oma.bcast.provisioningtrigger",
            PermissibleValue(text="vnd.oma.bcast.provisioningtrigger"))
        setattr(cls, "vnd.oma.bcast.sgboot",
            PermissibleValue(text="vnd.oma.bcast.sgboot"))
        setattr(cls, "vnd.oma.bcast.sgdd+xml",
            PermissibleValue(text="vnd.oma.bcast.sgdd+xml"))
        setattr(cls, "vnd.oma.bcast.sgdu",
            PermissibleValue(text="vnd.oma.bcast.sgdu"))
        setattr(cls, "vnd.oma.bcast.simple-symbol-container",
            PermissibleValue(text="vnd.oma.bcast.simple-symbol-container"))
        setattr(cls, "vnd.oma.bcast.smartcard-trigger+xml",
            PermissibleValue(text="vnd.oma.bcast.smartcard-trigger+xml"))
        setattr(cls, "vnd.oma.bcast.sprov+xml",
            PermissibleValue(text="vnd.oma.bcast.sprov+xml"))
        setattr(cls, "vnd.oma.bcast.stkm",
            PermissibleValue(text="vnd.oma.bcast.stkm"))
        setattr(cls, "vnd.oma.cab-address-book+xml",
            PermissibleValue(text="vnd.oma.cab-address-book+xml"))
        setattr(cls, "vnd.oma.cab-feature-handler+xml",
            PermissibleValue(text="vnd.oma.cab-feature-handler+xml"))
        setattr(cls, "vnd.oma.cab-pcc+xml",
            PermissibleValue(text="vnd.oma.cab-pcc+xml"))
        setattr(cls, "vnd.oma.cab-subs-invite+xml",
            PermissibleValue(text="vnd.oma.cab-subs-invite+xml"))
        setattr(cls, "vnd.oma.cab-user-prefs+xml",
            PermissibleValue(text="vnd.oma.cab-user-prefs+xml"))
        setattr(cls, "vnd.oma.dcd",
            PermissibleValue(text="vnd.oma.dcd"))
        setattr(cls, "vnd.oma.dcdc",
            PermissibleValue(text="vnd.oma.dcdc"))
        setattr(cls, "vnd.oma.dd2+xml",
            PermissibleValue(text="vnd.oma.dd2+xml"))
        setattr(cls, "vnd.oma.drm.risd+xml",
            PermissibleValue(text="vnd.oma.drm.risd+xml"))
        setattr(cls, "vnd.oma.group-usage-list+xml",
            PermissibleValue(text="vnd.oma.group-usage-list+xml"))
        setattr(cls, "vnd.oma.lwm2m+cbor",
            PermissibleValue(text="vnd.oma.lwm2m+cbor"))
        setattr(cls, "vnd.oma.lwm2m+json",
            PermissibleValue(text="vnd.oma.lwm2m+json"))
        setattr(cls, "vnd.oma.lwm2m+tlv",
            PermissibleValue(text="vnd.oma.lwm2m+tlv"))
        setattr(cls, "vnd.oma.pal+xml",
            PermissibleValue(text="vnd.oma.pal+xml"))
        setattr(cls, "vnd.oma.poc.detailed-progress-report+xml",
            PermissibleValue(text="vnd.oma.poc.detailed-progress-report+xml"))
        setattr(cls, "vnd.oma.poc.final-report+xml",
            PermissibleValue(text="vnd.oma.poc.final-report+xml"))
        setattr(cls, "vnd.oma.poc.groups+xml",
            PermissibleValue(text="vnd.oma.poc.groups+xml"))
        setattr(cls, "vnd.oma.poc.invocation-descriptor+xml",
            PermissibleValue(text="vnd.oma.poc.invocation-descriptor+xml"))
        setattr(cls, "vnd.oma.poc.optimized-progress-report+xml",
            PermissibleValue(text="vnd.oma.poc.optimized-progress-report+xml"))
        setattr(cls, "vnd.oma.push",
            PermissibleValue(text="vnd.oma.push"))
        setattr(cls, "vnd.oma.scidm.messages+xml",
            PermissibleValue(text="vnd.oma.scidm.messages+xml"))
        setattr(cls, "vnd.oma.xcap-directory+xml",
            PermissibleValue(text="vnd.oma.xcap-directory+xml"))
        setattr(cls, "vnd.omads-email+xml",
            PermissibleValue(text="vnd.omads-email+xml"))
        setattr(cls, "vnd.omads-file+xml",
            PermissibleValue(text="vnd.omads-file+xml"))
        setattr(cls, "vnd.omads-folder+xml",
            PermissibleValue(text="vnd.omads-folder+xml"))
        setattr(cls, "vnd.omaloc-supl-init",
            PermissibleValue(text="vnd.omaloc-supl-init"))
        setattr(cls, "vnd.oma-scws-config",
            PermissibleValue(text="vnd.oma-scws-config"))
        setattr(cls, "vnd.oma-scws-http-request",
            PermissibleValue(text="vnd.oma-scws-http-request"))
        setattr(cls, "vnd.oma-scws-http-response",
            PermissibleValue(text="vnd.oma-scws-http-response"))
        setattr(cls, "vnd.onepager",
            PermissibleValue(text="vnd.onepager"))
        setattr(cls, "vnd.onepagertamp",
            PermissibleValue(text="vnd.onepagertamp"))
        setattr(cls, "vnd.onepagertamx",
            PermissibleValue(text="vnd.onepagertamx"))
        setattr(cls, "vnd.onepagertat",
            PermissibleValue(text="vnd.onepagertat"))
        setattr(cls, "vnd.onepagertatp",
            PermissibleValue(text="vnd.onepagertatp"))
        setattr(cls, "vnd.onepagertatx",
            PermissibleValue(text="vnd.onepagertatx"))
        setattr(cls, "vnd.onvif.metadata",
            PermissibleValue(text="vnd.onvif.metadata"))
        setattr(cls, "vnd.openblox.game-binary",
            PermissibleValue(text="vnd.openblox.game-binary"))
        setattr(cls, "vnd.openblox.game+xml",
            PermissibleValue(text="vnd.openblox.game+xml"))
        setattr(cls, "vnd.openeye.oeb",
            PermissibleValue(text="vnd.openeye.oeb"))
        setattr(cls, "vnd.openstreetmap.data+xml",
            PermissibleValue(text="vnd.openstreetmap.data+xml"))
        setattr(cls, "vnd.opentimestamps.ots",
            PermissibleValue(text="vnd.opentimestamps.ots"))
        setattr(cls, "vnd.openxmlformats-officedocument.custom-properties+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.custom-properties+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.customXmlProperties+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.customXmlProperties+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawing+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawing+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.chart+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.chart+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.chartshapes+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.chartshapes+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.diagramColors+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.diagramColors+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.diagramData+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.diagramData+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.extended-properties+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.extended-properties+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.comments+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.comments+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.notesMaster+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.notesMaster+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.notesSlide+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.presentation",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.presentation"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.presProps+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.presProps+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slide",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slide"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slide+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slide+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slideshow",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slideshow"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.tags+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.tags+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.template",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.template"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.template.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.template.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.presentationml.viewProps+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.comments+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.comments+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.connections+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.connections+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.table+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.table+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.template",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.template"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.theme+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.theme+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.themeOverride+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.themeOverride+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.vmlDrawing",
            PermissibleValue(text="vnd.openxmlformats-officedocument.vmlDrawing"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.comments+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.document",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.document"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.template",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.template"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"))
        setattr(cls, "vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
            PermissibleValue(text="vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml"))
        setattr(cls, "vnd.openxmlformats-package.core-properties+xml",
            PermissibleValue(text="vnd.openxmlformats-package.core-properties+xml"))
        setattr(cls, "vnd.openxmlformats-package.digital-signature-xmlsignature+xml",
            PermissibleValue(text="vnd.openxmlformats-package.digital-signature-xmlsignature+xml"))
        setattr(cls, "vnd.openxmlformats-package.relationships+xml",
            PermissibleValue(text="vnd.openxmlformats-package.relationships+xml"))
        setattr(cls, "vnd.oracle.resource+json",
            PermissibleValue(text="vnd.oracle.resource+json"))
        setattr(cls, "vnd.orange.indata",
            PermissibleValue(text="vnd.orange.indata"))
        setattr(cls, "vnd.osa.netdeploy",
            PermissibleValue(text="vnd.osa.netdeploy"))
        setattr(cls, "vnd.osgeo.mapguide.package",
            PermissibleValue(text="vnd.osgeo.mapguide.package"))
        setattr(cls, "vnd.osgi.bundle",
            PermissibleValue(text="vnd.osgi.bundle"))
        setattr(cls, "vnd.osgi.dp",
            PermissibleValue(text="vnd.osgi.dp"))
        setattr(cls, "vnd.osgi.subsystem",
            PermissibleValue(text="vnd.osgi.subsystem"))
        setattr(cls, "vnd.otps.ct-kip+xml",
            PermissibleValue(text="vnd.otps.ct-kip+xml"))
        setattr(cls, "vnd.oxli.countgraph",
            PermissibleValue(text="vnd.oxli.countgraph"))
        setattr(cls, "vnd.pagerduty+json",
            PermissibleValue(text="vnd.pagerduty+json"))
        setattr(cls, "vnd.palm",
            PermissibleValue(text="vnd.palm"))
        setattr(cls, "vnd.panoply",
            PermissibleValue(text="vnd.panoply"))
        setattr(cls, "vnd.paos.xml",
            PermissibleValue(text="vnd.paos.xml"))
        setattr(cls, "vnd.patentdive",
            PermissibleValue(text="vnd.patentdive"))
        setattr(cls, "vnd.patientecommsdoc",
            PermissibleValue(text="vnd.patientecommsdoc"))
        setattr(cls, "vnd.pawaafile",
            PermissibleValue(text="vnd.pawaafile"))
        setattr(cls, "vnd.pcos",
            PermissibleValue(text="vnd.pcos"))
        setattr(cls, "vnd.pg.format",
            PermissibleValue(text="vnd.pg.format"))
        setattr(cls, "vnd.pg.osasli",
            PermissibleValue(text="vnd.pg.osasli"))
        setattr(cls, "vnd.piaccess.application-licence",
            PermissibleValue(text="vnd.piaccess.application-licence"))
        setattr(cls, "vnd.picsel",
            PermissibleValue(text="vnd.picsel"))
        setattr(cls, "vnd.pmi.widget",
            PermissibleValue(text="vnd.pmi.widget"))
        setattr(cls, "vnd.poc.group-advertisement+xml",
            PermissibleValue(text="vnd.poc.group-advertisement+xml"))
        setattr(cls, "vnd.pocketlearn",
            PermissibleValue(text="vnd.pocketlearn"))
        setattr(cls, "vnd.powerbuilder6",
            PermissibleValue(text="vnd.powerbuilder6"))
        setattr(cls, "vnd.powerbuilder6-s",
            PermissibleValue(text="vnd.powerbuilder6-s"))
        setattr(cls, "vnd.powerbuilder7",
            PermissibleValue(text="vnd.powerbuilder7"))
        setattr(cls, "vnd.powerbuilder75",
            PermissibleValue(text="vnd.powerbuilder75"))
        setattr(cls, "vnd.powerbuilder75-s",
            PermissibleValue(text="vnd.powerbuilder75-s"))
        setattr(cls, "vnd.powerbuilder7-s",
            PermissibleValue(text="vnd.powerbuilder7-s"))
        setattr(cls, "vnd.preminet",
            PermissibleValue(text="vnd.preminet"))
        setattr(cls, "vnd.previewsystems.box",
            PermissibleValue(text="vnd.previewsystems.box"))
        setattr(cls, "vnd.proteus.magazine",
            PermissibleValue(text="vnd.proteus.magazine"))
        setattr(cls, "vnd.psfs",
            PermissibleValue(text="vnd.psfs"))
        setattr(cls, "vnd.pt.mundusmundi",
            PermissibleValue(text="vnd.pt.mundusmundi"))
        setattr(cls, "vnd.publishare-delta-tree",
            PermissibleValue(text="vnd.publishare-delta-tree"))
        setattr(cls, "vnd.pvi.ptid1",
            PermissibleValue(text="vnd.pvi.ptid1"))
        setattr(cls, "vnd.pwg-multiplexed",
            PermissibleValue(text="vnd.pwg-multiplexed"))
        setattr(cls, "vnd.pwg-xhtml-print+xml",
            PermissibleValue(text="vnd.pwg-xhtml-print+xml"))
        setattr(cls, "vnd.qualcomm.brew-app-res",
            PermissibleValue(text="vnd.qualcomm.brew-app-res"))
        setattr(cls, "vnd.quarantainenet",
            PermissibleValue(text="vnd.quarantainenet"))
        setattr(cls, "vnd.Quark.QuarkXPress",
            PermissibleValue(text="vnd.Quark.QuarkXPress"))
        setattr(cls, "vnd.quobject-quoxdocument",
            PermissibleValue(text="vnd.quobject-quoxdocument"))
        setattr(cls, "vnd.radisys.moml+xml",
            PermissibleValue(text="vnd.radisys.moml+xml"))
        setattr(cls, "vnd.radisys.msml-audit-conf+xml",
            PermissibleValue(text="vnd.radisys.msml-audit-conf+xml"))
        setattr(cls, "vnd.radisys.msml-audit-conn+xml",
            PermissibleValue(text="vnd.radisys.msml-audit-conn+xml"))
        setattr(cls, "vnd.radisys.msml-audit-dialog+xml",
            PermissibleValue(text="vnd.radisys.msml-audit-dialog+xml"))
        setattr(cls, "vnd.radisys.msml-audit-stream+xml",
            PermissibleValue(text="vnd.radisys.msml-audit-stream+xml"))
        setattr(cls, "vnd.radisys.msml-audit+xml",
            PermissibleValue(text="vnd.radisys.msml-audit+xml"))
        setattr(cls, "vnd.radisys.msml-conf+xml",
            PermissibleValue(text="vnd.radisys.msml-conf+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-base+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-base+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-fax-detect+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-fax-detect+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-fax-sendrecv+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-fax-sendrecv+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-group+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-group+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-speech+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-speech+xml"))
        setattr(cls, "vnd.radisys.msml-dialog-transform+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog-transform+xml"))
        setattr(cls, "vnd.radisys.msml-dialog+xml",
            PermissibleValue(text="vnd.radisys.msml-dialog+xml"))
        setattr(cls, "vnd.radisys.msml+xml",
            PermissibleValue(text="vnd.radisys.msml+xml"))
        setattr(cls, "vnd.rainstor.data",
            PermissibleValue(text="vnd.rainstor.data"))
        setattr(cls, "vnd.rapid",
            PermissibleValue(text="vnd.rapid"))
        setattr(cls, "vnd.rar",
            PermissibleValue(text="vnd.rar"))
        setattr(cls, "vnd.realvnc.bed",
            PermissibleValue(text="vnd.realvnc.bed"))
        setattr(cls, "vnd.recordare.musicxml",
            PermissibleValue(text="vnd.recordare.musicxml"))
        setattr(cls, "vnd.recordare.musicxml+xml",
            PermissibleValue(text="vnd.recordare.musicxml+xml"))
        setattr(cls, "vnd.relpipe",
            PermissibleValue(text="vnd.relpipe"))
        setattr(cls, "vnd.RenLearn.rlprint",
            PermissibleValue(text="vnd.RenLearn.rlprint"))
        setattr(cls, "vnd.resilient.logic",
            PermissibleValue(text="vnd.resilient.logic"))
        setattr(cls, "vnd.restful+json",
            PermissibleValue(text="vnd.restful+json"))
        setattr(cls, "vnd.rig.cryptonote",
            PermissibleValue(text="vnd.rig.cryptonote"))
        setattr(cls, "vnd.route66.link66+xml",
            PermissibleValue(text="vnd.route66.link66+xml"))
        setattr(cls, "vnd.rs-274x",
            PermissibleValue(text="vnd.rs-274x"))
        setattr(cls, "vnd.ruckus.download",
            PermissibleValue(text="vnd.ruckus.download"))
        setattr(cls, "vnd.s3sms",
            PermissibleValue(text="vnd.s3sms"))
        setattr(cls, "vnd.sailingtracker.track",
            PermissibleValue(text="vnd.sailingtracker.track"))
        setattr(cls, "vnd.sar",
            PermissibleValue(text="vnd.sar"))
        setattr(cls, "vnd.sbm.cid",
            PermissibleValue(text="vnd.sbm.cid"))
        setattr(cls, "vnd.sbm.mid2",
            PermissibleValue(text="vnd.sbm.mid2"))
        setattr(cls, "vnd.scribus",
            PermissibleValue(text="vnd.scribus"))
        setattr(cls, "vnd.sealed.3df",
            PermissibleValue(text="vnd.sealed.3df"))
        setattr(cls, "vnd.sealed.csf",
            PermissibleValue(text="vnd.sealed.csf"))
        setattr(cls, "vnd.sealed.doc",
            PermissibleValue(text="vnd.sealed.doc"))
        setattr(cls, "vnd.sealed.eml",
            PermissibleValue(text="vnd.sealed.eml"))
        setattr(cls, "vnd.sealed.mht",
            PermissibleValue(text="vnd.sealed.mht"))
        setattr(cls, "vnd.sealed.net",
            PermissibleValue(text="vnd.sealed.net"))
        setattr(cls, "vnd.sealed.ppt",
            PermissibleValue(text="vnd.sealed.ppt"))
        setattr(cls, "vnd.sealed.tiff",
            PermissibleValue(text="vnd.sealed.tiff"))
        setattr(cls, "vnd.sealed.xls",
            PermissibleValue(text="vnd.sealed.xls"))
        setattr(cls, "vnd.sealedmedia.softseal.html",
            PermissibleValue(text="vnd.sealedmedia.softseal.html"))
        setattr(cls, "vnd.sealedmedia.softseal.pdf",
            PermissibleValue(text="vnd.sealedmedia.softseal.pdf"))
        setattr(cls, "vnd.seemail",
            PermissibleValue(text="vnd.seemail"))
        setattr(cls, "vnd.seis+json",
            PermissibleValue(text="vnd.seis+json"))
        setattr(cls, "vnd.sema",
            PermissibleValue(text="vnd.sema"))
        setattr(cls, "vnd.semd",
            PermissibleValue(text="vnd.semd"))
        setattr(cls, "vnd.semf",
            PermissibleValue(text="vnd.semf"))
        setattr(cls, "vnd.shade-save-file",
            PermissibleValue(text="vnd.shade-save-file"))
        setattr(cls, "vnd.shana.informed.formdata",
            PermissibleValue(text="vnd.shana.informed.formdata"))
        setattr(cls, "vnd.shana.informed.formtemplate",
            PermissibleValue(text="vnd.shana.informed.formtemplate"))
        setattr(cls, "vnd.shana.informed.interchange",
            PermissibleValue(text="vnd.shana.informed.interchange"))
        setattr(cls, "vnd.shana.informed.package",
            PermissibleValue(text="vnd.shana.informed.package"))
        setattr(cls, "vnd.shootproof+json",
            PermissibleValue(text="vnd.shootproof+json"))
        setattr(cls, "vnd.shopkick+json",
            PermissibleValue(text="vnd.shopkick+json"))
        setattr(cls, "vnd.shp",
            PermissibleValue(text="vnd.shp"))
        setattr(cls, "vnd.shx",
            PermissibleValue(text="vnd.shx"))
        setattr(cls, "vnd.sigrok.session",
            PermissibleValue(text="vnd.sigrok.session"))
        setattr(cls, "vnd.SimTech-MindMapper",
            PermissibleValue(text="vnd.SimTech-MindMapper"))
        setattr(cls, "vnd.siren+json",
            PermissibleValue(text="vnd.siren+json"))
        setattr(cls, "vnd.smaf",
            PermissibleValue(text="vnd.smaf"))
        setattr(cls, "vnd.smart.notebook",
            PermissibleValue(text="vnd.smart.notebook"))
        setattr(cls, "vnd.smart.teacher",
            PermissibleValue(text="vnd.smart.teacher"))
        setattr(cls, "vnd.smintio.portals.archive",
            PermissibleValue(text="vnd.smintio.portals.archive"))
        setattr(cls, "vnd.snesdev-page-table",
            PermissibleValue(text="vnd.snesdev-page-table"))
        setattr(cls, "vnd.software602.filler.form+xml",
            PermissibleValue(text="vnd.software602.filler.form+xml"))
        setattr(cls, "vnd.software602.filler.form-xml-zip",
            PermissibleValue(text="vnd.software602.filler.form-xml-zip"))
        setattr(cls, "vnd.solent.sdkm+xml",
            PermissibleValue(text="vnd.solent.sdkm+xml"))
        setattr(cls, "vnd.spotfire.dxp",
            PermissibleValue(text="vnd.spotfire.dxp"))
        setattr(cls, "vnd.spotfire.sfs",
            PermissibleValue(text="vnd.spotfire.sfs"))
        setattr(cls, "vnd.sqlite3",
            PermissibleValue(text="vnd.sqlite3"))
        setattr(cls, "vnd.sss-cod",
            PermissibleValue(text="vnd.sss-cod"))
        setattr(cls, "vnd.sss-dtf",
            PermissibleValue(text="vnd.sss-dtf"))
        setattr(cls, "vnd.sss-ntf",
            PermissibleValue(text="vnd.sss-ntf"))
        setattr(cls, "vnd.stepmania.package",
            PermissibleValue(text="vnd.stepmania.package"))
        setattr(cls, "vnd.stepmania.stepchart",
            PermissibleValue(text="vnd.stepmania.stepchart"))
        setattr(cls, "vnd.street-stream",
            PermissibleValue(text="vnd.street-stream"))
        setattr(cls, "vnd.sun.wadl+xml",
            PermissibleValue(text="vnd.sun.wadl+xml"))
        setattr(cls, "vnd.sus-calendar",
            PermissibleValue(text="vnd.sus-calendar"))
        setattr(cls, "vnd.svd",
            PermissibleValue(text="vnd.svd"))
        setattr(cls, "vnd.swiftview-ics",
            PermissibleValue(text="vnd.swiftview-ics"))
        setattr(cls, "vnd.sybyl.mol2",
            PermissibleValue(text="vnd.sybyl.mol2"))
        setattr(cls, "vnd.sycle+xml",
            PermissibleValue(text="vnd.sycle+xml"))
        setattr(cls, "vnd.syft+json",
            PermissibleValue(text="vnd.syft+json"))
        setattr(cls, "vnd.syncml.dm.notification",
            PermissibleValue(text="vnd.syncml.dm.notification"))
        setattr(cls, "vnd.syncml.dmddf+xml",
            PermissibleValue(text="vnd.syncml.dmddf+xml"))
        setattr(cls, "vnd.syncml.dmtnds+wbxml",
            PermissibleValue(text="vnd.syncml.dmtnds+wbxml"))
        setattr(cls, "vnd.syncml.dmtnds+xml",
            PermissibleValue(text="vnd.syncml.dmtnds+xml"))
        setattr(cls, "vnd.syncml.dmddf+wbxml",
            PermissibleValue(text="vnd.syncml.dmddf+wbxml"))
        setattr(cls, "vnd.syncml.dm+wbxml",
            PermissibleValue(text="vnd.syncml.dm+wbxml"))
        setattr(cls, "vnd.syncml.dm+xml",
            PermissibleValue(text="vnd.syncml.dm+xml"))
        setattr(cls, "vnd.syncml.ds.notification",
            PermissibleValue(text="vnd.syncml.ds.notification"))
        setattr(cls, "vnd.syncml+xml",
            PermissibleValue(text="vnd.syncml+xml"))
        setattr(cls, "vnd.tableschema+json",
            PermissibleValue(text="vnd.tableschema+json"))
        setattr(cls, "vnd.tao.intent-module-archive",
            PermissibleValue(text="vnd.tao.intent-module-archive"))
        setattr(cls, "vnd.tcpdump.pcap",
            PermissibleValue(text="vnd.tcpdump.pcap"))
        setattr(cls, "vnd.think-cell.ppttc+json",
            PermissibleValue(text="vnd.think-cell.ppttc+json"))
        setattr(cls, "vnd.tml",
            PermissibleValue(text="vnd.tml"))
        setattr(cls, "vnd.tmd.mediaflex.api+xml",
            PermissibleValue(text="vnd.tmd.mediaflex.api+xml"))
        setattr(cls, "vnd.tmobile-livetv",
            PermissibleValue(text="vnd.tmobile-livetv"))
        setattr(cls, "vnd.tri.onesource",
            PermissibleValue(text="vnd.tri.onesource"))
        setattr(cls, "vnd.trid.tpt",
            PermissibleValue(text="vnd.trid.tpt"))
        setattr(cls, "vnd.triscape.mxs",
            PermissibleValue(text="vnd.triscape.mxs"))
        setattr(cls, "vnd.trueapp",
            PermissibleValue(text="vnd.trueapp"))
        setattr(cls, "vnd.truedoc",
            PermissibleValue(text="vnd.truedoc"))
        setattr(cls, "vnd.ubisoft.webplayer",
            PermissibleValue(text="vnd.ubisoft.webplayer"))
        setattr(cls, "vnd.ufdl",
            PermissibleValue(text="vnd.ufdl"))
        setattr(cls, "vnd.uiq.theme",
            PermissibleValue(text="vnd.uiq.theme"))
        setattr(cls, "vnd.umajin",
            PermissibleValue(text="vnd.umajin"))
        setattr(cls, "vnd.unity",
            PermissibleValue(text="vnd.unity"))
        setattr(cls, "vnd.uoml+xml",
            PermissibleValue(text="vnd.uoml+xml"))
        setattr(cls, "vnd.uplanet.alert",
            PermissibleValue(text="vnd.uplanet.alert"))
        setattr(cls, "vnd.uplanet.alert-wbxml",
            PermissibleValue(text="vnd.uplanet.alert-wbxml"))
        setattr(cls, "vnd.uplanet.bearer-choice",
            PermissibleValue(text="vnd.uplanet.bearer-choice"))
        setattr(cls, "vnd.uplanet.bearer-choice-wbxml",
            PermissibleValue(text="vnd.uplanet.bearer-choice-wbxml"))
        setattr(cls, "vnd.uplanet.cacheop",
            PermissibleValue(text="vnd.uplanet.cacheop"))
        setattr(cls, "vnd.uplanet.cacheop-wbxml",
            PermissibleValue(text="vnd.uplanet.cacheop-wbxml"))
        setattr(cls, "vnd.uplanet.channel",
            PermissibleValue(text="vnd.uplanet.channel"))
        setattr(cls, "vnd.uplanet.channel-wbxml",
            PermissibleValue(text="vnd.uplanet.channel-wbxml"))
        setattr(cls, "vnd.uplanet.list",
            PermissibleValue(text="vnd.uplanet.list"))
        setattr(cls, "vnd.uplanet.listcmd",
            PermissibleValue(text="vnd.uplanet.listcmd"))
        setattr(cls, "vnd.uplanet.listcmd-wbxml",
            PermissibleValue(text="vnd.uplanet.listcmd-wbxml"))
        setattr(cls, "vnd.uplanet.list-wbxml",
            PermissibleValue(text="vnd.uplanet.list-wbxml"))
        setattr(cls, "vnd.uri-map",
            PermissibleValue(text="vnd.uri-map"))
        setattr(cls, "vnd.uplanet.signal",
            PermissibleValue(text="vnd.uplanet.signal"))
        setattr(cls, "vnd.valve.source.material",
            PermissibleValue(text="vnd.valve.source.material"))
        setattr(cls, "vnd.vcx",
            PermissibleValue(text="vnd.vcx"))
        setattr(cls, "vnd.vd-study",
            PermissibleValue(text="vnd.vd-study"))
        setattr(cls, "vnd.vectorworks",
            PermissibleValue(text="vnd.vectorworks"))
        setattr(cls, "vnd.vel+json",
            PermissibleValue(text="vnd.vel+json"))
        setattr(cls, "vnd.verimatrix.vcas",
            PermissibleValue(text="vnd.verimatrix.vcas"))
        setattr(cls, "vnd.veritone.aion+json",
            PermissibleValue(text="vnd.veritone.aion+json"))
        setattr(cls, "vnd.veryant.thin",
            PermissibleValue(text="vnd.veryant.thin"))
        setattr(cls, "vnd.ves.encrypted",
            PermissibleValue(text="vnd.ves.encrypted"))
        setattr(cls, "vnd.vidsoft.vidconference",
            PermissibleValue(text="vnd.vidsoft.vidconference"))
        setattr(cls, "vnd.visio",
            PermissibleValue(text="vnd.visio"))
        setattr(cls, "vnd.visionary",
            PermissibleValue(text="vnd.visionary"))
        setattr(cls, "vnd.vividence.scriptfile",
            PermissibleValue(text="vnd.vividence.scriptfile"))
        setattr(cls, "vnd.vsf",
            PermissibleValue(text="vnd.vsf"))
        setattr(cls, "vnd.wap.sic",
            PermissibleValue(text="vnd.wap.sic"))
        setattr(cls, "vnd.wap.slc",
            PermissibleValue(text="vnd.wap.slc"))
        setattr(cls, "vnd.wap.wbxml",
            PermissibleValue(text="vnd.wap.wbxml"))
        setattr(cls, "vnd.wap.wmlc",
            PermissibleValue(text="vnd.wap.wmlc"))
        setattr(cls, "vnd.wap.wmlscriptc",
            PermissibleValue(text="vnd.wap.wmlscriptc"))
        setattr(cls, "vnd.wasmflow.wafl",
            PermissibleValue(text="vnd.wasmflow.wafl"))
        setattr(cls, "vnd.webturbo",
            PermissibleValue(text="vnd.webturbo"))
        setattr(cls, "vnd.wfa.dpp",
            PermissibleValue(text="vnd.wfa.dpp"))
        setattr(cls, "vnd.wfa.p2p",
            PermissibleValue(text="vnd.wfa.p2p"))
        setattr(cls, "vnd.wfa.wsc",
            PermissibleValue(text="vnd.wfa.wsc"))
        setattr(cls, "vnd.windows.devicepairing",
            PermissibleValue(text="vnd.windows.devicepairing"))
        setattr(cls, "vnd.wmc",
            PermissibleValue(text="vnd.wmc"))
        setattr(cls, "vnd.wmf.bootstrap",
            PermissibleValue(text="vnd.wmf.bootstrap"))
        setattr(cls, "vnd.wolfram.mathematica",
            PermissibleValue(text="vnd.wolfram.mathematica"))
        setattr(cls, "vnd.wolfram.mathematica.package",
            PermissibleValue(text="vnd.wolfram.mathematica.package"))
        setattr(cls, "vnd.wolfram.player",
            PermissibleValue(text="vnd.wolfram.player"))
        setattr(cls, "vnd.wordlift",
            PermissibleValue(text="vnd.wordlift"))
        setattr(cls, "vnd.wordperfect",
            PermissibleValue(text="vnd.wordperfect"))
        setattr(cls, "vnd.wqd",
            PermissibleValue(text="vnd.wqd"))
        setattr(cls, "vnd.wrq-hp3000-labelled",
            PermissibleValue(text="vnd.wrq-hp3000-labelled"))
        setattr(cls, "vnd.wt.stf",
            PermissibleValue(text="vnd.wt.stf"))
        setattr(cls, "vnd.wv.csp+xml",
            PermissibleValue(text="vnd.wv.csp+xml"))
        setattr(cls, "vnd.wv.csp+wbxml",
            PermissibleValue(text="vnd.wv.csp+wbxml"))
        setattr(cls, "vnd.wv.ssp+xml",
            PermissibleValue(text="vnd.wv.ssp+xml"))
        setattr(cls, "vnd.xacml+json",
            PermissibleValue(text="vnd.xacml+json"))
        setattr(cls, "vnd.xara",
            PermissibleValue(text="vnd.xara"))
        setattr(cls, "vnd.xfdl",
            PermissibleValue(text="vnd.xfdl"))
        setattr(cls, "vnd.xfdl.webform",
            PermissibleValue(text="vnd.xfdl.webform"))
        setattr(cls, "vnd.xmi+xml",
            PermissibleValue(text="vnd.xmi+xml"))
        setattr(cls, "vnd.xmpie.cpkg",
            PermissibleValue(text="vnd.xmpie.cpkg"))
        setattr(cls, "vnd.xmpie.dpkg",
            PermissibleValue(text="vnd.xmpie.dpkg"))
        setattr(cls, "vnd.xmpie.plan",
            PermissibleValue(text="vnd.xmpie.plan"))
        setattr(cls, "vnd.xmpie.ppkg",
            PermissibleValue(text="vnd.xmpie.ppkg"))
        setattr(cls, "vnd.xmpie.xlim",
            PermissibleValue(text="vnd.xmpie.xlim"))
        setattr(cls, "vnd.yamaha.hv-dic",
            PermissibleValue(text="vnd.yamaha.hv-dic"))
        setattr(cls, "vnd.yamaha.hv-script",
            PermissibleValue(text="vnd.yamaha.hv-script"))
        setattr(cls, "vnd.yamaha.hv-voice",
            PermissibleValue(text="vnd.yamaha.hv-voice"))
        setattr(cls, "vnd.yamaha.openscoreformat.osfpvg+xml",
            PermissibleValue(text="vnd.yamaha.openscoreformat.osfpvg+xml"))
        setattr(cls, "vnd.yamaha.openscoreformat",
            PermissibleValue(text="vnd.yamaha.openscoreformat"))
        setattr(cls, "vnd.yamaha.remote-setup",
            PermissibleValue(text="vnd.yamaha.remote-setup"))
        setattr(cls, "vnd.yamaha.smaf-audio",
            PermissibleValue(text="vnd.yamaha.smaf-audio"))
        setattr(cls, "vnd.yamaha.smaf-phrase",
            PermissibleValue(text="vnd.yamaha.smaf-phrase"))
        setattr(cls, "vnd.yamaha.through-ngn",
            PermissibleValue(text="vnd.yamaha.through-ngn"))
        setattr(cls, "vnd.yamaha.tunnel-udpencap",
            PermissibleValue(text="vnd.yamaha.tunnel-udpencap"))
        setattr(cls, "vnd.yaoweme",
            PermissibleValue(text="vnd.yaoweme"))
        setattr(cls, "vnd.yellowriver-custom-menu",
            PermissibleValue(text="vnd.yellowriver-custom-menu"))
        setattr(cls, "vnd.youtube.yt (OBSOLETED in favor of video/vnd.youtube.yt)",
            PermissibleValue(text="vnd.youtube.yt (OBSOLETED in favor of video/vnd.youtube.yt)"))
        setattr(cls, "vnd.zul",
            PermissibleValue(text="vnd.zul"))
        setattr(cls, "vnd.zzazz.deck+xml",
            PermissibleValue(text="vnd.zzazz.deck+xml"))
        setattr(cls, "voicexml+xml",
            PermissibleValue(text="voicexml+xml"))
        setattr(cls, "voucher-cms+json",
            PermissibleValue(text="voucher-cms+json"))
        setattr(cls, "vq-rtcpxr",
            PermissibleValue(text="vq-rtcpxr"))
        setattr(cls, "watcherinfo+xml",
            PermissibleValue(text="watcherinfo+xml"))
        setattr(cls, "webpush-options+json",
            PermissibleValue(text="webpush-options+json"))
        setattr(cls, "whoispp-query",
            PermissibleValue(text="whoispp-query"))
        setattr(cls, "whoispp-response",
            PermissibleValue(text="whoispp-response"))
        setattr(cls, "wordperfect5.1",
            PermissibleValue(text="wordperfect5.1"))
        setattr(cls, "wsdl+xml",
            PermissibleValue(text="wsdl+xml"))
        setattr(cls, "wspolicy+xml",
            PermissibleValue(text="wspolicy+xml"))
        setattr(cls, "x-pki-message",
            PermissibleValue(text="x-pki-message"))
        setattr(cls, "x-www-form-urlencoded",
            PermissibleValue(text="x-www-form-urlencoded"))
        setattr(cls, "x-x509-ca-cert",
            PermissibleValue(text="x-x509-ca-cert"))
        setattr(cls, "x-x509-ca-ra-cert",
            PermissibleValue(text="x-x509-ca-ra-cert"))
        setattr(cls, "x-x509-next-ca-cert",
            PermissibleValue(text="x-x509-next-ca-cert"))
        setattr(cls, "x400-bp",
            PermissibleValue(text="x400-bp"))
        setattr(cls, "xacml+xml",
            PermissibleValue(text="xacml+xml"))
        setattr(cls, "xcap-att+xml",
            PermissibleValue(text="xcap-att+xml"))
        setattr(cls, "xcap-caps+xml",
            PermissibleValue(text="xcap-caps+xml"))
        setattr(cls, "xcap-diff+xml",
            PermissibleValue(text="xcap-diff+xml"))
        setattr(cls, "xcap-el+xml",
            PermissibleValue(text="xcap-el+xml"))
        setattr(cls, "xcap-error+xml",
            PermissibleValue(text="xcap-error+xml"))
        setattr(cls, "xcap-ns+xml",
            PermissibleValue(text="xcap-ns+xml"))
        setattr(cls, "xcon-conference-info-diff+xml",
            PermissibleValue(text="xcon-conference-info-diff+xml"))
        setattr(cls, "xcon-conference-info+xml",
            PermissibleValue(text="xcon-conference-info+xml"))
        setattr(cls, "xenc+xml",
            PermissibleValue(text="xenc+xml"))
        setattr(cls, "xhtml+xml",
            PermissibleValue(text="xhtml+xml"))
        setattr(cls, "xliff+xml",
            PermissibleValue(text="xliff+xml"))
        setattr(cls, "xml-dtd",
            PermissibleValue(text="xml-dtd"))
        setattr(cls, "xml-patch+xml",
            PermissibleValue(text="xml-patch+xml"))
        setattr(cls, "xmpp+xml",
            PermissibleValue(text="xmpp+xml"))
        setattr(cls, "xop+xml",
            PermissibleValue(text="xop+xml"))
        setattr(cls, "xslt+xml",
            PermissibleValue(text="xslt+xml"))
        setattr(cls, "xv+xml",
            PermissibleValue(text="xv+xml"))
        setattr(cls, "yang-data+cbor",
            PermissibleValue(text="yang-data+cbor"))
        setattr(cls, "yang-data+json",
            PermissibleValue(text="yang-data+json"))
        setattr(cls, "yang-data+xml",
            PermissibleValue(text="yang-data+xml"))
        setattr(cls, "yang-patch+json",
            PermissibleValue(text="yang-patch+json"))
        setattr(cls, "yang-patch+xml",
            PermissibleValue(text="yang-patch+xml"))
        setattr(cls, "yin+xml",
            PermissibleValue(text="yin+xml"))

class ProvisionTypes(EnumDefinitionImpl):

    private = PermissibleValue(
        text="private",
        description="A service, which is provided for one customer exclusively.")
    public = PermissibleValue(
        text="public",
        description="A service, which is used by several customers, simultaneously.")
    hybrid = PermissibleValue(
        text="hybrid",
        description="""A service, which has components, which are exclusively provided to one customers and components, which are used simultaneously with other clients""")

    _defn = EnumDefinition(
        name="ProvisionTypes",
    )

class TenantSeparation(EnumDefinitionImpl):

    physical = PermissibleValue(
        text="physical",
        description="TBD")

    _defn = EnumDefinition(
        name="TenantSeparation",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hw-virtualized",
            PermissibleValue(
                text="hw-virtualized",
                description="TBD"))
        setattr(cls, "sw-virtualized",
            PermissibleValue(
                text="sw-virtualized",
                description="TBD"))
        setattr(cls, "os-virtualized",
            PermissibleValue(
                text="os-virtualized",
                description="TBD"))
        setattr(cls, "os-hw-virtualized",
            PermissibleValue(
                text="os-hw-virtualized",
                description="TBD"))
        setattr(cls, "hw-partitioned",
            PermissibleValue(
                text="hw-partitioned",
                description="TBD"))

class ContainerFormat(EnumDefinitionImpl):
    """
    Possible values for container image format.
    """
    dockerv1 = PermissibleValue(
        text="dockerv1",
        description="Container is packaged with Docker v1 format.")
    dockerv2 = PermissibleValue(
        text="dockerv2",
        description="Container is packaged with Docker v2 format.")
    oci = PermissibleValue(
        text="oci",
        description="Container is packaged with OCI format.")
    lxc = PermissibleValue(
        text="lxc",
        description="Container is packaged with LXC format.")
    lxd = PermissibleValue(
        text="lxd",
        description="Container is packaged with LXD format.")

    _defn = EnumDefinition(
        name="ContainerFormat",
        description="Possible values for container image format.",
    )

class ProtectionFrequency(EnumDefinitionImpl):

    Hourly = PermissibleValue(
        text="Hourly",
        description="For describing protection policies triggered once an hour")
    Daily = PermissibleValue(
        text="Daily",
        description="For describing protection policies triggered once a day")
    Weekly = PermissibleValue(
        text="Weekly",
        description="For describing protection policies triggered once a week")
    Monthly = PermissibleValue(
        text="Monthly",
        description="For describing protection policies triggered once a month")
    Continuously = PermissibleValue(
        text="Continuously",
        description="For describing protection policies triggered continuously, ie each time data are modified")
    OnDemand = PermissibleValue(
        text="OnDemand",
        description="For describing unplanned protection policies triggered on demand")

    _defn = EnumDefinition(
        name="ProtectionFrequency",
    )

class ProtectionMethod(EnumDefinitionImpl):

    Incremental = PermissibleValue(
        text="Incremental",
        description="""For describing protection through differential copy of protected data, ie only modifications are copied""")

    _defn = EnumDefinition(
        name="ProtectionMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-Copy",
            PermissibleValue(
                text="Full-Copy",
                description="For describing protection through full copy of protected data"))

class GeoReplicationScope(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GeoReplicationScope",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cross-Region",
            PermissibleValue(
                text="Cross-Region",
                description="Whenever replication is span across multiple regions"))
        setattr(cls, "Cross-DC",
            PermissibleValue(
                text="Cross-DC",
                description="Whenever replication is span across multiple datacenters within a region"))
        setattr(cls, "Cross-AZ",
            PermissibleValue(
                text="Cross-AZ",
                description="Whenever replication is span across multiple availability zones"))

class ConsistencyType(EnumDefinitionImpl):

    Strong = PermissibleValue(
        text="Strong",
        description="""Strong consistency model, cf https://en.wikipedia.org/wiki/Consistency_model#Strong_consistency_models.""")
    Session = PermissibleValue(
        text="Session",
        description="""Eventual consistency model, cf https://en.wikipedia.org/wiki/Consistency_model#Session_guarantees.""")
    Eventual = PermissibleValue(
        text="Eventual",
        description="Eventual consistency model, cf https://en.wikipedia.org/wiki/Eventual_consistency.")
    Other = PermissibleValue(
        text="Other",
        description="Unspecified consistency model.")

    _defn = EnumDefinition(
        name="ConsistencyType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bounded-Staleness",
            PermissibleValue(
                text="Bounded-Staleness",
                description="""Consistency model where the lag between replicas is bounded, either by a number of updates or a time limit."""))

class StorageRedundancyMechanism(EnumDefinitionImpl):

    RAID0 = PermissibleValue(
        text="RAID0",
        description="Standard RAID-0 block-level striping, cf https://en.wikipedia.org/wiki/RAID_0")
    RAID1 = PermissibleValue(
        text="RAID1",
        description="Standard RAID-1 data mirroring, cf https://en.wikipedia.org/wiki/RAID_1")
    RAID2 = PermissibleValue(
        text="RAID2",
        description="Standard RAID-2 bit-level striping, cf https://en.wikipedia.org/wiki/RAID_2")
    RAID3 = PermissibleValue(
        text="RAID3",
        description="Standard RAID-3 byte-level striping, cf https://en.wikipedia.org/wiki/RAID_3")
    RAID4 = PermissibleValue(
        text="RAID4",
        description="""Standard RAID-4 block-level striping with dedicated parity, cf https://en.wikipedia.org/wiki/RAID_4""")
    RAID5 = PermissibleValue(
        text="RAID5",
        description="""Standard RAID-5 block-level striping with distributed parity, cf https://en.wikipedia.org/wiki/RAID_5""")
    RAID6 = PermissibleValue(
        text="RAID6",
        description="""Standard RAID-6 block-level striping with double distributed parity, cf https://en.wikipedia.org/wiki/RAID_6""")
    HybridRAID = PermissibleValue(
        text="HybridRAID",
        description="Other hybrid or nested RAID combinations, cf https://en.wikipedia.org/wiki/Nested_RAID_levels")
    RS_Code = PermissibleValue(
        text="RS_Code",
        description="""Reed-Solomon Erasure Code, cf https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction""")
    Other = PermissibleValue(
        text="Other",
        description="Unspecified redundancy mechanism")

    _defn = EnumDefinition(
        name="StorageRedundancyMechanism",
    )

class FileAccessProtocol(EnumDefinitionImpl):

    NFSv3 = PermissibleValue(
        text="NFSv3",
        description="NFS Version 3")
    NFSv4 = PermissibleValue(
        text="NFSv4",
        description="NFS Version 4")
    CIFS = PermissibleValue(
        text="CIFS",
        description="Common Internet File System")
    AFS = PermissibleValue(
        text="AFS",
        description="Andrew File System")
    HDFS = PermissibleValue(
        text="HDFS",
        description="Hadoop File System")
    IPFS = PermissibleValue(
        text="IPFS",
        description="InterPlanetary File System, cf https://en.wikipedia.org/wiki/IPFS")
    Other = PermissibleValue(
        text="Other",
        description="Any other proprietary access protocol")

    _defn = EnumDefinition(
        name="FileAccessProtocol",
    )

class FileSystemType(EnumDefinitionImpl):

    FAT = PermissibleValue(
        text="FAT",
        description="FAT file system, cf https://en.wikipedia.org/wiki/File_Allocation_Table")
    ExtFAT = PermissibleValue(
        text="ExtFAT",
        description="Extended FAT file system")
    NTFS = PermissibleValue(
        text="NTFS",
        description="Microsoft New Technology File System, cf https://en.wikipedia.org/wiki/NTFS")
    XFS = PermissibleValue(
        text="XFS",
        description="XFS file system, cf https://en.wikipedia.org/wiki/XFS")
    JFS = PermissibleValue(
        text="JFS",
        description="""IBM Journaling File System, cf https://en.wikipedia.org/wiki/IBM_Journaled_File_System_2_(JFS2)""")
    Ext4 = PermissibleValue(
        text="Ext4",
        description="Extended file system version 4, cf https://en.wikipedia.org/wiki/Ext4")
    Reiser4 = PermissibleValue(
        text="Reiser4",
        description="Successor of ReiserFS, cf https://en.wikipedia.org/wiki/Reiser4")
    GlusterFS = PermissibleValue(
        text="GlusterFS",
        description="Gluster File System, cf https://en.wikipedia.org/wiki/Gluster#GlusterFS")
    MapR_FS = PermissibleValue(
        text="MapR_FS",
        description="MapR clustered file system, cf https://en.wikipedia.org/wiki/MapR_FS")
    OneFS = PermissibleValue(
        text="OneFS",
        description="Dell One File Fystem,cf https://en.wikipedia.org/wiki/One_File_System")
    Other = PermissibleValue(
        text="Other",
        description="Any other proprietary file system")

    _defn = EnumDefinition(
        name="FileSystemType",
    )

class BlockStorageTechnology(EnumDefinitionImpl):

    HDD = PermissibleValue(
        text="HDD",
        description="Regular magnetic Hard Drive Disk")
    SSD = PermissibleValue(
        text="SSD",
        description="Solid State Drive")
    Optane = PermissibleValue(
        text="Optane",
        description="Intel Optane Drive")

    _defn = EnumDefinition(
        name="BlockStorageTechnology",
    )

class BlockAccessProtocol(EnumDefinitionImpl):

    FCP = PermissibleValue(
        text="FCP",
        description="Fiber Channel Protocol, cf https://en.wikipedia.org/wiki/Fibre_Channel")
    FCoE = PermissibleValue(
        text="FCoE",
        description="""Fiber Channel over Ethernet protocol, cf https://en.wikipedia.org/wiki/Fibre_Channel_over_Ethernet""")
    Infiniband = PermissibleValue(
        text="Infiniband",
        description="Infiniband protocol, cf https://en.wikipedia.org/wiki/InfiniBand")
    SAS = PermissibleValue(
        text="SAS",
        description="Directly attached local storage using SAS interface")
    SATA = PermissibleValue(
        text="SATA",
        description="Directly attached local storage using SATA interface")
    NVME = PermissibleValue(
        text="NVME",
        description="Directly attached local storage using NVME interface")
    Other = PermissibleValue(
        text="Other",
        description="Unspecified protocol")

    _defn = EnumDefinition(
        name="BlockAccessProtocol",
    )

class DeduplicationMethod(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DeduplicationMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Inline-Content-Agnostic",
            PermissibleValue(
                text="Inline-Content-Agnostic",
                description="Inline deduplication not requiring any awareness of data formats"))
        setattr(cls, "Inline-Content-Aware",
            PermissibleValue(
                text="Inline-Content-Aware",
                description="Inline deduplication leveraging knowledge of data formats"))
        setattr(cls, "Post-Process-Content-Agnostic",
            PermissibleValue(
                text="Post-Process-Content-Agnostic",
                description="Post processing deduplication not requiring any awareness of data formats"))
        setattr(cls, "Post-Process-Content-Aware",
            PermissibleValue(
                text="Post-Process-Content-Aware",
                description="Post processing deduplication leveraging knowledge of data formats"))

class CompressionAlgorithm(EnumDefinitionImpl):

    LZMA = PermissibleValue(
        text="LZMA",
        description="""Lempel-Ziv with Markov chain algorithm, cf https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm""")
    LZSS = PermissibleValue(
        text="LZSS",
        description="""Lempel-Ziv-Storer–Szymanski algorithm, cf https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Storer%E2%80%93Szymanski""")
    LZ = PermissibleValue(
        text="LZ",
        description="""LZ277 or LZ278 algorithms from Lempel-Ziv familly, cf https://en.wikipedia.org/wiki/LZ77_and_LZ78""")
    LZW = PermissibleValue(
        text="LZW",
        description="Lempel-Ziv-Welch algorithm, cf https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch")
    Huffman_Coding = PermissibleValue(
        text="Huffman_Coding",
        description="Huffman Coding algorithm, cf https://en.wikipedia.org/wiki/Huffman_coding")
    PPM = PermissibleValue(
        text="PPM",
        description="""Prediction by partial matching algorithm, cf https://en.wikipedia.org/wiki/Prediction_by_partial_matching""")
    ANS = PermissibleValue(
        text="ANS",
        description="Entropy encoding algorithm, cf https://en.wikipedia.org/wiki/Asymmetric_numeral_systems")
    Other = PermissibleValue(
        text="Other",
        description="Unspecified compression algorithm")

    _defn = EnumDefinition(
        name="CompressionAlgorithm",
    )

class AccessAttribute(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AccessAttribute",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Read-Only",
            PermissibleValue(
                text="Read-Only",
                description="Allow for access in read-mode only"))
        setattr(cls, "Read-Write",
            PermissibleValue(
                text="Read-Write",
                description="Allow for access in both read-mode and write-mode (data deletion included)"))
        setattr(cls, "Append-Only",
            PermissibleValue(
                text="Append-Only",
                description="""Allow for access in read-mode and to append data (ie write addtionnal data after the previous last byte)"""))

class StorageAPI(EnumDefinitionImpl):

    Swift = PermissibleValue(
        text="Swift",
        description="OpenStack Swift API")
    CDMI = PermissibleValue(
        text="CDMI",
        description="Cloud Data Management Interface API (open ISO standard)")
    S3 = PermissibleValue(
        text="S3",
        description="Amazon S3 API")
    CloudStorage = PermissibleValue(
        text="CloudStorage",
        description="Google Cloud Storage API")

    _defn = EnumDefinition(
        name="StorageAPI",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Azure-Blob",
            PermissibleValue(
                text="Azure-Blob",
                description="Azure Blob API"))

class PublicIpAddressProvisioningTypes(EnumDefinitionImpl):

    floating = PermissibleValue(
        text="floating",
        description="TBD")
    fixed = PermissibleValue(
        text="fixed",
        description="TBD")

    _defn = EnumDefinition(
        name="PublicIpAddressProvisioningTypes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "provider-network",
            PermissibleValue(
                text="provider-network",
                description="TBD"))

class IpVersionTypes(EnumDefinitionImpl):

    IPv4 = PermissibleValue(text="IPv4")
    IPv6 = PermissibleValue(text="IPv6")

    _defn = EnumDefinition(
        name="IpVersionTypes",
    )

class ProtocolType(EnumDefinitionImpl):

    Ethernet = PermissibleValue(
        text="Ethernet",
        description="TBD")
    ARP = PermissibleValue(
        text="ARP",
        description="TBD")
    PPP = PermissibleValue(
        text="PPP",
        description="TBD")
    VLAN = PermissibleValue(
        text="VLAN",
        description="TBD")
    Other = PermissibleValue(
        text="Other",
        description="TBD")

    _defn = EnumDefinition(
        name="ProtocolType",
    )

class IPIType(EnumDefinitionImpl):

    Physical = PermissibleValue(
        text="Physical",
        description="TBD")
    Link = PermissibleValue(
        text="Link",
        description="TBD")
    URI = PermissibleValue(
        text="URI",
        description="TBD")
    Network = PermissibleValue(
        text="Network",
        description="TBD")
    Other = PermissibleValue(
        text="Other",
        description="TBD")

    _defn = EnumDefinition(
        name="IPIType",
    )

class VlanType(EnumDefinitionImpl):

    qinq = PermissibleValue(
        text="qinq",
        description="TBD")
    dot1q = PermissibleValue(
        text="dot1q",
        description="TBD")
    other = PermissibleValue(
        text="other",
        description="TBD")

    _defn = EnumDefinition(
        name="VlanType",
    )

class ComputeFunctionDeploymentMethod(EnumDefinitionImpl):
    """
    Methods for deploying compute function code.
    """
    inlineEditor = PermissibleValue(
        text="inlineEditor",
        description="Use of the integrated code editor")
    gitLab = PermissibleValue(
        text="gitLab",
        description="Import code from a gitLab repository")
    objectStorage = PermissibleValue(
        text="objectStorage",
        description="Import code from an object storage bucket")
    integratedRepo = PermissibleValue(
        text="integratedRepo",
        description="Import code from an integrated code repository service")
    other = PermissibleValue(
        text="other",
        description="Other/Unspecified method")

    _defn = EnumDefinition(
        name="ComputeFunctionDeploymentMethod",
        description="Methods for deploying compute function code.",
    )

class ComputeFunctionLanguage(EnumDefinitionImpl):
    """
    Language runtime for compute function code.
    """
    golang = PermissibleValue(
        text="golang",
        description="GO runtime")
    python = PermissibleValue(
        text="python",
        description="Python runtime")
    jre = PermissibleValue(
        text="jre",
        description="Java runtime")
    other = PermissibleValue(
        text="other",
        description="Other/Unspecified language")

    _defn = EnumDefinition(
        name="ComputeFunctionLanguage",
        description="Language runtime for compute function code.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "node.js",
            PermissibleValue(
                text="node.js",
                description="Node.js runtime (javascript)"))

class FirmType(EnumDefinitionImpl):
    """
    Possible values for VM image's firmetype required by hypervisor.
    """
    BIOS = PermissibleValue(text="BIOS")
    UEFI = PermissibleValue(text="UEFI")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="FirmType",
        description="Possible values for VM image's firmetype required by hypervisor.",
    )

class WatchDogActions(EnumDefinitionImpl):
    """
    Possible values for VM image's watchdog actions.
    """
    disabled = PermissibleValue(
        text="disabled",
        description="No watchdog is enabled. No action will be performed if server hangs.")
    reset = PermissibleValue(
        text="reset",
        description="Restart of guest us forced if server hangs.")
    poweroff = PermissibleValue(
        text="poweroff",
        description="Power of of guest is forced if server hangs.")
    pause = PermissibleValue(
        text="pause",
        description="Pause of guest is forced, if server hangs.")
    none = PermissibleValue(
        text="none",
        description="Watchdog is enabled, but not action is defined and performed if server hangs.")

    _defn = EnumDefinition(
        name="WatchDogActions",
        description="Possible values for VM image's watchdog actions.",
    )

class RNGTypes(EnumDefinitionImpl):

    Quantum = PermissibleValue(
        text="Quantum",
        description="Hardware random generator is based in electronic quantum effects.")

    _defn = EnumDefinition(
        name="RNGTypes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Electrical noise",
            PermissibleValue(
                text="Electrical noise",
                description="Hardware random generator is based on electronic noise."))
        setattr(cls, "Chaos-based",
            PermissibleValue(
                text="Chaos-based",
                description="Hardware random generator is based on chaos."))
        setattr(cls, "Free-running oscillators",
            PermissibleValue(
                text="Free-running oscillators",
                description="Hardware random generator is based in electronic free-running oscillators."))
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No hardware random generator (RNG) is used. Entropy is taken from /dev/urandom."))

class VMDiskType(EnumDefinitionImpl):

    RAW = PermissibleValue(text="RAW")
    QCOW2 = PermissibleValue(text="QCOW2")
    VHD = PermissibleValue(text="VHD")
    VMDK = PermissibleValue(text="VMDK")
    ISO = PermissibleValue(text="ISO")
    CVF = PermissibleValue(text="CVF")
    CVA = PermissibleValue(text="CVA")

    _defn = EnumDefinition(
        name="VMDiskType",
    )

# Slots
class slots:
    pass

slots.value = Slot(uri=QUDT.value, name="value", curie=QUDT.curie('value'),
                   model_uri=GX.value, domain=None, range=float)

slots.unit = Slot(uri=QUDT.unit, name="unit", curie=QUDT.curie('unit'),
                   model_uri=GX.unit, domain=None, range=str)

slots.address__countryCode = Slot(uri=GX.countryCode, name="address__countryCode", curie=GX.curie('countryCode'),
                   model_uri=GX.address__countryCode, domain=None, range=str)

slots.address__gps = Slot(uri=GX.gps, name="address__gps", curie=GX.curie('gps'),
                   model_uri=GX.address__gps, domain=None, range=Optional[Union[Union[dict, GPSLocation], List[Union[dict, GPSLocation]]]])

slots.address__streetAddress = Slot(uri=VCARD['street-address'], name="address__streetAddress", curie=VCARD.curie('street-address'),
                   model_uri=GX.address__streetAddress, domain=None, range=Optional[str])

slots.address__postalCode = Slot(uri=VCARD['postal-code'], name="address__postalCode", curie=VCARD.curie('postal-code'),
                   model_uri=GX.address__postalCode, domain=None, range=Optional[str])

slots.address__locality = Slot(uri=VCARD.locality, name="address__locality", curie=VCARD.curie('locality'),
                   model_uri=GX.address__locality, domain=None, range=Optional[str])

slots.gPSLocation__latitude = Slot(uri=GX.latitude, name="gPSLocation__latitude", curie=GX.curie('latitude'),
                   model_uri=GX.gPSLocation__latitude, domain=None, range=str)

slots.gPSLocation__longitude = Slot(uri=GX.longitude, name="gPSLocation__longitude", curie=GX.curie('longitude'),
                   model_uri=GX.gPSLocation__longitude, domain=None, range=str)

slots.gPSLocation__altitude = Slot(uri=GX.altitude, name="gPSLocation__altitude", curie=GX.curie('altitude'),
                   model_uri=GX.gPSLocation__altitude, domain=None, range=Optional[str])

slots.gPSLocation__crs = Slot(uri=GX.crs, name="gPSLocation__crs", curie=GX.curie('crs'),
                   model_uri=GX.gPSLocation__crs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CRS'))

slots.gPSUnit__degrees = Slot(uri=GX.degrees, name="gPSUnit__degrees", curie=GX.curie('degrees'),
                   model_uri=GX.gPSUnit__degrees, domain=None, range=int)

slots.gPSUnit__minutes = Slot(uri=GX.minutes, name="gPSUnit__minutes", curie=GX.curie('minutes'),
                   model_uri=GX.gPSUnit__minutes, domain=None, range=Optional[int])

slots.gPSUnit__seconds = Slot(uri=GX.seconds, name="gPSUnit__seconds", curie=GX.curie('seconds'),
                   model_uri=GX.gPSUnit__seconds, domain=None, range=Optional[int])

slots.gPSUnit__decimals = Slot(uri=GX.decimals, name="gPSUnit__decimals", curie=GX.curie('decimals'),
                   model_uri=GX.gPSUnit__decimals, domain=None, range=Optional[float])

slots.gaiaXEntity__name = Slot(uri=GX.name, name="gaiaXEntity__name", curie=GX.curie('name'),
                   model_uri=GX.gaiaXEntity__name, domain=None, range=Optional[str])

slots.gaiaXEntity__description = Slot(uri=GX.description, name="gaiaXEntity__description", curie=GX.curie('description'),
                   model_uri=GX.gaiaXEntity__description, domain=None, range=Optional[str])

slots.cPU__cpuArchitecture = Slot(uri=GX.cpuArchitecture, name="cPU__cpuArchitecture", curie=GX.curie('cpuArchitecture'),
                   model_uri=GX.cPU__cpuArchitecture, domain=None, range=Optional[Union[str, "Architectures"]])

slots.cPU__cpuFlag = Slot(uri=GX.cpuFlag, name="cPU__cpuFlag", curie=GX.curie('cpuFlag'),
                   model_uri=GX.cPU__cpuFlag, domain=None, range=Optional[Union[str, List[str]]])

slots.cPU__smtEnabled = Slot(uri=GX.smtEnabled, name="cPU__smtEnabled", curie=GX.curie('smtEnabled'),
                   model_uri=GX.cPU__smtEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.cPU__numberOfCores = Slot(uri=GX.numberOfCores, name="cPU__numberOfCores", curie=GX.curie('numberOfCores'),
                   model_uri=GX.cPU__numberOfCores, domain=None, range=Optional[int])

slots.cPU__numberOfThreads = Slot(uri=GX.numberOfThreads, name="cPU__numberOfThreads", curie=GX.curie('numberOfThreads'),
                   model_uri=GX.cPU__numberOfThreads, domain=None, range=Optional[int])

slots.cPU__baseFrequency = Slot(uri=GX.baseFrequency, name="cPU__baseFrequency", curie=GX.curie('baseFrequency'),
                   model_uri=GX.cPU__baseFrequency, domain=None, range=Optional[Union[dict, Frequency]])

slots.cPU__boostFrequency = Slot(uri=GX.boostFrequency, name="cPU__boostFrequency", curie=GX.curie('boostFrequency'),
                   model_uri=GX.cPU__boostFrequency, domain=None, range=Optional[Union[dict, Frequency]])

slots.cPU__lastLevelCacheSize = Slot(uri=GX.lastLevelCacheSize, name="cPU__lastLevelCacheSize", curie=GX.curie('lastLevelCacheSize'),
                   model_uri=GX.cPU__lastLevelCacheSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.cPU__thermalDesignPower = Slot(uri=GX.thermalDesignPower, name="cPU__thermalDesignPower", curie=GX.curie('thermalDesignPower'),
                   model_uri=GX.cPU__thermalDesignPower, domain=None, range=Optional[Union[dict, Power]])

slots.encryption__cipher = Slot(uri=GX.cipher, name="encryption__cipher", curie=GX.curie('cipher'),
                   model_uri=GX.encryption__cipher, domain=None, range=Union[str, "EncryptionAlgorithm"])

slots.encryption__keyManagement = Slot(uri=GX.keyManagement, name="encryption__keyManagement", curie=GX.curie('keyManagement'),
                   model_uri=GX.encryption__keyManagement, domain=None, range=Union[str, "KeyManagement"])

slots.checkSum__checkSumCalculation = Slot(uri=GX.checkSumCalculation, name="checkSum__checkSumCalculation", curie=GX.curie('checkSumCalculation'),
                   model_uri=GX.checkSum__checkSumCalculation, domain=None, range=Union[str, "ChecksumAlgorithm"])

slots.checkSum__checkSumValue = Slot(uri=GX.checkSumValue, name="checkSum__checkSumValue", curie=GX.curie('checkSumValue'),
                   model_uri=GX.checkSum__checkSumValue, domain=None, range=str)

slots.signature__signatureValue = Slot(uri=GX.signatureValue, name="signature__signatureValue", curie=GX.curie('signatureValue'),
                   model_uri=GX.signature__signatureValue, domain=None, range=str)

slots.signature__hashAlgorithm = Slot(uri=GX.hashAlgorithm, name="signature__hashAlgorithm", curie=GX.curie('hashAlgorithm'),
                   model_uri=GX.signature__hashAlgorithm, domain=None, range=Union[str, "ChecksumAlgorithm"])

slots.signature__signatureAlgorithm = Slot(uri=GX.signatureAlgorithm, name="signature__signatureAlgorithm", curie=GX.curie('signatureAlgorithm'),
                   model_uri=GX.signature__signatureAlgorithm, domain=None, range=Union[str, "SignatureAlgorithm"])

slots.device__vendor = Slot(uri=GX.vendor, name="device__vendor", curie=GX.curie('vendor'),
                   model_uri=GX.device__vendor, domain=None, range=Optional[str])

slots.device__generation = Slot(uri=GX.generation, name="device__generation", curie=GX.curie('generation'),
                   model_uri=GX.device__generation, domain=None, range=Optional[str])

slots.device__defaultOversubscriptionRatio = Slot(uri=GX.defaultOversubscriptionRatio, name="device__defaultOversubscriptionRatio", curie=GX.curie('defaultOversubscriptionRatio'),
                   model_uri=GX.device__defaultOversubscriptionRatio, domain=None, range=Optional[int])

slots.device__supportedOversubscriptionRatio = Slot(uri=GX.supportedOversubscriptionRatio, name="device__supportedOversubscriptionRatio", curie=GX.curie('supportedOversubscriptionRatio'),
                   model_uri=GX.device__supportedOversubscriptionRatio, domain=None, range=Optional[int])

slots.disk__diskSize = Slot(uri=GX.diskSize, name="disk__diskSize", curie=GX.curie('diskSize'),
                   model_uri=GX.disk__diskSize, domain=None, range=Union[dict, MemorySize])

slots.disk__diskType = Slot(uri=GX.diskType, name="disk__diskType", curie=GX.curie('diskType'),
                   model_uri=GX.disk__diskType, domain=None, range=Optional[Union[str, "DiskType"]])

slots.disk__diskBusType = Slot(uri=GX.diskBusType, name="disk__diskBusType", curie=GX.curie('diskBusType'),
                   model_uri=GX.disk__diskBusType, domain=None, range=Optional[Union[str, "DiskBusType"]])

slots.endpoint__endpointURL = Slot(uri=GX.endpointURL, name="endpoint__endpointURL", curie=GX.curie('endpointURL'),
                   model_uri=GX.endpoint__endpointURL, domain=None, range=Optional[Union[str, URI]])

slots.endpoint__standardConformity = Slot(uri=GX.standardConformity, name="endpoint__standardConformity", curie=GX.curie('standardConformity'),
                   model_uri=GX.endpoint__standardConformity, domain=None, range=Union[Union[dict, StandardConformity], List[Union[dict, StandardConformity]]])

slots.endpoint__formalDescription = Slot(uri=GX.formalDescription, name="endpoint__formalDescription", curie=GX.curie('formalDescription'),
                   model_uri=GX.endpoint__formalDescription, domain=None, range=Optional[str])

slots.gPU__gpuMemory = Slot(uri=GX.gpuMemory, name="gPU__gpuMemory", curie=GX.curie('gpuMemory'),
                   model_uri=GX.gPU__gpuMemory, domain=None, range=Optional[Union[dict, MemorySize]])

slots.gPU__gpuInterconnection = Slot(uri=GX.gpuInterconnection, name="gPU__gpuInterconnection", curie=GX.curie('gpuInterconnection'),
                   model_uri=GX.gPU__gpuInterconnection, domain=None, range=Optional[Union[str, "GPUInterconnetionTypes"]])

slots.gPU__gpuProcessingUnits = Slot(uri=GX.gpuProcessingUnits, name="gPU__gpuProcessingUnits", curie=GX.curie('gpuProcessingUnits'),
                   model_uri=GX.gPU__gpuProcessingUnits, domain=None, range=Optional[int])

slots.gPU__gpuPassthrough = Slot(uri=GX.gpuPassthrough, name="gPU__gpuPassthrough", curie=GX.curie('gpuPassthrough'),
                   model_uri=GX.gPU__gpuPassthrough, domain=None, range=Optional[Union[bool, Bool]])

slots.image__fileSize = Slot(uri=GX.fileSize, name="image__fileSize", curie=GX.curie('fileSize'),
                   model_uri=GX.image__fileSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.image__operatingSystem = Slot(uri=GX.operatingSystem, name="image__operatingSystem", curie=GX.curie('operatingSystem'),
                   model_uri=GX.image__operatingSystem, domain=None, range=Optional[Union[dict, OperatingSystem]])

slots.image__cpuReq = Slot(uri=GX.cpuReq, name="image__cpuReq", curie=GX.curie('cpuReq'),
                   model_uri=GX.image__cpuReq, domain=None, range=Optional[Union[dict, CPU]])

slots.image__gpuReq = Slot(uri=GX.gpuReq, name="image__gpuReq", curie=GX.curie('gpuReq'),
                   model_uri=GX.image__gpuReq, domain=None, range=Optional[Union[dict, GPU]])

slots.image__ramReq = Slot(uri=GX.ramReq, name="image__ramReq", curie=GX.curie('ramReq'),
                   model_uri=GX.image__ramReq, domain=None, range=Optional[Union[dict, Memory]])

slots.image__videoRamSize = Slot(uri=GX.videoRamSize, name="image__videoRamSize", curie=GX.curie('videoRamSize'),
                   model_uri=GX.image__videoRamSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.image__rootDiskReq = Slot(uri=GX.rootDiskReq, name="image__rootDiskReq", curie=GX.curie('rootDiskReq'),
                   model_uri=GX.image__rootDiskReq, domain=None, range=Optional[Union[dict, Disk]])

slots.image__encryption = Slot(uri=GX.encryption, name="image__encryption", curie=GX.curie('encryption'),
                   model_uri=GX.image__encryption, domain=None, range=Optional[Union[dict, Encryption]])

slots.image__checkSum = Slot(uri=GX.checkSum, name="image__checkSum", curie=GX.curie('checkSum'),
                   model_uri=GX.image__checkSum, domain=None, range=Optional[Union[dict, CheckSum]])

slots.image__secureBoot = Slot(uri=GX.secureBoot, name="image__secureBoot", curie=GX.curie('secureBoot'),
                   model_uri=GX.image__secureBoot, domain=None, range=Optional[Union[bool, Bool]])

slots.image__vPMU = Slot(uri=GX.vPMU, name="image__vPMU", curie=GX.curie('vPMU'),
                   model_uri=GX.image__vPMU, domain=None, range=Optional[Union[bool, Bool]])

slots.image__multiQueues = Slot(uri=GX.multiQueues, name="image__multiQueues", curie=GX.curie('multiQueues'),
                   model_uri=GX.image__multiQueues, domain=None, range=Optional[Union[bool, Bool]])

slots.image__updateStrategy = Slot(uri=GX.updateStrategy, name="image__updateStrategy", curie=GX.curie('updateStrategy'),
                   model_uri=GX.image__updateStrategy, domain=None, range=Optional[Union[dict, UpdateStrategy]])

slots.image__licenseIncluded = Slot(uri=GX.licenseIncluded, name="image__licenseIncluded", curie=GX.curie('licenseIncluded'),
                   model_uri=GX.image__licenseIncluded, domain=None, range=Optional[Union[bool, Bool]])

slots.image__maintenance = Slot(uri=GX.maintenance, name="image__maintenance", curie=GX.curie('maintenance'),
                   model_uri=GX.image__maintenance, domain=None, range=Optional[Union[dict, MaintenanceSubscription]])

slots.maintenanceSubscription__subscriptionIncluded = Slot(uri=GX.subscriptionIncluded, name="maintenanceSubscription__subscriptionIncluded", curie=GX.curie('subscriptionIncluded'),
                   model_uri=GX.maintenanceSubscription__subscriptionIncluded, domain=None, range=Optional[Union[bool, Bool]])

slots.maintenanceSubscription__subscriptionRequired = Slot(uri=GX.subscriptionRequired, name="maintenanceSubscription__subscriptionRequired", curie=GX.curie('subscriptionRequired'),
                   model_uri=GX.maintenanceSubscription__subscriptionRequired, domain=None, range=Optional[Union[bool, Bool]])

slots.maintenanceSubscription__maintainedUntil = Slot(uri=GX.maintainedUntil, name="maintenanceSubscription__maintainedUntil", curie=GX.curie('maintainedUntil'),
                   model_uri=GX.maintenanceSubscription__maintainedUntil, domain=None, range=Optional[Union[str, XSDDate]])

slots.updateStrategy__replaceFrequency = Slot(uri=GX.replaceFrequency, name="updateStrategy__replaceFrequency", curie=GX.curie('replaceFrequency'),
                   model_uri=GX.updateStrategy__replaceFrequency, domain=None, range=Optional[Union[str, "UpdateFrequency"]])

slots.updateStrategy__hotfixHours = Slot(uri=GX.hotfixHours, name="updateStrategy__hotfixHours", curie=GX.curie('hotfixHours'),
                   model_uri=GX.updateStrategy__hotfixHours, domain=None, range=Optional[int])

slots.updateStrategy__oldVersionsValidUntil = Slot(uri=GX.oldVersionsValidUntil, name="updateStrategy__oldVersionsValidUntil", curie=GX.curie('oldVersionsValidUntil'),
                   model_uri=GX.updateStrategy__oldVersionsValidUntil, domain=None, range=Optional[str])

slots.updateStrategy__providedUntil = Slot(uri=GX.providedUntil, name="updateStrategy__providedUntil", curie=GX.curie('providedUntil'),
                   model_uri=GX.updateStrategy__providedUntil, domain=None, range=Optional[str])

slots.latestN__value = Slot(uri=GX.value, name="latestN__value", curie=GX.curie('value'),
                   model_uri=GX.latestN__value, domain=None, range=Optional[int])

slots.issuer__gaiaxTermsAndConditions = Slot(uri=GX.gaiaxTermsAndConditions, name="issuer__gaiaxTermsAndConditions", curie=GX.curie('gaiaxTermsAndConditions'),
                   model_uri=GX.issuer__gaiaxTermsAndConditions, domain=None, range=Union[str, "GaiaXTermsAndConditions"])

slots.legalPerson__registrationNumber = Slot(uri=GX.registrationNumber, name="legalPerson__registrationNumber", curie=GX.curie('registrationNumber'),
                   model_uri=GX.legalPerson__registrationNumber, domain=None, range=URIRef)

slots.legalPerson__legalAddress = Slot(uri=GX.legalAddress, name="legalPerson__legalAddress", curie=GX.curie('legalAddress'),
                   model_uri=GX.legalPerson__legalAddress, domain=None, range=Union[dict, Address])

slots.legalPerson__headquartersAddress = Slot(uri=GX.headquartersAddress, name="legalPerson__headquartersAddress", curie=GX.curie('headquartersAddress'),
                   model_uri=GX.legalPerson__headquartersAddress, domain=None, range=Union[dict, Address])

slots.legalPerson__parentOrganizationOf = Slot(uri=GX.parentOrganizationOf, name="legalPerson__parentOrganizationOf", curie=GX.curie('parentOrganizationOf'),
                   model_uri=GX.legalPerson__parentOrganizationOf, domain=None, range=Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]])

slots.legalPerson__subOrganisationOf = Slot(uri=GX.subOrganisationOf, name="legalPerson__subOrganisationOf", curie=GX.curie('subOrganisationOf'),
                   model_uri=GX.legalPerson__subOrganisationOf, domain=None, range=Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]])

slots.localRegistrationNumber__local = Slot(uri=GX.local, name="localRegistrationNumber__local", curie=GX.curie('local'),
                   model_uri=GX.localRegistrationNumber__local, domain=None, range=URIRef)

slots.vatID__vatID = Slot(uri=GX.vatID, name="vatID__vatID", curie=GX.curie('vatID'),
                   model_uri=GX.vatID__vatID, domain=None, range=URIRef)

slots.leiCode__leiCode = Slot(uri=SCHEMA.leiCode, name="leiCode__leiCode", curie=SCHEMA.curie('leiCode'),
                   model_uri=GX.leiCode__leiCode, domain=None, range=URIRef)

slots.eORI__eori = Slot(uri=GX.eori, name="eORI__eori", curie=GX.curie('eori'),
                   model_uri=GX.eORI__eori, domain=None, range=URIRef)

slots.eUID__euid = Slot(uri=GX.euid, name="eUID__euid", curie=GX.curie('euid'),
                   model_uri=GX.eUID__euid, domain=None, range=URIRef)

slots.memory__memorySize = Slot(uri=GX.memorySize, name="memory__memorySize", curie=GX.curie('memorySize'),
                   model_uri=GX.memory__memorySize, domain=None, range=Union[dict, MemorySize])

slots.memory__memoryClass = Slot(uri=GX.memoryClass, name="memory__memoryClass", curie=GX.curie('memoryClass'),
                   model_uri=GX.memory__memoryClass, domain=None, range=Optional[Union[str, "MemoryClasses"]])

slots.memory__memoryRank = Slot(uri=GX.memoryRank, name="memory__memoryRank", curie=GX.curie('memoryRank'),
                   model_uri=GX.memory__memoryRank, domain=None, range=Optional[Union[str, "MemoryRanks"]])

slots.memory__eccEnabled = Slot(uri=GX.eccEnabled, name="memory__eccEnabled", curie=GX.curie('eccEnabled'),
                   model_uri=GX.memory__eccEnabled, domain=None, range=Optional[Union[bool, Bool]])

slots.memory__hardwareEncryption = Slot(uri=GX.hardwareEncryption, name="memory__hardwareEncryption", curie=GX.curie('hardwareEncryption'),
                   model_uri=GX.memory__hardwareEncryption, domain=None, range=Optional[Union[bool, Bool]])

slots.floatPercentage__value = Slot(uri=GX.value, name="floatPercentage__value", curie=GX.curie('value'),
                   model_uri=GX.floatPercentage__value, domain=None, range=Optional[float])

slots.pXEImage__pxeImageDiskFormat = Slot(uri=GX.pxeImageDiskFormat, name="pXEImage__pxeImageDiskFormat", curie=GX.curie('pxeImageDiskFormat'),
                   model_uri=GX.pXEImage__pxeImageDiskFormat, domain=None, range=Optional[Union[str, "PXEDiskType"]])

slots.resource__aggregationOfResources = Slot(uri=GX.aggregationOfResources, name="resource__aggregationOfResources", curie=GX.curie('aggregationOfResources'),
                   model_uri=GX.resource__aggregationOfResources, domain=None, range=Optional[Union[str, List[str]]])

slots.virtualResource__copyrightOwnedBy = Slot(uri=GX.copyrightOwnedBy, name="virtualResource__copyrightOwnedBy", curie=GX.curie('copyrightOwnedBy'),
                   model_uri=GX.virtualResource__copyrightOwnedBy, domain=None, range=Union[str, List[str]])

slots.virtualResource__license = Slot(uri=GX.license, name="virtualResource__license", curie=GX.curie('license'),
                   model_uri=GX.virtualResource__license, domain=None, range=Union[str, List[str]])

slots.virtualResource__resourcePolicy = Slot(uri=GX.resourcePolicy, name="virtualResource__resourcePolicy", curie=GX.curie('resourcePolicy'),
                   model_uri=GX.virtualResource__resourcePolicy, domain=None, range=Union[str, List[str]])

slots.physicalResource__maintainedBy = Slot(uri=GX.maintainedBy, name="physicalResource__maintainedBy", curie=GX.curie('maintainedBy'),
                   model_uri=GX.physicalResource__maintainedBy, domain=None, range=Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]])

slots.physicalResource__ownedBy = Slot(uri=GX.ownedBy, name="physicalResource__ownedBy", curie=GX.curie('ownedBy'),
                   model_uri=GX.physicalResource__ownedBy, domain=None, range=Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]])

slots.physicalResource__manufacturedBy = Slot(uri=GX.manufacturedBy, name="physicalResource__manufacturedBy", curie=GX.curie('manufacturedBy'),
                   model_uri=GX.physicalResource__manufacturedBy, domain=None, range=Optional[Union[Union[str, LegalPersonRegistrationNumber], List[Union[str, LegalPersonRegistrationNumber]]]])

slots.physicalResource__location = Slot(uri=GX.location, name="physicalResource__location", curie=GX.curie('location'),
                   model_uri=GX.physicalResource__location, domain=None, range=Union[Union[dict, Address], List[Union[dict, Address]]])

slots.softwareResource__checksum = Slot(uri=GX.checksum, name="softwareResource__checksum", curie=GX.curie('checksum'),
                   model_uri=GX.softwareResource__checksum, domain=None, range=Optional[Union[dict, CheckSum]])

slots.softwareResource__signature = Slot(uri=GX.signature, name="softwareResource__signature", curie=GX.curie('signature'),
                   model_uri=GX.softwareResource__signature, domain=None, range=Optional[Union[dict, Signature]])

slots.softwareResource__version = Slot(uri=GX.version, name="softwareResource__version", curie=GX.curie('version'),
                   model_uri=GX.softwareResource__version, domain=None, range=Optional[str])

slots.softwareResource__patchLevel = Slot(uri=GX.patchLevel, name="softwareResource__patchLevel", curie=GX.curie('patchLevel'),
                   model_uri=GX.softwareResource__patchLevel, domain=None, range=Optional[str])

slots.softwareResource__buildDate = Slot(uri=GX.buildDate, name="softwareResource__buildDate", curie=GX.curie('buildDate'),
                   model_uri=GX.softwareResource__buildDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.operatingSystem__osDistribution = Slot(uri=GX.osDistribution, name="operatingSystem__osDistribution", curie=GX.curie('osDistribution'),
                   model_uri=GX.operatingSystem__osDistribution, domain=None, range=Union[str, "OSDistribution"])

slots.hypervisor__hypervisorType = Slot(uri=GX.hypervisorType, name="hypervisor__hypervisorType", curie=GX.curie('hypervisorType'),
                   model_uri=GX.hypervisor__hypervisorType, domain=None, range=Union[str, "HypervisorType"])

slots.serviceOffering__providedBy = Slot(uri=GX.providedBy, name="serviceOffering__providedBy", curie=GX.curie('providedBy'),
                   model_uri=GX.serviceOffering__providedBy, domain=None, range=Union[str, LegalPersonRegistrationNumber])

slots.serviceOffering__dependsOn = Slot(uri=GX.dependsOn, name="serviceOffering__dependsOn", curie=GX.curie('dependsOn'),
                   model_uri=GX.serviceOffering__dependsOn, domain=None, range=Optional[Union[str, List[str]]])

slots.serviceOffering__aggregationOfResources = Slot(uri=GX.aggregationOfResources, name="serviceOffering__aggregationOfResources", curie=GX.curie('aggregationOfResources'),
                   model_uri=GX.serviceOffering__aggregationOfResources, domain=None, range=Optional[Union[str, List[str]]])

slots.serviceOffering__serviceOfferingTermsAndConditions = Slot(uri=GX.serviceOfferingTermsAndConditions, name="serviceOffering__serviceOfferingTermsAndConditions", curie=GX.curie('serviceOfferingTermsAndConditions'),
                   model_uri=GX.serviceOffering__serviceOfferingTermsAndConditions, domain=None, range=Union[Union[dict, TermsAndConditions], List[Union[dict, TermsAndConditions]]])

slots.serviceOffering__servicePolicy = Slot(uri=GX.servicePolicy, name="serviceOffering__servicePolicy", curie=GX.curie('servicePolicy'),
                   model_uri=GX.serviceOffering__servicePolicy, domain=None, range=Union[str, List[str]])

slots.serviceOffering__dataProtectionRegime = Slot(uri=GX.dataProtectionRegime, name="serviceOffering__dataProtectionRegime", curie=GX.curie('dataProtectionRegime'),
                   model_uri=GX.serviceOffering__dataProtectionRegime, domain=None, range=Optional[Union[Union[str, "PersonalDataProtectionRegime"], List[Union[str, "PersonalDataProtectionRegime"]]]])

slots.serviceOffering__dataAccountExport = Slot(uri=GX.dataAccountExport, name="serviceOffering__dataAccountExport", curie=GX.curie('dataAccountExport'),
                   model_uri=GX.serviceOffering__dataAccountExport, domain=None, range=Union[Union[dict, DataAccountExport], List[Union[dict, DataAccountExport]]])

slots.serviceOffering__keyword = Slot(uri=GX.keyword, name="serviceOffering__keyword", curie=GX.curie('keyword'),
                   model_uri=GX.serviceOffering__keyword, domain=None, range=Optional[Union[str, List[str]]])

slots.serviceOffering__provisionType = Slot(uri=GX.provisionType, name="serviceOffering__provisionType", curie=GX.curie('provisionType'),
                   model_uri=GX.serviceOffering__provisionType, domain=None, range=Optional[Union[str, "ProvisionTypes"]])

slots.serviceOffering__endpoint = Slot(uri=GX.endpoint, name="serviceOffering__endpoint", curie=GX.curie('endpoint'),
                   model_uri=GX.serviceOffering__endpoint, domain=None, range=Optional[Union[dict, Endpoint]])

slots.serviceOffering__hostedOn = Slot(uri=GX.hostedOn, name="serviceOffering__hostedOn", curie=GX.curie('hostedOn'),
                   model_uri=GX.serviceOffering__hostedOn, domain=None, range=Optional[Union[str, List[str]]])

slots.computeServiceOffering__tenantSeparation = Slot(uri=GX.tenantSeparation, name="computeServiceOffering__tenantSeparation", curie=GX.curie('tenantSeparation'),
                   model_uri=GX.computeServiceOffering__tenantSeparation, domain=None, range=Optional[Union[str, "TenantSeparation"]])

slots.virtualMachineServiceOffering__codeArtifact = Slot(uri=GX.codeArtifact, name="virtualMachineServiceOffering__codeArtifact", curie=GX.curie('codeArtifact'),
                   model_uri=GX.virtualMachineServiceOffering__codeArtifact, domain=None, range=Union[Union[dict, VMImage], List[Union[dict, VMImage]]])

slots.virtualMachineServiceOffering__instantiationReq = Slot(uri=GX.instantiationReq, name="virtualMachineServiceOffering__instantiationReq", curie=GX.curie('instantiationReq'),
                   model_uri=GX.virtualMachineServiceOffering__instantiationReq, domain=None, range=Union[Union[dict, ServerFlavor], List[Union[dict, ServerFlavor]]])

slots.containerServiceOffering__codeArtifact = Slot(uri=GX.codeArtifact, name="containerServiceOffering__codeArtifact", curie=GX.curie('codeArtifact'),
                   model_uri=GX.containerServiceOffering__codeArtifact, domain=None, range=Union[Union[dict, ContainerImage], List[Union[dict, ContainerImage]]])

slots.containerServiceOffering__instantiationReq = Slot(uri=GX.instantiationReq, name="containerServiceOffering__instantiationReq", curie=GX.curie('instantiationReq'),
                   model_uri=GX.containerServiceOffering__instantiationReq, domain=None, range=Union[Union[dict, ContainerResourceLimits], List[Union[dict, ContainerResourceLimits]]])

slots.bareMetalServiceOffering__codeArtifact = Slot(uri=GX.codeArtifact, name="bareMetalServiceOffering__codeArtifact", curie=GX.curie('codeArtifact'),
                   model_uri=GX.bareMetalServiceOffering__codeArtifact, domain=None, range=Union[Union[dict, PXEImage], List[Union[dict, PXEImage]]])

slots.bareMetalServiceOffering__instantiationReq = Slot(uri=GX.instantiationReq, name="bareMetalServiceOffering__instantiationReq", curie=GX.curie('instantiationReq'),
                   model_uri=GX.bareMetalServiceOffering__instantiationReq, domain=None, range=Union[Union[dict, ServerFlavor], List[Union[dict, ServerFlavor]]])

slots.termsAndConditions__url = Slot(uri=GX.url, name="termsAndConditions__url", curie=GX.curie('url'),
                   model_uri=GX.termsAndConditions__url, domain=None, range=Union[str, URI])

slots.termsAndConditions__hash = Slot(uri=GX.hash, name="termsAndConditions__hash", curie=GX.curie('hash'),
                   model_uri=GX.termsAndConditions__hash, domain=None, range=str)

slots.dataAccountExport__requestType = Slot(uri=GX.requestType, name="dataAccountExport__requestType", curie=GX.curie('requestType'),
                   model_uri=GX.dataAccountExport__requestType, domain=None, range=Union[str, "RequestTypes"])

slots.dataAccountExport__accessType = Slot(uri=GX.accessType, name="dataAccountExport__accessType", curie=GX.curie('accessType'),
                   model_uri=GX.dataAccountExport__accessType, domain=None, range=Union[str, "AccessTypes"])

slots.dataAccountExport__formatType = Slot(uri=GX.formatType, name="dataAccountExport__formatType", curie=GX.curie('formatType'),
                   model_uri=GX.dataAccountExport__formatType, domain=None, range=Union[str, "MIMETypes"])

slots.standardConformity__title = Slot(uri=GX.title, name="standardConformity__title", curie=GX.curie('title'),
                   model_uri=GX.standardConformity__title, domain=None, range=str)

slots.standardConformity__standardReference = Slot(uri=GX.standardReference, name="standardConformity__standardReference", curie=GX.curie('standardReference'),
                   model_uri=GX.standardConformity__standardReference, domain=None, range=Union[str, URI])

slots.standardConformity__publisher = Slot(uri=GX.publisher, name="standardConformity__publisher", curie=GX.curie('publisher'),
                   model_uri=GX.standardConformity__publisher, domain=None, range=Optional[str])

slots.dataResource__producedBy = Slot(uri=GX.producedBy, name="dataResource__producedBy", curie=GX.curie('producedBy'),
                   model_uri=GX.dataResource__producedBy, domain=None, range=Union[str, LegalPersonRegistrationNumber])

slots.dataResource__exposedThrough = Slot(uri=GX.exposedThrough, name="dataResource__exposedThrough", curie=GX.curie('exposedThrough'),
                   model_uri=GX.dataResource__exposedThrough, domain=None, range=Union[Union[dict, DataExchangeComponent], List[Union[dict, DataExchangeComponent]]])

slots.dataResource__obsoleteDateTime = Slot(uri=GX.obsoleteDateTime, name="dataResource__obsoleteDateTime", curie=GX.curie('obsoleteDateTime'),
                   model_uri=GX.dataResource__obsoleteDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dataResource__expirationDateTime = Slot(uri=GX.expirationDateTime, name="dataResource__expirationDateTime", curie=GX.curie('expirationDateTime'),
                   model_uri=GX.dataResource__expirationDateTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dataResource__containsPII = Slot(uri=GX.containsPII, name="dataResource__containsPII", curie=GX.curie('containsPII'),
                   model_uri=GX.dataResource__containsPII, domain=None, range=Union[bool, Bool])

slots.dataResource__dataController = Slot(uri=GX.dataController, name="dataResource__dataController", curie=GX.curie('dataController'),
                   model_uri=GX.dataResource__dataController, domain=None, range=Optional[Union[Union[dict, Participant], List[Union[dict, Participant]]]])

slots.dataResource__consent = Slot(uri=GX.consent, name="dataResource__consent", curie=GX.curie('consent'),
                   model_uri=GX.dataResource__consent, domain=None, range=Optional[Union[Union[dict, Consent], List[Union[dict, Consent]]]])

slots.consent__legalBasis = Slot(uri=GX.legalBasis, name="consent__legalBasis", curie=GX.curie('legalBasis'),
                   model_uri=GX.consent__legalBasis, domain=None, range=str)

slots.consent__dataProtectionContactPoint = Slot(uri=GX.dataProtectionContactPoint, name="consent__dataProtectionContactPoint", curie=GX.curie('dataProtectionContactPoint'),
                   model_uri=GX.consent__dataProtectionContactPoint, domain=None, range=Union[str, List[str]])

slots.consent__purpose = Slot(uri=GX.purpose, name="consent__purpose", curie=GX.curie('purpose'),
                   model_uri=GX.consent__purpose, domain=None, range=Union[str, List[str]])

slots.consent__consentWithdrawalContactPoint = Slot(uri=GX.consentWithdrawalContactPoint, name="consent__consentWithdrawalContactPoint", curie=GX.curie('consentWithdrawalContactPoint'),
                   model_uri=GX.consent__consentWithdrawalContactPoint, domain=None, range=Union[str, List[str]])

slots.datacenter__aggregationOfResources = Slot(uri=GX.aggregationOfResources, name="datacenter__aggregationOfResources", curie=GX.curie('aggregationOfResources'),
                   model_uri=GX.datacenter__aggregationOfResources, domain=None, range=Union[Union[dict, AvailabilityZone], List[Union[dict, AvailabilityZone]]])

slots.region__aggregationOfResources = Slot(uri=GX.aggregationOfResources, name="region__aggregationOfResources", curie=GX.curie('aggregationOfResources'),
                   model_uri=GX.region__aggregationOfResources, domain=None, range=Union[Union[dict, Datacenter], List[Union[dict, Datacenter]]])

slots.containerImage__baseContainerImage = Slot(uri=GX.baseContainerImage, name="containerImage__baseContainerImage", curie=GX.curie('baseContainerImage'),
                   model_uri=GX.containerImage__baseContainerImage, domain=None, range=Union[dict, BaseContainerImage])

slots.containerImage__containerFormat = Slot(uri=GX.containerFormat, name="containerImage__containerFormat", curie=GX.curie('containerFormat'),
                   model_uri=GX.containerImage__containerFormat, domain=None, range=Union[str, "ContainerFormat"])

slots.baseContainerImage__containerImageTag = Slot(uri=GX.containerImageTag, name="baseContainerImage__containerImageTag", curie=GX.curie('containerImageTag'),
                   model_uri=GX.baseContainerImage__containerImageTag, domain=None, range=Optional[Union[str, List[str]]])

slots.baseContainerImage__containerImageLink = Slot(uri=GX.containerImageLink, name="baseContainerImage__containerImageLink", curie=GX.curie('containerImageLink'),
                   model_uri=GX.baseContainerImage__containerImageLink, domain=None, range=Union[str, URI])

slots.containerResourceLimits__cpuRequirements = Slot(uri=GX.cpuRequirements, name="containerResourceLimits__cpuRequirements", curie=GX.curie('cpuRequirements'),
                   model_uri=GX.containerResourceLimits__cpuRequirements, domain=None, range=Optional[Union[dict, CPU]])

slots.containerResourceLimits__numberOfCoresLimit = Slot(uri=GX.numberOfCoresLimit, name="containerResourceLimits__numberOfCoresLimit", curie=GX.curie('numberOfCoresLimit'),
                   model_uri=GX.containerResourceLimits__numberOfCoresLimit, domain=None, range=Optional[int])

slots.containerResourceLimits__memoryRequirements = Slot(uri=GX.memoryRequirements, name="containerResourceLimits__memoryRequirements", curie=GX.curie('memoryRequirements'),
                   model_uri=GX.containerResourceLimits__memoryRequirements, domain=None, range=Optional[Union[dict, Memory]])

slots.containerResourceLimits__memoryLimit = Slot(uri=GX.memoryLimit, name="containerResourceLimits__memoryLimit", curie=GX.curie('memoryLimit'),
                   model_uri=GX.containerResourceLimits__memoryLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.containerResourceLimits__gpuRequirements = Slot(uri=GX.gpuRequirements, name="containerResourceLimits__gpuRequirements", curie=GX.curie('gpuRequirements'),
                   model_uri=GX.containerResourceLimits__gpuRequirements, domain=None, range=Optional[Union[dict, GPU]])

slots.containerResourceLimits__gpuLimit = Slot(uri=GX.gpuLimit, name="containerResourceLimits__gpuLimit", curie=GX.curie('gpuLimit'),
                   model_uri=GX.containerResourceLimits__gpuLimit, domain=None, range=Optional[int])

slots.containerResourceLimits__confidential = Slot(uri=GX.confidential, name="containerResourceLimits__confidential", curie=GX.curie('confidential'),
                   model_uri=GX.containerResourceLimits__confidential, domain=None, range=Union[bool, Bool])

slots.containerResourceLimits__confidentialComputingTechnology = Slot(uri=GX.confidentialComputingTechnology, name="containerResourceLimits__confidentialComputingTechnology", curie=GX.curie('confidentialComputingTechnology'),
                   model_uri=GX.containerResourceLimits__confidentialComputingTechnology, domain=None, range=Optional[Union[dict, ConfidentialComputing]])

slots.dataProtectionPolicy__protectionFrequency = Slot(uri=GX.protectionFrequency, name="dataProtectionPolicy__protectionFrequency", curie=GX.curie('protectionFrequency'),
                   model_uri=GX.dataProtectionPolicy__protectionFrequency, domain=None, range=Union[str, "ProtectionFrequency"])

slots.dataProtectionPolicy__protectionRetention = Slot(uri=GX.protectionRetention, name="dataProtectionPolicy__protectionRetention", curie=GX.curie('protectionRetention'),
                   model_uri=GX.dataProtectionPolicy__protectionRetention, domain=None, range=Union[dict, RetentionDuration])

slots.dataProtectionPolicy__protectionMethod = Slot(uri=GX.protectionMethod, name="dataProtectionPolicy__protectionMethod", curie=GX.curie('protectionMethod'),
                   model_uri=GX.dataProtectionPolicy__protectionMethod, domain=None, range=Optional[Union[str, "ProtectionMethod"]])

slots.backupPolicy__backupLocation = Slot(uri=GX.backupLocation, name="backupPolicy__backupLocation", curie=GX.curie('backupLocation'),
                   model_uri=GX.backupPolicy__backupLocation, domain=None, range=Union[Union[dict, Resource], List[Union[dict, Resource]]])

slots.backupPolicy__backupReplication = Slot(uri=GX.backupReplication, name="backupPolicy__backupReplication", curie=GX.curie('backupReplication'),
                   model_uri=GX.backupPolicy__backupReplication, domain=None, range=Optional[Union[Union[dict, ReplicationPolicy], List[Union[dict, ReplicationPolicy]]]])

slots.snapshotPolicy__snapshotReplication = Slot(uri=GX.snapshotReplication, name="snapshotPolicy__snapshotReplication", curie=GX.curie('snapshotReplication'),
                   model_uri=GX.snapshotPolicy__snapshotReplication, domain=None, range=Optional[Union[Union[dict, ReplicationPolicy], List[Union[dict, ReplicationPolicy]]]])

slots.replicationPolicy__synchronousReplication = Slot(uri=GX.synchronousReplication, name="replicationPolicy__synchronousReplication", curie=GX.curie('synchronousReplication'),
                   model_uri=GX.replicationPolicy__synchronousReplication, domain=None, range=Optional[Union[bool, Bool]])

slots.replicationPolicy__consistencyType = Slot(uri=GX.consistencyType, name="replicationPolicy__consistencyType", curie=GX.curie('consistencyType'),
                   model_uri=GX.replicationPolicy__consistencyType, domain=None, range=Optional[Union[str, "ConsistencyType"]])

slots.replicationPolicy__replicaNumber = Slot(uri=GX.replicaNumber, name="replicationPolicy__replicaNumber", curie=GX.curie('replicaNumber'),
                   model_uri=GX.replicationPolicy__replicaNumber, domain=None, range=Optional[Union[int, List[int]]])

slots.replicationPolicy__geoReplication = Slot(uri=GX.geoReplication, name="replicationPolicy__geoReplication", curie=GX.curie('geoReplication'),
                   model_uri=GX.replicationPolicy__geoReplication, domain=None, range=Optional[Union[Union[str, "GeoReplicationScope"], List[Union[str, "GeoReplicationScope"]]]])

slots.qoSMetric__metric = Slot(uri=GX.metric, name="qoSMetric__metric", curie=GX.curie('metric'),
                   model_uri=GX.qoSMetric__metric, domain=None, range=Union[dict, Quantity])

slots.qoSMetric__guaranteed = Slot(uri=GX.guaranteed, name="qoSMetric__guaranteed", curie=GX.curie('guaranteed'),
                   model_uri=GX.qoSMetric__guaranteed, domain=None, range=Optional[Union[dict, FloatPercentage]])

slots.bandWidth__metric = Slot(uri=GX.metric, name="bandWidth__metric", curie=GX.curie('metric'),
                   model_uri=GX.bandWidth__metric, domain=None, range=Union[dict, DataRate])

slots.roundTripTime__metric = Slot(uri=GX.metric, name="roundTripTime__metric", curie=GX.curie('metric'),
                   model_uri=GX.roundTripTime__metric, domain=None, range=Union[dict, Time])

slots.availability__metric = Slot(uri=GX.metric, name="availability__metric", curie=GX.curie('metric'),
                   model_uri=GX.availability__metric, domain=None, range=Union[dict, Time])

slots.packetLoss__metric = Slot(uri=GX.metric, name="packetLoss__metric", curie=GX.curie('metric'),
                   model_uri=GX.packetLoss__metric, domain=None, range=Union[dict, FloatPercentage])

slots.jitter__metric = Slot(uri=GX.metric, name="jitter__metric", curie=GX.curie('metric'),
                   model_uri=GX.jitter__metric, domain=None, range=Union[dict, Time])

slots.latency__metric = Slot(uri=GX.metric, name="latency__metric", curie=GX.curie('metric'),
                   model_uri=GX.latency__metric, domain=None, range=Union[dict, Time])

slots.targetPercentile__metric = Slot(uri=GX.metric, name="targetPercentile__metric", curie=GX.curie('metric'),
                   model_uri=GX.targetPercentile__metric, domain=None, range=Union[dict, FloatPercentage])

slots.throughput__metric = Slot(uri=GX.metric, name="throughput__metric", curie=GX.curie('metric'),
                   model_uri=GX.throughput__metric, domain=None, range=Union[dict, DataRate])

slots.iOPS__metric = Slot(uri=GX.metric, name="iOPS__metric", curie=GX.curie('metric'),
                   model_uri=GX.iOPS__metric, domain=None, range=Union[dict, DataRate])

slots.qoS__throughput = Slot(uri=GX.throughput, name="qoS__throughput", curie=GX.curie('throughput'),
                   model_uri=GX.qoS__throughput, domain=None, range=Optional[Union[dict, Throughput]])

slots.qoS__iops = Slot(uri=GX.iops, name="qoS__iops", curie=GX.curie('iops'),
                   model_uri=GX.qoS__iops, domain=None, range=Optional[Union[dict, IOPS]])

slots.qoS__bandWidth = Slot(uri=GX.bandWidth, name="qoS__bandWidth", curie=GX.curie('bandWidth'),
                   model_uri=GX.qoS__bandWidth, domain=None, range=Optional[Union[dict, BandWidth]])

slots.qoS__roundTripTime = Slot(uri=GX.roundTripTime, name="qoS__roundTripTime", curie=GX.curie('roundTripTime'),
                   model_uri=GX.qoS__roundTripTime, domain=None, range=Optional[Union[dict, RoundTripTime]])

slots.qoS__availability = Slot(uri=GX.availability, name="qoS__availability", curie=GX.curie('availability'),
                   model_uri=GX.qoS__availability, domain=None, range=Optional[Union[dict, Availability]])

slots.qoS__packetLoss = Slot(uri=GX.packetLoss, name="qoS__packetLoss", curie=GX.curie('packetLoss'),
                   model_uri=GX.qoS__packetLoss, domain=None, range=Optional[Union[dict, PacketLoss]])

slots.qoS__jitter = Slot(uri=GX.jitter, name="qoS__jitter", curie=GX.curie('jitter'),
                   model_uri=GX.qoS__jitter, domain=None, range=Optional[Union[dict, Jitter]])

slots.qoS__latency = Slot(uri=GX.latency, name="qoS__latency", curie=GX.curie('latency'),
                   model_uri=GX.qoS__latency, domain=None, range=Optional[Union[dict, Latency]])

slots.qoS__targetPercentile = Slot(uri=GX.targetPercentile, name="qoS__targetPercentile", curie=GX.curie('targetPercentile'),
                   model_uri=GX.qoS__targetPercentile, domain=None, range=Optional[Union[dict, TargetPercentile]])

slots.storageConfiguration__storageCompression = Slot(uri=GX.storageCompression, name="storageConfiguration__storageCompression", curie=GX.curie('storageCompression'),
                   model_uri=GX.storageConfiguration__storageCompression, domain=None, range=Optional[Union[Union[str, "CompressionAlgorithm"], List[Union[str, "CompressionAlgorithm"]]]])

slots.storageConfiguration__storageDeduplication = Slot(uri=GX.storageDeduplication, name="storageConfiguration__storageDeduplication", curie=GX.curie('storageDeduplication'),
                   model_uri=GX.storageConfiguration__storageDeduplication, domain=None, range=Optional[Union[Union[str, "DeduplicationMethod"], List[Union[str, "DeduplicationMethod"]]]])

slots.storageConfiguration__storageEncryption = Slot(uri=GX.storageEncryption, name="storageConfiguration__storageEncryption", curie=GX.curie('storageEncryption'),
                   model_uri=GX.storageConfiguration__storageEncryption, domain=None, range=Union[Union[dict, Encryption], List[Union[dict, Encryption]]])

slots.storageConfiguration__storageRedundancyMechanism = Slot(uri=GX.storageRedundancyMechanism, name="storageConfiguration__storageRedundancyMechanism", curie=GX.curie('storageRedundancyMechanism'),
                   model_uri=GX.storageConfiguration__storageRedundancyMechanism, domain=None, range=Optional[Union[Union[str, "StorageRedundancyMechanism"], List[Union[str, "StorageRedundancyMechanism"]]]])

slots.storageConfiguration__storageProtection = Slot(uri=GX.storageProtection, name="storageConfiguration__storageProtection", curie=GX.curie('storageProtection'),
                   model_uri=GX.storageConfiguration__storageProtection, domain=None, range=Optional[Union[Union[dict, DataProtectionPolicy], List[Union[dict, DataProtectionPolicy]]]])

slots.storageConfiguration__storageQoS = Slot(uri=GX.storageQoS, name="storageConfiguration__storageQoS", curie=GX.curie('storageQoS'),
                   model_uri=GX.storageConfiguration__storageQoS, domain=None, range=Optional[Union[Union[dict, QoS], List[Union[dict, QoS]]]])

slots.storageConfiguration__blockSize = Slot(uri=GX.blockSize, name="storageConfiguration__blockSize", curie=GX.curie('blockSize'),
                   model_uri=GX.storageConfiguration__blockSize, domain=None, range=Optional[Union[Union[dict, MemorySize], List[Union[dict, MemorySize]]]])

slots.fileStorageConfiguration__fileSystemType = Slot(uri=GX.fileSystemType, name="fileStorageConfiguration__fileSystemType", curie=GX.curie('fileSystemType'),
                   model_uri=GX.fileStorageConfiguration__fileSystemType, domain=None, range=Optional[Union[Union[str, "FileSystemType"], List[Union[str, "FileSystemType"]]]])

slots.fileStorageConfiguration__highLevelAccessProtocol = Slot(uri=GX.highLevelAccessProtocol, name="fileStorageConfiguration__highLevelAccessProtocol", curie=GX.curie('highLevelAccessProtocol'),
                   model_uri=GX.fileStorageConfiguration__highLevelAccessProtocol, domain=None, range=Optional[Union[Union[str, "FileAccessProtocol"], List[Union[str, "FileAccessProtocol"]]]])

slots.blockStorageConfiguration__blockStorageTechnology = Slot(uri=GX.blockStorageTechnology, name="blockStorageConfiguration__blockStorageTechnology", curie=GX.curie('blockStorageTechnology'),
                   model_uri=GX.blockStorageConfiguration__blockStorageTechnology, domain=None, range=Optional[Union[Union[str, "BlockStorageTechnology"], List[Union[str, "BlockStorageTechnology"]]]])

slots.blockStorageConfiguration__lowLevelBlockAccessProtocol = Slot(uri=GX.lowLevelBlockAccessProtocol, name="blockStorageConfiguration__lowLevelBlockAccessProtocol", curie=GX.curie('lowLevelBlockAccessProtocol'),
                   model_uri=GX.blockStorageConfiguration__lowLevelBlockAccessProtocol, domain=None, range=Optional[Union[Union[str, "BlockAccessProtocol"], List[Union[str, "BlockAccessProtocol"]]]])

slots.storageServiceOffering__minimumSize = Slot(uri=GX.minimumSize, name="storageServiceOffering__minimumSize", curie=GX.curie('minimumSize'),
                   model_uri=GX.storageServiceOffering__minimumSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.storageServiceOffering__maximumSize = Slot(uri=GX.maximumSize, name="storageServiceOffering__maximumSize", curie=GX.curie('maximumSize'),
                   model_uri=GX.storageServiceOffering__maximumSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.storageServiceOffering__storageConfiguration = Slot(uri=GX.storageConfiguration, name="storageServiceOffering__storageConfiguration", curie=GX.curie('storageConfiguration'),
                   model_uri=GX.storageServiceOffering__storageConfiguration, domain=None, range=Union[dict, StorageConfiguration])

slots.storageServiceOffering__lifetimeManagement = Slot(uri=GX.lifetimeManagement, name="storageServiceOffering__lifetimeManagement", curie=GX.curie('lifetimeManagement'),
                   model_uri=GX.storageServiceOffering__lifetimeManagement, domain=None, range=Optional[int])

slots.storageServiceOffering__versioning = Slot(uri=GX.versioning, name="storageServiceOffering__versioning", curie=GX.curie('versioning'),
                   model_uri=GX.storageServiceOffering__versioning, domain=None, range=Optional[Union[bool, Bool]])

slots.storageServiceOffering__storageConsistency = Slot(uri=GX.storageConsistency, name="storageServiceOffering__storageConsistency", curie=GX.curie('storageConsistency'),
                   model_uri=GX.storageServiceOffering__storageConsistency, domain=None, range=Optional[Union[str, "ConsistencyType"]])

slots.storageServiceOffering__dataViews = Slot(uri=GX.dataViews, name="storageServiceOffering__dataViews", curie=GX.curie('dataViews'),
                   model_uri=GX.storageServiceOffering__dataViews, domain=None, range=Optional[Union[bool, Bool]])

slots.storageServiceOffering__multipleViews = Slot(uri=GX.multipleViews, name="storageServiceOffering__multipleViews", curie=GX.curie('multipleViews'),
                   model_uri=GX.storageServiceOffering__multipleViews, domain=None, range=Optional[Union[bool, Bool]])

slots.fileStorageServiceOffering__storageConfiguration = Slot(uri=GX.storageConfiguration, name="fileStorageServiceOffering__storageConfiguration", curie=GX.curie('storageConfiguration'),
                   model_uri=GX.fileStorageServiceOffering__storageConfiguration, domain=None, range=Union[dict, FileStorageConfiguration])

slots.fileStorageServiceOffering__accessSemantics = Slot(uri=GX.accessSemantics, name="fileStorageServiceOffering__accessSemantics", curie=GX.curie('accessSemantics'),
                   model_uri=GX.fileStorageServiceOffering__accessSemantics, domain=None, range=Optional[Union[bool, Bool]])

slots.fileStorageServiceOffering__accessAttributes = Slot(uri=GX.accessAttributes, name="fileStorageServiceOffering__accessAttributes", curie=GX.curie('accessAttributes'),
                   model_uri=GX.fileStorageServiceOffering__accessAttributes, domain=None, range=Optional[Union[Union[str, "AccessAttribute"], List[Union[str, "AccessAttribute"]]]])

slots.blockStorageServiceOffering__storageConfiguration = Slot(uri=GX.storageConfiguration, name="blockStorageServiceOffering__storageConfiguration", curie=GX.curie('storageConfiguration'),
                   model_uri=GX.blockStorageServiceOffering__storageConfiguration, domain=None, range=Union[dict, BlockStorageConfiguration])

slots.objectStorageServiceOffering__accessAttributes = Slot(uri=GX.accessAttributes, name="objectStorageServiceOffering__accessAttributes", curie=GX.curie('accessAttributes'),
                   model_uri=GX.objectStorageServiceOffering__accessAttributes, domain=None, range=Optional[Union[Union[str, "AccessAttribute"], List[Union[str, "AccessAttribute"]]]])

slots.objectStorageServiceOffering__maximumObjectSize = Slot(uri=GX.maximumObjectSize, name="objectStorageServiceOffering__maximumObjectSize", curie=GX.curie('maximumObjectSize'),
                   model_uri=GX.objectStorageServiceOffering__maximumObjectSize, domain=None, range=Optional[Union[dict, MemorySize]])

slots.objectStorageServiceOffering__objectAPICompatibility = Slot(uri=GX.objectAPICompatibility, name="objectStorageServiceOffering__objectAPICompatibility", curie=GX.curie('objectAPICompatibility'),
                   model_uri=GX.objectStorageServiceOffering__objectAPICompatibility, domain=None, range=Optional[Union[Union[str, "StorageAPI"], List[Union[str, "StorageAPI"]]]])

slots.connectivityServiceOffering__connectivityConfiguration = Slot(uri=GX.connectivityConfiguration, name="connectivityServiceOffering__connectivityConfiguration", curie=GX.curie('connectivityConfiguration'),
                   model_uri=GX.connectivityServiceOffering__connectivityConfiguration, domain=None, range=Union[Union[dict, ConnectivityConfiguration], List[Union[dict, ConnectivityConfiguration]]])

slots.connectivityServiceOffering__connectivityQoS = Slot(uri=GX.connectivityQoS, name="connectivityServiceOffering__connectivityQoS", curie=GX.curie('connectivityQoS'),
                   model_uri=GX.connectivityServiceOffering__connectivityQoS, domain=None, range=Optional[Union[dict, QoS]])

slots.networkConnectivityServiceOffering__serviceType = Slot(uri=GX.serviceType, name="networkConnectivityServiceOffering__serviceType", curie=GX.curie('serviceType'),
                   model_uri=GX.networkConnectivityServiceOffering__serviceType, domain=None, range=Optional[str])

slots.networkConnectivityServiceOffering__publicIpAddressProvisioning = Slot(uri=GX.publicIpAddressProvisioning, name="networkConnectivityServiceOffering__publicIpAddressProvisioning", curie=GX.curie('publicIpAddressProvisioning'),
                   model_uri=GX.networkConnectivityServiceOffering__publicIpAddressProvisioning, domain=None, range=Optional[Union[str, "PublicIpAddressProvisioningTypes"]])

slots.networkConnectivityServiceOffering__ipVersion = Slot(uri=GX.ipVersion, name="networkConnectivityServiceOffering__ipVersion", curie=GX.curie('ipVersion'),
                   model_uri=GX.networkConnectivityServiceOffering__ipVersion, domain=None, range=Optional[Union[str, "IpVersionTypes"]])

slots.networkConnectivityServiceOffering__tenantSeparation = Slot(uri=GX.tenantSeparation, name="networkConnectivityServiceOffering__tenantSeparation", curie=GX.curie('tenantSeparation'),
                   model_uri=GX.networkConnectivityServiceOffering__tenantSeparation, domain=None, range=Optional[Union[str, "TenantSeparation"]])

slots.interconnectionServiceOffering__connectedNetworkA = Slot(uri=GX.connectedNetworkA, name="interconnectionServiceOffering__connectedNetworkA", curie=GX.curie('connectedNetworkA'),
                   model_uri=GX.interconnectionServiceOffering__connectedNetworkA, domain=None, range=Optional[Union[int, List[int]]])

slots.interconnectionServiceOffering__connectedNetworkZ = Slot(uri=GX.connectedNetworkZ, name="interconnectionServiceOffering__connectedNetworkZ", curie=GX.curie('connectedNetworkZ'),
                   model_uri=GX.interconnectionServiceOffering__connectedNetworkZ, domain=None, range=Optional[Union[int, List[int]]])

slots.interconnectionServiceOffering__prefixSetA = Slot(uri=GX.prefixSetA, name="interconnectionServiceOffering__prefixSetA", curie=GX.curie('prefixSetA'),
                   model_uri=GX.interconnectionServiceOffering__prefixSetA, domain=None, range=Optional[Union[str, List[str]]])

slots.interconnectionServiceOffering__prefixSetZ = Slot(uri=GX.prefixSetZ, name="interconnectionServiceOffering__prefixSetZ", curie=GX.curie('prefixSetZ'),
                   model_uri=GX.interconnectionServiceOffering__prefixSetZ, domain=None, range=Optional[Union[str, List[str]]])

slots.interconnectionServiceOffering__vlanConfiguration = Slot(uri=GX.vlanConfiguration, name="interconnectionServiceOffering__vlanConfiguration", curie=GX.curie('vlanConfiguration'),
                   model_uri=GX.interconnectionServiceOffering__vlanConfiguration, domain=None, range=Optional[Union[dict, VLANConfiguration]])

slots.interconnectionServiceOffering__connectionType = Slot(uri=GX.connectionType, name="interconnectionServiceOffering__connectionType", curie=GX.curie('connectionType'),
                   model_uri=GX.interconnectionServiceOffering__connectionType, domain=None, range=Optional[Union[str, List[str]]])

slots.interconnectionServiceOffering__interfaceType = Slot(uri=GX.interfaceType, name="interconnectionServiceOffering__interfaceType", curie=GX.curie('interfaceType'),
                   model_uri=GX.interconnectionServiceOffering__interfaceType, domain=None, range=Optional[Union[str, List[str]]])

slots.linkConnectivityServiceOffering__protocolType = Slot(uri=GX.protocolType, name="linkConnectivityServiceOffering__protocolType", curie=GX.curie('protocolType'),
                   model_uri=GX.linkConnectivityServiceOffering__protocolType, domain=None, range=Union[str, "ProtocolType"])

slots.linkConnectivityServiceOffering__vlanConfiguration = Slot(uri=GX.vlanConfiguration, name="linkConnectivityServiceOffering__vlanConfiguration", curie=GX.curie('vlanConfiguration'),
                   model_uri=GX.linkConnectivityServiceOffering__vlanConfiguration, domain=None, range=Optional[Union[dict, VLANConfiguration]])

slots.physicalConnectivityServiceOffering__circuitType = Slot(uri=GX.circuitType, name="physicalConnectivityServiceOffering__circuitType", curie=GX.curie('circuitType'),
                   model_uri=GX.physicalConnectivityServiceOffering__circuitType, domain=None, range=str)

slots.physicalConnectivityServiceOffering__interfaceType = Slot(uri=GX.interfaceType, name="physicalConnectivityServiceOffering__interfaceType", curie=GX.curie('interfaceType'),
                   model_uri=GX.physicalConnectivityServiceOffering__interfaceType, domain=None, range=str)

slots.connectivityConfiguration__sourceIdentifierA = Slot(uri=GX.sourceIdentifierA, name="connectivityConfiguration__sourceIdentifierA", curie=GX.curie('sourceIdentifierA'),
                   model_uri=GX.connectivityConfiguration__sourceIdentifierA, domain=None, range=Optional[str])

slots.connectivityConfiguration__destinationIdentifierZ = Slot(uri=GX.destinationIdentifierZ, name="connectivityConfiguration__destinationIdentifierZ", curie=GX.curie('destinationIdentifierZ'),
                   model_uri=GX.connectivityConfiguration__destinationIdentifierZ, domain=None, range=Optional[str])

slots.physicalInterconnectionPointIdentifier__interconnectionPointIdentifier = Slot(uri=GX.interconnectionPointIdentifier, name="physicalInterconnectionPointIdentifier__interconnectionPointIdentifier", curie=GX.curie('interconnectionPointIdentifier'),
                   model_uri=GX.physicalInterconnectionPointIdentifier__interconnectionPointIdentifier, domain=None, range=Union[str, InterconnectionPointIdentifierCompleteIPI])

slots.virtualInterconnectionPointIdentifier__interconnectionPointIdentifier = Slot(uri=GX.interconnectionPointIdentifier, name="virtualInterconnectionPointIdentifier__interconnectionPointIdentifier", curie=GX.curie('interconnectionPointIdentifier'),
                   model_uri=GX.virtualInterconnectionPointIdentifier__interconnectionPointIdentifier, domain=None, range=Union[str, InterconnectionPointIdentifierCompleteIPI])

slots.interconnectionPointIdentifier__ipiType = Slot(uri=GX.ipiType, name="interconnectionPointIdentifier__ipiType", curie=GX.curie('ipiType'),
                   model_uri=GX.interconnectionPointIdentifier__ipiType, domain=None, range=Optional[Union[str, "IPIType"]])

slots.interconnectionPointIdentifier__ipiProvider = Slot(uri=GX.ipiProvider, name="interconnectionPointIdentifier__ipiProvider", curie=GX.curie('ipiProvider'),
                   model_uri=GX.interconnectionPointIdentifier__ipiProvider, domain=None, range=Optional[str])

slots.interconnectionPointIdentifier__specificParameters = Slot(uri=GX.specificParameters, name="interconnectionPointIdentifier__specificParameters", curie=GX.curie('specificParameters'),
                   model_uri=GX.interconnectionPointIdentifier__specificParameters, domain=None, range=Optional[str])

slots.interconnectionPointIdentifier__completeIPI = Slot(uri=GX.completeIPI, name="interconnectionPointIdentifier__completeIPI", curie=GX.curie('completeIPI'),
                   model_uri=GX.interconnectionPointIdentifier__completeIPI, domain=None, range=URIRef)

slots.interconnectionPointIdentifier__datacenterAllocation = Slot(uri=GX.datacenterAllocation, name="interconnectionPointIdentifier__datacenterAllocation", curie=GX.curie('datacenterAllocation'),
                   model_uri=GX.interconnectionPointIdentifier__datacenterAllocation, domain=None, range=Optional[Union[dict, DatacenterAllocation]])

slots.interconnectionPointIdentifier__macAddress = Slot(uri=GX.macAddress, name="interconnectionPointIdentifier__macAddress", curie=GX.curie('macAddress'),
                   model_uri=GX.interconnectionPointIdentifier__macAddress, domain=None, range=Optional[str],
                   pattern=re.compile(r'(?:[0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2}'))

slots.interconnectionPointIdentifier__ipAddress = Slot(uri=GX.ipAddress, name="interconnectionPointIdentifier__ipAddress", curie=GX.curie('ipAddress'),
                   model_uri=GX.interconnectionPointIdentifier__ipAddress, domain=None, range=Optional[str],
                   pattern=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'))

slots.datacenterAllocation__refersTo = Slot(uri=GX.refersTo, name="datacenterAllocation__refersTo", curie=GX.curie('refersTo'),
                   model_uri=GX.datacenterAllocation__refersTo, domain=None, range=Union[dict, Datacenter])

slots.datacenterAllocation__floor = Slot(uri=GX.floor, name="datacenterAllocation__floor", curie=GX.curie('floor'),
                   model_uri=GX.datacenterAllocation__floor, domain=None, range=Optional[str])

slots.datacenterAllocation__rackNumber = Slot(uri=GX.rackNumber, name="datacenterAllocation__rackNumber", curie=GX.curie('rackNumber'),
                   model_uri=GX.datacenterAllocation__rackNumber, domain=None, range=Optional[str])

slots.datacenterAllocation__patchPanel = Slot(uri=GX.patchPanel, name="datacenterAllocation__patchPanel", curie=GX.curie('patchPanel'),
                   model_uri=GX.datacenterAllocation__patchPanel, domain=None, range=Optional[str])

slots.datacenterAllocation__portNumber = Slot(uri=GX.portNumber, name="datacenterAllocation__portNumber", curie=GX.curie('portNumber'),
                   model_uri=GX.datacenterAllocation__portNumber, domain=None, range=Optional[int])

slots.vLANConfiguration__vlanType = Slot(uri=GX.vlanType, name="vLANConfiguration__vlanType", curie=GX.curie('vlanType'),
                   model_uri=GX.vLANConfiguration__vlanType, domain=None, range=Optional[Union[str, "VlanType"]])

slots.vLANConfiguration__vlanTag = Slot(uri=GX.vlanTag, name="vLANConfiguration__vlanTag", curie=GX.curie('vlanTag'),
                   model_uri=GX.vLANConfiguration__vlanTag, domain=None, range=Optional[int])

slots.vLANConfiguration__vlanEtherType = Slot(uri=GX.vlanEtherType, name="vLANConfiguration__vlanEtherType", curie=GX.curie('vlanEtherType'),
                   model_uri=GX.vLANConfiguration__vlanEtherType, domain=None, range=Optional[str])

slots.computeFunctionConfiguration__computeFunctionQuotas = Slot(uri=GX.computeFunctionQuotas, name="computeFunctionConfiguration__computeFunctionQuotas", curie=GX.curie('computeFunctionQuotas'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionQuotas, domain=None, range=Optional[Union[Union[dict, ComputeFunctionQuotas], List[Union[dict, ComputeFunctionQuotas]]]])

slots.computeFunctionConfiguration__computeFunctionLibrary = Slot(uri=GX.computeFunctionLibrary, name="computeFunctionConfiguration__computeFunctionLibrary", curie=GX.curie('computeFunctionLibrary'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionLibrary, domain=None, range=Optional[Union[Union[dict, ComputeFunctionTemplate], List[Union[dict, ComputeFunctionTemplate]]]])

slots.computeFunctionConfiguration__computeFunctionRuntime = Slot(uri=GX.computeFunctionRuntime, name="computeFunctionConfiguration__computeFunctionRuntime", curie=GX.curie('computeFunctionRuntime'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionRuntime, domain=None, range=Union[Union[dict, ComputeFunctionRuntime], List[Union[dict, ComputeFunctionRuntime]]])

slots.computeFunctionConfiguration__computeFunctionSDK = Slot(uri=GX.computeFunctionSDK, name="computeFunctionConfiguration__computeFunctionSDK", curie=GX.curie('computeFunctionSDK'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionSDK, domain=None, range=Optional[Union[Union[dict, ComputeFunctionRuntime], List[Union[dict, ComputeFunctionRuntime]]]])

slots.computeFunctionConfiguration__computeFunctionTrigger = Slot(uri=GX.computeFunctionTrigger, name="computeFunctionConfiguration__computeFunctionTrigger", curie=GX.curie('computeFunctionTrigger'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionTrigger, domain=None, range=Optional[Union[Union[dict, ComputeFunctionTrigger], List[Union[dict, ComputeFunctionTrigger]]]])

slots.computeFunctionConfiguration__computeFunctionDeploymentMethod = Slot(uri=GX.computeFunctionDeploymentMethod, name="computeFunctionConfiguration__computeFunctionDeploymentMethod", curie=GX.curie('computeFunctionDeploymentMethod'),
                   model_uri=GX.computeFunctionConfiguration__computeFunctionDeploymentMethod, domain=None, range=Optional[Union[Union[str, "ComputeFunctionDeploymentMethod"], List[Union[str, "ComputeFunctionDeploymentMethod"]]]])

slots.computeFunctionConfiguration__confidentialComputingTechnology = Slot(uri=GX.confidentialComputingTechnology, name="computeFunctionConfiguration__confidentialComputingTechnology", curie=GX.curie('confidentialComputingTechnology'),
                   model_uri=GX.computeFunctionConfiguration__confidentialComputingTechnology, domain=None, range=Optional[Union[dict, ConfidentialComputing]])

slots.computeFunctionQuotas__functionMaximumNumber = Slot(uri=GX.functionMaximumNumber, name="computeFunctionQuotas__functionMaximumNumber", curie=GX.curie('functionMaximumNumber'),
                   model_uri=GX.computeFunctionQuotas__functionMaximumNumber, domain=None, range=Optional[int])

slots.computeFunctionQuotas__functionStorageLimit = Slot(uri=GX.functionStorageLimit, name="computeFunctionQuotas__functionStorageLimit", curie=GX.curie('functionStorageLimit'),
                   model_uri=GX.computeFunctionQuotas__functionStorageLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.computeFunctionQuotas__functionTimeLimit = Slot(uri=GX.functionTimeLimit, name="computeFunctionQuotas__functionTimeLimit", curie=GX.curie('functionTimeLimit'),
                   model_uri=GX.computeFunctionQuotas__functionTimeLimit, domain=None, range=Optional[Union[dict, Time]])

slots.computeFunctionQuotas__functionMemoryLimit = Slot(uri=GX.functionMemoryLimit, name="computeFunctionQuotas__functionMemoryLimit", curie=GX.curie('functionMemoryLimit'),
                   model_uri=GX.computeFunctionQuotas__functionMemoryLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.computeFunctionQuotas__functionSizeLimit = Slot(uri=GX.functionSizeLimit, name="computeFunctionQuotas__functionSizeLimit", curie=GX.curie('functionSizeLimit'),
                   model_uri=GX.computeFunctionQuotas__functionSizeLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.computeFunctionQuotas__functionConcurrencyLimit = Slot(uri=GX.functionConcurrencyLimit, name="computeFunctionQuotas__functionConcurrencyLimit", curie=GX.curie('functionConcurrencyLimit'),
                   model_uri=GX.computeFunctionQuotas__functionConcurrencyLimit, domain=None, range=Optional[int])

slots.computeFunctionQuotas__functionRequestSizeLimit = Slot(uri=GX.functionRequestSizeLimit, name="computeFunctionQuotas__functionRequestSizeLimit", curie=GX.curie('functionRequestSizeLimit'),
                   model_uri=GX.computeFunctionQuotas__functionRequestSizeLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.computeFunctionQuotas__functionResponseSizeLimit = Slot(uri=GX.functionResponseSizeLimit, name="computeFunctionQuotas__functionResponseSizeLimit", curie=GX.curie('functionResponseSizeLimit'),
                   model_uri=GX.computeFunctionQuotas__functionResponseSizeLimit, domain=None, range=Optional[Union[dict, MemorySize]])

slots.computeFunctionRuntime__supportedLanguage = Slot(uri=GX.supportedLanguage, name="computeFunctionRuntime__supportedLanguage", curie=GX.curie('supportedLanguage'),
                   model_uri=GX.computeFunctionRuntime__supportedLanguage, domain=None, range=Union[str, "ComputeFunctionLanguage"])

slots.computeFunctionRuntime__supportedVersion = Slot(uri=GX.supportedVersion, name="computeFunctionRuntime__supportedVersion", curie=GX.curie('supportedVersion'),
                   model_uri=GX.computeFunctionRuntime__supportedVersion, domain=None, range=Union[str, List[str]])

slots.computeFunctionTrigger__triggeringService = Slot(uri=GX.triggeringService, name="computeFunctionTrigger__triggeringService", curie=GX.curie('triggeringService'),
                   model_uri=GX.computeFunctionTrigger__triggeringService, domain=None, range=Optional[Union[dict, ServiceOffering]])

slots.computeFunctionTrigger__triggeringEvent = Slot(uri=GX.triggeringEvent, name="computeFunctionTrigger__triggeringEvent", curie=GX.curie('triggeringEvent'),
                   model_uri=GX.computeFunctionTrigger__triggeringEvent, domain=None, range=Optional[Union[str, List[str]]])

slots.computeFunctionTemplate__computeFunctionName = Slot(uri=GX.computeFunctionName, name="computeFunctionTemplate__computeFunctionName", curie=GX.curie('computeFunctionName'),
                   model_uri=GX.computeFunctionTemplate__computeFunctionName, domain=None, range=str)

slots.computeFunctionTemplate__computeFunctionDescription = Slot(uri=GX.computeFunctionDescription, name="computeFunctionTemplate__computeFunctionDescription", curie=GX.curie('computeFunctionDescription'),
                   model_uri=GX.computeFunctionTemplate__computeFunctionDescription, domain=None, range=str)

slots.computeFunctionTemplate__computeFunctionTemplateRuntime = Slot(uri=GX.computeFunctionTemplateRuntime, name="computeFunctionTemplate__computeFunctionTemplateRuntime", curie=GX.curie('computeFunctionTemplateRuntime'),
                   model_uri=GX.computeFunctionTemplate__computeFunctionTemplateRuntime, domain=None, range=Union[Union[dict, ComputeFunctionRuntime], List[Union[dict, ComputeFunctionRuntime]]])

slots.computeFunctionServiceOffering__computeFunctionConfiguration = Slot(uri=GX.computeFunctionConfiguration, name="computeFunctionServiceOffering__computeFunctionConfiguration", curie=GX.curie('computeFunctionConfiguration'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionConfiguration, domain=None, range=Union[dict, ComputeFunctionConfiguration])

slots.computeFunctionServiceOffering__computeFunctionDebugTools = Slot(uri=GX.computeFunctionDebugTools, name="computeFunctionServiceOffering__computeFunctionDebugTools", curie=GX.curie('computeFunctionDebugTools'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionDebugTools, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionEditor = Slot(uri=GX.computeFunctionEditor, name="computeFunctionServiceOffering__computeFunctionEditor", curie=GX.curie('computeFunctionEditor'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionEditor, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionAllowQuota = Slot(uri=GX.computeFunctionAllowQuota, name="computeFunctionServiceOffering__computeFunctionAllowQuota", curie=GX.curie('computeFunctionAllowQuota'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionAllowQuota, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionAllowTimeout = Slot(uri=GX.computeFunctionAllowTimeout, name="computeFunctionServiceOffering__computeFunctionAllowTimeout", curie=GX.curie('computeFunctionAllowTimeout'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionAllowTimeout, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionAllowVersioning = Slot(uri=GX.computeFunctionAllowVersioning, name="computeFunctionServiceOffering__computeFunctionAllowVersioning", curie=GX.curie('computeFunctionAllowVersioning'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionAllowVersioning, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionAllowAutoScaling = Slot(uri=GX.computeFunctionAllowAutoScaling, name="computeFunctionServiceOffering__computeFunctionAllowAutoScaling", curie=GX.curie('computeFunctionAllowAutoScaling'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionAllowAutoScaling, domain=None, range=Optional[Union[bool, Bool]])

slots.computeFunctionServiceOffering__computeFunctionAllowFSMount = Slot(uri=GX.computeFunctionAllowFSMount, name="computeFunctionServiceOffering__computeFunctionAllowFSMount", curie=GX.curie('computeFunctionAllowFSMount'),
                   model_uri=GX.computeFunctionServiceOffering__computeFunctionAllowFSMount, domain=None, range=Optional[Union[bool, Bool]])

slots.vMImage__vmImageDiskFormat = Slot(uri=GX.vmImageDiskFormat, name="vMImage__vmImageDiskFormat", curie=GX.curie('vmImageDiskFormat'),
                   model_uri=GX.vMImage__vmImageDiskFormat, domain=None, range=Optional[Union[str, "VMDiskType"]])

slots.vMImage__hypervisorType = Slot(uri=GX.hypervisorType, name="vMImage__hypervisorType", curie=GX.curie('hypervisorType'),
                   model_uri=GX.vMImage__hypervisorType, domain=None, range=Optional[Union[str, "HypervisorType"]])

slots.vMImage__firmwareType = Slot(uri=GX.firmwareType, name="vMImage__firmwareType", curie=GX.curie('firmwareType'),
                   model_uri=GX.vMImage__firmwareType, domain=None, range=Optional[Union[str, "FirmType"]])

slots.vMImage__hwRngTypeOfImage = Slot(uri=GX.hwRngTypeOfImage, name="vMImage__hwRngTypeOfImage", curie=GX.curie('hwRngTypeOfImage'),
                   model_uri=GX.vMImage__hwRngTypeOfImage, domain=None, range=Optional[Union[str, "RNGTypes"]])

slots.vMImage__watchDogAction = Slot(uri=GX.watchDogAction, name="vMImage__watchDogAction", curie=GX.curie('watchDogAction'),
                   model_uri=GX.vMImage__watchDogAction, domain=None, range=Optional[Union[str, "WatchDogActions"]])

slots.serverFlavor__cpu = Slot(uri=GX.cpu, name="serverFlavor__cpu", curie=GX.curie('cpu'),
                   model_uri=GX.serverFlavor__cpu, domain=None, range=Union[dict, CPU])

slots.serverFlavor__ram = Slot(uri=GX.ram, name="serverFlavor__ram", curie=GX.curie('ram'),
                   model_uri=GX.serverFlavor__ram, domain=None, range=Union[dict, Memory])

slots.serverFlavor__gpu = Slot(uri=GX.gpu, name="serverFlavor__gpu", curie=GX.curie('gpu'),
                   model_uri=GX.serverFlavor__gpu, domain=None, range=Optional[Union[dict, GPU]])

slots.serverFlavor__network = Slot(uri=GX.network, name="serverFlavor__network", curie=GX.curie('network'),
                   model_uri=GX.serverFlavor__network, domain=None, range=Optional[str])

slots.serverFlavor__bootVolume = Slot(uri=GX.bootVolume, name="serverFlavor__bootVolume", curie=GX.curie('bootVolume'),
                   model_uri=GX.serverFlavor__bootVolume, domain=None, range=Union[dict, Disk])

slots.serverFlavor__additionalVolume = Slot(uri=GX.additionalVolume, name="serverFlavor__additionalVolume", curie=GX.curie('additionalVolume'),
                   model_uri=GX.serverFlavor__additionalVolume, domain=None, range=Optional[Union[Union[dict, Disk], List[Union[dict, Disk]]]])

slots.serverFlavor__confidentialComputing = Slot(uri=GX.confidentialComputing, name="serverFlavor__confidentialComputing", curie=GX.curie('confidentialComputing'),
                   model_uri=GX.serverFlavor__confidentialComputing, domain=None, range=Optional[Union[dict, ConfidentialComputing]])

slots.serverFlavor__hypervisor = Slot(uri=GX.hypervisor, name="serverFlavor__hypervisor", curie=GX.curie('hypervisor'),
                   model_uri=GX.serverFlavor__hypervisor, domain=None, range=Optional[Union[dict, Hypervisor]])

slots.serverFlavor__hardwareAssistedVirtualization = Slot(uri=GX.hardwareAssistedVirtualization, name="serverFlavor__hardwareAssistedVirtualization", curie=GX.curie('hardwareAssistedVirtualization'),
                   model_uri=GX.serverFlavor__hardwareAssistedVirtualization, domain=None, range=Optional[Union[bool, Bool]])

slots.serverFlavor__hwRngTypeOfFlavor = Slot(uri=GX.hwRngTypeOfFlavor, name="serverFlavor__hwRngTypeOfFlavor", curie=GX.curie('hwRngTypeOfFlavor'),
                   model_uri=GX.serverFlavor__hwRngTypeOfFlavor, domain=None, range=Optional[Union[str, "RNGTypes"]])

slots.confidentialComputing__technology = Slot(uri=GX.technology, name="confidentialComputing__technology", curie=GX.curie('technology'),
                   model_uri=GX.confidentialComputing__technology, domain=None, range=str)

slots.confidentialComputing__attestationServiceURI = Slot(uri=GX.attestationServiceURI, name="confidentialComputing__attestationServiceURI", curie=GX.curie('attestationServiceURI'),
                   model_uri=GX.confidentialComputing__attestationServiceURI, domain=None, range=Optional[Union[str, URI]])
