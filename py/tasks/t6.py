import ctypes
from typing import Generic, Iterator, TypeVar, Union, overload

T = TypeVar("T")


class DynArray(Generic[T]):
    def __str__(self):
        return "[" + ", ".join(str(self._array[i]) for i in range(self._count)) + "]"

    def __init__(self):
        self._count = 0
        self._capacity = 16
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._count

    def __iter__(self) -> Iterator[T]:
        for i in range(0, self._count):
            yield self._array[i]

    def __reversed__(self) -> Iterator[T]:
        for i in range(self._count - 1, 0, -1):
            yield self._array[i]

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    @overload
    def __getitem__(self, i: int) -> T: ...

    @overload
    def __getitem__(self, i: slice) -> list[T]: ...

    def __getitem__(self, i) -> Union[T, list[T]]:
        if isinstance(i, slice):
            start, stop, step = i.indices(self._count)
            return [self._array[i] for i in range(start, stop, step)]
        if i < 0 or i >= self._count:
            raise IndexError("Index is out of bounds")
        return self._array[i]

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._count):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, itm):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._count] = itm
        self._count += 1

    def insert(self, i: int, itm: T):
        if i < 0 or i > self._count:
            raise IndexError("Index is out of bounds")
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._count, i, -1):
            self._array[j] = self._array[j - 1]
        self._array[i] = itm
        self._count += 1

    def delete(self, i: int) -> T:
        if i < 0 or i >= self._count:
            raise IndexError("Index is out of bounds")
        value = self._array[i]
        for j in range(i, self._count - 1):
            self._array[j] = self._array[j + 1]
        self._count -= 1
        if self._count < 0.5 * self._capacity:
            new_capacity = max(int(self._capacity / 1.5), 16)
            self._resize(new_capacity)
        return value


class Deque(Generic[T]):
    def __init__(self):
        self.array = DynArray[T]()

    def addFront(self, item: T):
        self.array.insert(0, item)

    def addTail(self, item: T):
        self.array.append(item)

    def removeFront(self) -> T | None:
        try:
            return self.array.delete(0)
        except IndexError:
            return None

    def removeTail(self):
        try:
            return self.array.delete(len(self.array) - 1)
        except IndexError:
            return None

    def size(self):
        return len(self.array)

    def __iter__(self) -> Iterator[T]:
        return iter(self.array)

    def is_palindrome(self):
        mid = len(self.array) // 2
        return all(
            a == b for a, b in zip(self.array[:mid], reversed(self.array[-mid:]))
        )
