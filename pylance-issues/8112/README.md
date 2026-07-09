# Issue 8112 — "4+1 indenting on new line when tabs in a file"

- **Issue:** https://github.com/microsoft/pylance-release/issues/8112
- **Related:** https://github.com/microsoft/pylance-release/issues/5635
- **Labels:** bug, user responded
- **Reported env:** Pylance 2026.2.1, Windows 10.0.19045, Python 3.14.5
- **Classification:** Bug — format-on-type auto-indent (Pylance-only feature)

## Summary

In a Python file that **mixes tab-indented lines and space-indented lines**,
pressing <kbd>Enter</kbd> after a **tab-indented** parent line makes Pylance's
format-on-type auto-indent emit **more than 4 spaces** (the reporter and
maintainer @rchiodo saw **5**) on the new line, instead of matching the file's
real 4-space / 1-tab indent unit. This is the "4+1" the reporters describe.
Disabling the Pylance extension makes the problem go away (it removes Pylance's
`onTypeFormatting` Enter handler).

## Root cause (confirmed by code inspection + repro test)

Pylance's tokenizer computes a single `predominantTabSequence` for the whole
file (`packages/pyright/.../parser/tokenizer.ts` ~L787-808). When tabs are **not**
the majority indent, it falls into the "space" branch and sets the predominant
indent width to the **average** spaces-per-indent, rounded and capped at 8:
`averageSpacePerIndent = round(_indentSpacesTotal / _indentCount)`.

For this file the average lands at **5–6** (the mix of `\t`, 4-space, 8-space,
and one **9-space** body line skews the average above 4). Then, when Enter is
pressed after the tab-indented `\timport ac` line, Pylance derives the new
line's indentation from the parent line via
`IndentationUtils.getIndentationFromText` /
`_getIndentationFromIndentToken` (`packages/pylance-internal/src/common/indentationUtils.ts`
~L288-301, ~L559-582), which **expands each leading tab to that inferred
width** (`_getTabSize`, ~L1259-1268). So a single leading tab becomes 5–6
columns, and `createHangingReindentString` renders that many spaces on the new
line — hence "4+1".

Note: `editor.tabSize` is **not** the driver in this specific (space-predominant)
file — a repro test showed the emitted indent is 6 regardless of
`editor.tabSize` (4/5/8). The driver is the tokenizer's averaged
`predominantTabSequence`. (`editor.tabSize` only matters in the separate
*pure-tab-predominant* variant of this bug family.)

## Files

- `scenarios/issue_8112.py` — @rchiodo's exact maintainer-confirmed repro text.
  `import ac` is indented with a literal **tab** and has a **trailing tab**;
  the `class Button` body uses 4/8 spaces with one **9-space** line.

## Repro steps (real VS Code + Pylance)

1. Open this folder in VS Code with the Pylance extension active.
2. Open `scenarios/issue_8112.py`.
3. Confirm format-on-type is enabled (this workspace's `.vscode/settings.json`
   sets `"editor.formatOnType": true` for Python; it is also on by default with
   the Python extension). Leave `editor.detectIndentation` at its default
   (`true`) and `editor.tabSize` at `4`.
4. Click at the **end** of the `\timport ac\t` line (line 5) — i.e. after the
   `import ac` text and its trailing whitespace.
5. Press <kbd>Enter</kbd>.

## Expected vs actual

- **Expected:** the new (blank) line is indented to match the `try:` body — i.e.
  **4 spaces** (or one tab), the file's real indent unit.
- **Actual (bug):** the new line is indented with **5 spaces** (rchiodo's file)
  — more than 4. In this transcription the same mechanism yields **6 spaces**;
  the exact count (5 vs 6) depends on the precise per-line space counts, but it
  is always **> 4**, which is the defect.

## Verification signal

The wrong indent (a leading-whitespace-only auto-indent producing **more than 4
spaces / not matching the file's 4-space indent unit**) on the line created by
pressing Enter after `\timport ac\t` confirms the bug. Matching exactly 4
spaces (or 1 tab) would mean the issue does not reproduce.
