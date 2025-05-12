import unittest

from t3 import DynArray


class TestDynArray(unittest.TestCase):
    def test_initialization(self):
        da = DynArray()
        self.assertEqual(len(da), 0)
        self.assertEqual(da.capacity, 16)

    def test_append(self):
        da = DynArray()
        da.append(10)
        self.assertEqual(len(da), 1)
        self.assertEqual(da[0], 10)

        for i in range(15):
            da.append(i)
        self.assertEqual(len(da), 16)
        self.assertEqual(da.capacity, 16)

        da.append(100)
        self.assertEqual(len(da), 17)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da[16], 100)

    def test_getitem(self):
        da = DynArray()
        da.append(1)
        da.append(2)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 2)
        with self.assertRaises(IndexError):
            _ = da[2]

    def test_resize(self):
        da = DynArray()
        for i in range(16):
            da.append(i)
        self.assertEqual(len(da), 16)
        self.assertEqual(da.capacity, 16)

        da.append(100)
        self.assertEqual(len(da), 17)
        self.assertEqual(da.capacity, 32)

    def test_insert(self):
        da = DynArray()
        for i in range(5):
            da.append(i)
        da.insert(2, 99)
        self.assertEqual(len(da), 6)
        self.assertEqual(da[2], 99)
        self.assertEqual(da[3], 2)

        with self.assertRaises(IndexError):
            da.insert(10, 100)

        with self.assertRaises(IndexError):
            da.insert(20, 200)

        da.insert(0, -1)
        self.assertEqual(len(da), 7)
        self.assertEqual(da[0], -1)
        self.assertEqual(da[1], 0)

        da.insert(len(da), 999)
        self.assertEqual(len(da), 8)
        self.assertEqual(da[7], 999)

        for i in range(8, 16):
            da.insert(len(da), i)
        da.insert(16, 500)
        self.assertEqual(len(da), 17)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da[16], 500)

    def test_delete(self):
        da = DynArray()
        for i in range(32):
            da.append(i)

        da.delete(10)
        self.assertEqual(len(da), 31)
        self.assertEqual(da[10], 11)

        for _ in range(24):
            da.delete(0)

        self.assertEqual(len(da), 7)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da[0], 25)

        with self.assertRaises(IndexError):
            da.delete(9)


if __name__ == "__main__":
    unittest.main()
