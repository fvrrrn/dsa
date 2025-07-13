from typing import Callable


class BloomFilter:
    def __init__(
        self,
        f_len: int,
        bloom_filter: int = 0,
        *hash_fns: Callable[[str], int],
    ):
        self.f_len = BloomFilter.__round_power_2(f_len)
        self.mask = (1 << f_len) - 1
        self.filter = bloom_filter
        # cannot set default parameter to * and ** types
        self.hash_fns = (
            list(hash_fns)
            if hash_fns
            else [
                lambda s: hash1(s) & (self.f_len - 1),
                lambda s: hash2(s) & (self.f_len - 1),
            ]
        )

    def __str__(self):
        return bin(self.f_len)

    @staticmethod
    def __round_power_2(n: int) -> int:
        # 1 -> 1, 5 -> 8, 15 -> 16, 32 -> 32
        if n <= 1:
            return 1
        return 1 << (n - 1).bit_length()

    # TODO: remove after tests passed
    def hash1(self, str1: str) -> int:
        hash_value = 0
        power = 1
        for c in str1:
            hash_value += ord(c) * power
            power *= 17
        return hash_value & (self.f_len - 1)

    # TODO: remove after tests passed
    def hash2(self, str1: str) -> int:
        hash_value = 0
        power = 1
        for c in str1:
            hash_value += ord(c) * power
            power *= 223
        return hash_value & (self.f_len - 1)

    def add(self, str1: str):
        self.filter |= sum(1 << f(str1) for f in self.hash_fns)

    def is_value(self, str1: str) -> bool:
        return bool(self.filter & sum(1 << f(str1) for f in self.hash_fns))


def hash1(str1: str) -> int:
    return sum(ord(c) * (17**i) for i, c in enumerate(str1))


def hash2(str1: str) -> int:
    return sum(ord(c) * (223**i) for i, c in enumerate(str1))
