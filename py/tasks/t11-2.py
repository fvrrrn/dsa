import unittest
from itertools import product
from typing import Callable, List

from t11 import BloomFilter, hash1, hash2


# TASK: 1.11.2*
# TITLE: Bloom filter merge
# TIME COMPLEXITY: O(1)
# SPACE COMPLEXITY: O(1) does not depend on hash_fns size
# REFLECTION:
#   - Probability of false-positivity does not change on filter merge
#     because it only depends on `m` and `n` where m is f_len and n is len(str)
#   - `str` string-only hash function parameter can be expanded to generic `Hashable`
#   - *hash_fns can be changed to just List[hash_fns] and have default parameter
#   - .bit_length() how many bits total
#   - .bit_count() how many bits=1 total
#   - Python adds bits on demand so binary representation of `int i = 0;` is `0` and not `0...0`
#   - compare self.f_len and other.f_len
# CODE:
class AddableBloomFilter(BloomFilter):
    def __add__(self, other: "AddableBloomFilter"):
        return AddableBloomFilter(
            self.f_len,
            self.bit_array | other.bit_array,
            *(self.hash_fns + other.hash_fns),
        )


# TASK: 1.11.3*
# TITLE: Bloom filter with removable elements
# TIME COMPLEXITY: O(1) hash_fns and bit_array iterations do not depend on elements amount
# SPACE COMPLEXITY: O(1) though array is used its size does not depend on elements amount
# REFLECTION:
#   - hash function should just only hash (duh), there shouldn't be modulo or bit-shift and whatnot
#   - there can be interger overflow in `add`
# CODE:
class RemovableBloomFilter(BloomFilter):
    def __init__(
        self,
        f_len: int,
        *hash_fns: Callable[[str], int],
    ):
        self.f_len = f_len
        self.bit_array = [0] * self.f_len
        # cannot set default parameter to * and ** types
        self.hash_fns = (
            list(hash_fns)
            if hash_fns
            else [
                lambda s: ((hash1(s) % self.f_len)),
                lambda s: ((hash2(s) % self.f_len)),
            ]
        )

    def __str__(self) -> str:
        return str(self.bit_array)

    def add(self, str1: str):
        for f in self.hash_fns:
            self.bit_array[f(str1)] += 1

    def is_value(self, str1: str) -> bool:
        mask = [0] * self.f_len
        for f in self.hash_fns:
            mask[f(str1)] += 1
        for e1, e2 in zip(mask, self.bit_array):
            if e1 > 0 and e1 > e2:
                return False
        return True

    def remove(self, str1: str):
        for f in self.hash_fns:
            self.bit_array[f(str1)] = max(0, self.bit_array[f(str1)] - 1)


# TASK: 1.11.4*
# TITLE: Bloom filter elements reconstruction
# TIME COMPLEXITY: O(p ^ n) where is power of alphabet (distinct symbols count, "abc" is 3 for instance)
# SPACE COMPLEXITY: O(p ^ n) to store all the elements
# REFLECTION:
#   - 1. Let k = len(bloom_filter.hash_fns), m = bloom_filter.bit_array.bit_length(), k = 0,6931 * m / n
#     Then n = m * 0.6931 / k
#     2. For all possible ordered n repeatable combinations of values of str (0-9a-zA-Z, emoji etc.)
#     check if given string of such combination is within bloom filter
#   - Knowing beforehand what symbols we are after could significantly improve performance (for instance phone numbers)
#   - Can be parallelized or ran with GPU since we are doing binary operations
#   - TODO: 0.6931 is ln 2, check why
# CODE:
def reconstruct(bloom_filter: BloomFilter) -> List[str]:
    result: List[str] = []
    k = len(bloom_filter.hash_fns)
    m = bloom_filter.bit_array.bit_length()
    n = min(1, int(round(m * 0.6931) / k))
    for chars in product("0123456789", repeat=n):
        candidate = "".join(chars)
        if bloom_filter.is_value(candidate):
            result += candidate
    return result


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

    def test_chain_addition(self):
        f1 = AddableBloomFilter(32, 0b100, lambda _: 4)
        f2 = AddableBloomFilter(32, 0b010, lambda _: 5)
        f3 = AddableBloomFilter(32, 0b001, lambda _: 6)
        merged = f1 + f2 + f3
        self.assertEqual(merged.bit_array, 0b111)
        self.assertEqual(len(merged.hash_fns), 3)
        outputs = sorted(fn("x") for fn in merged.hash_fns)
        self.assertEqual(outputs, [4, 5, 6])


class TestRemovableBloomFilter(unittest.TestCase):
    def setUp(self):
        self.f_len = 32
        self.bf = RemovableBloomFilter(self.f_len)
        s = "0123456789"
        self.data = [s[x:] + s[:x] for x in range(len(s))]
        self.assertLess(self.bf.hash_fns[0]("0123456789"), 32)

    def test_add_and_query_single(self):
        for item in self.data:
            self.bf.add(item)
        for item in self.data:
            self.assertTrue(self.bf.is_value(item))

    def test_shared_bits_false_positive_possible(self):
        self.bf.add("apple")
        # Add another value that shares at least one hash result with "banana"
        # But don’t add "banana" itself
        self.assertFalse(self.bf.is_value("banana"))  # may still be false
        # Add banana to make sure it becomes detectable
        self.bf.add("banana")
        self.assertTrue(self.bf.is_value("banana"))

    def test_counting_preserves_multiple_adds(self):
        self.bf.add("apple")
        self.bf.add("apple")
        self.assertTrue(self.bf.is_value("apple"))
        # Manually check that all hash positions are incremented twice
        positions = [f("apple") for f in self.bf.hash_fns]
        for p in positions:
            self.assertEqual(self.bf.bit_array[p], 2)

    def test_remove_one(self):
        self.bf.add(self.data[0])
        self.bf.add(self.data[0])
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[0](self.data[0])], 2)
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[1](self.data[0])], 2)
        self.assertTrue(self.bf.is_value(self.data[0]))
        self.bf.remove(self.data[0])
        self.assertTrue(self.bf.is_value(self.data[0]))
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[0](self.data[0])], 1)
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[1](self.data[0])], 1)
        self.bf.remove(self.data[0])
        self.assertFalse(self.bf.is_value(self.data[0]))
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[0](self.data[0])], 0)
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[1](self.data[0])], 0)
        self.bf.remove(self.data[0])
        self.assertFalse(self.bf.is_value(self.data[0]))
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[0](self.data[0])], 0)
        self.assertEqual(self.bf.bit_array[self.bf.hash_fns[1](self.data[0])], 0)

    def test_remove_many(self):
        for item in self.data:
            self.bf.add(item)
        for i in range(len(self.data)):
            self.bf.remove(self.data[i])
            # each i-th of data is removed
            # then we check if all other elements are positive/false-positive
            # there shouldn't once be false-negative
            for item in self.data[i:]:
                self.bf.is_value(item)


if __name__ == "__main__":
    unittest.main()
