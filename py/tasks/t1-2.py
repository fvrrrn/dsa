from typing import Optional

from t1 import LinkedList, Node


def t1_8(l1: LinkedList[int], l2: LinkedList[int]) -> Optional[LinkedList[int]]:
    """
    Merge two linked lists by summing corresponding elements.

    :param l1: The first linked list.
    :type l1: LinkedList[int]
    :param l2: The second linked list.
    :type l2: LinkedList[int]
    :returns: A new linked list with summed elements if input lists are equal-length, otherwise None.
    :rtype: Optional[LinkedList[int]]
    """
    if len(l1) != len(l2):
        return None
    merged = LinkedList[int]()
    for n1, n2 in zip(l1, l2):
        merged.add_in_tail(Node(n1.value + n2.value))
    return merged
