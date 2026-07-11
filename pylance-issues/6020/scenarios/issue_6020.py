# SCENARIO: hover on a common key of a union TypedDict should avoid duplicate identical entries
# TARGET: the `"common"` key inside `func({"type_": 1, "common": 1})` below, not the field declarations above
# TRIGGER: Hover
# EXPECT: hover opens for the targeted dict key expression
# VERIFY: hover content contains a single `common: int` entry; if identical `common: int` appears more than once, record fail
# RECOVER: no recovery needed

from typing import TypedDict


class A(TypedDict):
    type_: int
    common: int


class B(TypedDict):
    type_: str
    common: int


def func(arg: A | B):
    pass


func({"type_": 1, "common": 1})