import unittest

from t5 import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue_single_item(self):
        queue = Queue[int]()
        queue.enqueue(10)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue._head.next.value, 10)
        self.assertEqual(queue._tail.prev.value, 10)

    def test_enqueue_multiple_items(self):
        queue = Queue[int]()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(len(queue), 3)
        self.assertEqual(queue._head.next.value, 10)
        self.assertEqual(queue._tail.prev.value, 30)
        self.assertEqual(queue._head.next.next.value, 20)

    def test_dequeue_single_item(self):
        queue = Queue[int](10)
        value = queue.dequeue()

        self.assertEqual(value, 10)
        self.assertEqual(len(queue), 0)

    def test_dequeue_multiple_items(self):
        queue = Queue[int]()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 30)
        self.assertEqual(len(queue), 0)

    def test_dequeue_empty_queue(self):
        queue = Queue[int]()
        value = queue.dequeue()

        self.assertIsNone(value)
        self.assertEqual(len(queue), 0)

    def test_size(self):
        queue = Queue[int](10, 20)
        self.assertEqual(queue.size(), 2)
        queue.enqueue(30)
        self.assertEqual(queue.size(), 3)
        queue.dequeue()
        self.assertEqual(queue.size(), 2)

    def test_str_representation(self):
        queue = Queue[int](10, 20, 30)
        self.assertEqual(str(queue), "10 -> 20 -> 30")

    def test_reversed(self):
        queue = Queue[int](10, 20, 30)
        reversed_values = list(reversed(queue))
        self.assertEqual([value for value in reversed_values], [30, 20, 10])


if __name__ == "__main__":
    unittest.main()
