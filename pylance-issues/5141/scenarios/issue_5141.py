# SCENARIO: match/case completion should prioritize the union member classes
# TARGET: the cursor position after `case ` on the final line below
# TRIGGER: Completion
# EXPECT: completion opens in the pattern position for `v: First | Second`
# VERIFY: the visible top of the completion list includes `First` and `Second` as the prioritized suggestions for the union-typed match subject
# RECOVER: no recovery needed

class First:
    first_attr: bool = True


class Second:
    second_attr: int = 42


def handle_obj(v: First | Second) -> None:
    match v:
        case 