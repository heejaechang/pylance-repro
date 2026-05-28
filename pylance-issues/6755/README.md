# Issue #6755 — Jupyter Notebook import resolution breaks in multiroot workspace

## Issue

https://github.com/microsoft/pylance-release/issues/6755

## Summary

When a `.code-workspace` file includes both a subfolder (`dir1`) and the workspace
root itself (`.`) as workspace folders, import resolution for a notebook inside
`dir1/.jupyter/testing.ipynb` breaks — Pylance reports missing-import warnings
for `database.settings` and `database` even though the `database/` package is a
sibling of the notebook inside `dir1`.

Opening only `dir1` as a single folder works fine.

## Repro steps (real VS Code required)

1. Open `testing.code-workspace` in VS Code (multiroot workspace).
2. Open `dir1/.jupyter/testing.ipynb`.
3. Select the `.venv` kernel from `dir1/.venv/`.
4. Observe that `from database.settings import DATABASE_URL` and
   `from database import connect` have missing-import warnings.
5. Close the workspace. Open only `dir1/` as a single folder.
6. Reopen the same notebook — warnings disappear.

## Expected result

Imports from `database` should resolve in both single-folder and multiroot mode.

## Workspace layout

```
testing.code-workspace   ← defines two roots: "dir1" and "." (root)
dir1/
  .jupyter/
    testing.ipynb        ← notebook under test
  .venv/                 ← local venv with ipykernel
  database/
    __init__.py          ← defines connect()
    settings.py          ← defines DATABASE_URL
  pyproject.toml
```

## Last known repro status

**Reproduced** on Pylance 2026.2.100 prerelease (staff confirmation 2026-04-23).

## Notes

- This requires a real VS Code rerun (notebook + multiroot); Jest alone is not faithful.
- The overlapping roots (`dir1` inside `.`) confuse import-path resolution.
- Cloned from https://github.com/Real-Gecko/vscode-jupyter-bug
