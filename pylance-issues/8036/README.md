# Issue 8036 - Incorrect preview of imported constant values

Issue: https://github.com/microsoft/pylance-release/issues/8036

## Files (verbatim from issue body)

`foo.py`:
```python
# <some comment>
MY_CONSTANT: None = print()
```

`bar.py`:
```python
from foo import MY_CONSTANT

del MY_CONSTANT  # silence unused import
```

## Exact repro steps from the issue (do NOT alter)

1. Open `bar.py`.
2. Hover over `MY_CONSTANT` on line 1 (the import). Record the full hover popup text.
3. Open `foo.py` and change the length of `# <some comment>` to `# 1` (save).
4. Switch to `bar.py` and re-hover `MY_CONSTANT`. Record the popup text.
5. Repeat step 3 with `# 12`, then `# 1234567`. Re-hover after each save.

## Expected

Hover always shows `(constant) MY_CONSTANT: None = print()` (the literal value expression from `foo.py`).

## Reported actual

Hover shows arbitrary garbage substrings whose contents shift with the
length of preceding text in `foo.py` (e.g. `= NT`, `= T`, `= del MY_`,
`= ort Any`). The garbled text is read from stale buffer offsets after
`foo.py` is edited.

## Verifier instructions

- Use Pylance **prerelease** (channel = prerelease).
- For every hover, capture the full popup text (a screenshot of the
  tooltip is required) — do NOT only report the type line.
- Outcome = `reproduced` if ANY of the four hovers shows a value
  expression that is not exactly `print()` (i.e. any garbled substring).
- Outcome = `not_reproduced` only if ALL four hovers show
  `(constant) MY_CONSTANT: None = print()` (or the value preview is
  legitimately absent in a consistent way that matches the type line).
