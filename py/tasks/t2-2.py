from typing import TypeVar

from t2 import LinkedList2, Node

T = TypeVar("T")


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
