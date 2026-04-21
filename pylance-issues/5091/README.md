# Issue 5091

This retained repro captures the Python block-comment indentation behavior from `microsoft/pylance-release#5091`.

## Repro

1. Open `main.py` in VS Code.
2. Select these two indented lines inside the `for` block:
   - `print(i / 10)`
   - `x.append(i)`
3. Run block comment (`Shift+Alt+A`).

## Expected

Block comments should preserve indentation-sensitive Python structure.

## Actual

The inserted triple-quote block can be placed in a way that breaks the surrounding indentation structure.

## Note

For current sweep purposes, this still looks more like a VS Code/editor block-comment issue than a Pylance-specific issue.