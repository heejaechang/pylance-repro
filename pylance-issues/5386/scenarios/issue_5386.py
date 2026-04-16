# SCENARIO: renaming a TypedDict key should also update string-literal index accesses that refer to that key
# TARGET: `bar` in the TypedDict definition below
# TRIGGER: Rename Symbol
# EXPECT: rename starts from the TypedDict key definition
# VERIFY: renaming `bar` to `baz` updates both the definition and the `mydict["bar"]` usage to `mydict["baz"]`
# RECOVER: revert the file to its original contents after the check

from typing import TypedDict


class Foo(TypedDict):
    bar: str


def myfunc(mydict: Foo):
    print(mydict["bar"])