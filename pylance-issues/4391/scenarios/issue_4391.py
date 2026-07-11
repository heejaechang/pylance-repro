# SCENARIO: signature help for a ParamSpec-forwarding helper should expand the callable argument's concrete parameters
# TARGET: the gap after `foo, ` inside `result = not_a_decorator(foo, )` below
# TRIGGER: Signature Help
# EXPECT: signature help opens for the `not_a_decorator` call
# VERIFY: the signature help content expands the callable argument into `foo`'s concrete parameters, surfacing `arg1: int`, `arg2: str`, and `arg3: float` rather than only `P.args` and `P.kwargs`
# RECOVER: no recovery needed

from typing import Callable, ParamSpec, TypeVar


P = ParamSpec('P')
V = TypeVar('V')


def not_a_decorator(fn: Callable[P, V], /, *args: P.args, **kwargs: P.kwargs) -> V:
    return fn(*args, **kwargs)


def foo(arg1: int, /, arg2: str, *, arg3: float) -> bool:
    return arg1 == 1 and arg2 == 'hi' and arg3 == 0.0


result = not_a_decorator(foo, )