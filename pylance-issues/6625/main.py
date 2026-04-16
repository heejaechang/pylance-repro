 # SCENARIO: TypedDict update operations should not produce false-positive diagnostics
 # TARGET: `c.update({"": ""})` and `c |= {"": ""}`
 # TRIGGER: inspect diagnostics on both update operations
 # EXPECT: the operations analyze without spurious TypedDict errors
 # VERIFY: if either line is flagged incorrectly, the bug still reproduces
 # RECOVER: no recovery needed

import typing


class C(typing.TypedDict):
    abc: str


c: C = {}
c.update({"": ""})
c |= {"": ""}