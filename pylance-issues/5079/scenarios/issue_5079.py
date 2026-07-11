# SCENARIO: signature help for an overload without a docstring should not borrow another overload's docstring
# TARGET: the cursor position inside `fn(True|)` below
# TRIGGER: Signature Help
# EXPECT: the active overload corresponds to the `bool` overload
# VERIFY: the signature-help surface for the `bool` overload does not show `Has int as input` or `Has str as input`
# RECOVER: no recovery needed

from typing import overload


@overload
def fn(x: int) -> int:
    '''Has int as input'''
    ...


@overload
def fn(x: str) -> str:
    '''Has str as input'''
    ...


@overload
def fn(x: bool) -> bool:
    ...


def fn(x):
    return x


fn(True)