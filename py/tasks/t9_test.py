import unittest

from t9 import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def test_put_and_get(self):
        d = NativeDictionary[int](2)
        self.assertIsNone(d.get("key1"))
        d.put("key1", 42)
        self.assertEqual(d.get("key1"), 42)

    def test_setitem_and_getitem(self):
        d = NativeDictionary[int](2)
        d["alpha"] = 100
        self.assertEqual(d["alpha"], 100)

    def test_is_key(self):
        d = NativeDictionary[int](2)
        self.assertFalse(d.is_key("missing"))
        d.put("exists", 1)
        self.assertTrue(d.is_key("exists"))

    def test_overwrite_value(self):
        d = NativeDictionary[int](2)
        d.put("key", 1)
        d.put("key", 99)
        self.assertEqual(d.get("key"), 99)
        self.assertEqual(len(d), 1)  # size shouldn't increase

    def test_len_tracking(self):
        d = NativeDictionary[int](2)
        self.assertEqual(len(d), 0)
        d.put("k1", 1)
        d.put("k2", 2)
        self.assertEqual(len(d), 2)

    def test_setitem(self):
        d = NativeDictionary[int](2)
        d["k1"] = 1
        d["k2"] = 2
        self.assertEqual(len(d), 2)

    def test_getitem(self):
        d = NativeDictionary[int](2)
        d["k1"] = 1
        d["k2"] = 2
        self.assertEqual(1, d["k1"])
        self.assertEqual(2, d["k2"])

    def test_nonexistent_key(self):
        d = NativeDictionary[int](2)
        self.assertIsNone(d.get("ghost"))
        self.assertFalse(d.is_key("ghost"))


if __name__ == "__main__":
    unittest.main()
