# Issue 6026 Verification Workspace

**Issue**: https://github.com/microsoft/pylance-release/issues/6026
**Title**: Find All References on list comprehension var in notebook cell includes results from outer name scope

## Workspace Contents

- `notebook.ipynb` — Two-cell notebook matching the issue body exactly:
  - Cell 0: `j = "str"` and `[j for j in range(1, 6)]`
  - Cell 1: `j = 3`

## Verification Checklist

Per issue body:

1. Open `notebook.ipynb` in VS Code
2. In cell 0 (first cell), place cursor on `j` within the list comprehension `[j for j in range(1, 6)]`
3. Right-click → "Find All References" (or Shift+F12)

### Expected behavior (from issue)

> Only the two references within the list comprehension are provided because the list comprehension is a separate name scope. This is the behavior you'll see if all three lines are in the same cell or are in a `.py` file.

Expected: 2 references — both `j` occurrences within `[j for j in range(1, 6)]`

### Actual behavior (from issue — bug)

> The use of the unrelated variable (also named `j`) in the second cell is also included

Actual: 3+ references including `j = 3` from cell 1

## Notes

- Jest in-process test does NOT reproduce this bug (returns only 2 references correctly)
- Issue was revalidated 2026-04-24 by @heejaechang in real VS Code — still reproduced
- Difference may be in how real VS Code handles notebook cell chaining vs. Jest in-process harness
- A real VS Code Playwright-based verification is needed to confirm current state
