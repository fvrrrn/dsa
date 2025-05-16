from typing import Generic, Iterator, TypeVar

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


class Queue(Generic[T]):
    def __init__(self, *values: T) -> None:
        self._head = Dummy()
        self._tail = Dummy()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
        for value in values:
            self.enqueue(value)

    def size(self):
        return self._size

    def enqueue(self, value: T) -> Node[T]:
        """Add an element to the end of the queue for O(1) time complexity and O(1) space complexity.

        Args:
            value (T): The value to be added to the queue.

        Returns:
            Node[T]: The node containing the enqueued value.
        """
        node = Node(value)
        node.prev = self._tail.prev
        node.next = self._tail
        self._tail.prev.next = node
        self._tail.prev = node
        self._size += 1
        return node

    def dequeue(self) -> T | None:
        """Remove and return the first element from the queue for O(1) time complexity and O(1) space complexity.

        Returns:
            T | None: The value of the dequeued node, or None if the queue is empty.
        """
        match self._head.next:
            case Dummy():
                return None
            case Node():
                value = self._head.next.value
                self._head.next = self._head.next.next
                self._size -= 1
                return value

    def __iter__(self) -> Iterator[T]:
        node = self._head.next
        # prevent infinite loop if cycles are present
        for _ in range(self._size):
            match node:
                case Dummy():
                    break
                case Node():
                    yield node.value
                    node = node.next

    def __reversed__(self) -> Iterator[T]:
        node = self._tail.prev
        # prevent infinite loop if cycles are present
        for _ in range(self._size):
            match node:
                case Dummy():
                    break
                case Node():
                    yield node.value
                    node = node.prev

    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        for i, value in enumerate(self):
            if i == index:
                return value
        # theoretically unreachable due to check above
        raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: T) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        node = self._head.next
        for _ in range(index):
            node = node.next
        match node:
            case Dummy():
                raise IndexError("Index out of range")
            case Node():
                node.value = value

    def __len__(self):
        return self._size

    def __str__(self):
        return " -> ".join(str(value) for value in self)
