from typing import Generic, Iterator, List, Optional, Protocol, TypeGuard, TypeVar, cast


class Equalable(Protocol):
    def __eq__(self, other: object, /) -> bool: ...


T = TypeVar("T", bound=Equalable)


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self.value: T = v
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        # TODO: make fields read-only so that there won't be erroneous states
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size = 0

    def __iter__(self) -> Iterator[Node[T]]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        return " -> ".join(str(node.value) for node in self)

    def add_in_tail(self, item: Node[T]) -> None:
        match self.head, self.tail:
            case None, None:
                self.head = item
                self.tail = item
                self.size += 1
            case _, None:
                pass
            case None, _:
                pass
            case _, _:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item
                self.size += 1

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
            self.size -= 1
            if all is False:
                return

    def clean(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def len(self) -> int:
        return self.size

    def insert(self, afterNode: Optional[Node[T]], newNode: Node[T]) -> None:
        match self.head, self.tail, afterNode:
            case None, None, None:
                self.add_in_tail(newNode)
            case None, _, _:
                pass
            case _, None, _:
                pass
            case _, _, None:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                self.size += 1
            case _, _, _:
                # TypeGuard does not work with match-case
                if is_tail(afterNode):
                    afterNode.next = newNode
                    newNode.prev = cast(Node[T], afterNode)
                    self.size += 1
                    self.tail = newNode
                elif is_head(afterNode) or is_middle(afterNode):
                    afterNode.next.prev = newNode
                    newNode.next = afterNode.next
                    afterNode.next = newNode
                    newNode.prev = cast(Node[T], afterNode)
                    self.size += 1


class HasNext(Protocol, Generic[T]):
    prev: Optional[Node[T]]
    next: Node[T]


class HasPrev(Protocol, Generic[T]):
    prev: Node[T]
    next: Optional[Node[T]]


class HasPrevNext(Protocol, Generic[T]):
    prev: Node[T]
    next: Node[T]


def is_head(node: Node[T]) -> TypeGuard[HasNext[T]]:
    return node.prev is None


def is_tail(node: Node[T]) -> TypeGuard[HasPrev[T]]:
    return node.next is None


def is_middle(node: Node[T]) -> TypeGuard[HasPrevNext[T]]:
    return node.prev is not None and node.next is not None
