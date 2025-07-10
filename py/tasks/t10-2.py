import unittest
from typing import Generic, TypeVar

from t10 import PowerSet

T = TypeVar("T")

# TASK: 1.10.4*
# TITLE: Cartesian product of two sets
# TIME COMPLEXITY: O(n*m)
# SPACE COMPLEXITY: O(n*m)
# REFLECTION:
#   - for `Bag` add option to create pairs only for keys and yield their count
# CODE: t10.py#L32
# def cartesian_product(self, set2: "PowerSet[T]") -> Iterator[Tuple[T, T]]:
#     for e1 in self:
#         for e2 in set2:
#             yield (e1, e2)


# TASK: 1.10.6*
# TITLE: Multiset `Bag` with frequency operations
# TIME COMPLEXITY:
#   - put, __delitem__, __getitem__, __setitem__:
#       O(n) if collision
#       o(1) if load factor (s.length/s.capacity) is below certain value (which I don't know)
#       Theta(1/(1-s.length/s.capacity) if hash function creates uniform distribution
#       Omega(1) if no collision
#   - intersection, union, difference: where n is self.length, m is set2.length
#       O(n + m)
#       o(n + m)
#       Theta(n + m)
#       Omega(n + m)
#   - issubset, __eq__:
#       O(n)
#       o(n)
#       Theta(n)
#       Omega(1) if first element is not in set
# SPACE COMPLEXITY: O(n)
# REFLECTION:
#   - TODO: instead of `for e in set2` use `for k, v in set2.elements.items() so not to call O(n) set2[e] later
#   - defaultdict can be used to have all keys set to 0 be default to avoid None check
#   - difference_keys can be added to have a method that returns difference discarding how many `e` within given set
# CODE:
class Bag(Generic[T], PowerSet[T]):
    def put(self, element: T, value=1) -> None:
        self[element] += value

    def __setitem__(self, element: T, value: int) -> None:
        self.elements[element] = value

    def __delitem__(self, element: T) -> bool:
        match self.elements.get(element, 0) - 1:
            case -1:
                return False
            case 0:
                del self.elements[element]
                return True
            case _:
                self.elements[element] -= 1
                return True

    def intersection(self, set2: "PowerSet[T]") -> "Bag[T]":
        set3 = Bag()
        for e in self:
            if e in set2:
                set3[e] = min(self[e], set2[e])
        for e in set2:
            if e in self:
                set3[e] = min(self[e], set2[e])
        return set3

    def union(self, set2: "PowerSet[T]") -> "Bag[T]":
        set3 = Bag()
        for e in self:
            set3.put(e, self[e])
        for e in set2:
            set3.put(e, set2[e])
        return set3

    def difference(self, set2: "PowerSet[T]") -> "Bag[T]":
        set3 = Bag()
        for e in self:
            if e in set2:
                diff_value = max(0, self[e] - set2[e])
                if diff_value:
                    set3[e] = diff_value
            else:
                set3[e] = self[e]
        return set3

    def issubset(self, set2: "PowerSet[T]") -> bool:
        return all(e in self and set2[e] <= self[e] for e in set2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PowerSet):
            return False
        if len(self) != len(other):
            return False
        return all(
            e2 in self and e1 in other and self[e1] == other[e2]
            for e1, e2 in zip(self, other)
        )


class TestBag(unittest.TestCase):
    def setUp(self):
        self.bag1 = Bag("a", "b", "b", "c")
        self.bag2 = Bag("b", "b", "c", "d")

    def test_put_and_get(self):
        self.bag1.put("d", 2)
        self.assertIn("d", self.bag1)
        self.assertEqual(self.bag1["d"], 2)

    def test_remove_and_delitem(self):
        self.assertTrue(self.bag1.remove("b"))  # b count goes from 2 to 1
        self.assertTrue(
            self.bag1.remove("b")
        )  # b count goes from 1 to 0, should be deleted
        self.assertFalse("b" in self.bag1)
        self.assertFalse(
            self.bag1.remove("b")
        )  # Removing nonexistent now returns False

    def test_intersection(self):
        result = self.bag1.intersection(self.bag2)
        self.assertEqual(result["b"], 2)
        self.assertEqual(result["c"], 1)
        self.assertNotIn("a", result)
        self.assertNotIn("d", result)

    def test_union(self):
        result = self.bag1.union(self.bag2)
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 4)
        self.assertEqual(result["c"], 2)
        self.assertEqual(result["d"], 1)

    def test_difference(self):
        result = self.bag1.difference(self.bag2)
        self.assertEqual(result["a"], 1)
        self.assertNotIn("c", result)
        self.assertEqual(result["b"], 0)  # max(2 - 2, 0) = 0, should be skipped

    def test_issubset(self):
        bag3 = Bag("b", "c")
        self.assertFalse(bag3.issubset(self.bag2))
        self.assertTrue(self.bag2.issubset(bag3))

    def test_eq(self):
        bag1_copy = Bag("a", "b", "b", "c")
        self.assertEqual(self.bag1, bag1_copy)
        bag1_copy.put("c")
        self.assertNotEqual(self.bag1, bag1_copy)


if __name__ == "__main__":
    unittest.main()
