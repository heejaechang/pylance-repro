# Issue 3970

This retained repro captures the strongest current screenshot-consistent hypothesis for `microsoft/pylance-release#3970`.

## Important caveat

The original issue body currently contains only a screenshot and no code snippet, settings, or follow-up comments. This folder is therefore not presented as the exact original reporter source. It preserves the closest deterministic shape the sweep could validate on current bits.

## Why this shape

The sweep's deterministic repro isolated a meaningful split:

- a module-level `@app.route` handler is not reported unused
- a nested `@app.route` handler inside an app-factory-style function is reported unused

This folder preserves that exact shape in a reusable workspace.

## Repro

1. Open `app.py` in VS Code with Pylance enabled.
2. Let analysis settle.
3. Compare the diagnostics on `top_level_route` and `nested_route`.

## Expected current hypothesis

- `top_level_route` is not marked unused.
- `nested_route` is marked unused or unaccessed.

## Notes

- The local `flask/__init__.pyi` stub is intentional. It keeps the repro focused on unused-symbol behavior instead of requiring a real Flask install.
- If future issue evidence reveals the original source shape or settings, prefer that stronger grounding over this hypothesis workspace.
