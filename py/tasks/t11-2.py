import unittest

from t11 import BloomFilter


# TASK: 1.11.2*
# TITLE: Bloom filter merge
# TIME COMPLEXITY: O(1)
# SPACE COMPLEXITY: O(1) does not depend on hash_fns size
# REFLECTION:
#   - Let F1 = (0b010,) P = 0,6931 ** (m/n), m is in {2 ** i | i is in N}, n is in N
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
            self.bit_array | other.bit_array,
            *(self.hash_fns + other.hash_fns),
        )


class TestBloomFilter(unittest.TestCase):
    def test_merge_bits_and_funcs(self):
        f1 = AddableBloomFilter(32, 0b0011, lambda _: 0)
        f2 = AddableBloomFilter(32, 0b0101, lambda _: 1)
        merged = f1 + f2
        self.assertEqual(merged.bit_array, 0b0111)
        self.assertEqual(merged.f_len, 32)
        self.assertEqual(len(merged.hash_fns), 2)
        self.assertEqual(merged.hash_fns[0]("x"), 0)
        self.assertEqual(merged.hash_fns[1]("x"), 1)
        self.assertEqual(f1.bit_array, 0b0011)
        self.assertEqual(f2.bit_array, 0b0101)

    def test_merge_different_sizes(self):
        f1 = AddableBloomFilter(32, 0b1, lambda _: 2)
        f2 = AddableBloomFilter(64, 0b10, lambda _: 3)
        merged = f1 + f2
        self.assertEqual(merged.f_len, 64)
        self.assertEqual(merged.bit_array, 0b11)
        self.assertEqual(len(merged.hash_fns), 2)
        outputs = sorted(fn("x") for fn in merged.hash_fns)
        self.assertEqual(outputs, [2, 3])

    def test_chain_addition(self):
        f1 = AddableBloomFilter(32, 0b100, lambda _: 4)
        f2 = AddableBloomFilter(32, 0b010, lambda _: 5)
        f3 = AddableBloomFilter(32, 0b001, lambda _: 6)
        merged = f1 + f2 + f3
        self.assertEqual(merged.bit_array, 0b111)
        self.assertEqual(len(merged.hash_fns), 3)
        outputs = sorted(fn("x") for fn in merged.hash_fns)
        self.assertEqual(outputs, [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
