import unittest

from t6 import Deque


class TestDeque(unittest.TestCase):
    def test_addFront_single_element(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.size(), 0)

    def test_addTail_single_element(self):
        deque = Deque()
        deque.addTail(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.removeTail(), 1)
        self.assertEqual(deque.size(), 0)

    def test_addFront_multiple_elements(self):
        deque = Deque()
        deque.addFront(1)
        deque.addFront(2)
        deque.addFront(3)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.removeFront(), 3)
        self.assertEqual(deque.removeFront(), 2)
        self.assertEqual(deque.removeFront(), 1)

    def test_addTail_multiple_elements(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.removeTail(), 3)
        self.assertEqual(deque.removeTail(), 2)
        self.assertEqual(deque.removeTail(), 1)

    def test_removeFront_empty_deque(self):
        deque = Deque()
        self.assertIsNone(deque.removeFront())

    def test_removeTail_empty_deque(self):
        deque = Deque()
        self.assertIsNone(deque.removeTail())

    def test_mixed_operations(self):
        deque = Deque()
        deque.addTail(1)
        deque.addFront(2)
        deque.addTail(3)
        deque.addFront(4)
        self.assertEqual(deque.size(), 4)
        self.assertEqual(deque.removeFront(), 4)
        self.assertEqual(deque.removeTail(), 3)
        self.assertEqual(deque.removeFront(), 2)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.size(), 0)

    def test_iterator(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        elements = list(deque)
        self.assertEqual(elements, [1, 2, 3])

    def test_empty_deque(self):
        dq = Deque[str]()
        self.assertTrue(dq.is_palindrome())

    def test_single_element(self):
        dq = Deque[str]()
        dq.addTail("a")
        self.assertTrue(dq.is_palindrome())

    def test_two_identical_elements(self):
        dq = Deque[str]()
        dq.addTail("a")
        dq.addTail("a")
        self.assertTrue(dq.is_palindrome())

    def test_two_different_elements(self):
        dq = Deque[str]()
        dq.addTail("a")
        dq.addTail("b")
        self.assertFalse(dq.is_palindrome())

    def test_even_length_palindrome(self):
        dq = Deque[str]()
        for char in "abba":
            dq.addTail(char)
        self.assertTrue(dq.is_palindrome())

    def test_even_length_non_palindrome(self):
        dq = Deque[str]()
        for char in "abca":
            dq.addTail(char)
        self.assertFalse(dq.is_palindrome())

    def test_odd_length_palindrome(self):
        dq = Deque[str]()
        for char in "racecar":
            dq.addTail(char)
        self.assertTrue(dq.is_palindrome())

    def test_odd_length_non_palindrome(self):
        dq = Deque[str]()
        for char in "hello":
            dq.addTail(char)
        self.assertFalse(dq.is_palindrome())

    def test_numeric_palindrome(self):
        dq = Deque[int]()
        for num in [1, 2, 3, 2, 1]:
            dq.addTail(num)
        self.assertTrue(dq.is_palindrome())

    def test_numeric_non_palindrome(self):
        dq = Deque[int]()
        for num in [1, 2, 3, 4, 5]:
            dq.addTail(num)
        self.assertFalse(dq.is_palindrome())

    def test_mixed_data_types(self):
        dq = Deque[object]()
        dq.addTail("a")
        dq.addTail(1)
        dq.addTail("a")
        self.assertTrue(dq.is_palindrome())

        dq = Deque[object]()
        dq.addTail("a")
        dq.addTail(1)
        dq.addTail("b")
        self.assertFalse(dq.is_palindrome())


if __name__ == "__main__":
    unittest.main()
