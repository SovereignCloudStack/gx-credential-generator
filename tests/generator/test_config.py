import unittest

import generator as config


class ConfigTestCase(unittest.TestCase):
    def test_get_value(self):
        conf = config.Config({"key1": {"key2": {"key3": "value"}}})
        self.assertEqual({"key3": "value"}, conf.get_value(["key1", "key2"]))  # add assertion here
        self.assertEqual("value", conf.get_value(["key1", "key2", "key3"]))  # add assertion here


if __name__ == "__main__":
    unittest.main()
