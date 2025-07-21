from dataclasses import dataclass
from typing import Generic, TypeGuard, TypeVar

T = TypeVar("T")
L = TypeVar("L")
R = TypeVar("R")


class Maybe(Generic[T]):
    pass


@dataclass(frozen=True)
class Just(Maybe[T]):
    def __bool__(self) -> bool:
        return True

    value: T


def is_just(m: Maybe[T]) -> TypeGuard[Just[T]]:
    return isinstance(m, Just)


@dataclass(frozen=True)
class Nothing(Maybe[T]):
    __match_args__ = ()  # TODO: not working: allow match-case to work cleanly

    def __bool__(self) -> bool:
        return False


class Either(Generic[L, R]):
    pass


@dataclass(frozen=True)
class Left(Either[L, R]):
    value: L


@dataclass(frozen=True)
class Right(Either[L, R]):
    value: R
