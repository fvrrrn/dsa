import ctypes
import unittest
from typing import Generic, Iterator, TypeVar

from stack import Stack
from tasks.t5 import Queue


def t5_4(queue: Queue, n: int):
    n = n % queue.size() if queue.size() > 0 else 0
    for _ in range(n):
        queue.enqueue(queue.dequeue())


class PersistentQueue_5_5:
    def __init__(self):
        self._enqueued = Stack()
        self._dequeued = Stack()

    @property
    def queued(self):
        for item in self._enqueued:
            yield item
        for item in reversed(self._dequeued):
            yield item

    @property
    def dequeued(self):
        return reversed(self._dequeued)

    @property
    def enqueued(self):
        return self._enqueued

    def __len__(self):
        return len(self._enqueued)

    def enqueue(self, value):
        self._enqueued.push(value)

    def dequeue(self):
        match self._enqueued.pop():
            case None:
                return None
            case value:
                self._dequeued.push(value)
                return value


def t5_6(queue: Queue):
    reversed_queue = Queue()
    for value in reversed(queue):
        reversed_queue.enqueue(value)
    return reversed_queue


def t5_6_2(queue: Queue):
    n = queue.size()
    for i in range(n // 2):
        queue[i], queue[n - 1 - i] = queue[n - 1 - i], queue[i]


class StaticQueue_5_7:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = (capacity * ctypes.py_object)()
        self._start = 0
        self._end = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, item):
        if self.is_full():
            return None
        else:
            at = self._end
            self._queue[self._end] = item
            self._end = (self._end + 1) % self._capacity
            self._size += 1
            return at

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            item = self._queue[self._start]
            self._start = (self._start + 1) % self._capacity
            self._size -= 1
            return item


class Test5_2(unittest.TestCase):
    def test_t5_4(self):
        queue = Queue()
        for i in range(1, 6):
            queue.enqueue(i)

        t5_4(queue, 0)
        self.assertListEqual(list(queue), [1, 2, 3, 4, 5])

        t5_4(queue, 2)
        self.assertListEqual(list(queue), [3, 4, 5, 1, 2])

        t5_4(queue, 5)
        self.assertListEqual(list(queue), [3, 4, 5, 1, 2])

        t5_4(queue, 7)
        self.assertListEqual(list(queue), [5, 1, 2, 3, 4])

        empty_queue = Queue()
        t5_4(empty_queue, 3)
        self.assertListEqual(list(empty_queue), [])

    def test_PersistentQueue_5_5(self):
        q = PersistentQueue_5_5()

        self.assertEqual(len(q), 0)
        self.assertListEqual(list(q.enqueued), [])
        self.assertListEqual(list(q.dequeued), [])
        self.assertListEqual(list(q.queued), [])

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(len(q), 3)
        self.assertListEqual(list(q.enqueued), [3, 2, 1])
        self.assertListEqual(list(q.dequeued), [])
        self.assertListEqual(list(q.queued), [3, 2, 1])

        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(len(q), 2)
        self.assertListEqual(list(q.enqueued), [2, 1])
        self.assertListEqual(list(q.dequeued), [3])
        self.assertListEqual(list(q.queued), [2, 1, 3])

        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertIsNone(q.dequeue())

        self.assertEqual(len(q), 0)
        self.assertListEqual(list(q.enqueued), [])
        self.assertListEqual(list(q.dequeued), [3, 2, 1])
        self.assertListEqual(list(q.queued), [3, 2, 1])
        q.enqueue(5)
        self.assertListEqual(list(q.queued), [5, 3, 2, 1])
        self.assertListEqual(list(q.enqueued), [5])

    def test_t5_6(self):
        queue = Queue()
        for i in range(1, 6):
            queue.enqueue(i)

        reversed_queue = t5_6(queue)
        self.assertListEqual(list(reversed_queue), [5, 4, 3, 2, 1])

        empty_queue = Queue()
        reversed_empty = t5_6(empty_queue)
        self.assertListEqual(list(reversed_empty), [])

        single_element_queue = Queue()
        single_element_queue.enqueue(42)
        reversed_single = t5_6(single_element_queue)
        self.assertListEqual(list(reversed_single), [42])

    def test_5_6_2(self):
        queue = Queue()
        for i in range(1, 6):
            queue.enqueue(i)
        t5_6_2(queue)
        self.assertListEqual(list(queue), [5, 4, 3, 2, 1])

        queue2 = Queue()
        for i in range(1, 7):
            queue2.enqueue(i)
        t5_6_2(queue2)
        self.assertListEqual(list(queue2), [6, 5, 4, 3, 2, 1])

        empty_queue = Queue()
        t5_6_2(empty_queue)
        self.assertListEqual(list(empty_queue), [])

        single_element_queue = Queue()
        single_element_queue.enqueue(42)
        t5_6_2(single_element_queue)
        self.assertListEqual(list(single_element_queue), [42])

    def test_StaticQueue_5_7(self):
        queue = StaticQueue_5_7(3)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

        self.assertEqual(queue.enqueue(10), 0)
        self.assertEqual(queue._queue[0], 10)
        self.assertEqual(queue._size, 1)

        self.assertEqual(queue.enqueue(20), 1)
        self.assertEqual(queue.enqueue(30), 2)
        self.assertTrue(queue.is_full())
        self.assertEqual(queue._size, 3)
        self.assertIsNone(queue.enqueue(40))

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.dequeue())

        queue.enqueue(1)
        queue.enqueue(2)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertTrue(queue.is_full())
        self.assertIsNone(queue.enqueue(4))
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertTrue(queue.is_empty())


if __name__ == "__main__":
    unittest.main()
