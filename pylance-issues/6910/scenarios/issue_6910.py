# SCENARIO: inserted return type inlay hints should preserve the displayed numpy scalar type when the return value is a list
# TARGET: the return type inlay hint on `def foo()` below
# TRIGGER: apply the visible return type inlay hint
# EXPECT: applying the hint inserts `-> list[numpy.float64]`
# VERIFY: the inserted annotation does not become a broken or over-resolved form
# RECOVER: revert the file to its original text after the check

import numpy


def foo():
    return [numpy.float64(1.5)]