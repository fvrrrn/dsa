import unittest

from t3 import DynArray


class TestDynArrayMethods(unittest.TestCase):

    def setUp(self):
        self.array = DynArray()

    def test_insert_no_buffer_increase(self):
        for i in range(15):
            self.array.insert(i, i)
        self.assertEqual(len(self.array), 15)
        self.assertEqual(self.array.capacity, 16)
        self.array.insert(15, 99)
        self.assertEqual(len(self.array), 16)
        self.assertEqual(self.array.capacity, 16)
        self.assertEqual(self.array[15], 99)

    def test_insert_with_buffer_increase(self):
        for i in range(16):
            self.array.insert(i, i)
        self.array.insert(16, 99)
        self.assertEqual(len(self.array), 17)
        self.assertGreater(self.array.capacity, 16)
        self.assertEqual(self.array[16], 99)

    def test_insert_invalid_position(self):
        with self.assertRaises(IndexError):
            self.array.insert(-1, 5)
        with self.assertRaises(IndexError):
            self.array.insert(100, 5)

    def test_delete_no_buffer_decrease(self):
        for i in range(16):
            self.array.insert(i, i)
        self.array.delete(15)
        self.assertEqual(len(self.array), 15)
        self.assertEqual(self.array.capacity, 16)

    def test_delete_with_buffer_decrease(self):
        for i in range(32):
            self.array.insert(i, i)
        for _ in range(25):
            self.array.delete(len(self.array) - 1)
        self.assertEqual(len(self.array), 7)
        self.assertLess(self.array.capacity, 32)

    def test_delete_invalid_position(self):
        with self.assertRaises(IndexError):
            self.array.delete(-1)
        with self.assertRaises(IndexError):
            self.array.delete(100)


if __name__ == "__main__":
    unittest.main()
