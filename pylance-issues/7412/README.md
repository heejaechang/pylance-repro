# Issue 7412

This workspace reproduces the current gap tracked in `microsoft/pylance-release#7412`: Find All References on a source symbol also includes the generated strict-editable shadow file under `build/__editable__...`.

## Setup

1. Open this folder in VS Code with Pylance enabled.
2. Open `pegen/parser.py`.
3. Run Find All References on `logger`.

## Expected

Results should stay on the source-side files and exclude the generated strict-editable shadow file.

## Actual

On current bits, Find All References still includes `build/__editable__.pegen-0.3.1.dev6+qcf8e62d-py3-none-any/pegen/grammar_parser.py`.