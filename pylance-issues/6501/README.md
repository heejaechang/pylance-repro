# Issue 6501

This workspace reproduces the current gap tracked in `microsoft/pylance-release#6501`: call-argument-name inlay hints render, but interacting with them does not navigate to the corresponding parameter definition.

## Setup

1. Open this folder in VS Code with Pylance enabled.
2. Open `scenarios/issue_6501.py`.
3. Wait for call-argument-name inlay hints to render on the `method(...)` call.

The workspace already enables `python.analysis.inlayHints.callArgumentNames = "all"` in `.vscode/settings.json`.

## Expected

Clicking a rendered parameter-name inlay hint such as `alpha=` should navigate to the matching callee parameter definition, or an equivalent definition target.

## Actual

On current prerelease Pylance `2026.2.100`, clicking the rendered `alpha=` hint left the caret on the call line instead of navigating.
