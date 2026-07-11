# SCENARIO: hover on a decorated overloaded function alias should preserve the original docstring
# TARGET: the symbol `g` on the final line below
# TRIGGER: hover over `g`
# EXPECT: the hover includes `Docstring for f`
# VERIFY: the overloaded decorated alias keeps the docstring through the hover provider
# RECOVER: no recovery needed

from typing import Callable, ParamSpec, TypeVar, overload

T = TypeVar('T')
P = ParamSpec('P')


def decorator(fn: Callable[P, T]) -> Callable[P, T]:
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
        return fn(*args, **kwargs)

    return wrapped


@overload
def f(x: int) -> int:
    """Docstring for f"""


@overload
def f(x: str) -> str:
    """Docstring for f"""


def f(x: int | str) -> int | str:
    """Docstring for f"""
    return x


g = decorator(f)