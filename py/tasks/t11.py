class BloomFilter:
    def __init__(self, f_len: int):
        self.f_len = BloomFilter.__round_power_2(f_len)
        self.mask = (1 << f_len) - 1
        self.filter = 0

    @staticmethod
    def __round_power_2(n: int) -> int:
        # 1 -> 1, 5 -> 8, 15 -> 16, 32 -> 32
        if n <= 1:
            return 1
        return 1 << (n - 1).bit_length()

    def hash1(self, str1: str) -> int:
        hash_value = 0
        power = 1
        for c in str1:
            hash_value += ord(c) * power
            power *= 17
        return hash_value & (self.f_len - 1)

    def hash2(self, str1: str) -> int:
        hash_value = 0
        power = 1
        for c in str1:
            hash_value += ord(c) * power
            power *= 223
        return hash_value & (self.f_len - 1)

    def add(self, str1: str):
        self.filter |= 1 << self.hash1(str1)
        self.filter |= 1 << self.hash2(str1)

    def is_value(self, str1: str) -> bool:
        bit1 = (self.filter >> self.hash1(str1)) & 1
        bit2 = (self.filter >> self.hash2(str1)) & 1
        return bool(bit1 & bit2)
