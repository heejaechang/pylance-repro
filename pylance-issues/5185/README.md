# Issue 5185 repro workspace

This workspace preserves the current still-repro contract for `microsoft/pylance-release#5185`.

## Setup

The workspace enables:

```json
"python.analysis.autoFormatStrings": true
```

## Manual validation

1. Open `scenarios/issue_5185.py`.
2. Place the cursor immediately after `\N` in `emoji = "\NBLACK CAT}"`.
3. Type `{`.

Expected behavior: the text becomes a normal unicode-name escape string, `"\N{BLACK CAT}"`.

Still-repro behavior: Pylance inserts an `f` prefix and rewrites the literal as an f-string.

This was revalidated publicly on current prerelease Pylance `2026.2.100` in https://github.com/microsoft/pylance-release/issues/5185#issuecomment-4306482908.