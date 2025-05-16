import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        ll = LinkedList[int]()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.head, 1)
        self.assertEqual(ll._tail.prev.value, 2)

    def test_prepend(self):
        ll = LinkedList[int]()
        ll.prepend(1)
        ll.prepend(2)
        self.assertEqual(ll.head, 2)
        self.assertEqual(ll._tail.prev.value, 1)

    def test_find(self):
        ll = LinkedList[int](1, 2, 3)
        node = ll.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)  # type: ignore

    def test_find_not_found(self):
        ll = LinkedList[int](1, 2, 3)
        node = ll.find(4)
        self.assertIsNone(node)

    def test_find_all(self):
        ll = LinkedList[int](1, 2, 1, 3)
        nodes = ll.find_all(1)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].value, 1)
        self.assertEqual(nodes[1].value, 1)

    def test_delete(self):
        ll = LinkedList[int](1, 2, 3, 2)
        ll.delete(2)
        self.assertEqual([node.value for node in ll], [1, 3, 2])

    def test_delete_all(self):
        ll = LinkedList[int](1, 2, 3, 2)
        ll.delete(2, all=True)
        self.assertEqual([node.value for node in ll], [1, 3])

    def test_clean(self):
        ll = LinkedList[int](1, 2, 3)
        ll.clean()
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.head)

    def test_len(self):
        ll = LinkedList[int](1, 2, 3)
        self.assertEqual(len(ll), 3)

    def test_str(self):
        ll = LinkedList[int](1, 2, 3)
        self.assertEqual(str(ll), "1 -> 2 -> 3")

    def test_reverse(self):
        ll = LinkedList[int](1, 2, 3)
        reversed_values = [node.value for node in reversed(ll)]
        self.assertEqual(reversed_values, [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
