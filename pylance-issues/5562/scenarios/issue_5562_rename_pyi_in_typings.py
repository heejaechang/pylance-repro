# Issue 5562: Moving a .pyi file shouldn't move its .py twin when under the typings folder
#
# SETUP:
# - outsideLib/needs_stub.py exists with `def foo(x): return x`
# - typings/needs_stub.pyi exists with `def foo(x: int) -> int: ...`
# - python.analysis.extraPaths = ["./outsideLib"]
# - python.analysis.stubPath = "typings"
#
# REPRO STEPS:
# 1. Create a new folder "newfolder" under typings/
# 2. Rename/move typings/needs_stub.pyi → typings/newfolder/needs_stub.pyi
#    (e.g. via drag-and-drop in Explorer or F2 rename)
# 3. Observe what edits Pylance proposes via workspace/willRenameFiles
#
# EXPECTED: Only the .pyi file moves. The .py file under outsideLib/ stays put.
# ACTUAL (BUG): Pylance also emits a RenameFile edit moving
#   outsideLib/needs_stub.py → typings/newfolder/needs_stub.py
#
# ROOT CAUSE: renameFileProvider.ts _getStubAndFilePairInfo does not
# special-case stubs that live inside the configured stubPath; it always
# pairs the stub with its .py twin and co-renames both.
#
# VERIFICATION: This is a rename-provider behavior, not a static-analysis
# result. Verification requires triggering willRenameFiles on the .pyi path
# and checking whether the response includes an unwanted RenameFile edit
# for the .py twin. A Jest test (using PylanceTestState + rename provider)
# is the faithful repro path.

from needs_stub import foo

reveal_type(foo)  # Should resolve via stub: (x: int) -> int
