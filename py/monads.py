from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


class Maybe(Generic[T]):
    pass


@dataclass(frozen=True)
class Just(Maybe[T]):
    value: T


@dataclass(frozen=True)
class Nothing(Maybe[T]):
    pass
