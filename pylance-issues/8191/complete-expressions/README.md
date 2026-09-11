# Django reverse relations in nested applications

Public report and source of the model example:
https://github.com/microsoft/pylance-release/issues/8191

An existing public workspace for the original report is also available:
https://github.com/heejaechang/pylance-repro/tree/main/pylance-issues/8191

## Setup

Open this directory as the VS Code workspace. Install the Python and Pylance
extensions, create a Python environment, and install `requirements.txt`:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On Linux/macOS, use `.venv/bin/python` instead. Select that environment with
**Python: Select Interpreter**. The workspace settings enable experimental
Django support and basic type checking.
If VS Code exposes separate Python and Pylance interpreter selectors,
confirm that both select this same environment.

The recorded run used the Pylance 2026.3.103 candidate. As of September 11,
2026, the latest public release is 2026.3.102. No extension binaries are
included here.

## Reproduction steps

1. Reload the VS Code window after selecting the interpreter.
2. Open `sample/groups/models.py` and `sample/networks/models.py`.
3. Return to `sample/groups/models.py` and inspect `self.networks` in
   `get_networks`. It should not have an unknown-attribute error.
4. In `get_first_network`, place the caret immediately after `self.` and
   before the existing `networks` text. Invoke completion with Ctrl+Space.
   The list should include `networks`.
5. Open `use_models.py`. Place the caret after `network.` but before `group`.
   Completion should include `group`.
6. Repeat after `network_from_method.` and before `group`.
   Completion should again include `group`.

## Observed behavior

On September 11, 2026, the complete model source still produced:

```text
Cannot access attribute "networks" for class "Group*"
  Attribute "networks" is unknown
```

The diagnostic was `reportAttributeAccessIssue`, at `self.networks` in both
`get_networks` and `get_first_network`. It persisted after a language-server
restart and reopening both model files.

Completion after `self.` showed ordinary Django model members, but no
`networks`. Completion after `network.` and `network_from_method.` each
showed **No suggestions.**, rather than `group`, on the initial attempt and
retry.

The Python Language Server output reported generation of two stubs covering
four models and one relation. There were no syntax or unresolved-import
errors. Django imported successfully, and `python manage.py check` reported
no issues.

## Recorded environment

| Component | Version |
| --- | --- |
| Pylance candidate | 2026.3.103 |
| VS Code | 1.137.0 |
| Python extension | 2026.4.0 |
| Python | 3.14.4, x64 |
| Django | 5.1.15 |
| OS | Windows 11, build 26200 |

## Evidence and limitations

All model files are deliberately syntactically complete. Do not replace a
complete expression with a permanently unfinished `self.` line before opening
the project. Downstream examples live separately from the model declarations.

The model source comes from the public issue; the additional complete
expressions exercise the same reverse relation. These editor-only steps do
not require database migrations or executing `use_models.py`.
The observations above are from this complete-source workspace, not from an
unfinished completion example. They establish the editor behavior in the
listed environment, not a root cause or a result on other Python versions.
