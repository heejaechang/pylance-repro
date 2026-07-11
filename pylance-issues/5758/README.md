# Issue #5758 - Surface reportAttributeAccessIssue even when type checking mode set to off

**Issue**: https://github.com/microsoft/pylance-release/issues/5758
**Type**: Enhancement request

## Reproduction

This is an enhancement request, not a bug. The workspace demonstrates the **current behavior** (no diagnostic) which the reporter wants changed.

### Setup

- `.vscode/settings.json` sets `"python.analysis.typeCheckingMode": "off"`
- `test.py` contains a TypedDict with dot-access (which causes a runtime error)

### Steps

1. Open `test.py` in VS Code with Pylance
2. Observe that `p.name` (line 10) has **no** diagnostic squiggle

### Expected (per enhancement request)

> "Surface `reportAttributeAccessIssue` as a suggestion/hint diagnostic even when `typeCheckingMode` is `"off"`"
>
> The user expects `p.name` to show an information/hint-level diagnostic indicating that TypedDict keys should be accessed with `p["name"]` syntax.

### Actual (current behavior - by design)

No diagnostic is shown because `typeCheckingMode: "off"` sets `reportAttributeAccessIssue: 'none'`.

## Verification checklist

- [ ] With `typeCheckingMode: "off"`, confirm `p.name` produces NO diagnostic (current behavior)
- [ ] With `typeCheckingMode: "standard"`, confirm `p.name` produces an error diagnostic (proves the rule works)

## Notes

- Enhancement requires a product decision on whether to surface diagnostics in "off" mode
- Existing plan at `.github/plans/future/FIX_5758_TYPEDDICT_SUGGESTION_PLAN.md`
- The `.vscode/settings.json` is required to set typeCheckingMode to "off" as the issue describes
