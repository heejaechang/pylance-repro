# Issue 7295

Use this folder to check the external-edit recovery scenario in `fileWatcher.py`.

Issue `7295` reproduces when diagnostics and symbol resolution recover after the external edit, but semantic highlighting still lags.

## Steps

1. Open `fileWatcher.py`.
2. From outside VS Code, uncomment the helper definition in `lib/changeExternally.py`.
3. Watch the importer file refresh after the external edit.

## Expected Result

- Diagnostics and symbol resolution recover after the external edit.
- Semantic highlighting should recover at the same time.
- If the import-site token remains stale immediately after the edit even though diagnostics/symbol resolution have already refreshed, the issue still reproduces.
