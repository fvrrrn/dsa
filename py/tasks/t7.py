from typing import Any, Generic, Iterator, Literal, Optional, Protocol, TypeVar


class Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool: ...
    def __ne__(self, other: Any, /) -> bool: ...
    def __lt__(self, other: Any, /) -> bool: ...
    def __le__(self, other: Any, /) -> bool: ...
    def __gt__(self, other: Any, /) -> bool: ...
    def __ge__(self, other: Any, /) -> bool: ...


def is_comparable(obj: Any) -> bool:
    try:
        _ = obj < obj
        _ = obj <= obj
        _ = obj > obj
        _ = obj >= obj
        _ = obj == obj
        return True
    except (TypeError, AttributeError):
        return False


T = TypeVar("T", bound=Comparable)


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


class OrderedList(Generic[T]):
    def __init__(self, asc) -> None:
        self.head = Dummy()
        self.tail = Dummy()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.__ascending = asc

    def compare(self, v1: T, v2: T) -> Literal[-1, 0, 1]:
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1

    def add(self, value: T) -> None:
        node = self.head.next
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    if node.value <= value:
                        break
                    node = node.next

        added = Node(value)
        node.prev.next = added
        added.prev = node.prev
        added.next = node
        node.prev = added

    def find(self, val: T) -> Optional[Node[T]]:
        node = self.head.next
        while True:
            match node:
                case Dummy():
                    return None
                case Node():
                    if node.value == val:
                        return node
                    node = node.next

    def delete(self, val):
        pass  # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        pass  # здесь будет ваш код

    def len(self):
        return self.size

    def get_all(self):
        r = []
        node = self.head.next
        while not isinstance(node, Dummy):
            r.append(node.value)
            node = node.next
        return r

    def __iter__(self) -> Iterator[T]:
        node = self.head.next
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    yield node.value
                    node = node.next

    def __reversed__(self):
        node = self.tail.prev
        while True:
            match node:
                case Dummy():
                    break
                case Node():
                    yield node
                    node = node.prev

    def __len__(self):
        return self.size

    def __str__(self):
        return " -> ".join(str(value) for value in self)
