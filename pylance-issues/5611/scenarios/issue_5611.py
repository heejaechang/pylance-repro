# SCENARIO: semantic highlighting should recognize obvious `Final` constants consistently with uppercase constants
# TARGET: compare `A_CONSTANT` with `another_constant: Final`
# TRIGGER: inspect semantic token classes with semantic highlighting enabled
# EXPECT: the `Final` constant should be highlighted consistently with the uppercase constant rather than as an ordinary variable
# VERIFY: if `another_constant` still renders as a plain variable while `A_CONSTANT` gets constant-style highlighting, the issue remains valid
# RECOVER: no recovery needed

from typing import Final


A_CONSTANT = None
another_constant: Final = None