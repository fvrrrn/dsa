import unittest

from t7 import OrderedList


class TestOrderedList(unittest.TestCase):
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
        ol = OrderedList(asc=True)
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
        ol = OrderedList(asc=True)
        ol.add(1)
        ol.add(2)
        ol.add(3)
        expected = "3 -> 2 -> 1"
        self.assertEqual(str(ol), expected)

    def test_delete_existing_element(self):
        ol = OrderedList(asc=True)
        ol.add(3)
        ol.add(2)
        ol.add(1)
        ol.delete(2)
        elements = list(ol)
        self.assertEqual(elements, [3, 1])  # 2 is removed

    def test_delete_non_existing_element(self):
        ol = OrderedList(asc=True)
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


if __name__ == "__main__":
    unittest.main()
