 # SCENARIO: inlay hints should honor the configured Python version
 # TARGET: the inferred return type of `get`
 # TRIGGER: turn on inlay hints and inspect the inferred return type for `get`
 # EXPECT: with Python 3.8 configured, the hint uses `Optional[int]` rather than `int | None`
 # VERIFY: if the hint shows `int | None`, the bug still reproduces
 # RECOVER: no recovery needed

import os


def get(id=None):
    return None if os.getenv('something') else int(1)