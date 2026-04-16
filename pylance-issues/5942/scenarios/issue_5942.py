# SCENARIO: go to definition from a variable definition should stay at that definition instead of jumping to a later usage
# TARGET: the `a` in `a = MyType()` below, not the `a` in `a.name`
# TRIGGER: Go to Definition
# EXPECT: the cursor is on the assignment-target definition before triggering the command
# VERIFY: after go to definition, the cursor stays on the `a = MyType()` line and does not jump to `a.name`
# RECOVER: no recovery needed

class MyType:
    name: str


a = MyType()

a.name