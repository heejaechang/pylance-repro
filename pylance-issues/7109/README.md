# Issue #7109 — Pylance does not set cwd to workspace root when discovering sys.path

**Source**: https://github.com/microsoft/pylance-release/issues/7109

## What This Tests

Pylance runs Python to discover `sys.path`. The user reports that the cwd during this execution
is the extension directory (`~/.vscode/extensions/.../dist`) rather than the workspace root.
This breaks setups that rely on `sitecustomize.py` hooks that modify `sys.path` based on cwd.

## Workspace Structure

- `sitecustomize.py` — adds `./lib` to `sys.path` if `os.getcwd()/lib` is a directory
- `lib/mylib/__init__.py` — a library that should be importable
- `main.py` — imports from `mylib`

**Note**: `sitecustomize.py` is placed in the workspace root for demonstration purposes.
In the user's real scenario, it lives in the site-packages directory and uses cwd to
determine which project's `lib/` to add. The mechanism is identical: `sitecustomize.py`
relies on `os.getcwd()` being the workspace root.

## Verification Steps (from issue body)

1. Open this workspace folder in VS Code with Pylance.
2. Open `main.py`.
3. **Expected**: No import errors for `from mylib import greet, MY_CONSTANT` — because
   `sitecustomize.py` should add `./lib` to `sys.path` when cwd is the workspace root.
4. **Actual (reported)**: Pylance shows `reportMissingImports` because when it runs Python
   to discover sys.path, the cwd is NOT the workspace root, so `sitecustomize.py` does
   not find `./lib`.

## Root Cause (from code analysis)

In `packages/pyright/packages/pyright-internal/src/common/fullAccessHost.ts`:
- `_executeCodeInInterpreter()` (line 314) calls `child_process.execFileSync()` **without**
  a `cwd` option, so it inherits the Node.js process's cwd.
- For `extractSys` (sys.path discovery), the `-I` flag is NOT passed, so `sitecustomize.py`
  DOES run — but with the wrong cwd.

## Workaround

Add `./lib` to `python.analysis.extraPaths` in `.vscode/settings.json`:
```json
{
    "python.analysis.extraPaths": ["./lib"]
}
```
