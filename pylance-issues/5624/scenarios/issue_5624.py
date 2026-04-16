# SCENARIO: an unresolved member access on a value narrowed by `None` should offer a quick fix that inserts an `assert x is not None` guard
# TARGET: `foo` in `x.foo()` below
# TRIGGER: Quick Fix
# EXPECT: the quick-fix menu opens on the member-access error
# VERIFY: executing the assert-based narrowing quick fix inserts `assert x is not None` immediately above `x.foo()`
# RECOVER: revert the file to its original contents after the check

class A:
    def foo(self):
        pass


def bar(x) -> A | None:
    if x > 1:
        return A()
    else:
        return None


x = bar(2)
x.foo()