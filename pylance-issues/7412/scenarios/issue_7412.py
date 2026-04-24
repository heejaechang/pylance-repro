# SCENARIO: Find All References should ignore strict-editable shadow-tree files under `build/__editable__...`.
# TARGET: `logger` in `../pegen/parser.py`
# TRIGGER: run Find All References on `logger` in `pegen/parser.py`
# EXPECT: results include the source-side `src/pegen/grammar_parser.py` import but exclude `../build/__editable__.pegen-0.3.1.dev6+qcf8e62d-py3-none-any/pegen/grammar_parser.py`
# VERIFY: if the `build/__editable__...` file appears in the reference list, the bug still reproduces
# RECOVER: no recovery needed