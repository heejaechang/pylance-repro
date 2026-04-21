# Issue 5125

This workspace reproduces the missing `Extract Method` refactoring when the selected block starts or ends with a comment line.

## Setup

No third-party packages are required for this repro.

1. Open this folder in VS Code with Pylance active.
2. Open `scenarios/issue_5125.py`.

## Repro steps

1. In `leading_comment_case`, select the marked comment line and the next line `c = a * b`.
2. Invoke `Refactor...` from the context menu or Command Palette.
3. Observe that `Extract Method` is missing.
4. In `control_case`, select the two plain statements `c = a * b` and `d = a + b`.
5. Invoke `Refactor...` again and observe that `Extract Method` is available.
6. In `trailing_comment_case`, select `c = a * b` and the marked trailing comment line.
7. Invoke `Refactor...` and observe that `Extract Method` is missing there as well.

## Expected result

The still-repro behavior is that comment-edge selections do not surface `Extract Method`, even though the equivalent no-comment control selection does.

The issue thread also includes a maintainer repro confirmation, and the current sweep kept this workspace focused on the minimal pure-Python one-file contract.