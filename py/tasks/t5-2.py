import unittest
from typing import Generic, Iterator, TypeVar

from stack import Stack
from tasks.t5 import Queue


def t5_4(self, n: int):
    n = n % self.size() if self.size() > 0 else 0
    for _ in range(n):
        self.enqueue(self.dequeue())


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


if __name__ == "__main__":
    unittest.main()
