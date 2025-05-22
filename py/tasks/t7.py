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
    def __init__(self, asc, *values: T) -> None:
        self.head = Dummy()
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size = 0
        self.__ascending = asc
        for v in values:
            self.add(v)

    @property
    def is_asc(self) -> bool:
        return self.__ascending

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
                    comparison = self.compare(node.value, value)
                    if (self.__ascending and comparison > 0) or (
                        not self.__ascending and comparison < 0
                    ):
                        break
                    node = node.next

        new_node = Node(value)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def find(self, val: T) -> Optional[Node[T]]:
        node = self.head.next

        if not isinstance(self.head.next, Dummy):
            # node=Node(2) and val=1 return None because 2 is the smallest number
            if self.__ascending and self.compare(val, node.value) == -1:
                return None
            # node=Node(5) and val=6 return None because 6 is the largest number
            elif not self.__ascending and self.compare(val, node.value) == 1:
                return None

        while True:
            match node:
                case Dummy():
                    return None
                case Node():
                    if node.value == val:
                        return node
                    node = node.next

    def delete(self, val: T):
        node = self.find(val)
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

    def clean(self, asc):
        self.__ascending = asc
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size = 0

    def len(self):
        return self.size

    def get_all(self):
        r = []
        node = self.head.next
        while not isinstance(node, Dummy):
            r.append(node)
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


class OrderedStringList(OrderedList[str]):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        strippedV1 = v1.strip()
        strippedV2 = v2.strip()

        if strippedV1 < strippedV2:
            return -1
        if strippedV1 == strippedV2:
            return 0
        return 1
