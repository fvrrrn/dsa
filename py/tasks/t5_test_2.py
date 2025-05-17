import random
import unittest

from t5 import Queue


class TestQueueOneItem(unittest.TestCase):
    def setUp(self):
        self.s_queue = Queue()
        self.number = random.randint(0, 100)
        self.s_queue.enqueue(self.number)

    def test_one_item_size(self):
        self.assertEqual(self.s_queue.size(), 1)

    def test_one_item_enqueue(self):
        len_queue = self.s_queue.size()
        new_item = random.randint(0, 100)
        self.s_queue.enqueue(new_item)
        self.assertEqual(self.s_queue.size(), len_queue + 1)
        # self.assertEqual(self.s_queue.queue[-1], new_item)

    def test_one_item_dequeue(self):
        len_queue = self.s_queue.size()
        dequeue_result = self.s_queue.dequeue()
        self.assertEqual(dequeue_result, self.number)
        self.assertEqual(self.s_queue.size(), len_queue - 1)
        # self.assertEqual(self.s_queue.queue, [])


class TestQueueEmpty(unittest.TestCase):

    def setUp(self):
        self.s_queue = Queue()

    def test_empty_size(self):
        self.assertEqual(self.s_queue.size(), 0)

    def test_empty_enqueue(self):
        len_queue = self.s_queue.size()
        new_item = random.randint(0, 100)
        self.s_queue.enqueue(new_item)
        self.assertEqual(self.s_queue.size(), len_queue + 1)
        # self.assertEqual(self.s_queue.queue[-1], new_item)

    def test_empty_dequeue(self):
        len_queue = self.s_queue.size()
        dequeue_result = self.s_queue.dequeue()
        self.assertIsNone(dequeue_result)
        self.assertEqual(self.s_queue.size(), len_queue)
        # self.assertEqual(self.s_queue.queue, [])


class TestQueueManyItems(unittest.TestCase):

    def setUp(self):
        self.s_queue = Queue()
        number = random.randrange(3, 100)
        self.items_list = [random.randint(0, 100) for _ in range(number)]
        for item in self.items_list:
            self.s_queue.enqueue(item)

    def test_many_items_size(self):
        self.assertEqual(self.s_queue.size(), len(self.items_list))

    def test_many_items_enqueue(self):
        len_queue = self.s_queue.size()
        new_item = random.randint(0, 100)
        self.s_queue.enqueue(new_item)
        self.assertEqual(self.s_queue.size(), len_queue + 1)
        # self.assertEqual(self.s_queue.queue[-1], new_item)

    def test_many_items_dequeue(self):
        len_queue = self.s_queue.size()
        dequeue_result = self.s_queue.dequeue()
        self.assertEqual(dequeue_result, self.items_list[0])
        self.assertEqual(self.s_queue.size(), len_queue - 1)
        # self.assertListEqual(self.s_queue.queue, self.items_list[1:])


if __name__ == "__main__":
    unittest.main()
