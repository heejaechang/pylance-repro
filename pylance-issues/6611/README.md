# Issue #6611 - mkdocstrings cross-reference syntax support

**Issue**: https://github.com/microsoft/pylance-release/issues/6611
**Type**: Enhancement request

## What to verify

The user reports that mkdocstrings cross-reference syntax renders "ugly" in Pylance hover:
- `[`SomeClass`][full.path.SomeClass]` — shows raw brackets and backticks
- `[`full.path.SomeClass`][]` — shows raw brackets and backticks

Compare with Sphinx syntax (`:class:`SomeClass``) which renders cleanly.

## Verification steps

1. Open `mymodule.py`
2. Hover over `example` function
3. Observe docstring rendering in hover panel

## Expected (user request)
The mkdocstrings cross-reference syntax should render cleanly (e.g., just showing `SomeClass` as a link or clean text).

## Actual (current behavior)
The raw markdown link syntax `[`SomeClass`][mymodule.SomeClass]` is displayed verbatim in the hover panel.

## Notes
- This is an enhancement request, not a bug
- The issue body provides screenshots comparing Sphinx (clean) vs mkdocstrings (ugly)
- PR #7469 added clickable links for RST `:class:` / `:func:` syntax but does NOT cover mkdocstrings markdown-style references
