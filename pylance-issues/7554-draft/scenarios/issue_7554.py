# SCENARIO: kwargs typed with `Unpack[...]` should not cause call-site keyword names to be tokenized as variables
# TARGET: compare `bar` in `foo(bar='lol')` with `bar` in `foobar(bar='lol')`
# TRIGGER: inspect editor token classes with semantic highlighting disabled
# EXPECT: both keyword names are tokenized consistently as call-site keyword syntax
# VERIFY: the `bar` token in the typed-kwargs call should not render differently from the untyped control call
# RECOVER: no recovery needed

from typing import TypedDict, Unpack


class FooRequest(TypedDict):
    bar: str


def foo(**kwargs: Unpack[FooRequest]):
    pass


def foobar(**kwargs):
    pass


foo(bar='lol')
foobar(bar='lol')