# SCENARIO: hover on `dict.update` should surface a docstring just like nearby `dict.fromkeys`
# TARGET: `update` in `{}.update()` below
# TRIGGER: Hover
# EXPECT: nearby `fromkeys` has a docstring-bearing hover surface for comparison
# VERIFY: hover on `update` includes a real docstring rather than only a signature line
# RECOVER: no recovery needed

{}.update()
{}.fromkeys([])