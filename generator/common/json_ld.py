"""
Methods and classes needed/useful for JSON-LD serialization.
"""
import inspect
from datetime import date, datetime
from typing import List
from uuid import uuid4

from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions,
)
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import URI
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str

from generator.common.gx_schema import GX, QUDT, SCHEMA, VCARD, slots

from json import JSONDecoder

from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate, XSDDateTime
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int

from generator.common.gx_schema import GX, QUDT, SCHEMA, VCARD, slots
from linkml_runtime.utils.yamlutils import TypedNode
from typing import List, Tuple

from uuid import uuid4
from datetime import date, datetime

from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str

class JsonLdObject:
    """Wrapper class to store properties and id of a GX object instance. This class is required, because python
<<<<<<< HEAD
    classes of Gaia-X Credential does not have an attribute to store instance's id and id is essential in GX Credentials.
    """

    def __init__(self, gx_object: YAMLRoot, gx_id: str = None):
        """
        Create a new object of JsonLdObejct
    classes of Gaia-X Credential does not have an attribute to store instance's id."""

    def __init__(self, gx_object: YAMLRoot, gx_id=None):
        """
        @param gx_object: Gaia-X object
        @type gx_object: YAMLRoot
        @param gx_id: id of Gaia-X object
        @type gx_id: basestring
        """
        self.gx_object = gx_object
        self.gx_id = gx_id
        if self.gx_id is None:
            self.gx_id = str(uuid4())


def get_json_ld_context() -> dict:
    """
    Return JSON-LD context as dict.

    @return: JSON-LD context as dictionary
    @rtype: dict
    """
    return {
        "@context": {
            GX.prefix: GX,
            QUDT.prefix: QUDT,
            SCHEMA.prefix: SCHEMA,
            VCARD.prefix: VCARD,
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "ex": "https://example.com/",
        }
    }


def to_json_ld(obj) -> dict:
    """
    JSON serializer callback method.
        1) Adds object's id, if any
        2) Adds type information of instance and its attributes. As JSON-LD interprets all attributes without any type
        information as string, we need to add type to non-string attributes explicitly.
        3) Adds curie to instance and its attributes
        4) Filters out empty values (None, {}, and [])

    @param obj: object to be serialized
    @return:  object as dictionary
    @rtype: dict
    """
    json_ld = dict()
    if isinstance(obj, JsonLdObject):
        # if JsonLdObject add id
        gx_object = obj.gx_object
        json_ld["@id"] = "ex:" + obj.gx_id.replace(" ", "")
        # call to_json_ld for gx_object
        json_ld.update(to_json_ld(gx_object))
        return json_ld
    elif isinstance(obj, YAMLRoot):
        # if YAMLRoot (= all top level classes in Gaia-X Credential Schema)
        # Using one type is sufficient
        # json_ld['@type'] = get_types(obj.__class__)
        try:
            # set type of Gaia-X object if possible
            json_ld["@type"] = obj.class_class_curie
        except AttributeError:
            pass
        for key, value in obj.__dict__.items():
            # serialize each attribute of object
            if value is None or value == [] or value == {}:
                # skip emtpy values
                continue
            slot_curie = get_slot_curie(key, obj)
            if isinstance(value, list):
                # Add type for datetime
                json_ld[slot_curie] = dict()
                json_ld[slot_curie]["@type"] = "xsd:dateTime"
                json_ld[slot_curie]["@value"] = value
            elif isinstance(value, XSDDate):
                # add type for date
                json_ld[slot_curie] = dict()
                json_ld[slot_curie]["@type"] = "xsd:date"
                json_ld[slot_curie]["@value"] = value
            elif isinstance(value, float):
                # add type for float
                json_ld[slot_curie] = dict()
                json_ld[slot_curie]["@type"] = "xsd:float"
                json_ld[slot_curie]["@value"] = value
            elif isinstance(value, str) and value.startswith("http"):
                # linkML's python generator maps datatype 'anyURI' to 'string', but we need a URL here. Hence, we must
                # check if string is a URL, by evaluation string's start and change datatype in JSON-LD appropriately.
                json_ld[slot_curie] = dict()
                json_ld[slot_curie]["@type"] = "xsd:anyURI"
                json_ld[slot_curie]["@value"] = value
            elif isinstance(value, bool):
                # add type for boolean
                json_ld[slot_curie] = dict()
                json_ld[slot_curie]["@type"] = "xsd:boolean"
                json_ld[slot_curie]["@value"] = value
            elif isinstance(value, list):
               if isinstance(value, list):
         # call to_json_ld for each entry in list
                json_ld[slot_curie] = list()
                for item in value:
                    json_ld[slot_curie].append(to_json_ld(item))
            elif isinstance(obj, EnumDefinitionImpl):
                # add text for enumeration values instead of code
                return obj.code.text
            elif isinstance(obj, PermissibleValue):
                # add text for enumeration values instead of code
                return obj.text
            else:
                json_ld[slot_curie] = to_json_ld(value)
        return json_ld
    elif isinstance(obj, datetime):
        # Add type for datetime
        return {"@type": "xsd:dateTime", "@value": obj.strftime("%Y-%m-%dT%H:%M:%S")}
    elif isinstance(obj, date):
        # add type for date
        return {"@type": "xsd:date", "@value": obj}
    elif isinstance(obj, float):
        # add type for float
        return {"@type": "xsd:float", "@value": obj}
    elif isinstance(obj, URI):
        # add type for URI
        return {"@type": "xsd:anyURI", "@value": obj}
    elif isinstance(obj, bool):
        # add type for boolean
        return {"@type": "xsd:boolean", "@value": obj}
    else:
        return obj


def get_slot_curie(slot_name: str, gx_object: object) -> str:
    """
    Returns curie of slot with given SLOT_NAME of given GX_OBJECT.

    @param slot_name: name of slot whose curie is requested
    @type slot_name: str
    @param gx_object: GX object given slot may belong to
    @type gx_object: object
    @return: slot's curie as str, if given GX_OBJECT has slot with given SLOT_NAME. Otherwise None
    """
    for s_class in _get_super_classes(gx_object.__class__):
        s_class = s_class.__name__[0].lower() + s_class.__name__[1:]
        if hasattr(slots, s_class + "__" + slot_name):
            return getattr(slots, s_class + "__" + slot_name).curie
        elif hasattr(slots, slot_name):
            return getattr(slots, slot_name).curie

def get_types(gx_object: type) -> List[type]:
    """
    Returns all types as curie of given GX_OBJECT. Types are instance's class as well as all its super classes.
    @param gaia_object: GX object, whose type is to be retrived
    @type gaia_object: type
    """
    types = []
    for base in _get_super_classes(gx_object):
        try:
            types.append(base.class_class_curie)
        except AttributeError:
            pass
    for base in inspect.getmro(gx_object):
        if isinstance(base, YAMLRoot):
            types.append(base.class_class_curie)
    return types


def _get_super_classes(class_name) -> List:
    """
    Return all super classes of class with given CLASS_NAME.
    @param class_name: name of class
    @return: list of all super classes
    """
    classes = []
    for base in inspect.getmro(class_name):
        try:
            classes.append(base)
        except AttributeError:
            pass
    return classes
