# Go to Definition in a JavaScript cell magic

Issue: https://github.com/microsoft/pylance-release/issues/8198

Related feature: https://github.com/microsoft/pylance-release/issues/4969

This workspace isolates navigation from a JavaScript function call to a
function defined in the same Python notebook cell.

## Setup

Install the VS Code Python, Pylance, and Jupyter extensions. Keep the built-in
TypeScript and JavaScript Language Features extension enabled.

Use a Pylance build that supports `python.analysis.cellMagicLanguages`.
The scenario is intended for Pylance 2026.3.103. As of September 11, 2026,
the latest public release is 2026.3.102 and the cell-magic feature is
announced for a subsequent release. No extension binaries are included here.

Open this directory itself as the VS Code workspace, not the repository root.
Create a Python environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On Linux/macOS, use `.venv/bin/python` instead of
`.\.venv\Scripts\python.exe`. Select this environment with
**Python: Select Interpreter** and choose it as the notebook kernel.
If VS Code exposes separate Python and Pylance interpreter selectors,
confirm that both select this same environment.

The checked-in workspace setting maps `js` to `javascript`:

```json
{
    "python.analysis.cellMagicLanguages": {
        "js": "javascript"
    }
}
```

## Reproduction steps

1. Open `activate.py` once to activate the Python extensions.
2. Open `definition.ipynb` in the notebook editor.
3. Select the Python kernel. Do not execute the cell.
4. Place the caret on `greet` in `const greeting = greet("Ada");`.
5. Run **Go to Definition** from the context menu or press F12.
6. Inspect the active editor and caret location.

## Expected behavior

VS Code stays in the notebook editor and moves to
`function greet(name) {` in the same cell.

As a separate language-service control, hover over `toUpperCase` in
`word.toUpperCase()`. The tooltip should describe JavaScript's string method.

## Observed behavior

On September 11, 2026, Go to Definition opened a second
`definition.ipynb` preview editor with language mode **JSON**, no text, and
the caret at line 1, column 1. The editor offered **Open in Notebook Editor**.
Its URI used the `pylance-cell-magic:` scheme instead of returning to the
declaration in the visible notebook cell.

Reopening the actual notebook and repeating Go to Definition from the
function call produced the same result.

The independent hover worked:

```text
(method) String.toUpperCase(): string
Converts all the alphabetic characters in a string to uppercase.
```

## Recorded environment

| Component | Version |
| --- | --- |
| Pylance candidate | 2026.3.103 |
| VS Code | 1.137.0 |
| Python extension | 2026.4.0 |
| Jupyter extension | 2025.9.1 |
| Python | 3.14.4, x64 |
| ipykernel | 7.3.0 |
| jupyter_client | 8.10.0 |
| OS | Windows 11, build 26200 |

Python type checking was `off`. The Python extension, Pylance, and notebook
kernel used the same interpreter.

## Evidence and limitations

This is an editor-only scenario. It does not require a JavaScript runtime,
Node.js, notebook execution, a database, or external services. The notebook
contains no saved output.

The hover control distinguishes a missing destination-language provider
from a navigation failure. This example makes no assertion that ordinary
JavaScript reports undeclared-variable errors without opting into type checking.
The precise cause of the navigation failure has not been established.
