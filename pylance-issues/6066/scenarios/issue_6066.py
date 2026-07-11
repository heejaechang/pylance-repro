# SCENARIO: completion inside a list literal should not offer the next named parameter from the outer call
# TARGET: the empty line inside the `ranges=[ ... ]` list in the `Model(` call below
# TRIGGER: Completion
# EXPECT: completion opens at the cursor inside the list literal
# VERIFY: the suggestion list does not contain `commands=` while the cursor is still inside the `ranges` list
# RECOVER: no recovery needed


class Model:
    def __init__(self, ranges: list[str], commands: list[str]) -> None:
        pass


m = Model(
    ranges=[
        "a",
        
    ]
)