# SCENARIO: signature help for an unpacked parameterized TypedDict should resolve the concrete parameter type
# TARGET: signature help at `func(`
# TRIGGER: place the cursor inside `func(` and show signature help
# EXPECT: the signature help shows `(*, t: int) -> None`
# VERIFY: if the popup still shows `t: T@TD` instead of `t: int`, the bug still reproduces
# RECOVER: no recovery needed

from typing import TypedDict, Unpack


class TD[T](TypedDict):
    t: T


def func(**kwargs: Unpack[TD[int]]):
    pass


func(