import unittest

from t4 import Stack


def t4_5_and_4_6(brackets: str) -> bool:
    """
    Checks if a string of brackets is properly balanced.

    The function validates that every opening bracket has a corresponding closing bracket
    in the correct order and that the types of brackets (()) are properly nested.

    Args:
        brackets (str): A string containing only bracket characters.

    Returns:
        bool: True if the string is properly balanced, False otherwise.
    """
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


if __name__ == "__main__":
    unittest.main()
