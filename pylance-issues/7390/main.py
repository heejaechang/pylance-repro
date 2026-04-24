# SCENARIO: protocol attributes implemented by concrete classes should stay linked for Find All References and Rename.
# TARGET: `P.a`, `Q.a`, `self.a`, `B.a` and `P.b`, `Q.b`, `self.b`, `B.b`
# TRIGGER: run Find All References or Rename on representative `a` and `b` members below.
# EXPECT: each `a` site is linked with the other `a` declarations/implementations, and each `b` site is linked with the other `b` declarations/implementations.
# VERIFY: if any probe returns only a partial or isolated set, the bug still reproduces.
# RECOVER: undo the rename or reload the file.

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