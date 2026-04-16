# SCENARIO: variable type inlay hints for ParamSpec-instantiated generics should display the ParamSpec result rather than a spurious Callable payload
# TARGET: the variable type inlay hint for `b =` below
# TRIGGER: inspect the visible variable type inlay hint
# EXPECT: the hint reflects `A[(int), str]`
# VERIFY: the inlay hint does not expand the ParamSpec position into `Callable[[int], Any]`
# RECOVER: no recovery needed

from typing import Callable, reveal_type


class A[**P, R]:
    @classmethod
    def from_fn(cls, fn: Callable[P, R]) -> 'A[P, R]': ...


def f(a: int) -> str: ...


b = A[[int], str].from_fn(f)

reveal_type(b)