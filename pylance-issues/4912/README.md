# Issue #4912 — TextMate grammar incorrectly marks call-then-attribute decorator as syntax error

**Issue URL**: https://github.com/microsoft/pylance-release/issues/4912

## Reporter's scenario

A decorator defined as an instance method of a class, used via `@Formatter().decorator`,
gets visually highlighted as a syntax error (red/invalid) by the TextMate grammar, even
though the code is valid Python and runs correctly.

## Expected behavior

`@Formatter().decorator` should be highlighted normally (no red/invalid marking).
The pattern `@<expr>.<attr>` where `<expr>` includes a function call is valid Python 3.9+
decorator syntax (PEP 614 relaxed decorator expressions).

## Actual behavior

The `.decorator` portion (attribute access after the call) is highlighted as
`invalid.illegal.decorator.python` by the MagicPython TextMate grammar.

## Root cause (prior investigation)

In `packages/magicpython/grammars/src/MagicPython.syntax.yaml`, the `decorator` rule
opens with `((@)) \s* (?=[[:alpha:]_]\w*)` — an identifier-first lookahead — and only
chains one trailing `#function-arguments` block. It does not support continuing with
attribute access after a call (e.g., `@Cls().method`).

Existing in-repo fixture `packages/magicpython/test/functions/decorators8.py` independently
encodes this same structural pattern as invalid: `@deco().abc  # SyntaxError: invalid syntax`
with `.abc` classified as `invalid.illegal.decorator.python`.

## Verification checklist

1. [ ] Open `scenarios/formatter_decorator.py` in VS Code
2. [ ] Check line 12: `@Formatter().decorator`
3. [ ] Observe whether `.decorator` is highlighted as invalid (red/error scope)
4. [ ] If still invalid → issue is **still reproduced**
5. [ ] If highlighted normally → issue is **no longer reproduced** (grammar was fixed)

## Verification method

This is a **TextMate grammar** issue (syntax highlighting), NOT a Pylance diagnostic.
Verification requires checking the **tokenization scopes** in a real VS Code instance
(Developer: Inspect Editor Tokens and Scopes) or running `syntaxdev` against the grammar.

- Look for scope `invalid.illegal.decorator.python` on the `.decorator` portion
- A Pylance diagnostic (squiggly underline from the language server) is a separate concern
