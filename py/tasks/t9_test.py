import unittest

from t9 import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def test_hash_fun_consistency(self):
        ht = NativeDictionary(sz=10, stp=1)
        val = "abc123"
        h1 = ht.hash_fun(val)
        h2 = ht.hash_fun(val)
        self.assertEqual(
            h1, h2, "hash_fun should return consistent results for same input"
        )

    def test_hash_fun_different_strings(self):
        ht = NativeDictionary(sz=10, stp=1)
        h1 = ht.hash_fun("abc")
        h2 = ht.hash_fun("abd")
        self.assertNotEqual(
            h1, h2, "hash_fun should return different values for different strings"
        )

    def test_seek_slot_empty_table(self):
        ht = NativeDictionary[str](sz=5, stp=1)
        index = ht.seek_slot("abc")
        self.assertIsNotNone(index)
        # type won't infer
        assert index is not None
        self.assertGreaterEqual(index, 0)
        self.assertLess(index, ht.size)

    def test_put_and_find_single_element(self):
        ht = NativeDictionary[str](sz=10, stp=1)
        val = "test"
        idx_put = ht.put("key", val)
        self.assertIsNotNone(idx_put, "put should return an index for new element")
        self.assertEqual(val, ht.get("key"), "find should locate the element after put")

    def test_put_duplicate_value(self):
        ht = NativeDictionary[str](sz=10, stp=1)
        val = "dup"
        idx1 = ht.put("key", val)
        idx2 = ht.put("key", val)
        self.assertEqual(idx1, idx2, "put of duplicate value should return same index")

    def test_find_nonexistent_value(self):
        ht = NativeDictionary[str](sz=10, stp=1)
        ht.put("key", "exists")
        idx = ht.get("missing")
        self.assertIsNone(idx, "find should return None for non-existent value")

    def test_put_until_full_and_fail(self):
        ht = NativeDictionary(sz=3, stp=1)
        self.assertIsNotNone(ht.put("a", "a"))
        self.assertIsNotNone(ht.put("b", "b"))
        self.assertIsNotNone(ht.put("c", "c"))
        idx = ht.put("d", "d")
        self.assertIsNone(idx, "put should return None if table is full")

    def test_collision_resolution(self):
        ht = NativeDictionary(sz=5, stp=1)
        val1 = "Aa"  # likely to produce specific hash
        val2 = "BB"
        idx1 = ht.put(val1, val1)
        idx2 = ht.put(val2, val2)
        self.assertIsNotNone(idx1)
        self.assertIsNotNone(idx2)
        self.assertNotEqual(
            idx1, idx2, "collision resolution should put values in different slots"
        )
        self.assertEqual(ht.get(val1), val1)
        self.assertEqual(ht.get(val2), val2)

    def test_seek_slot_returns_none_when_full(self):
        ht = NativeDictionary(sz=3, stp=1)
        ht.put("x", "x")
        ht.put("y", "y")
        ht.put("z", "z")
        slot = ht.seek_slot("new")
        self.assertIsNone(slot, "seek_slot should return None if no slots available")

    def test_put_with_step_greater_than_one(self):
        ht = NativeDictionary(sz=10, stp=3)
        val1 = "value1"
        val2 = "value2"
        idx1 = ht.put(val1, val1)
        idx2 = ht.put(val2, val2)
        self.assertIsNotNone(idx1)
        self.assertIsNotNone(idx2)
        self.assertNotEqual(idx1, idx2, "put should work correctly with step > 1")
        self.assertEqual(ht.get(val1), val1)
        self.assertEqual(ht.get(val2), val2)


if __name__ == "__main__":
    unittest.main()
