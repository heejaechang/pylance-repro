# Issue #4036 — Code folding on `with` blocks breaks on multi-line `with` statement

**Issue URL**: https://github.com/microsoft/pylance-release/issues/4036  
**Reporter**: jphalliwell  
**Labels**: bug, P2  
**Created**: 2023-03-01  

## Expected Behavior

When a `with` statement spans multiple lines (e.g., after Black formatting), the entire `with` block (including its body) should be foldable as a single unit, similar to how multiline `for` statements work.

## Actual Behavior

Only the multi-line `with` statement itself gets a fold arrow (for the `open(...)` call). The `with` suite/body does NOT get a separate fold arrow on the line containing the colon (`:`), because VS Code drops the second folding range when its start line equals the end line of the first range.

Pylance emits two overlapping ranges:
1. For the `open(...)` call: from end of line 1 to beginning of line 3 (the `(...)` span)
2. For the `with` suite: from end of line 3 (`:`) to end of line 4

Since both ranges share line 3 as a boundary, VS Code drops the second one.

## Maintainer Notes (debonte)

> "Since a `>` folding control isn't displayed on line 3, I believe that VS Code is dropping the second one. Probably because the two ranges are overlapping in an unsupported way."

## Verification Checklist

1. Open this workspace folder in VS Code with Pylance enabled
2. Open `scenarios/multiline_with.py`
3. Verify that on line 1 (`with open(...)`), a fold arrow appears
4. Click the fold arrow on line 1 — observe that it only folds the multi-line call expression, NOT the body
5. Verify that NO fold arrow appears on line 3 (the `) as ...:` line) for the with-suite body
6. Compare with `scenarios/multiline_for.py` — verify that the `for` loop body IS foldable (fold arrow on the last line of the `for` statement)
7. Compare with `scenarios/single_line_with.py` — verify that a single-line `with` statement correctly folds its entire body

### Bug confirmed if:
- Step 5 shows no fold arrow for the with-suite body (the body cannot be folded independently)
- Step 6 shows that multiline `for` does NOT have this problem

### Bug fixed if:
- A fold arrow appears on line 3 (or an equivalent mechanism) that allows folding the with-suite body
- OR Pylance shapes its ranges to avoid the VS Code limitation (e.g., by adjusting the call-expression range to not share a boundary line with the suite range)
