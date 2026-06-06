# Repro workspace — pylance-release issue #5125

**Issue:** Refactoring is not possible if marked block starts with a comment
https://github.com/microsoft/pylance-release/issues/5125

Pure Python, single-file contract. No third-party packages or environment-specific
setup are required — the bug is purely in Extract Method/Variable selection→node
resolution. Open `scenarios/issue_5125.py` in VS Code with Pylance active.

## Issue body (verbatim minimal example, andreas-wolf)

```Python
def test():
    a = 5
    b = 6
    # mark this and the next line, choose refactor -> nothing
    c = a * b
    return a + b, c
```

> If you want to refactor out the line `c = a * b` and also select the comment, you
> don't get the option to extract as method. I would expect to get a new method with
> the comment as first line.

Follow-up clarification (@zakv):

> I'll add that this issue occurs whenever the comment is the first *or last* line of
> the highlighted code.

## Expected vs. Actual (verbatim)

- **Expected:** "Marked code blocks can be refactored/extracted into a new method, even
  if the first selected line is a comment line."
- **Actual:** "The option to extract the method is missing"

## Verification checklist (every step, in order)

1. Open `scenarios/issue_5125.py`.
2. **Leading comment (issue body):** In `test()` / `leading_comment_case()`, select the
   marked comment line **and** the following `c = a * b` line, then invoke `Refactor...`.
   - Current bits: `Extract Method` **now appears** (leading-comment case fixed by pyrx #8418).
3. **Control:** In `control_case()`, select only the two plain statements (`c = a * b`
   plus context) and invoke `Refactor...`. `Extract Method` appears.
4. **Trailing comment (still broken — @zakv "first *or last* line"):** In
   `trailing_comment_case()`, select `c = a * b` **plus** the following trailing
   comment line as the **last** selected line, then invoke `Refactor...`.
   - Current bits: `Extract Method` is **missing** → reproduces the remaining bug.

## Status summary

- Leading-comment edge: FIXED (pyrx #8418, addresses duplicate #4586).
- Trailing-comment-on-its-own-line edge: STILL REPRODUCES on current bits.
