from enum import StrEnum


# Case A - a plain, top-level StrEnum
class OrdStatus(StrEnum):
    NEW = "0"
    FILLED = "2"


# Case B - a StrEnum nested inside classes
class FIX:
    class ExecType:
        Tag = 150

        class Val(StrEnum):
            NEW = "0"
            PARTIAL_FILL = "1"
            FILL = "2"


# Verification steps:
#   1. Place the cursor immediately after the dot on `OrdStatus.` below and
#      trigger completion (Ctrl/Cmd+Space).
#   2. Repeat for `FIX.ExecType.Val.`.
#
# Expected: declared enum members (NEW, FILLED / NEW, PARTIAL_FILL, FILL) at the
#           TOP of the list.
# Actual (bug): members appear at the BOTTOM, below inherited str methods
#           (capitalize, casefold, ...) and object/EnumType dunders.

OrdStatus.
FIX.ExecType.Val.
