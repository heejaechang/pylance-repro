# Issue #7204 - Pylance sometimes looks into excluded folders like "~/.pyenv"

**Issue URL**: https://github.com/microsoft/pylance-release/issues/7204

## Problem Description

User reports that Pylance intermittently reports diagnostics (reportAssignmentType,
reportMissingImports, reportAttributeAccessIssue) on stdlib files inside `~/.pyenv`,
despite having exclude patterns set. The user suspects GitHub Copilot agentic mode
triggers this by opening stdlib files.

## Root Cause (from code investigation)

When a file is opened by the client (via `textDocument/didOpen`) and it's NOT already
in Pyright's program, `setFileOpened` in `program.ts` creates a new `SourceFileInfo`
with `isThirdPartyImport: false` hardcoded. Combined with `_shouldCheckFile` returning
true unconditionally for `isOpenByClient` files, this causes full type-checking
diagnostics to be reported on library/stdlib files.

The exclude patterns are irrelevant because they only control `isTracked` (whether a
file is part of the workspace analysis set). The `_shouldCheckFile` function bypasses
the `isTracked` check for any file opened by the client.

## Verification Steps

### Prerequisites
- VS Code with Pylance extension
- Python installed via pyenv (or any interpreter outside the workspace)
- GitHub Copilot with agentic mode (to trigger the behavior)

### Reproduction Steps (from issue body)

1. Open this workspace in VS Code
2. Ensure `python.analysis.exclude` includes `**/.pyenv` and `~/.pyenv` (already in settings.json)
3. Trigger Copilot agentic mode to navigate into a stdlib `.py` file (e.g., `functools.py`)
   - Alternatively, manually open a stdlib `.py` file from the pyenv installation:
     e.g., `~/.pyenv/versions/3.12.7/lib/python3.12/functools.py`
4. Check the Problems panel for diagnostics on the stdlib file

### Expected Behavior (from issue)

> No diagnostics should be reported on files in excluded directories like `~/.pyenv`

### Actual Behavior (from issue)

> Pylance reports diagnostics like `reportAssignmentType`, `reportMissingImports`,
> `reportAttributeAccessIssue` on stdlib files in `~/.pyenv`

### Verification Checklist

- [ ] Open workspace in VS Code with Pylance
- [ ] Confirm no diagnostics on stdlib files initially
- [ ] Open a stdlib `.py` file from pyenv installation (simulating Copilot agentic mode)
- [ ] Check if diagnostics appear on the opened stdlib file
- [ ] Verify the diagnostics include types reported by user: reportAssignmentType, reportMissingImports, reportAttributeAccessIssue

## Files

- `main.py` - Simple Python file that imports functools (ensures stdlib is resolved)
- `.vscode/settings.json` - Contains the user's exclude patterns

## Notes

- The issue is intermittent because it depends on whether the stdlib `.py` file is
  already in the program (from import resolution) when Copilot opens it.
- If the file IS already in the program (as a third-party import), opening it just
  sets `isOpenByClient=true` and the existing `isThirdPartyImport=true` protects it.
- If the file is NOT in the program (different URI from typeshed stub, or program not
  fully initialized), it enters as a new file with `isThirdPartyImport=false` → full diagnostics.
- The actual stdlib `.py` files (not stubs) contain patterns that trigger Pyright diagnostics
  (e.g., imports from C extension modules like `_functools` that Pyright can't resolve).
