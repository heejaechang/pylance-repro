from typing import Protocol, final
import dataclasses

class P(Protocol):
    a: float
    b: float

class Q(Protocol):
    a: float
    b: float

@final
class A(P, Q):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b: float = b

@final
@dataclasses.dataclass
class B(P, Q):
    a: float
    b: float
