# Issue #7928 — Pylance doesn't auto-update settings on `pyproject.toml` change

**Issue**: https://github.com/microsoft/pylance-release/issues/7928

## Problem

When `pyproject.toml` with `[tool.pyright]` is used for Pylance config, editing and saving the file does not trigger a settings update. Pylance logs say "Settings have not changed. Skipping update."

## Verification Steps (from issue body)

1. Open this workspace in VS Code with Pylance installed
2. Set log level to Trace (already configured in `.vscode/settings.json`)
3. Observe Pylance output: note the current settings are loaded
4. Edit `pyproject.toml` — change the `exclude` list, e.g.:
   ```toml
   [tool.pyright]
   exclude = ["some_folder"]
   ```
5. Save `pyproject.toml`

### Expected (quoted from issue)

Pylance should detect the change and update its settings automatically (same as when `settings.json` is modified).

### Actual (quoted from issue)

> "Settings have not changed. Skipping update."

The user must either restart Pylance or make a dummy change to `settings.json` to force a settings reload.

## Root Cause

In `packages/pylance-internal/src/server/asyncServer.ts`:

1. The `configOptionsChanged` handler (line ~548) only sends a notification to the client — it does NOT call `_updateSettingsForWorkspace()`
2. `calculateSettingsHash()` only hashes VS Code settings (the `serverSettings` object), so even if `_updateSettingsForWorkspace()` were called, the hash would be unchanged because config file content isn't part of the hash

## Fix Direction

In the `configOptionsChanged` handler:
- Reset `workspace.settingsHash` to `undefined` (to bypass the hash check)
- Call `_updateSettingsForWorkspace()` to trigger a full settings reload

## Files Added

- `pyproject.toml` — Pyright config file (the file the user edits)
- `main.py` — Minimal Python file so Pylance has something to analyze
- `.vscode/settings.json` — Enables Trace logging to observe the "Settings have not changed" message
