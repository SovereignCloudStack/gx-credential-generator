import datetime
import unittest

from generator.common.gx_schema import GaiaX, GaiaXEntity, ServerFlavor
from generator.common.json_ld import get_json_ld_types, get_slot_curie


class JsonLDTestCase(unittest.TestCase):
    def test_get_types(self):
        self.assertEqual(
            ["gx:ServerFlavor", "gx:InstantiationRequirement", "gx:GaiaXEntity"],
            get_json_ld_types(ServerFlavor),
        )

    def test_get_json_ld_context(self):
        self.assertEqual(
            {
                "@context": {
                    "ex": "https://example.com/",
                    "gx": Namespace("https://w3id.org/gaia-x/ONTOLOGY_VERSION/"),
                    "qudt": Namespace("http://qudt.org/vocab/"),
                    "schema": Namespace("http://schema.org/"),
                    "vcard": Namespace("http://www.w3.org/2006/vcard/ns#"),
                    "xsd": "http://www.w3.org/2001/XMLSchema#",
                }
            },
            get_json_ld_context(),
        )

    def test_to_json_ld(self):
        addr = Address(countryCode="DE")
        self.assertEqual(
            {"@type": "vcard:Address", "gx:countryCode": "DE"}, to_json_ld(addr)
        )
        self.assertEqual(
            {"@id": "ex:foo", "@type": "vcard:Address", "gx:countryCode": "DE"},
            to_json_ld(JsonLdObject(gx_object=addr, gx_id="foo")),
        )

        # test attribute is emtpy
        for value in [None, []]:
            addr.countryCode = value
            self.assertEqual({"@type": "vcard:Address"}, to_json_ld(addr))

        # test attribute is an empty list
        addr.countryCode = ["DE", "FR"]
        self.assertEqual(
            {"@type": "vcard:Address", "gx:countryCode": ["DE", "FR"]}, to_json_ld(addr)
        )

        # test attribute is a PermissibleValue
        addr.countryCode = CountryNameAlpha2.DE
        self.assertEqual(
            {"@type": "vcard:Address", "gx:countryCode": "DE"}, to_json_ld(addr)
        )

        # test attribute is EnumDefinitionImpl
        addr.countryCode = CountryNameAlpha2("DE")
        self.assertEqual(
            {"@type": "vcard:Address", "gx:countryCode": "DE"}, to_json_ld(addr)
        )

        # test attribute is date and datetime
        addr.countryCode = datetime.date(2014, 5, 12)
        self.assertEqual(
            {
                "@type": "vcard:Address",
                "gx:countryCode": {"@type": "xsd:date", "@value": "2014-05-12"},
            },
            to_json_ld(addr),
        )
        addr.countryCode = datetime.datetime(2014, 5, 12, 18, 50, 32)
        self.assertEqual(
            {
                "@type": "vcard:Address",
                "gx:countryCode": {
                    "@type": "xsd:dateTime",
                    "@value": "2014-05-12T18:50:32",
                },
            },
            to_json_ld(addr),
        )

        # test simple data types
        addr.countryCode = 1.5
        self.assertEqual(
            {
                "@type": "vcard:Address",
                "gx:countryCode": {"@type": "xsd:float", "@value": 1.5},
            },
            to_json_ld(addr),
        )
        addr.countryCode = URI("https::example.com")
        self.assertEqual(
            {
                "@type": "vcard:Address",
                "gx:countryCode": {
                    "@type": "xsd:anyURI",
                    "@value": "https::example.com",
                },
            },
            to_json_ld(addr),
        )
        addr.countryCode = False
        self.assertEqual(
            {
                "@type": "vcard:Address",
                "gx:countryCode": {"@type": "xsd:boolean", "@value": False},
            },
            to_json_ld(addr),
        )

    def test_get_slot_curie(self):
        self.assertEqual(
            "qudt:value",
            get_slot_curie(
                "value",
                MemorySize(value=12, unit="https://qudt.org/vocab/unit/MegaBYTE"),
            ),
        )

    def test_init_empty_gx_id(self):
        self.assertIsNotNone(
            JsonLdObject(
                gx_object=Image(
                    copyrightOwnedBy=["Foo"],
                    license=["Bar"],
                    resourcePolicy=["default: allow intent"],
                )
            ).gx_id
        )


if __name__ == "__main__":
    unittest.main()
