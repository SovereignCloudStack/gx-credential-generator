import unittest

from generator.common.gx_schema import GaiaX, GaiaXEntity, ServerFlavor
from generator.common.json_ld import get_json_ld_types, get_slot_curie


class JsonLDTestCase(unittest.TestCase):
    def test_get_types(self):
        self.assertEqual(
            ["gx:ServerFlavor", "gx:InstantiationRequirement", "gx:GaiaXEntity"],
            get_json_ld_types(ServerFlavor),
        )

    def test_get_slot_curie(self):
        self.assertEqual("gx:name", get_slot_curie("name", GaiaXEntity()))  # add assertion here
        self.assertIsNone(get_slot_curie("name", GaiaX()))  # add assertion here


if __name__ == "__main__":
    unittest.main()
