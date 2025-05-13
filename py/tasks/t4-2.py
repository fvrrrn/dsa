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
# and then override its methods
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

    def min(self):
        return self.min_stack.peek()


class AvgStack_4_8:
    def __init__(self):
        self.stack = Stack[int]()
        self._sum = 0

    def pop(self):
        value = self.stack.pop()
        if isinstance(value, int):
            self._sum -= value
        return value

    def push(self, value: int):
        self.stack.push(value)
        self._sum += value

    def avg(self):
        if self.stack.size() == 0:
            return 0
        return self._sum / self.stack.size()


# because Python does not support `-` in file name
# and it is not enough to just `from "t4-2" import t4_5`
# it is easier to just put tests here


class TestStack2(unittest.TestCase):
    def test_t4_5(self):
        self.assertTrue(t4_5_and_4_6(""))

        self.assertFalse(t4_5_and_4_6("("))
        self.assertFalse(t4_5_and_4_6("{"))
        self.assertFalse(t4_5_and_4_6("["))

        self.assertFalse(t4_5_and_4_6(")"))
        self.assertFalse(t4_5_and_4_6("}"))
        self.assertFalse(t4_5_and_4_6("]"))

        self.assertFalse(t4_5_and_4_6("(]"))
        self.assertFalse(t4_5_and_4_6("{)"))
        self.assertFalse(t4_5_and_4_6("[}"))
        self.assertFalse(t4_5_and_4_6("({[})]"))

        self.assertTrue(t4_5_and_4_6("()"))
        self.assertTrue(t4_5_and_4_6("{}"))
        self.assertTrue(t4_5_and_4_6("[]"))
        self.assertTrue(t4_5_and_4_6("({[]})"))
        self.assertTrue(t4_5_and_4_6("([{}])"))

        self.assertFalse(t4_5_and_4_6("(()"))
        self.assertFalse(t4_5_and_4_6("({[})"))
        self.assertFalse(t4_5_and_4_6("([)]"))
        self.assertFalse(t4_5_and_4_6("{[)]}"))

    def test_min_stack_operations(self):
        min_stack = MinStack_4_7()

        self.assertIsNone(min_stack.min())

        min_stack.push(3)
        min_stack.push(2)
        min_stack.push(5)

        self.assertEqual(min_stack.min(), 2)

        self.assertEqual(min_stack.pop(), 5)
        self.assertEqual(min_stack.min(), 2)

        self.assertEqual(min_stack.pop(), 2)
        self.assertEqual(min_stack.min(), 3)

        min_stack.push(1)
        self.assertEqual(min_stack.min(), 1)

        self.assertEqual(min_stack.pop(), 1)
        self.assertEqual(min_stack.min(), 3)

        min_stack.pop()
        self.assertIsNone(min_stack.min())

        min_stack.push(3)
        min_stack.push(3)
        min_stack.push(3)
        self.assertEqual(min_stack.min(), 3)

        self.assertEqual(min_stack.pop(), 3)
        self.assertEqual(min_stack.min(), 3)
        self.assertEqual(min_stack.pop(), 3)
        self.assertEqual(min_stack.min(), 3)

        min_stack.pop()
        self.assertIsNone(min_stack.min())

    def test_avg_stack_operations(self):
        avg_stack = AvgStack_4_8()

        self.assertEqual(avg_stack.avg(), 0)

        avg_stack.push(3)
        self.assertEqual(avg_stack.avg(), 3.0)
        avg_stack.push(2)
        self.assertEqual(avg_stack.avg(), 2.5)
        avg_stack.push(5)
        self.assertEqual(avg_stack.avg(), 3.3333333333333335)

        self.assertEqual(avg_stack.pop(), 5)
        self.assertEqual(avg_stack.avg(), 2.5)

        self.assertEqual(avg_stack.pop(), 2)
        self.assertEqual(avg_stack.avg(), 3.0)

        avg_stack.push(1)
        self.assertEqual(avg_stack.avg(), 2.0)

        self.assertEqual(avg_stack.pop(), 1)
        self.assertEqual(avg_stack.avg(), 3.0)

        avg_stack.pop()
        self.assertEqual(avg_stack.avg(), 0)

        avg_stack.push(3)
        avg_stack.push(3)
        avg_stack.push(3)
        self.assertEqual(avg_stack.avg(), 3.0)


if __name__ == "__main__":
    unittest.main()
