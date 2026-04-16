# SCENARIO: go to definition on `os.chmod` should open a real library source or doc-bearing file rather than falling back to a bare typeshed stub
# TARGET: `chmod` in `os.chmod('tmp-target', 0o777)` below
# TRIGGER: Go to Definition
# EXPECT: the symbol resolves and navigation opens a definition target
# VERIFY: after Go to Definition, the active editor lands in a real `os` library source location rather than a `typeshed-fallback` `.pyi` stub for `os.chmod`
# RECOVER: navigate back to this scenario file after the check

import os


os.chmod('tmp-target', 0o777)