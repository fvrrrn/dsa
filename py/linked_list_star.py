from typing import Optional

from linked_list import LinkedList, Node


def merge_equal_list_and_sum(
    l1: LinkedList[int], l2: LinkedList[int]
) -> Optional[LinkedList[int]]:
    if len(l1) != len(l2):
        return None
    merged = LinkedList[int]()
    for n1, n2 in zip(l1, l2):
        merged.add_in_tail(Node(n1.value + n2.value))
    return merged
