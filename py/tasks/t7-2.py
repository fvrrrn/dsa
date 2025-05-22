import unittest
from collections import defaultdict
from typing import (
    Any,
    Callable,
    Generic,
    Iterator,
    Literal,
    Optional,
    Protocol,
    TypeVar,
)

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
        # hi I've got your note about not using try/catch
        # I completely agree (hence monads.py in the root directory)
        # however in this particular case it is the only way to check if a value has comparability
        # checking v.__eq__ is Callable or
        # hasattr('__eq__') not working :/
        _ = obj < obj
        _ = obj <= obj
        _ = obj > obj
        _ = obj >= obj
        _ = obj == obj
        return True
    except (TypeError, AttributeError):
        return False


# TODO: covariant=True causes errors, check on this later
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
            dedupedOl.unsafe_append(value)
            currentValue = value
    return dedupedOl


class IteratorStrategy(Protocol[T]):
    def __iter__(self) -> Iterator[T]: ...


class ConcreteIteratorStrategyAscending(IteratorStrategy):
    def __init__(self, ol: OrderedList[T]):
        self.list = ol

    def __iter__(self):
        match self.list.is_asc:
            case True:
                return iter(self.list)
            case False:
                return reversed(self.list)


class ConcreteIteratorStrategyDescending(IteratorStrategy):
    def __init__(self, ol: OrderedList[T]):
        self.list = ol

    def __iter__(self):
        match self.list.is_asc:
            case True:
                return reversed(self.list)
            case False:
                return iter(self.list)


def strategyByOrder(asc: bool) -> Callable[[OrderedList[T]], IteratorStrategy[T]]:
    match asc:
        case True:
            return ConcreteIteratorStrategyAscending
        case False:
            return ConcreteIteratorStrategyDescending


# TODO: rename IteratorStrategy to MergeStrategy and put compare in it
def compare(asc: bool, v1: T, v2: T) -> bool:
    match asc:
        case True:
            return v1 <= v2
        case False:
            return v1 >= v2


# 1. pick merged list order strategy `asc` (ascending/descending)
# 2. pick accorning iterator for each list
# for OrderedList(True, 1,2,3) it is iter() if asc=True
# for OrderedList(False, 3,2,1) it is reversed() if asc=True
# and vice versa
# 3. create pointers at the start of those iterators (e.g. [from 1,2, to 3], [to 3,2,from 1]) for asc=True)
# 4. compare pointers' values by strategy (<= for asc, >= for desc)
def t7_9(ol1: OrderedList[T], ol2: OrderedList[T], asc: bool):
    iteratorStrategy = strategyByOrder(asc)
    merged = OrderedList[T](asc=asc)
    iterator1 = iter(iteratorStrategy(ol1))
    pointer1 = next(iterator1, None)
    iterator2 = iter(iteratorStrategy(ol2))
    pointer2 = next(iterator2, None)
    while True:
        match pointer1, pointer2:
            case None, None:
                return merged
            case _, None:
                merged.unsafe_append(pointer1)
                pointer1 = next(iterator1, None)
            case None, _:
                merged.unsafe_append(pointer2)
                pointer2 = next(iterator2, None)
            case _, _:
                if compare(asc, pointer2, pointer1):
                    merged.unsafe_append(pointer2)
                    pointer2 = next(iterator2, None)
                else:
                    merged.unsafe_append(pointer1)
                    pointer1 = next(iterator1, None)


# task 7.10 is OrderedList.__contains__


def t7_11(ol: OrderedList[T]) -> Optional[T]:
    if len(ol) == 0:
        return None

    frequencyDict = defaultdict(int)
    # sorting dict by desc and picking first element is less efficient
    max_count = 0
    result: Optional[T] = None

    for value in ol:
        frequencyDict[value] += 1
        if frequencyDict[value] > max_count:
            max_count = frequencyDict[value]
            result = value

    return result


