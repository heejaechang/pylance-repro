from enum import Enum
from typing import Any, Generic, TypeVar, TypedDict
from typing import overload as _overload


class Domain(Enum):
    FULL = "full"
    REDUCED = "reduced"


@_overload
def convert(value: int) -> int: ...


@_overload
def convert(value: str) -> str: ...


def convert(value: int | str) -> int | str:
    return value


T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value


def identity(value: T) -> T:
    return value


class Metadata(TypedDict, total=False):
    signature: dict[str, Any]


metadata: Metadata = {}
metadata_get = metadata.get
