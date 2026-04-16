# SCENARIO: variable type inlay hints containing `Callable[..., Any]` should remain insertable
# TARGET: the variable type inlay hint for `conv = {` below
# TRIGGER: apply the visible variable type inlay hint
# EXPECT: with variable type inlay hints enabled, `conv` shows an inferred hint that includes `Callable[..., Any]`
# VERIFY: applying the hint inserts a concrete type annotation for `conv` that includes `Callable[..., Any]`
# RECOVER: revert the file to its original text after the check

from io import StringIO
from typing import Any, Callable

import numpy as np

s = StringIO('1.618, 2.296\n3.141, 4.669\n')
conv = {
    0: lambda x: np.floor(float(x)),
    1: lambda x: np.ceil(float(x)),
}
a = np.loadtxt(s, delimiter=',', converters=conv)
print(a)