# 7.12
class OrderedDynArray(Generic[T]):
    def __init__(self, asc: bool = True):
        self.__array: list[T] = []
        self.__ascending = asc

    def _compare(self, a: T, b: T) -> Literal[-1, 0, 1]:
        if a < b:
            return -1 if self.__ascending else 1
        if a > b:
            return 1 if self.__ascending else -1
        return 0

    def add(self, item: T):
        if not self.__array:
            self.__array.append(item)
            return

        left, right = 0, len(self.__array)
        while left < right:
            mid = (left + right) // 2
            cmp = self._compare(item, self.__array[mid])
            if cmp < 0:
                right = mid
            else:
                left = mid + 1
        self.__array.insert(left, item)

    def find(self, item: T) -> int:
        left, right = 0, len(self.__array) - 1
        while left <= right:
            mid = (left + right) // 2
            cmp = self._compare(item, self.__array[mid])
            if cmp == 0:
                return mid
            elif cmp < 0:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def __getitem__(self, i):
        return self.__array[i]

    def __len__(self):
        return len(self.__array)

    def __iter__(self):
        return iter(self.__array)

    def __reversed__(self):
        return reversed(self.__array)


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

    def test_merge_both_nonempty_ascending(self):
        ol1 = OrderedList(asc=True)
        ol2 = OrderedList(asc=True)
        for val in [1, 3, 5]:
            ol1.add(val)
        for val in [2, 4, 6]:
            ol2.add(val)

        merged = t7_9(ol1, ol2, asc=True)
        result = list(merged)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_merge_both_nonempty_descending(self):
        ol1 = OrderedList(asc=False)
        ol2 = OrderedList(asc=False)
        for val in [5, 3, 1]:
            ol1.add(val)
        for val in [6, 4, 2]:
            ol2.add(val)

        merged = t7_9(ol1, ol2, asc=False)
        result = list(merged)
        self.assertEqual(result, [6, 5, 4, 3, 2, 1])

    def test_merge_both_nonempty_ascending_descending(self):
        ol1 = OrderedList(asc=False)
        ol2 = OrderedList(asc=True)
        for val in [5, 3, 1]:
            ol1.add(val)
        for val in [1, 2, 3]:
            ol2.add(val)

        merged = t7_9(ol1, ol2, asc=True)
        result = list(merged)
        self.assertEqual(result, [1, 1, 2, 3, 3, 5])

    def test_merge_one_empty(self):
        ol1 = OrderedList(asc=True)
        ol2 = OrderedList(asc=True)
        for val in [1, 2, 3]:
            ol1.add(val)
        # ol2 remains empty

        merged = t7_9(ol1, ol2, asc=True)
        result = list(merged)
        self.assertEqual(result, [1, 2, 3])

    def test_merge_both_empty(self):
        ol1 = OrderedList(asc=True)
        ol2 = OrderedList(asc=True)
        merged = t7_9(ol1, ol2, asc=True)
        result = list(merged)
        self.assertEqual(result, [])

    def test_merge_duplicates(self):
        ol1 = OrderedList(asc=True)
        ol2 = OrderedList(asc=True)
        for val in [1, 2, 3]:
            ol1.add(val)
        for val in [2, 3, 4]:
            ol2.add(val)

        merged = t7_9(ol1, ol2, asc=True)
        result = list(merged)
        self.assertEqual(result, [1, 2, 2, 3, 3, 4])

    def test_empty_sublist(self):
        main = OrderedList(asc=True)
        for v in [1, 2, 3]:
            main.add(v)

        sub = OrderedList(asc=True)
        self.assertTrue(sub in main)

    def test_exact_match(self):
        main = OrderedList(asc=True)
        for v in [1, 2, 3]:
            main.add(v)

        sub = OrderedList(asc=True)
        for v in [1, 2, 3]:
            sub.add(v)

        self.assertTrue(sub in main)

    def test_sublist_match_middle(self):
        main = OrderedList(asc=True)
        for v in [1, 2, 3, 4, 5]:
            main.add(v)

        sub = OrderedList(asc=True)
        for v in [3, 4]:
            sub.add(v)

        self.assertTrue(sub in main)

    def test_sublist_not_present(self):
        main = OrderedList(asc=True)
        for v in [1, 2, 3, 4, 5]:
            main.add(v)

        sub = OrderedList(asc=True)
        for v in [2, 4]:
            sub.add(v)

        self.assertFalse(sub in main)

    def test_sublist_larger_than_main(self):
        main = OrderedList(asc=True)
        for v in [1, 2]:
            main.add(v)

        sub = OrderedList(asc=True)
        for v in [1, 2, 3]:
            sub.add(v)

        self.assertFalse(sub in main)

    def test_empty_main_non_empty_sub(self):
        main = OrderedList(asc=True)

        sub = OrderedList(asc=True)
        sub.add(1)

        self.assertFalse(sub in main)

    def test_direction_mismatch(self):
        main = OrderedList(asc=True)
        for v in [1, 2, 3, 4, 5]:
            main.add(v)

        sub = OrderedList(asc=False)
        for v in [3, 2]:
            sub.add(v)

        self.assertFalse(sub in main)

    def test_descending_contains(self):
        main = OrderedList(asc=False)
        for v in [5, 4, 3, 2, 1]:
            main.add(v)

        sub = OrderedList(asc=False)
        for v in [4, 3, 2]:
            sub.add(v)

        self.assertTrue(sub in main)

    def test_empty_ordered_list(self):
        ol = OrderedList(asc=True)
        self.assertIsNone(t7_11(ol))

    def test_single_element(self):
        ol = OrderedList(asc=True)
        ol.add(42)
        self.assertEqual(t7_11(ol), 42)

    def test_multiple_unique_elements(self):
        ol = OrderedList(asc=True)
        for v in [1, 2, 3, 4, 5]:
            ol.add(v)
        self.assertIn(t7_11(ol), [1, 2, 3, 4, 5])  # all appear once

    def test_clear_most_common(self):
        ol = OrderedList(asc=True)
        for v in [1, 2, 2, 3, 3, 3, 4]:
            ol.add(v)
        self.assertEqual(t7_11(ol), 3)

    def test_tie_returns_first_encountered(self):
        ol = OrderedList(asc=True)
        for v in [1, 2, 2, 3, 3]:
            ol.add(v)
        result = t7_11(ol)
        self.assertIn(result, [2, 3])  # Either 2 or 3 is acceptable in a tie

    def test_descending_order(self):
        ol = OrderedList(asc=False)
        for v in [5, 4, 4, 3, 2]:
            ol.add(v)
        self.assertEqual(t7_11(ol), 4)

    def test_add_ascending(self):
        arr = OrderedDynArray[int](asc=True)
        for val in [5, 1, 3, 2, 4]:
            arr.add(val)
        self.assertEqual(list(arr), [1, 2, 3, 4, 5])

    def test_add_descending(self):
        arr = OrderedDynArray[int](asc=False)
        for val in [2, 4, 1, 3, 5]:
            arr.add(val)
        self.assertEqual(list(arr), [5, 4, 3, 2, 1])

    def test_find_existing_ascending(self):
        arr = OrderedDynArray[int](asc=True)
        for val in [3, 1, 4, 2]:
            arr.add(val)
        self.assertEqual(arr.find(1), 0)
        self.assertEqual(arr.find(3), 2)
        self.assertEqual(arr.find(4), 3)

    def test_find_existing_descending(self):
        arr = OrderedDynArray[int](asc=False)
        for val in [1, 3, 2, 4]:
            arr.add(val)
        self.assertEqual(arr.find(4), 0)
        self.assertEqual(arr.find(3), 1)
        self.assertEqual(arr.find(1), 3)

    def test_find_not_existing(self):
        arr = OrderedDynArray[int](asc=True)
        for val in [10, 20, 30]:
            arr.add(val)
        self.assertEqual(arr.find(25), -1)
        self.assertEqual(arr.find(5), -1)
        self.assertEqual(arr.find(100), -1)

    def test_empty_find(self):
        arr = OrderedDynArray[int](asc=True)
        self.assertEqual(arr.find(1), -1)

    def test_add_duplicates(self):
        arr = OrderedDynArray[int](asc=True)
        for val in [2, 1, 2, 3, 2]:
            arr.add(val)
        self.assertEqual(list(arr), [1, 2, 2, 2, 3])
        self.assertIn(arr.find(2), [1, 2, 3])  # any of the 2s is acceptable


if __name__ == "__main__":
    unittest.main()
