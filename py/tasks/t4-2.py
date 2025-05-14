import unittest
from dataclasses import dataclass
from typing import Generic, Literal, TypeVar, Union

from t4 import Stack

T = TypeVar("T")


class Maybe(Generic[T]):
    pass


@dataclass(frozen=True)
class Just(Maybe[T]):
    value: T


@dataclass(frozen=True)
class Nothing(Maybe[T]):
    pass


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


class RPNEvaluator_4_9:
    def __init__(self):
        self.operators = Stack[Literal["+", "-", "*", "/", "="]]()
        self.operands = Stack[Maybe[int]]()

    def append(self, s: str) -> Union[None, Maybe[int]]:
        for c in s:
            match c:
                case "+" | "-" | "*" | "/" | "=":
                    self.operators.push(c)
                case _ if c.isdigit():
                    self.operands.push(Just(int(c)))

            match len(self.operators), len(self.operands):
                case 0, _:
                    pass
                case _, 0:
                    pass
                case _, 1:
                    pass
                case _, _:
                    maybeB = self.operands.pop()
                    maybeA = self.operands.pop()
                    operator = self.operators.pop()
                    match maybeA, operator, maybeB:
                        case Just(a), "+", Just(b):
                            self.operands.push(Just(a + b))
                        case Just(a), "-", Just(b):
                            self.operands.push(Just(a - b))
                        case Just(a), "*", Just(b):
                            self.operands.push(Just(a * b))
                        case Just(a), "/", Just(b):
                            match b:
                                case 0:
                                    self.operands.push(Nothing())
                                case _:
                                    # although technically it is possible to store floating-point numbers
                                    # I decided not to by strictly using integers as the task required
                                    self.operands.push(Just(a // b))
                        case _, "=", _:
                            return self.operands.pop()


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

    def test_rpn_operations(self):
        evaluator = RPNEvaluator_4_9()

        evaluator.append("12+")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.assertEqual(value, 3)
            case Nothing():
                self.fail("Result should not be Nothing.")

        evaluator.append("12-")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.assertEqual(value, -1)
            case Nothing():
                self.fail("Result should not be Nothing.")

        evaluator.append("22*")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.assertEqual(value, 4)
            case Nothing():
                self.assertEqual(result, Nothing())

        evaluator.append("42/")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.assertEqual(value, 2)
            case Nothing():
                self.fail("Result should not be Nothing.")

        evaluator.append("01/")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.assertEqual(value, 0)
            case Nothing():
                self.fail("Result should not be Nothing.")

        evaluator.append("00/")
        result = evaluator.operands.pop()
        match result:
            case Just(value):
                self.fail("Result should be Nothing due to division by zero.")
            case Nothing():
                self.assertEqual(result, Nothing())

        evaluator.append("82+5*9+")
        result = evaluator.append("=")
        match result:
            case Just(value):
                self.assertEqual(value, 59)
            case Nothing():
                self.fail("Result should not be Nothing.")


if __name__ == "__main__":
    unittest.main()
