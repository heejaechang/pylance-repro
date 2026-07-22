# Repro workspace — pylance-release #8135

**Issue:** [StrEnum members show at the bottom of the autocomplete list instead of the top](https://github.com/microsoft/pylance-release/issues/8135)

**Labels:** `team needs to reproduce`

## Summary

Completing on a `StrEnum` class (`MyStrEnum.`) puts the **declared enum members at the
bottom** of the suggestion list — below the inherited `str` methods (`capitalize`,
`casefold`, …) and `object`/`EnumType` dunders (`__str__`, …). The reporter expects the
declared members at the **top**.

This is isolated to Pylance's completion layer:

- The bundled pyright core (v1.1.411) already assigns the members the best `sortText`
  (`08.9999.<name>`, `SortCategory.EnumMember`), so they sort first.
- **basedpyright** (same pyright core, no Pylance proprietary layer) renders them at the
  top correctly.
- Only Pylance renders them last.

Reproduces for both a top-level `StrEnum` and a `StrEnum` nested inside other classes.

## How to verify

1. Open `scenarios/issue_8135.py`.
2. Put the cursor right after the dot on the `OrdStatus.` line and trigger completion
   (Ctrl/Cmd+Space).
3. Repeat for the `FIX.ExecType.Val.` line.

- **Expected:** `NEW`, `FILLED` (and `NEW`, `PARTIAL_FILL`, `FILL`) at the **top** of the
  completion list.
- **Actual (bug):** members appear at the **bottom**, below `capitalize` / `mro` /
  `__str__` / etc.

## Environment reported

- Pylance: 2026.3.1 (pyright 1.1.411, commit 9a9205fc)
- Python extension: 2026.4.0
- VS Code: 1.129.1
- OS: macOS (Darwin arm64 25.5.0)
- Python: 3.11+ (`StrEnum` requires 3.11)

No third-party dependencies — `enum.StrEnum` is stdlib (Python ≥ 3.11). Ensure the selected
interpreter is Python 3.11 or newer.

## Related

- #7376 — same alphabetical-ordering class of problem, fixed for the general case in
  2026.2.106; still reproduces for `StrEnum` members in 2026.3.1.
