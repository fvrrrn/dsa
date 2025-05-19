from t6 import Deque


def t6_1(s: str) -> bool:
    q = Deque[str]()
    mid = len(s) // 2
    for a, b in zip(s[:mid], reversed(s[-mid:])):
        q.addFront(a)
        q.addTail(b)
    return False
