import unittest
from typing import cast

from linked_list import LinkedList, Node, sort_linked_list


class TestLinkedList(unittest.TestCase):
    def test_add_in_tail(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        ll.append(node1)
        ll.append(node2)
        self.assertEqual(ll._head, node1)
        self.assertEqual(ll._tail, node2)
        # will not ever throw
        assert ll._head is not None
        self.assertEqual(ll._head.next, node2)

    def test_find(self):
        ll = LinkedList()
        node1 = Node(10)
        node2 = Node(20)
        ll.append(node1)
        ll.append(node2)
        found = ll.find(20)
        self.assertEqual(found, node2)

    def test_find_not_found(self):
        ll = LinkedList()
        ll.append(Node(5))
        self.assertIsNone(ll.find(99))

    def test_len(self):
        ll = LinkedList()
        self.assertEqual(ll.len(), 0)
        ll.append(Node(1))
        ll.append(Node(2))
        self.assertEqual(ll.len(), 2)

    def test_clean(self):
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.clean()
        self.assertIsNone(ll._head)
        self.assertIsNone(ll._tail)
        self.assertEqual(ll.len(), 0)

    def test_delete_only_node(self):
        ll = LinkedList[int]()
        node = Node(10)
        ll.append(node)
        ll.delete(10)
        self.assertIsNone(ll._head)
        self.assertIsNone(ll._tail)

    def test_delete_tail_only(self):
        ll = LinkedList[int]()
        ll.append(Node(1))
        node = Node(2)
        ll.append(node)
        ll.delete(2)
        self.assertEqual(cast(Node[int], ll._tail).value, 1)
        self.assertIsNone(cast(Node[int], ll._tail).next)

    def test_delete_head_only(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.append(node1)
        ll.append(Node(2))
        ll.delete(1)
        self.assertEqual(cast(Node[int], ll._head).value, 2)
        self.assertIsNone(cast(Node[int], ll._head).prev)

    def test_delete_middle_node(self):
        ll = LinkedList[int]()
        ll.append(Node(1))
        middle = Node(2)
        ll.append(middle)
        ll.append(Node(3))
        ll.delete(2)
        values = [node.value for node in ll]
        self.assertEqual(values, [1, 3])

    def test_delete_multiple_all_flag(self):
        ll = LinkedList[int]()
        ll.append(Node(5))
        ll.append(Node(5))
        ll.append(Node(5))
        ll.delete(5, all=True)
        self.assertIsNone(ll._head)
        self.assertIsNone(ll._tail)

    def test_delete_multiple_all_flag_2(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.append(node1)
        ll.append(Node(5))
        ll.append(Node(5))
        ll.append(Node(5))
        ll.delete(5, all=True)
        self.assertEqual(ll._head, node1)
        self.assertEqual(ll._tail, node1)

    def test_delete_multiple_all_flag_3(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        ll.append(node1)
        ll.append(node2)
        ll.append(Node(5))
        ll.append(Node(5))
        ll.append(Node(5))
        ll.delete(5, all=True)
        self.assertEqual(ll._head, node1)
        self.assertEqual(ll._tail, node2)

    def test_delete_first_occurrence_only(self):
        ll = LinkedList[int]()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.delete(2)
        values = [node.value for node in ll]
        self.assertEqual(values, [1, 2, 3])

    def test_insert_into_empty_list(self):
        ll = LinkedList[int]()
        node = Node(1)
        ll.insert(None, node)
        self.assertEqual(ll._head, node)
        self.assertEqual(ll._tail, node)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

    def test_insert_when_after_is_none(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.append(node1)
        node2 = Node(2)
        ll.insert(None, node2)
        self.assertEqual(ll._tail, node2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node1.next, node2)
        self.assertEqual(ll._head, node1)
        self.assertIsNone(node2.next)
        self.assertEqual(ll.len(), 2)

    def test_insert_after_head(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        ll.append(node1)
        ll.insert(node1, node2)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(ll._tail, node2)
        self.assertEqual(ll._head, node1)

    def test_insert_in_middle(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        ll.append(node1)
        ll.append(node3)
        ll.insert(node1, node2)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node2.next, node3)
        self.assertEqual(node3.prev, node2)

    def test_insert_after_tail(self):
        ll = LinkedList[int]()
        node1 = Node(1)
        ll.append(node1)
        node2 = Node(2)
        ll.insert(node1, node2)
        self.assertEqual(ll._head, node1)
        self.assertEqual(ll._tail, node2)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node2.prev, node1)
        self.assertIsNone(node2.next)

    def test_insert_middle(self):
        ll = LinkedList[str]()
        a1 = Node("a1")
        a2 = Node("a2")
        a3 = Node("a3")
        a4 = Node("a4")
        a5 = Node("a5")
        a7 = Node("a7")

        ll.append(a1)
        ll.append(a2)
        ll.append(a3)
        ll.append(a4)
        ll.append(a5)

        ll.insert(a3, a7)

        values = [node.value for node in ll]
        self.assertEqual(values, ["a1", "a2", "a3", "a7", "a4", "a5"])

    def test_add_in_head_empty_list(self):
        ll = LinkedList[int]()
        node = Node(1)
        ll.prepend(node)
        self.assertIs(ll._head, node)
        self.assertIs(ll._tail, node)
        self.assertEqual(ll._size, 1)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

    def test_add_in_head_single_node_list(self):
        ll = LinkedList[int]()
        first = Node(1)
        ll.append(first)

        second = Node(0)
        ll.prepend(second)

        self.assertIs(ll._head, second)
        self.assertIs(ll._tail, first)
        self.assertEqual(ll._size, 2)
        self.assertIs(second.next, first)
        self.assertIsNone(second.prev)
        self.assertIs(first.prev, second)
        self.assertIsNone(first.next)

    def test_add_in_head_multiple_nodes_list(self):
        ll = LinkedList[int]()
        first = Node(2)
        second = Node(3)
        ll.append(first)
        ll.append(second)

        new_head = Node(1)
        ll.prepend(new_head)

        self.assertIs(ll._head, new_head)
        self.assertEqual(ll._size, 3)
        self.assertIs(new_head.next, first)
        self.assertIsNone(new_head.prev)
        self.assertIs(first.prev, new_head)
        self.assertIs(first.next, second)
        self.assertIs(second.prev, first)
        self.assertIsNone(second.next)

    def test_linked_list_initialization(self):
        llist = LinkedList(5, 3, 8, 1, 4)
        self.assertEqual(str(llist), "5 -> 3 -> 8 -> 1 -> 4")

    def test_sort_linked_list(self):
        llist = LinkedList(5, 3, 8, 1, 4)
        sorted_llist = sort_linked_list(llist)
        self.assertEqual(str(sorted_llist), "1 -> 3 -> 4 -> 5 -> 8")

    def test_empty_list(self):
        llist = LinkedList()
        sorted_llist = sort_linked_list(llist)
        self.assertEqual(str(sorted_llist), "")

    def test_single_element(self):
        llist = LinkedList(42)
        sorted_llist = sort_linked_list(llist)
        self.assertEqual(str(sorted_llist), "42")

    def test_sorted_list(self):
        llist = LinkedList(1, 2, 3, 4, 5)
        sorted_llist = sort_linked_list(llist)
        self.assertEqual(str(sorted_llist), "1 -> 2 -> 3 -> 4 -> 5")

    def test_reverse_sorted_list(self):
        llist = LinkedList(5, 4, 3, 2, 1)
        sorted_llist = sort_linked_list(llist)
        self.assertEqual(str(sorted_llist), "1 -> 2 -> 3 -> 4 -> 5")

    def test_original_list_mutation(self):
        original_list = LinkedList(5, 3, 8, 1, 4)
        original_str = str(original_list)
        sort_linked_list(original_list)
        self.assertEqual(original_str, str(original_list))


if __name__ == "__main__":
    unittest.main()
