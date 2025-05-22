import unittest
from typing import Any, Generic, Iterator, Literal, Optional, Protocol, TypeVar

from t7 import OrderedList


class Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool: ...
    def __ne__(self, other: Any, /) -> bool: ...
    def __lt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


def is_comparable(obj: Any) -> bool:
    try:
        _ = obj < obj
        _ = obj <= obj
        _ = obj > obj
        _ = obj >= obj
        _ = obj == obj
        return True
    except (TypeError, AttributeError):
        return False


T = TypeVar("T", bound=Comparable)


def t7_8(ol: OrderedList[T]):
    dedupedOl = OrderedList(ol.is_asc)
    iterator = iter(ol)
    # because list is a collection of Comparables and `None` not supporting <=, >= etc.
    # currentValue can be safely set to `None` because there are no elements within list that are `None`
    # however if `None` can be a value of a list, I should do `class NeverEqual: __eq__() -> False __nq__() -> True`
    currentValue = None
    for value in iterator:
        if value != currentValue:
            # NOTE: instead of O(n) or O(n*lg n) `add` use O(1) `unsafe_append` because order is already preserved
            dedupedOl.add(value)
            currentValue = value
    return dedupedOl


class TestOrderedList(unittest.TestCase):
    def test_t7_8(self):
        ol = OrderedList(asc=False)
        deduped = t7_8(ol)
        result = list(deduped)
        self.assertEqual(result, [])

        ol = OrderedList(False, 1)
        deduped = t7_8(ol)
        result = list(deduped)
        self.assertEqual(result, [1])

        ol = OrderedList(asc=False)
        for val in [5, 5, 4, 4, 3, 2, 2, 1]:
            ol.add(val)
        deduped = t7_8(ol)
        result = list(deduped)
        self.assertEqual(result, [5, 4, 3, 2, 1])

        ol = OrderedList(asc=True)
        for val in [1, 1, 2, 2, 2, 3, 4, 4, 5]:
            ol.add(val)

        deduped = t7_8(ol)
        result = list(deduped)

        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
