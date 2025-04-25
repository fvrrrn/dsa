from typing import Generic, List, Optional, Protocol, TypeVar

# class Equalable(Protocol):
#     def __eq__(self, other: object) -> bool:
#         ...
#     def __ne__(self, other: object) -> bool:
#         ...

# T = TypeVar("T", bound=Equalable)
T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self.value: T = v
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size = 0

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def add_in_tail(self, item: Node[T]) -> None:
        match self.head, self.tail:
            case None, None:
                self.head = item
                self.tail = item
                # TODO: incorrectly initialized linked list
            case _, None:
                pass
            case None, _:
                pass
            case _, _:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item

    def print_all_nodes(self) -> None:
        for node in self:
            print(node.value)

    def find(self, val: T) -> Optional[Node[T]]:
        return next((node for node in self if node.value == val), None)

    def find_all(self, val: T) -> List[Node[T]]:
        return [node for node in self if node.value == val]

    def delete(self, val: T, all: bool = False) -> None:
        for node in self.find_all(val):
            if self.head is None or self.tail is None:
                break
            match node == self.head, node == self.tail:
                case True, True:
                    self.head = None
                    self.tail = None
                case True, False:
                    if headNext := self.head.next:
                        headNext.prev = None
                        self.head = headNext
                case False, True:
                    if tailPrev := self.tail.prev:
                        tailPrev.next = None
                        self.tail = tailPrev
                case False, False:
                    if (nodePrev := node.prev) and (nodeNext := node.next):
                        nodePrev.next = nodeNext
                        nodeNext.prev = nodePrev
            if all is False:
                return

    def clean(self) -> None:
        pass

    def len(self) -> int:
        return self.size

    def insert(self, afterNode: Optional[Node[T]], newNode: Node[T]) -> None:
        pass
