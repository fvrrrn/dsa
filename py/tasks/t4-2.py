import unittest
from typing import Generic

from t4 import Stack


def t4_5_and_4_6(brackets: str) -> bool:
    mapped_brackets = {"(": ")", "{": "}", "[": "]"}
    s = Stack[str]()
    for bracket in brackets:
        match mapped_brackets.get(bracket):
            # bracket is closing
            case None:
                if mapped_brackets.get(s.pop() or "") != bracket:
                    return False
            # bracket is opening
            case _:
                s.push(bracket)
    return s.size() == 0


# while I could inherit `Stack`
# I felt like creating a simple class to illustrate the solution
class MinStack_4_7:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def pop(self):
        value = self.stack.pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value

    def push(self, value):
        self.stack.push(value)
        if len(self.min_stack) == 0 or value <= self.min_stack.peek():
            self.min_stack.push(value)

    def peek(self):
        if self.stack.size() > 0:
            return self.stack.peek()
        else:
            return None

    def min(self):
        return self.min_stack.peek()


# because Python does not support `-` in file name
# and it is not enough to just `from "t4-2" import t4_5`
# it is easier to just put tests here


class TestStack2(unittest.TestCase):
    def test_t4_5(self):
        """
        Tests the t4_5 function for various cases:
        - Empty string
        - Single opening/closing brackets
        - Mismatched brackets
        - Properly nested brackets
        - Unbalanced brackets
        """
        # Empty string
        self.assertTrue(t4_5_and_4_6(""))

        # Single opening bracket
        self.assertFalse(t4_5_and_4_6("("))
        self.assertFalse(t4_5_and_4_6("{"))
        self.assertFalse(t4_5_and_4_6("["))

        # Single closing bracket
        self.assertFalse(t4_5_and_4_6(")"))
        self.assertFalse(t4_5_and_4_6("}"))
        self.assertFalse(t4_5_and_4_6("]"))

        # Mismatched brackets
        self.assertFalse(t4_5_and_4_6("(]"))
        self.assertFalse(t4_5_and_4_6("{)"))
        self.assertFalse(t4_5_and_4_6("[}"))
        self.assertFalse(t4_5_and_4_6("({[})]"))

        # Properly nested brackets
        self.assertTrue(t4_5_and_4_6("()"))
        self.assertTrue(t4_5_and_4_6("{}"))
        self.assertTrue(t4_5_and_4_6("[]"))
        self.assertTrue(t4_5_and_4_6("({[]})"))
        self.assertTrue(t4_5_and_4_6("([{}])"))

        # Unbalanced brackets
        self.assertFalse(t4_5_and_4_6("(()"))
        self.assertFalse(t4_5_and_4_6("({[})"))
        self.assertFalse(t4_5_and_4_6("([)]"))
        self.assertFalse(t4_5_and_4_6("{[)]}"))

    def test_min_stack_operations(self):
        min_stack = MinStack_4_7()

        # Test min is none
        self.assertIsNone(min_stack.min())

        # Test push and peek operations
        min_stack.push(3)
        self.assertEqual(min_stack.peek(), 3)
        min_stack.push(2)
        self.assertEqual(min_stack.peek(), 2)
        min_stack.push(5)
        self.assertEqual(min_stack.peek(), 5)

        # Test min after pushing elements
        self.assertEqual(min_stack.min(), 2)

        # Test pop and check min value after popping
        self.assertEqual(min_stack.pop(), 5)
        self.assertEqual(min_stack.min(), 2)

        # Pop 2
        self.assertEqual(min_stack.pop(), 2)
        self.assertEqual(min_stack.min(), 3)

        # Push 1 and test min
        min_stack.push(1)
        self.assertEqual(min_stack.min(), 1)

        # Pop 1
        self.assertEqual(min_stack.pop(), 1)
        self.assertEqual(min_stack.min(), 3)

        # Test on empty stack (peek and min should return None)
        min_stack.pop()  # Popped 3
        self.assertIsNone(min_stack.peek())
        self.assertIsNone(min_stack.min())

        # Test pushing equal elements
        min_stack.push(3)
        min_stack.push(3)
        min_stack.push(3)
        self.assertEqual(min_stack.min(), 3)

        # Pop and check min again
        self.assertEqual(min_stack.pop(), 3)
        self.assertEqual(min_stack.min(), 3)
        self.assertEqual(min_stack.pop(), 3)
        self.assertEqual(min_stack.min(), 3)

        # Pop and check min is none
        min_stack.pop()
        self.assertIsNone(min_stack.min())


if __name__ == "__main__":
    unittest.main()
