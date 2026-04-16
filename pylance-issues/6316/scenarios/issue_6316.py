# SCENARIO: go to definition on a collections.abc method should resolve to the real source file rather than typing.py or a fallback stub
# TARGET: `get` in `MutableMapping.get` below
# TRIGGER: Go to Definition
# EXPECT: hover or symbol info identifies `get` as a method on `MutableMapping`
# VERIFY: after Go to Definition, the opened location is in the real collections source implementation (for example `_collections_abc.py`), not in `typing.py` or a fallback stub file
# RECOVER: navigate back to the scenario file after the check

from collections.abc import MutableMapping


MutableMapping.get