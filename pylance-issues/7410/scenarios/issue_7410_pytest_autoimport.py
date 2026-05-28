# Issue 7410: Auto imports in pytest files are not working
# https://github.com/microsoft/pylance-release/issues/7410
#
# REPRO SCENARIO:
#   1. Open test_example.py (which references `FixtureRequest` without an import)
#   2. Place cursor on `FixtureRequest` (the unresolved name)
#   3. Trigger quick-fix / code action for auto-import
#   4. EXPECTED: A code action offers "from pytest import FixtureRequest"
#      and applying it adds `from pytest import FixtureRequest` at the top
#   5. ACTUAL (reported): Instead of `from pytest import FixtureRequest`,
#      the auto-import inserts `import pytest` and rewrites the annotation
#      to `pytest.FixtureRequest`, or no auto-import is offered at all.
#
# ROOT CAUSE (staff-identified):
#   The async hover/auto-import provider cannot use chained files to detect
#   pytest implicit imports. The sync path handles this via chained-file
#   lookup; the async path lacks this capability.
#
# DEPENDENCIES:
#   - pytest must be installed in the workspace's Python environment
#   - python.analysis.autoImportCompletions should be enabled (default)
#
# VERIFICATION:
#   - If auto-import code action correctly offers "from pytest import FixtureRequest"
#     → issue is FIXED
#   - If auto-import offers "import pytest" + rewrites to "pytest.FixtureRequest",
#     or no pytest-related auto-import appears → issue STILL REPRODUCES
