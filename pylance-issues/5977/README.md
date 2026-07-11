# Issue #5977 - Signature help inside string literals

**Issue**: https://github.com/microsoft/pylance-release/issues/5977

## Reported Problem

> "Annoying intellisense: showing me parameter popup during editing str parameter"

The user reports that signature help (parameter hints popup) appears when editing text
inside string literals in function call arguments.

## Verification Checklist

1. Open `test_scenario.py`
2. Place cursor inside the string `'hello'` in `foo(key1='hello')` (e.g., between `h` and `e`)
3. **Expected**: No signature help popup appears
4. **Actual (before fix)**: Signature help for `foo()` was shown
5. Place cursor inside the f-string literal portion `"hello "` in `foo(key1=f"hello {key2} world")`
6. **Expected**: No signature help popup appears inside the literal portion
7. Place cursor inside `{key2}` in the f-string expression
8. **Expected**: Signature help IS shown (cursor is in expression, not string content)

## Fix Reference

Fixed in PR #8383 (merged 2026-05-15). The fix adds a token-level guard in
`signatureHelpProvider.ts` that returns `undefined` when the cursor offset is
strictly inside a `TokenType.String` or `TokenType.FStringMiddle` token.

## Notes

- The reporter also mentioned unwanted *completions* inside strings (comment #2160575589),
  which is a separate VS Code completion trigger behavior issue, not signature help.
- The reporter found a workaround: `"editor.parameterHints.enabled": false`
