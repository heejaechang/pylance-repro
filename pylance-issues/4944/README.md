# Issue #4944 - Semantic modifiers for keyword arguments

**Issue**: https://github.com/microsoft/pylance-release/issues/4944

## Summary

User requests:
1. A semantic token modifier to distinguish keyword argument names (`bar=...`) from regular parameter references
2. Dataclass kwargs in constructor calls should get `parameter` type (not `property`/`variable`)

## Current Behavior (verified)

- **Regular class kwargs** (`RegularClass(bar=bar_kwarg)`): Gets `parameter` type with `keywordArgument` modifier ✅
- **Dataclass kwargs** (`Dataclass(bar=bar_kwarg)`): Gets `variable` type with `classMember` modifier ❌

## Expected Behavior

Both cases should produce `parameter` type with `keywordArgument` modifier.

## Verification Checklist

From the issue body:
> "An added modifier like `function-call` so we can color `parameter.function-call` should do the trick."

1. [ ] Check that `bar` in `RegularClass(bar=bar_kwarg)` gets semantic token type `parameter` with a distinguishing modifier — **PASSES** (gets `keywordArgument` modifier)
2. [ ] Check that `bar` in `Dataclass(bar=bar_kwarg)` gets semantic token type `parameter` (not `property` or `variable`) — **FAILS** (gets `variable` with `classMember`)

From user comment:
> "I strongly believe that whenever I call a function or class, we are only talking about parameters. Never properties."

## Root Cause

In `semanticTokenProvider.ts`, when the keyword argument name resolves to a declaration:
- For regular class `__init__` params: resolves as `DeclarationType.Param` → gets `parameter` + `keywordArgument`
- For dataclass fields: resolves as `DeclarationType.Variable` (class body variable) → gets `variable` + `classMember`, bypassing the `keywordArgument` logic

The `_getKeywordArgumentModifiers()` check is only applied in the `Param` case (line 855) and the fallback `else` branch (line 982). The `Variable` case (line 901) does not check for keyword argument context.

## Files

- `test_issue4944.py` — Exact code from the issue body
