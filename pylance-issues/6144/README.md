# Issue 6144

Use this folder to check the comment-sensitive Extract Method scenario in `main.py`.

Issue `6144` reproduces when Refactor -> Extract Method disappears for a selection that starts with a comment even though the non-comment control selection still offers it.

## Steps

1. Open `main.py`.
2. Select the comment plus the following assignment line.
3. Trigger Refactor / Quick Fix for the selection.
4. Compare that result with a control selection on only the assignment line.

## Expected Result

- The comment-inclusive selection should still offer `Extract method`.
- If the comment-inclusive selection omits `Extract method` while the control selection offers it, the issue still reproduces.
