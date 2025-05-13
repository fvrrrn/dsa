import unittest

from t4 import Stack


class TestStack(unittest.TestCase):
    def test_base_append_and_del(self):
        s = Stack()
        s.push(1)
        expect_pop = s.pop()
        expect_pop_2 = s.pop()
        self.assertEqual(expect_pop, 1)
        self.assertIsNone(expect_pop_2)

    def test_base_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push(1)
        s.push(1)
        s.push(1)
        self.assertEqual(s.size(), 4)
        s.pop()
        s.pop()
        s.pop()
        s.pop()
        self.assertEqual(s.size(), 0)

    def test_base_peek(self):
        s = Stack()
        s.push(96)
        s.push(97)
        s.push(98)
        s.push(99)
        self.assertEqual(s.peek(), 99)
        s.pop()
        self.assertEqual(s.peek(), 98)
        s.pop()
        self.assertEqual(s.peek(), 97)
        s.pop()
        self.assertEqual(s.peek(), 96)
        s.pop()
        self.assertIsNone(s.peek())
        s.pop()
        self.assertIsNone(s.peek())

    def test_base_pop(self):
        s = Stack()
        s.push(96)
        s.push(97)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.pop(), 97)
        self.assertEqual(s.pop(), 96)
        self.assertIsNone(s.pop())
        self.assertIsNone(s.pop())


if __name__ == "__main__":
    unittest.main()
