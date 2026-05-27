# Issue #7998 Verification Workspace

**Issue**: https://github.com/microsoft/pylance-release/issues/7998
**Title**: improve override completion signature generation

## Summary

Follow-up to #6036: when auto-completing an `__init__` override, Pylance should
preserve full default value expressions (e.g., `conf.getboolean(...)`) AND add the
necessary import statements for symbols used in that expression.

## Expected Behavior (from issue)

When accepting the `__init__` override completion for `_FileSensor(FileSensor)`:
1. The signature should include `deferrable: bool = conf.getboolean("operators", "default_deferrable", fallback=False)`
2. An import edit should be added: `from base import FileSensor, conf` (appending `, conf` to existing import)

## Verification Checklist

1. Open `test.py` in VS Code with Pylance
2. Place cursor after `def __init__` inside `_FileSensor`
3. Trigger completions and accept the `__init__` override
4. **Check**: The generated signature preserves `conf.getboolean("operators", "default_deferrable", fallback=False)` (not `...`)
5. **Check**: An `additionalTextEdit` adds `conf` to the import from `base`

## Status

**Already fixed** by PR #8194 (merged 2026-04-08), which predates the issue filing (2026-04-23).
The fix adds a probe+replay mechanism in `methodSignatureGenerator.ts` and `asyncMethodSignatureGenerator.ts`
that:
- Checks if all symbols in the default value expression are top-level and safely referenceable
- If yes, preserves the expression and stages the necessary imports
- If not, falls back to `...`

Existing regression tests in `completions.common.ts` (line ~1730) cover this exact scenario.
