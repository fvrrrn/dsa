import unittest

from linked_list_star import LinkedList, Node, merge_equal_list_and_sum


class TestLinkedListStar(unittest.TestCase):
    def test_empty(self):
        l1 = LinkedList[int]()
        l2 = LinkedList[int]()
        result = merge_equal_list_and_sum(l1, l2)
        self.assertEqual(str(result), "")
        self.assertIsInstance(result, LinkedList)
        assert result is not None
        self.assertIsNone(result.head)
        self.assertIsNone(result.tail)
        self.assertEqual(result.size, 0)

    def test_single_node(self):
        l1 = LinkedList[int]()
        l2 = LinkedList[int]()
        l1.add_in_tail(Node(1))
        l2.add_in_tail(Node(2))
        result = merge_equal_list_and_sum(l1, l2)
        self.assertEqual(str(result), "3")
        assert (
            result is not None and result.head is not None and result.tail is not None
        )
        self.assertEqual(result.size, l1.size)
        self.assertEqual(result.size, l2.size)
        assert l1.head is not None and l2.head is not None
        self.assertEqual(result.head.value, l1.head.value + l2.head.value)
        assert l1.tail is not None and l2.tail is not None
        self.assertEqual(result.tail.value, l1.tail.value + l2.tail.value)

    def test_multiple_nodes(self):
        l1 = LinkedList[int]()
        l2 = LinkedList[int]()
        for v in [1, 2, 3]:
            l1.add_in_tail(Node(v))
        for v in [4, 5, 6]:
            l2.add_in_tail(Node(v))
        result = merge_equal_list_and_sum(l1, l2)
        self.assertEqual(str(result), "5 -> 7 -> 9")

    def test_unequal_length(self):
        l1 = LinkedList[int]()
        l2 = LinkedList[int]()
        l1.add_in_tail(Node(1))
        l2.add_in_tail(Node(2))
        l2.add_in_tail(Node(3))
        result = merge_equal_list_and_sum(l1, l2)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
