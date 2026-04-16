# SCENARIO: hovering a subclass without its own docstring should inherit the parent class docstring
# TARGET: `B` in `b = B()` below, not the class declaration above
# TRIGGER: Hover
# EXPECT: hover opens on the subclass reference token
# VERIFY: the hover content for `B` includes `My docstring.` inherited from `A`
# RECOVER: no recovery needed

class A:
    """My docstring."""


class B(A):
    pass


a = A()
b = B()