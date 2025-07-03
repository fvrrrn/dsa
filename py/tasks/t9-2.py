import unittest
from typing import Callable, Iterator, List, Literal, Tuple, TypeVar

from monads import Either, Just, Left, Maybe, Nothing, Right
from protocols import Comparable

# TODO: check typing.assert_never and class.__match_args__ = ()
K = TypeVar("K", bound=Comparable)
V = TypeVar("V")


# 9.5
class OrderedDictionary[K, V]:
    def __init__(self):
        self.tuples: List[Tuple[K, V]] = []

    def __len__(self) -> int:
        return len(self.tuples)

    def __compare(self, a: K, b: K) -> Literal[-1, 0, 1]:
        if a < b:  # type: ignore wtf
            return -1
        if a > b:  # type: ignore ">" not supported for types "K@OrderedDictionary" and "K@OrderedDictionary" [reportOperatorIssue]
            return 1
        return 0

    # TODO: add @overload __contains__(self, a: T)
    def __contains__(self, a: K) -> bool:
        match self.__binary_search(lambda t: self.__compare(t[0], a)):
            case Right():
                return True
            case Left():
                return False
            case _:
                assert False, "Unreachable"

    def __setitem__(self, key: K, value: V) -> Maybe[int]:
        match self.__binary_search(lambda t: self.__compare(t[0], key)):
            case Right(value=index):
                self.tuples[index] = (key, value)
                return Just(index)
            case Left(value=index):
                self.tuples.insert(index, (key, value))
                return Nothing()
            case _:
                assert False, "Unreachable"

    def __getitem__(self, key: K) -> Maybe[V]:
        match self.__binary_search(lambda t: self.__compare(t[0], key)):
            case Right(value=index):
                return Just(self.tuples[index][1])
            case Left():
                return Nothing()
            case _:
                assert False, "Unreachable"

    def __binary_search(
        self,
        predicate: Callable[[Tuple[K, V]], Literal[-1, 0, 1]],
        # either element index or insertion index
    ) -> Either[int, int]:
        left, right = 0, len(self.tuples) - 1
        while left <= right:
            mid_index = (left + right) // 2
            t = self.tuples[mid_index]
            match predicate(t):
                case -1:
                    right = mid_index - 1
                case 0:
                    return Right(mid_index)
                case 1:
                    left = mid_index + 1
        return Left(left)

    def __iter__(self) -> Iterator[Tuple[K, V]]:
        return iter(self.tuples)

    def __str__(self) -> str:
        return str(self.tuples)


class BitDictionary[T]:
    def __init__(self, sz=16):
        self.size = BitDictionary.__round_power_2(sz)
        # TODO: check what step optimization can be made with bits
        self.step = 1
        self.slots: list[str | None] = [None] * self.size
        self.values: list[T | None] = [None] * self.size
        self.__base = 64
        self.__size = 0

    @staticmethod
    def __round_power_2(n: int) -> int:
        # 1 -> 1, 5 -> 8, 15 -> 16, 32 -> 32
        if n <= 1:
            return 1
        return 1 << (n - 1).bit_length()

    def hash_fun(self, key: str) -> int:
        hash_value = 0
        power = 1
        for c in reversed(key):
            hash_value += ord(c) * power
            power *= self.__base
        return hash_value & (self.size - 1)

    def __slots_iter(self, key: str) -> Iterator[int]:
        # because size if power of 2
        start = self.hash_fun(key)
        for i in range(self.size):
            yield (start + i * self.step) & (self.size - 1)

    def seek_slot(self, key: str) -> int | None:
        for index in self.__slots_iter(key):
            if self.slots[index] == None or self.slots[index] == key:
                return index
        return None

    def is_key(self, key: str) -> bool:
        for index in self.__slots_iter(key):
            if self.slots[index] == key:
                return True
        return False

    # TODO: add Maybe[int] after server tests
    def put(self, key: str, value: T):
        if (index := self.seek_slot(key)) is not None:
            self.__size += self.slots[index] != key
            # TODO: with dynamic resizing change step on each self.size change
            # TODO: also __round_power_2
            self.slots[index] = key
            self.values[index] = value
            return index

    def get(self, key: str) -> T | None:
        for index in self.__slots_iter(key):
            if self.slots[index] == key:
                return self.values[index]

    def __len__(self) -> int:
        return self.__size

    def __setitem__(self, key: str, value: T) -> int | None:
        return self.put(key, value)

    def __getitem__(self, key: str) -> T | None:
        return self.get(key)

    def __delitem__(self, key: str) -> int | None:
        for index in self.__slots_iter(key):
            if self.slots[index] == key:
                self.values[index] = None
                self.slots[index] = None
                return index


class TestOrderedDictionary(unittest.TestCase):
    def test_insert_and_get(self):
        d = OrderedDictionary[str, int]()
        self.assertEqual(d["a"], Nothing())
        self.assertEqual(len(d), 0)

        self.assertEqual(d.__setitem__("b", 2), Nothing())
        self.assertEqual(len(d), 1)
        self.assertEqual(d["b"], Just(2))

        d["a"] = 1
        d["c"] = 3
        self.assertEqual(len(d), 3)
        self.assertEqual(d["a"], Just(1))
        self.assertEqual(d["c"], Just(3))

        self.assertEqual(d.__setitem__("a", 10), Just(2))
        self.assertEqual(d["a"], Just(10))

    def test_contains(self):
        d = OrderedDictionary[str, int]()
        d["foo"] = 42
        d["bar"] = 99
        self.assertTrue("foo" in d)
        self.assertTrue("bar" in d)
        self.assertFalse("baz" in d)

    def test_str(self):
        d = OrderedDictionary[str, int]()
        d["x"] = 1
        d["y"] = 2
        s = str(d)
        self.assertIn("x", s)
        self.assertIn("y", s)


class TestBitDictionary(unittest.TestCase):
    def test_put_and_get(self):
        d = BitDictionary[int]()
        d.put("101", 42)
        d.put("111", 84)
        self.assertEqual(d.get("101"), 42)
        self.assertEqual(d.get("111"), 84)
        self.assertIsNone(d.get("000"))

    def test_setitem_getitem(self):
        d = BitDictionary[int]()
        d["000"] = 100
        d["001"] = 200
        self.assertEqual(d["000"], 100)
        self.assertEqual(d["001"], 200)
        self.assertIsNone(d["010"])

    def test_replacement(self):
        d = BitDictionary[int]()
        d["001"] = 1
        d["001"] = 2
        self.assertEqual(d["001"], 2)
        self.assertEqual(len(d), 1)

    def test_is_key(self):
        d = BitDictionary[int]()
        d["111"] = 5
        self.assertTrue(d.is_key("111"))
        self.assertFalse(d.is_key("000"))

    def test_len(self):
        d = BitDictionary[int]()
        self.assertEqual(len(d), 0)
        d["0"] = 1
        d["1"] = 2
        self.assertEqual(len(d), 2)
        d["1"] = 3
        self.assertEqual(len(d), 2)

    def test_del(self):
        d = BitDictionary[int]()
        d["key"] = 123
        self.assertEqual(d["key"], 123)
        del d["key"]
        self.assertIsNone(d["key"])
        self.assertEqual(len(d), 1)


if __name__ == "__main__":
    unittest.main()
