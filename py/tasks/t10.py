from collections import defaultdict
from itertools import zip_longest
from typing import Dict, Generic, Iterator, TypeVar

T = TypeVar("T")


class PowerSet(Generic[T]):
    def __init__(self, *elements: T) -> None:
        self.elements: Dict[T, int] = defaultdict(int)
        for e in elements:
            self.put(e)

    def __len__(self) -> int:
        return len(self.elements)

    def size(self) -> int:
        return len(self)

    def put(self, element: T, value=1) -> int:
        self[element] = value
        return self[element]

    def get(self, element: T) -> bool:
        return element in self

    def remove(self, element: T) -> bool:
        return self.__delitem__(element)

    def __contains__(self, element: T) -> bool:
        # prevent creating key by checking if element in defaultdict
        return element in self.elements and self.elements[element] > 0

    def __getitem__(self, element: T) -> int:
        return self.elements[element]

    def __setitem__(self, element: T, value: int) -> int:
        self.elements[element] = value
        return self.elements[element]

    def __delitem__(self, element: T) -> bool:
        # will create and delete key
        flag = self.elements[element]
        del self.elements[element]
        return bool(flag)

    def intersection(self, set2: "PowerSet[T]") -> "PowerSet[T]":
        set3 = PowerSet()
        for e in self:
            if e in set2:
                set3.put(e)
        for e in set2:
            if e in self:
                set3.put(e)
        return set3

    def union(self, set2: "PowerSet[T]") -> "PowerSet[T]":
        set3 = PowerSet()
        for e in self:
            set3.put(e)
        for e in set2:
            set3.put(e)
        return set3

    def difference(self, set2: "PowerSet[T]") -> "PowerSet[T]":
        set3 = PowerSet()
        for e in self:
            if e not in set2:
                set3.put(e)
        for e in set2:
            if e not in self:
                set3.put(e)
        return set3

    def issubset(self, set2: "PowerSet[T]") -> bool:
        return all(e in self for e in set2)

    def __iter__(self) -> Iterator[T]:
        return iter(self.elements)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PowerSet):
            return False
        if len(self) != len(other):
            return False
        return all(e2 in self and e1 in other for e1, e2 in zip(self, other))

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def equals(self, set2: "PowerSet[T]") -> bool:
        return self == set2
