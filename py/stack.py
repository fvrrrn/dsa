from typing import Generic, Iterator, Optional, TypeVar, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self.value: T = v
        self.next: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __str__(self):
        return str(self.value)


class Dummy(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __repr__(self) -> str:
        return "Dummy()"

    def __str__(self) -> str:
        return "Dummy"


class Stack(Generic[T]):
    def __init__(self, *values: T):
        self._head = Dummy()
        self._head.next = self._head
        self._size = 0
        for v in values:
            self.push(v)

    def size(self):
        return self._size

    def __str__(self):
        return ", ".join(str(node.value) for node in self)

    def __len__(self) -> int:
        return self._size

    def pop(self) -> Union[T, None]:
        """
        Removes and returns the top item from the stack for O(1) time complexity and O(1) space complexity.

        If the stack is empty, returns None.

        Returns:
            Union[T, None]: The value at the top of the stack if present,
                            otherwise None if the stack is empty.
        """
        match self._head.next:
            case Dummy():
                return None
            case Node():
                v = self._head.next.value
                self._head.next = self._head.next.next
                self._size -= 1
                return v

    def push(self, value: T) -> None:
        """
        Adds a new value to the top of the stack for O(1) time complexity and O(1) space complexity.

        This method creates a new node and places it at the front of the stack.

        Args:
            value (T): The value to be added to the stack.

        Returns:
            None: This method does not return a value.
        """
        node = Node(value)
        node.next = self._head.next
        self._head.next = node
        self._size += 1

    def peek(self) -> Union[T, None]:
        """
        Returns the value at the top of the stack without removing it for O(1) time complexity and O(1) space complexity.

        If the stack is empty, returns None.

        Returns:
            Union[T, None]: The value at the top of the stack if present,
                            otherwise None if the stack is empty.
        """
        match self._head.next:
            case Dummy():
                return None
            case Node():
                return self._head.next.value

    def __iter__(self) -> Iterator[Node[T]]:
        node = self._head.next
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    yield node
                    node = node.next
