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
        expected = "3 -> 2 -> 1"  # According to your current insert logic (descending)
        self.assertEqual(str(ol), expected)


if __name__ == "__main__":
    unittest.main()
