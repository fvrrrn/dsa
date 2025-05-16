from typing import Generic, Iterator, Optional, TypeVar, Union

from linked_list import Dummy, LinkedList, Node

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, *values: T):
        self._list = LinkedList()
        for v in values:
            self._list.prepend(v)

    def __str__(self):
        return ", ".join(str(value) for value in self)

    def __len__(self) -> int:
        return len(self._list)

    def pop(self) -> Optional[T]:
        match self._list._head.next:
            case Dummy():
                return None
            case Node():
                v = self._list._head.next.value
                self._list._head.next.next.prev = self._list._head
                self._list._head.next = self._list._head.next.next
                self._list._size -= 1
                return v

    def push(self, value: T) -> Node[T]:
        return self._list.prepend(value)

    def peek(self) -> Optional[T]:
        match self._list._head.next:
            case Dummy():
                return None
            case Node():
                return self._list._head.next.value

    def __iter__(self) -> Iterator[Node[T]]:
        node = self._list._head.next
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    yield node.value
                    node = node.next

    def __reversed__(self) -> Iterator[Node[T]]:
        node = self._list._tail.prev
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    yield node.value
                    node = node.prev
