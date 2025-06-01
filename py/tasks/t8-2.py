import unittest

from t8 import HashTable

# 8.3 is len(HashTable)


# 8.4
class DynHashTable:
    def __init__(self, size, step):
        self.slots = [None] * size
        self.__modulo = 1234567891
        self.__base = 67
        self.__size = 0
        self.size = size
        self.step = step

    def hash_fun(self, value: str) -> int:
        hash_value = 0
        power = 1
        for c in reversed(value):
            hash_value = (hash_value + ord(c) * power) % self.__modulo
            power = (power * self.__base) % self.__modulo
        return hash_value

    def seek_slot(self, value: str) -> int | None:
        index = self.hash_fun(value) % self.size
        for _ in range(self.size // self.step + 1):
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        if self.__size / self.size >= 0.75:
            self.__resize()

        match self.seek_slot(value):
            case None:
                return None
            case index:
                # increase only if element not in table already
                if self.slots[index] != value:
                    self.__size += 1
                self.slots[index] = value  # type: ignore cannot assign str to None
                return index

    def find(self, value) -> int | None:
        index = self.hash_fun(value) % self.size
        for _ in range(self.size // self.step + 1):
            if self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None

    def __resize(self):
        old_slots = [slot for slot in self.slots if slot is not None]
        self.size *= 2
        self.slots = [None] * self.size
        self.__size = 0
        for value in old_slots:
            self.put(value)

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        return (
            "{" + ", ".join(repr(item) for item in self.slots if item is not None) + "}"
        )


class TestHashTable(unittest.TestCase):
    def test_len_empty_table(self):
        ht = HashTable(sz=10, stp=1)
        self.assertEqual(len(ht), 0, "Empty table should have length 0")

    def test_len_after_one_put(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("one")
        self.assertEqual(len(ht), 1, "Table should have length 1 after one insertion")

    def test_len_after_duplicate_put(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("dup")
        ht.put("dup")
        self.assertEqual(len(ht), 1, "Inserting duplicate should not increase length")

    def test_len_after_duplicate_overflow(self):
        ht = HashTable(sz=2, stp=1)
        ht.put("dup")
        ht.put("dup")
        ht.put("dup")
        self.assertEqual(
            len(ht), 1, "Inserting duplicate overflow should not increase length"
        )

    def test_len_after_multiple_puts(self):
        ht = HashTable(sz=10, stp=1)
        ht.put("a")
        ht.put("b")
        ht.put("c")
        self.assertEqual(len(ht), 3, "Table should count unique slots filled")

    def test_len_after_failed_put(self):
        ht = HashTable(sz=3, stp=1)
        ht.put("x")
        ht.put("y")
        ht.put("z")
        index = ht.put("overflow")
        self.assertIsNone(index)
        self.assertEqual(len(ht), 3, "Length should not change after failed insertion")

    def test_basic_put_and_find(self):
        ht = DynHashTable(8, 1)
        index = ht.put("apple")
        self.assertIsNotNone(index)
        self.assertEqual(ht.find("apple"), index)

    def test_duplicate_insertion(self):
        ht = DynHashTable(8, 1)
        index1 = ht.put("banana")
        index2 = ht.put("banana")
        self.assertEqual(index1, index2)
        self.assertEqual(len(ht), 1)

    def test_collision_and_probing(self):
        ht = DynHashTable(4, 1)
        # Manually create a collision by adding different keys
        ht.put("key1")
        ht.put("key2")
        ht.put("key3")
        self.assertEqual(len(ht), 3)

    def test_auto_resize(self):
        ht = DynHashTable(4, 1)
        keys = ["a", "b", "c", "d"]
        for key in keys:
            ht.put(key)
        # This insert should trigger a resize (load factor > 0.75)
        ht.put("e")
        self.assertGreater(ht.size, 4)
        self.assertEqual(len(ht), 5)
        for key in keys + ["e"]:
            self.assertIsNotNone(ht.find(key))

    def test_resize_preserves_elements(self):
        ht = DynHashTable(2, 1)
        original_keys = [f"val{i}" for i in range(10)]
        for key in original_keys:
            ht.put(key)
        self.assertGreater(ht.size, 2)
        self.assertEqual(len(ht), len(original_keys))
        for key in original_keys:
            self.assertIsNotNone(ht.find(key))


if __name__ == "__main__":
    unittest.main()
