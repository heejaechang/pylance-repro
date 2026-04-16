# SCENARIO: keys in inline TypedDict syntax should not be treated as variables
# TARGET: hover over `"as_var"` inside the inline TypedDict annotation
# TRIGGER: inspect the hover or symbol classification for the key token
# EXPECT: the key is treated as a TypedDict key/string literal rather than a variable named `as_var`
# VERIFY: hovering the key should not report `(variable) as_var: Unknown`
# RECOVER: no recovery needed

from typing import TypedDict


a: TypedDict['as_var': int, 'normal': str] = ...

as_var = 2