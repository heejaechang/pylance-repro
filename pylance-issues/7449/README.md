# Issue #7449 - Pylance misidentifies a method as an attribute

**Issue**: https://github.com/microsoft/pylance-release/issues/7449

## Workspace Setup

- `test_script.py`: User's code verbatim from the issue (note: lines 8-9 have syntax errors from the original report — spaces in identifiers)
- `requirements.txt`: `azure-mgmt-authorization` and `azure-identity` (packages the user is using)
- `.venv/`: Virtual environment with installed packages (azure-mgmt-authorization==4.0.0)
- `.vscode/settings.json`: Points interpreter to the local venv, enables standard type checking

## Verification Checklist

From the issue body verbatim:

1. Open `test_script.py`
2. Verify: "PyLance throws an unknown attribute warning about `list_for_subscription` and marks my code as having a 'problem.'"
3. Right click on "list_for_subscription()"
4. Click Peek → Peek Definition
5. Verify: "This shows the definition as expected"

**Expected behavior** (user's words): "No squiggly highlights or 'your code has a problem' warning for perfectly valid code."

**Actual behavior** (user's words): PyLance throws an unknown attribute warning.

## Investigation Findings

The `azure-mgmt-authorization` v4.0.0:
- Ships `py.typed` (inline types, no separate stubs needed)
- Has a multi-API dispatch pattern: `role_assignments` property returns different `RoleAssignmentsOperations` classes depending on runtime API version selection
- The property has **no return type annotation** — Pylance infers a Union of ALL possible RoleAssignmentsOperations types
- `list_for_subscription` only exists in API versions: `v2020_10_01_preview`, `v2022_04_01`
- It does NOT exist in: `v2015_07_01`, `v2018_01_01_preview`, `v2018_09_01_preview`, `v2020_04_01_preview`
- Pylance correctly reports the attribute access is unsafe on the inferred Union type

**Conclusion**: This is correct Pylance behavior. The Azure SDK ships incomplete type annotations for its multi-API dispatch pattern.

## Notes

- The code in the issue has syntax errors on lines 8-9 (`role assignments = []` and `role_assignments iterable` — spaces in identifiers). These are likely copy-paste errors in the report and don't affect the core complaint about `list_for_subscription`.
