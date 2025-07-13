import unittest

from t11 import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter(32)
        s = "0123456789"
        self.data = [s[x:] + s[:x] for x in range(len(s))]

    def test_hash_ranges(self):
        for s in self.data:
            h1 = self.bf.hash1(s)
            h2 = self.bf.hash2(s)
            self.assertGreaterEqual(h1, 0)
            self.assertLess(h1, self.bf.f_len)
            self.assertGreaterEqual(h2, 0)
            self.assertLess(h2, self.bf.f_len)

    def test_add_and_query(self):
        self.assertFalse(self.bf.is_value("123"))
        self.bf.add("123")
        self.assertTrue(self.bf.is_value("123"))

    def test_multiple_items(self):
        for item in self.data:
            self.bf.add(item)
        for item in self.data:
            self.assertTrue(self.bf.is_value(item))

    def test_nonexistent_item(self):
        self.bf.add(self.data[0])
        self.assertFalse(self.bf.is_value(self.data[1]))


if __name__ == "__main__":
    unittest.main()
