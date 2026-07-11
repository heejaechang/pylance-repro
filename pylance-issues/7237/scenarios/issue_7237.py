# SCENARIO: autocomplete inside a match arm should not surface invalid values
# TARGET: the completion lists after `Direction.` and `Direction.F` inside the match arm
# TRIGGER: trigger completion inside the `case Move(direction=Direction.F)` arm
# EXPECT: enum-member completion should stay focused on valid enum values rather than unrelated identifiers like `find`
# VERIFY: if the suggest widget still mixes enum members with unrelated values in the match arm, the issue remains valid
# RECOVER: no recovery needed

from dataclasses import dataclass
from enum import StrEnum


class Direction(StrEnum):
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'


@dataclass
class Move:
    __match_args__ = ('direction', 'distance')

    direction: Direction
    distance: int


move = Move(Direction.FORWARD, 10)

match move:
    case Move(direction=Direction.F):
        ...
    case _:
        ...