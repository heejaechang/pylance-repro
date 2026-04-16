 # SCENARIO: semantic highlighting should stay consistent when a condition becomes unreachable after reassignment
 # TARGET: `argv` in `sys.argv` inside `first`
 # TRIGGER: compare the semantic highlighting of `sys.argv` in `first` and `second`
 # EXPECT: the `argv` segment is highlighted consistently in both functions
 # VERIFY: if `argv` is not highlighted in `first` but is highlighted in `second`, the bug still reproduces
 # RECOVER: no recovery needed

import sys
from typing import Optional
from copy import copy


def first(args: Optional[list[str]]) -> None:
    args = copy(sys.argv)
    print(sys.argv if args is None else args)


def second(args: Optional[list[str]]) -> None:
    print(sys.argv if sys.argv is None else args)