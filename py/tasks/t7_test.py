import unittest

from t7 import OrderedList, OrderedStringList


class TestOrderedList(unittest.TestCase):
    def test_add_ascending_order(self):
        ol = OrderedList(asc=True)
        ol.add(5)
        ol.add(3)
        ol.add(4)
        ol.add(1)
        ol.add(2)
        result = list(ol)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_add_descending_order(self):
        ol = OrderedList(asc=False)
        ol.add(1)
        ol.add(3)
        ol.add(2)
        ol.add(5)
        ol.add(4)
        result = list(ol)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_find_existing(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        node = ol.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)  # type: ignore

    def test_find_nonexistent(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(3)
        self.assertIsNone(ol.find(5))

    def test_delete_existing(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        ol.delete(2)
        result = list(ol)
        self.assertEqual(result, [1, 3])

    def test_delete_nonexistent(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.delete(5)  # should do nothing
        result = list(ol)
        self.assertEqual(result, [1, 2])

    def test_len_method(self):
        ol = OrderedList(asc=True)
        self.assertEqual(len(ol), 0)
        ol.add(1)
        ol.add(2)
        self.assertEqual(len(ol), 2)
        ol.delete(1)
        self.assertEqual(len(ol), 1)

    def test_get_all(self):
        ol = OrderedList(asc=True)
        ol.add(2)
        ol.add(1)
        nodes = ol.get_all()
        values = [n.value for n in nodes]
        self.assertEqual(values, [1, 2])

    def test_forward_iteration(self):
        ol = OrderedList(asc=True)
        for x in [3, 1, 2]:
            ol.add(x)
        values = list(ol)
        self.assertEqual(values, [1, 2, 3])

    def test_reverse_iteration(self):
        ol = OrderedList(asc=True)
        for x in [1, 3, 2]:
            ol.add(x)
        values = [node.value for node in reversed(ol)]
        self.assertEqual(values, [3, 2, 1])

    def test_str_representation(self):
        ol = OrderedList(asc=True)
        ol.add(3)
        ol.add(1)
        ol.add(2)
        self.assertEqual(str(ol), "1 -> 2 -> 3")

    def test_empty_list_has_length_zero(self):
        ol = OrderedList(asc=True)
        self.assertEqual(len(ol), 0)

    def test_add_single_element(self):
        ol = OrderedList(asc=True)
        ol.add(5)
        elements = list(ol)
        self.assertEqual(elements, [5])
        self.assertEqual(len(elements), 1)

    def test_add_multiple_elements_ascending(self):
        ol = OrderedList(asc=False)
        ol.add(5)
        ol.add(3)
        ol.add(7)
        elements = list(ol)
        self.assertEqual(elements, [7, 5, 3])  # based on your logic: highest first

    def test_add_multiple_elements_descending(self):
        ol = OrderedList(asc=False)
        ol.add(5)
        ol.add(3)
        ol.add(7)
        elements = list(ol)
        self.assertEqual(
            elements, [7, 5, 3]
        )  # Same result unless add() logic flips for descending

    def test_find_existing_element(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        node = ol.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)  # type: ignore

    def test_find_non_existing_element(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        node = ol.find(5)
        self.assertIsNone(node)

    def test_iterator_protocol(self):
        ol = OrderedList(asc=True)
        for value in [10, 20, 15]:
            ol.add(value)
        iterated = [x for x in ol]
        self.assertTrue(all(isinstance(i, int) for i in iterated))

    def test_string_representation(self):
        ol = OrderedList(asc=False)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        expected = "3 -> 2 -> 1"
        self.assertEqual(str(ol), expected)

    def test_delete_existing_element(self):
        ol = OrderedList(asc=False)
        ol.add(3)
        ol.add(2)
        ol.add(1)
        ol.delete(2)
        elements = list(ol)
        self.assertEqual(elements, [3, 1])  # 2 is removed

    def test_delete_non_existing_element(self):
        ol = OrderedList(asc=False)
        ol.add(1)
        ol.add(2)
        ol.delete(5)  # No exception should be raised
        elements = list(ol)
        self.assertEqual(elements, [2, 1])  # List unchanged

    def test_delete_from_empty_list(self):
        ol = OrderedList(asc=True)
        ol.delete(10)  # No exception should be raised
        elements = list(ol)
        self.assertEqual(elements, [])  # Still empty

    def test_delete_all_elements(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        ol.delete(1)
        ol.delete(2)
        ol.delete(3)
        self.assertEqual(list(ol), [])  # List is empty after deletions

    def test_delete_duplicate_element_once(self):
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(2)
        ol.delete(2)
        elements = list(ol)
        self.assertEqual(elements.count(2), 1)  # Only one 2 remains


class TestOrderedStringList(unittest.TestCase):
    def test_add_strings_preserves_spaces(self):
        osl = OrderedStringList(asc=True)
        osl.add("  banana ")
        osl.add("apple")
        osl.add("  cherry")
        result = list(osl)
        # Should be sorted using stripped values, but keep original strings
        self.assertEqual(result, ["apple", "  banana ", "  cherry"])

    def test_add_strings_descending_order(self):
        osl = OrderedStringList(asc=False)
        osl.add("  banana ")
        osl.add("apple")
        osl.add("  cherry")
        result = list(osl)
        self.assertEqual(result, ["  cherry", "  banana ", "apple"])

    def test_add_duplicate_strings_with_spaces(self):
        osl = OrderedStringList(asc=True)
        osl.add("wolf")
        osl.add("  wolf ")
        result = list(osl)
        self.assertEqual(result, ["wolf", "  wolf "])

    def test_str_representation_keeps_spaces(self):
        osl = OrderedStringList(asc=True)
        osl.add("  x ")
        osl.add("a")
        self.assertEqual(str(osl), "a ->   x ")


if __name__ == "__main__":
    unittest.main()
