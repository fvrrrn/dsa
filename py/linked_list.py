from typing import Generic, Iterator, List, Optional, TypeVar

from monads import Just, Maybe, Nothing

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self.value: T = v
        self.next: Node[T] | Dummy
        self.prev: Node[T] | Dummy

    def __repr__(self) -> str:
        return f"Node({self.value})"


class Dummy(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __repr__(self) -> str:
        return "Dummy()"

    def __str__(self) -> str:
        return "Dummy"


class LinkedList(Generic[T]):
    def __init__(self, *values: T) -> None:
        self._head = Dummy()
        self._tail = Dummy()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
        for value in values:
            self.append(value)

    @property
    def head(self) -> Optional[T]:
        match self._head.next:
            case Dummy():
                return None
            case Node():
                return self._head.next.value

    def __iter__(self) -> Iterator[Node[T]]:
        node = self._head.next
        # prevent infinite loop if cycles are present
        for _ in range(self._size):
            match node:
                case Dummy():
                    break
                case Node():
                    yield node
                    node = node.next

    def __len__(self):
        return self._size

    def __str__(self):
        return " -> ".join(str(node.value) for node in self)

    def __reversed__(self):
        node = self._tail.prev
        # prevent infinite loop if cycles are present
        for _ in range(self._size):
            match node:
                case Dummy():
                    break
                case Node():
                    yield node
                    node = node.prev

    def __getitem__(self, index: int) -> Maybe[Node[T]]:
        if not (0 <= index < self._size):
            return Nothing()
        node = self._head
        for _ in range(index):
            if node is not None:
                node = node.next
        if node is None:
            return Nothing()
        return Just(node)

    def prepend(self, value: T) -> Node[T]:
        node = Node(value)
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node
        self._size += 1
        return node

    def append(self, value: T) -> Node[T]:
        node = Node(value)
        node.prev = self._tail.prev
        node.next = self._tail
        self._tail.prev.next = node
        self._tail.prev = node
        self._size += 1
        return node

    def find(self, val: T) -> Optional[Node[T]]:
        return next((node for node in self if node.value == val), None)

    def find_all(self, val: T) -> List[Node[T]]:
        return [node for node in self if node.value == val]

    def delete(self, val: T, all: bool = False) -> None:
        for node in self.find_all(val):
            node.prev.next = node.next
            node.next.prev = node.prev
            self._size -= 1
            if all is False:
                return

    def clean(self) -> None:
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
