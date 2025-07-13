import unittest

from t11 import BloomFilter, hash1, hash2


# TASK: 1.11.2*
# TITLE: Bloom filter merge
# TIME COMPLEXITY: O(1)
# SPACE COMPLEXITY: O(1) does not depend on hash_fns size
# REFLECTION:
#   - `str` string-only hash function parameter can be expanded to generic `Hashable`
#   - *hash_fns can be changed to just List[hash_fns] and have default parameter
#   - .bit_length() how many bits total
#   - .bit_count() how many bits=1 total
#   - Python adds bits on demand so binary representation of `int i = 0;` is `0` and not `0...0`
# CODE:
class AddableBloomFilter(BloomFilter):
    def __add__(self, other: "AddableBloomFilter"):
        return AddableBloomFilter(
            max(self.f_len, other.f_len),
            self.filter | other.filter,
            *(self.hash_fns + other.hash_fns),
        )


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = AddableBloomFilter(
            32, 0b0, lambda s: hash1(s) & 31, lambda s: hash2(s) & 31
        )
        s = "0123456789"
        self.data = [s[x:] + s[:x] for x in range(len(s))]

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

    def test_merge_bits_and_funcs(self):
        f1 = AddableBloomFilter(32, 0b0011, lambda _: 0)
        f2 = AddableBloomFilter(32, 0b0101, lambda _: 1)
        merged = f1 + f2
        self.assertEqual(merged.filter, 0b0111)
        self.assertEqual(merged.f_len, 32)
        self.assertEqual(len(merged.hash_fns), 2)
        self.assertEqual(merged.hash_fns[0]("x"), 0)
        self.assertEqual(merged.hash_fns[1]("x"), 1)
        self.assertEqual(f1.filter, 0b0011)
        self.assertEqual(f2.filter, 0b0101)

    def test_merge_different_sizes(self):
        f1 = AddableBloomFilter(32, 0b1, lambda _: 2)
        f2 = AddableBloomFilter(64, 0b10, lambda _: 3)
        merged = f1 + f2
        self.assertEqual(merged.f_len, 64)
        self.assertEqual(merged.filter, 0b11)
        self.assertEqual(len(merged.hash_fns), 2)
        outputs = sorted(fn("x") for fn in merged.hash_fns)
        self.assertEqual(outputs, [2, 3])

    def test_chain_addition(self):
        f1 = AddableBloomFilter(32, 0b100, lambda _: 4)
        f2 = AddableBloomFilter(32, 0b010, lambda _: 5)
        f3 = AddableBloomFilter(32, 0b001, lambda _: 6)
        merged = f1 + f2 + f3
        self.assertEqual(merged.filter, 0b111)
        self.assertEqual(len(merged.hash_fns), 3)
        outputs = sorted(fn("x") for fn in merged.hash_fns)
        self.assertEqual(outputs, [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
