from typing import TypeVar

from t2 import LinkedList2, Node

from linked_list import LinkedList, sort_linked_list
from protocols import Comparable

T = TypeVar("T", bound=Comparable)


def t2_10(l: LinkedList2[T]) -> LinkedList2[T]:
    r = LinkedList2()
    for node in reversed(l):
        r.add_in_tail(Node(node.value))
    return r


def t2_11(l: LinkedList2[T]) -> bool:
    node = l.head
    for _ in range(l.size):
        if node is None:
            return False
        node = node.next
    return node is not None


def t2_12() -> LinkedList[int]:
    unsorted_list = LinkedList[int](1, 5, 6, 3, 1)
    return sort_linked_list(unsorted_list)


def t2_13(l1: LinkedList[T], l2: LinkedList[T]) -> LinkedList[T]:
    sorted_l1 = sort_linked_list(l1)
    sorted_l2 = sort_linked_list(l2)
    merged = LinkedList[T]()
    current1 = sorted_l1._head
    current2 = sorted_l2._head
    while True:
        match current1, current2:
            case None, None:
                return merged
            case _, None:
                merged.append(current1.value)
                current1 = current1.next
            case None, _:
                merged.append(current2.value)
                current2 = current2.next
            case _, _:
                if current2.value <= current1.value:
                    merged.append(current2.value)
                    current2 = current2.next
                else:
                    merged.append(current1.value)
                    current1 = current1.next
