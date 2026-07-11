# SCENARIO: inserted return type inlay hints should preserve the displayed alias form rather than resolving it to the expanded underlying type
# TARGET: the return type inlay hint on `def test()` below
# TRIGGER: apply the visible return type inlay hint
# EXPECT: applying the hint inserts `-> NDArray[Any]`
# VERIFY: the inserted annotation does not expand to the resolved alias form
# RECOVER: revert the file to its original text after the check

import numpy as np
from numpy.typing import NDArray


def test():
    a = np.array([1, 2, 3])
    return a