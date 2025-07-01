from typing import TypeVar

T = TypeVar("T")


class NativeDictionary[T]:
    def __init__(self, sz):
        self.size = sz
        self.slots: list[str | None] = [None] * self.size
        self.values: list[T | None] = [None] * self.size
        self.__modulo = 1234567891  # closest prime to 2**32 which is max int
        self.__base = 67  # 67 is the closest prime to 62 which is 23 lowercase latin letters + 23 uppercase + 10 digits
        self.__size = 0

    def hash_fun(self, key: str) -> int:
        hash_value = 0
        power = 1
        for c in reversed(key):
            hash_value = (hash_value + ord(c) * power) % self.__modulo
            power = (power * self.__base) % self.__modulo
        return hash_value

    def is_key(self, key: str) -> bool:
        return (
            self.slots[self.hash_fun(key) % self.size] is not None
            if self.__size > 0
            else False
        )

    def put(self, key: str, value: T) -> int | None:
        index = self.hash_fun(key) % self.size
        self.__size += self.slots[index] != key
        self.slots[index] = key
        self.values[index] = value
        return index

    def get(self, key: str) -> T | None:
        index = self.hash_fun(key) % self.size
        return self.values[index]

    def __len__(self) -> int:
        return self.__size

    def __setitem__(self, key: str, value: T) -> int | None:
        return self.put(key, value)

    def __getitem__(self, key: str) -> T | None:
        return self.get(key)
