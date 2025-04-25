import unittest
from typing import cast

from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def test_add_in_tail(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node2)
        # self.assertEqual(ll.head.next, node2)

    def test_find(self):
        ll = LinkedList()
        node1 = Node(10)
        node2 = Node(20)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        found = ll.find(20)
        self.assertEqual(found, node2)

    def test_find_not_found(self):
        ll = LinkedList()
        ll.add_in_tail(Node(5))
        self.assertIsNone(ll.find(99))

    def test_len(self):
        ll = LinkedList()
        self.assertEqual(ll.len(), 0)
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        self.assertEqual(ll.len(), 2)

    def test_clean(self):
        ll = LinkedList()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.clean()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.len(), 0)

    def test_delete_only_node(self):
        ll = LinkedList[int]()
        node = Node(10)
        ll.add_in_tail(node)
        ll.delete(10)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_delete_tail_only(self):
        ll = LinkedList[int]()
        ll.add_in_tail(Node(1))
        node = Node(2)
        ll.add_in_tail(node)
        ll.delete(2)
        self.assertEqual(cast(Node[int], ll.tail).value, 1)
        self.assertIsNone(cast(Node[int], ll.tail).next)

    def test_delete_head_only(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(Node(2))
        ll.delete(1)
        self.assertEqual(cast(Node[int], ll.head).value, 2)
        self.assertIsNone(cast(Node[int], ll.head).prev)

    def test_delete_middle_node(self):
        ll = LinkedList[int]()
        ll.add_in_tail(Node(1))
        middle = Node(2)
        ll.add_in_tail(middle)
        ll.add_in_tail(Node(3))
        ll.delete(2)
        values = [node.value for node in ll]
        self.assertEqual(values, [1, 3])

    def test_delete_multiple_all_flag(self):
        ll = LinkedList[int]()
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.delete(5, all=True)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_delete_multiple_all_flag_2(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.add_in_tail(node1)
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.delete(5, all=True)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node1)

    def test_delete_multiple_all_flag_3(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.add_in_tail(Node(5))
        ll.delete(5, all=True)
        self.assertEqual(ll.head, node1)
        self.assertEqual(ll.tail, node2)

    def test_delete_first_occurrence_only(self):
        ll = LinkedList[int]()
        ll.add_in_tail(Node(1))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(2))
        ll.add_in_tail(Node(3))
        ll.delete(2)
        values = [node.value for node in ll]
        self.assertEqual(values, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
