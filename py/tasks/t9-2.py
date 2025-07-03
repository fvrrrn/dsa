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


if __name__ == "__main__":
    unittest.main()
