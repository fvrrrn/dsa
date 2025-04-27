import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from typing import (
    Generic,
    Iterator,
    List,
    Optional,
    Protocol,
    TypeGuard,
    TypeVar,
    Union,
    cast,
)

from monads import Just, Maybe, Nothing
from protocols import Comparable

T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self.value: T = v
        self.next: Optional[Node[T]] = None
        self.prev: Optional[Node[T]] = None


class HasNext(Protocol, Generic[T]):
    value: T
    prev: Optional[Node[T]]
    next: Node[T]


class HasPrev(Protocol, Generic[T]):
    value: T
    prev: Node[T]
    next: Optional[Node[T]]


class HasPrevNext(Protocol, Generic[T]):
    value: T
    prev: Node[T]
    next: Node[T]


def is_head(node: Node[T]) -> TypeGuard[HasNext[T]]:
    return node.prev is None


def is_tail(node: Node[T]) -> TypeGuard[HasPrev[T]]:
    return node.next is None


def is_middle(node: Node[T]) -> TypeGuard[HasPrevNext[T]]:
    return node.prev is not None and node.next is not None


class LinkedList(Generic[T]):
    def __init__(self, *values: T) -> None:
        # TODO: make fields read-only so that there won't be erroneous states
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size = 0
        for value in values:
            self.add_in_tail(value)

    def __iter__(self) -> Iterator[Node[T]]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        return " -> ".join(str(node.value) for node in self)

    def __reversed__(self):
        node = self.tail
        while node is not None:
            yield node
            node = node.prev

    def __getitem__(self, index: int) -> Maybe[Node[T]]:
        if not (0 <= index < self.size):
            return Nothing()
        node = self.head
        for _ in range(index):
            if node is not None:
                node = node.next
        if node is None:
            return Nothing()
        return Just(node)

    def add_in_head(self, item: Union[Node[T], T]) -> None:
        if not isinstance(item, Node):
            item = Node(item)
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
                item.next = self.head
                self.head.prev = item
                self.head = item
                self.size += 1

    def add_in_tail(self, item: Union[Node[T], T]) -> None:
        if not isinstance(item, Node):
            item = Node(item)
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
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
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


def _partition(low: HasNext[T], high: HasPrev[T]) -> Node[T]:
    pivot = high
    i = cast(HasNext[T], low.prev)
    j = low

    while j != high:
        if j.value < pivot.value:
            i = cast(HasNext[T], i.next) if i else low
            i.value, j.value = j.value, i.value
        j = cast(HasNext[T], j.next)
    i = i.next if i else low
    i.value, pivot.value = pivot.value, i.value
    return cast(Node[T], i)


def _threaded_quick_sort_recursive(low: Node[T], high: Node[T]) -> None:
    if low and high and low != high and low != high.next:
        pivot = _partition(cast(HasNext[T], low), cast(HasPrev[T], high))
        left_thread = threading.Thread(
            target=_threaded_quick_sort_recursive, args=(low, pivot.prev)
        )
        right_thread = threading.Thread(
            target=_threaded_quick_sort_recursive, args=(pivot.next, high)
        )

        left_thread.start()
        right_thread.start()

        left_thread.join()
        right_thread.join()


def _quick_sort_recursive(low: Node[T], high: Node[T]) -> None:
    if low and high and low != high and low != high.next:
        pivot = _partition(cast(HasNext[T], low), cast(HasPrev[T], high))
        _quick_sort_recursive(low, pivot.prev)  # type: ignore
        _quick_sort_recursive(pivot.next, high)  # type: ignore


def _threaded_quick_sort_recursive_2(
    low: Node[T], high: Node[T], pool: ThreadPoolExecutor, threshold: int = 10
) -> None:
    if low and high and low != high and low != high.next:
        pivot = _partition(cast(HasNext[T], low), cast(HasPrev[T], high))
        if _partition_size(low, high) > threshold:
            futures = [
                pool.submit(_threaded_quick_sort_recursive_2, low, pivot.prev, pool, threshold),  # type: ignore
                pool.submit(_threaded_quick_sort_recursive_2, pivot.next, high, pool, threshold),  # type: ignore
            ]

            for future in as_completed(futures):
                future.result()
        else:
            _threaded_quick_sort_recursive_2(low, pivot.prev, pool, threshold)  # type: ignore
            _threaded_quick_sort_recursive_2(pivot.next, high, pool, threshold)  # type: ignore


def _partition_size(low: Node[T], high: Node[T]) -> int:
    size = 0
    current = low
    while current != high.next:
        size += 1
        current = current.next  # type: ignore
    return size


def _parallel_quick_sort_recursive(
    low: Node[T], high: Node[T], pool: ProcessPoolExecutor
) -> None:
    if low and high and low != high and low != high.next:
        pivot = _partition(cast(HasNext[T], low), cast(HasPrev[T], high))
        left_task = pool.submit(_parallel_quick_sort_recursive, low, pivot.prev, pool)  # type: ignore
        right_task = pool.submit(_parallel_quick_sort_recursive, pivot.next, high, pool)  # type: ignore
        left_task.result()
        right_task.result()


def sort_linked_list(llist: LinkedList[T]) -> LinkedList[T]:
    sorted_list = LinkedList[T]()
    for node in llist:
        # TODO: if node.value is not a primitive it should be deep-copied
        sorted_list.add_in_tail(node.value)
    if (
        llist.head is None
        or sorted_list.head is None
        or llist.tail is None
        or sorted_list.tail is None
    ):
        return llist
    # _threaded_quick_sort_recursive(sorted_list.head, sorted_list.tail)
    # with ProcessPoolExecutor() as pool:
    #     _parallel_quick_sort_recursive(sorted_list.head, sorted_list.tail, pool)
    with ThreadPoolExecutor() as pool:
        _threaded_quick_sort_recursive_2(sorted_list.head, sorted_list.tail, pool)
    # _quick_sort_recursive(sorted_list.head, sorted_list.tail)
    return sorted_list
