import unittest

from t6 import Deque


def t6_6(brackets: str) -> bool:
    mapped_brackets = {"(": ")", "{": "}", "[": "]"}
    d = Deque[str]()

    for bracket in brackets:
        if bracket in mapped_brackets:
            d.addTail(bracket)
        else:
            last_open = d.removeTail()
            if last_open is None or mapped_brackets.get(last_open) != bracket:
                return False

    return d.size() == 0


class TestBalancedBrackets(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(t6_6(""))

    def test_single_pair(self):
        self.assertTrue(t6_6("()"))
        self.assertTrue(t6_6("[]"))
        self.assertTrue(t6_6("{}"))

    def test_multiple_pairs(self):
        self.assertTrue(t6_6("()[]{}"))
        self.assertTrue(t6_6("({[]})"))

    def test_unbalanced_missing_closing(self):
        self.assertFalse(t6_6("("))
        self.assertFalse(t6_6("({["))

    def test_unbalanced_wrong_order(self):
        self.assertFalse(t6_6("([)]"))
        self.assertFalse(t6_6("{(})"))

    def test_unbalanced_extra_closing(self):
        self.assertFalse(t6_6("())"))
        self.assertFalse(t6_6("()]"))

    def test_long_balanced(self):
        self.assertTrue(t6_6("((({{{[[[]]]}}})))"))
        self.assertTrue(t6_6("(){}[]({[]})"))

    def test_long_unbalanced(self):
        self.assertFalse(t6_6("((({{{[[[}}})))"))
        self.assertFalse(t6_6("(){}[({[})])"))


if __name__ == "__main__":
    unittest.main()
