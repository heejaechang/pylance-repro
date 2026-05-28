# fmt: off
"""
Issue: https://github.com/microsoft/pylance-release/issues/7440
Title: Errors for standard library and external package files persist after the files are closed
Classification: bug — diagnostic lifecycle
Staff reproduced: 2025-07-23 (rchiodo)

SCENARIO: Verify diagnostics for non-workspace files clear on close

PRECONDITIONS:
- Python 3.10+ with asyncio.Runner available (3.11+)
- Pylance active, basic type checking mode or stricter
- No extra extensions that interfere with diagnostics

VERIFICATION STEPS:
1. Open main.py
2. Go-to-definition on Runner().run (Ctrl+click on "run")
   -> This opens asyncio/runners.py (stdlib source, not stub)
3. Wait for diagnostics to appear in the Problems panel for runners.py
   -> reportOptionalMemberAccess errors are expected on self._loop usage
4. Close the runners.py tab (not main.py)
5. Wait 3-5 seconds for diagnostic debounce
6. Check the Problems panel

PASS CRITERIA:
- After closing runners.py, its diagnostics are cleared from the Problems panel
  within ~5 seconds (no restart required)

FAIL CRITERIA (confirms bug still exists):
- Diagnostics for runners.py remain in the Problems panel after closing the tab
- Only clearing on language server restart

NOTES:
- rchiodo also saw diagnostics for base.pyi (django) without even opening it
- The issue may have two facets:
  (a) diagnostics persist after explicit close
  (b) diagnostics appear for files never explicitly opened
- Both are valid confirmations of this bug
- If Python < 3.11, asyncio.Runner won't exist; use an alternative stdlib file
  with known diagnostics or a third-party package repro instead
"""
# fmt: on
