# SCENARIO: `match` should stay keyword-colored when followed by the unary `~` operator
# TARGET: `match` on the first line below
# TRIGGER: inspect syntax coloring with semantic highlighting disabled
# EXPECT: textmate coloring is visible because semantic highlighting is disabled in workspace settings
# VERIFY: `match` is rendered with keyword coloring even in `match ~1:`
# RECOVER: no recovery needed

match ~1:
    case _:
        pass