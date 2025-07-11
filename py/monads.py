from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")
L = TypeVar("L")
R = TypeVar("R")


class Maybe(Generic[T]):
    pass


@dataclass(frozen=True)
class Just(Maybe[T]):
    value: T


@dataclass(frozen=True)
class Nothing(Maybe[T]):
    __match_args__ = ()  # TODO: not working: allow match-case to work cleanly


class Either(Generic[L, R]):
    pass


@dataclass(frozen=True)
class Left(Either[L, R]):
    value: L


@dataclass(frozen=True)
class Right(Either[L, R]):
    value: R
