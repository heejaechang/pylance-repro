# SCENARIO: semantic highlighting should color only the inner atom, not the surrounding parentheses
# TARGET: the parentheses around `foo`, `b`, `False`, `None`, and `1`
# TRIGGER: inspect semantic token coloring in the editor
# EXPECT: the inner atom can carry semantic coloring, but the parentheses stay punctuation-colored
# VERIFY: surrounding parentheses do not inherit the same semantic token class/color as the enclosed name or literal
# RECOVER: no recovery needed

class H:
    pass

foo = 1
(
    foo
)
b = 2
a = (((b)))
a = (False)
a = (None)
a = (H.mro)
a = ('string')
a: (int) = (1)

if True:
    c = (
        not a or not b
    )