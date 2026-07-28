# Repro workspace — pylance-release issue #8139

**Title:** Pylance causes auto whitespaces to be trimmed
**Issue:** https://github.com/microsoft/pylance-release/issues/8139
**Labels:** `team needs to reproduce`
**Reported environment:** Pylance 2026.3.1, VS Code, Windows 11 24H2 (Build 26100.8875)

## Summary

When the user presses **Enter** to split an already-indented line (cursor
positioned after the leading whitespace, before the code), Pylance's
format-on-type (DocumentOnTypeFormatting) Enter handler deletes the leading
whitespace that is left behind on the previous line.

Reported facts:
- Reproduces even with `"editor.trimAutoWhitespace": false` (user + workspace).
- Only occurs in `.py` files with the Pylance extension enabled.
- Placing a `#` on the affected line prevents the trimming.
- `editor.formatOnType` (default-on for Python) is the real gate.

## Repro steps

1. Open `scenarios/issue_8139.py`.
2. Put the cursor on the whitespace-only indented line, immediately in front of
   `print()` (character 4, after the 4 leading spaces).
3. Press **Enter**.

**Expected:** Everything after the cursor moves to a new line; everything
before the cursor (the leading whitespace) stays untouched.

**Actual:** Everything after the cursor moves to a new line, but the whitespace
before the cursor is removed.

## Root cause (from investigation)

Introduced by PR #8377 ("Clear whitespace-only previous line on Enter
format-on-type", commit 193cf0ae0). In
`packages/pylance-internal/src/languageService/pythonFormatOnTypeProvider.ts`,
`_formatOnTypeEnter` calls `_getWhitespaceOnlyPreviousLineCleanupEdit`, which
returns a `TextEdit.del` removing ALL leading whitespace of the previous line
whenever that line is whitespace-only and the preceding non-whitespace token is
2+ lines above (and no comment is nearby). That cleanup was intended for the
"press Enter twice on an auto-indented blank line" case, but it also fires when
the user deliberately splits an indented line, deleting user indentation.
