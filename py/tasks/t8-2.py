import unittest

from t8 import HashTable

# 8.3 is len(HashTable)


class TestHashTable(unittest.TestCase):
    def test_len_empty_table(self):
        ht = HashTable(sz=10, stp=1)
        self.assertEqual(len(ht), 0, "Empty table should have length 0")

    def test_len_after_one_put(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("one")
        self.assertEqual(len(ht), 1, "Table should have length 1 after one insertion")

    def test_len_after_duplicate_put(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("dup")
        ht.put("dup")
        self.assertEqual(len(ht), 1, "Inserting duplicate should not increase length")

    def test_len_after_duplicate_overflow(self):
        ht = HashTable(sz=2, stp=1)
        ht.put("dup")
        ht.put("dup")
        ht.put("dup")
        self.assertEqual(
            len(ht), 1, "Inserting duplicate overflow should not increase length"
        )

    def test_len_after_multiple_puts(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("a")
        ht.put("b")
        ht.put("c")
        self.assertEqual(len(ht), 3, "Table should count unique slots filled")

    def test_len_after_failed_put(self):
        ht = HashTable(sz=3, stp=1)
        ht.put("x")
        ht.put("y")
        ht.put("z")
        index = ht.put("overflow")
        self.assertIsNone(index)
        self.assertEqual(len(ht), 3, "Length should not change after failed insertion")


if __name__ == "__main__":
    unittest.main()
