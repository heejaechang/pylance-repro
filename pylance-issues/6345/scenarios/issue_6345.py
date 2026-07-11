# SCENARIO: when pyproject pins a lower pythonVersion than the selected interpreter, the user should be able to see that version mismatch from the UI
# TARGET: `reveal_type` in the import line below
# TRIGGER: Hover and inspect the visible status/version surfaces
# EXPECT: with the repo interpreter selected and pyproject pythonVersion set to 3.9, `reveal_type` reports as unavailable
# VERIFY: some user-visible surface identifies that the effective language version is 3.9 rather than only showing the interpreter version; if the diagnostic appears but no visible surface explains the 3.9-based behavior, record fail
# RECOVER: no recovery needed

from typing import Literal, overload, reveal_type