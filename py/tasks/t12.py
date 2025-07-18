from math import gcd
from typing import Callable, Generic, Hashable, Iterator, Protocol, Tuple, TypeVar, cast

from monads import Just, Maybe, Nothing

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")
G = TypeVar("G", covariant=True)


# TODO: use DynHashTable example when moving NativeDictionary to demonstration
# that way __setitem__ is more likely to record element


# Euler's totient function always returns at least 1 int if n > 1
def coprime(n: int) -> int:
    for i in range(1, n):
        if gcd(i, n) == 1:
            return i
    assert False, f"No coprime step found for size={n}"


def polynomial_hash(s: str, base=67, mod=1234567891) -> int:
    h = 0
    for c in s:
        h = (h * base + ord(c)) % mod
    return h


class NativeDictionary(Generic[K, V]):
    def __init__(self, sz, hasher: Callable[[K], int]):
        self.size = sz
        self.step = coprime(sz) if self.size > 1 else 1
        self.slots: list[K | None] = [None] * self.size
        self.values: list[V | None] = [None] * self.size
        self.__size = 0
        self.hasher = hasher

    def __slots_iter(self, key: K) -> Iterator[int]:
        start = self.hasher(key) % self.size
        for i in range(self.size // gcd(self.size, self.step)):
            yield (start + i * self.step) % self.size

    def seek_slot(self, key: K) -> int | None:
        for index in self.__slots_iter(key):
            if self.slots[index] == None or self.slots[index] == key:
                return index
        return None

    # TODO: add Maybe[int] after server tests
    def put(self, key: K, value: V):
        if (index := self.seek_slot(key)) is not None:
            self.__size += self.slots[index] != key
            # TODO: with dynamic resizing change step on each self.size change
            self.slots[index] = key
            self.values[index] = value
            return index

    def __contains__(self, key: K) -> Maybe[int]:
        for index in self.__slots_iter(key):
            if self.slots[index] == key:
                return Just(index)
        return Nothing()

    def get(self, key: K) -> Maybe[V]:
        match self.__contains__(key):
            case Just(value_index):
                return Just(cast(V, self.values[value_index]))
            case _:
                return Nothing()

    def __len__(self) -> int:
        return self.__size

    def __setitem__(self, key: K, value: V) -> int | None:
        return self.put(key, value)

    def __getitem__(self, key: K) -> Maybe[V]:
        return self.get(key)


class NativeCache(Generic[K, V]):
    def __init__(self, sz, getter: Callable[[K], V], hasher: Callable[[K], int]):
        self.size = sz
        self.dict = NativeDictionary[K, Tuple[V, int]](sz, hasher)
        self.getter = getter

    def __getitem__(self, key: K) -> Maybe[V]:
        maybe_index = self.dict.__contains__(key)
        match maybe_index:
            case Just(index):
                self.dict.slots[index] += 1  # type: ignore
                return Just(self.dict.values[index][0])  # type: ignore
            case _:
                value = self.getter(key)
                self.dict.put(key, (value, 0))
                return Just(value)
