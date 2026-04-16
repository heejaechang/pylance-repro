# Issue 6295

## Contract

- SCENARIO: Pylance's bundled `get_pytest_options.py` helper should fail gracefully when `pytest` is missing
- TARGET: the bundled helper script referenced below, run with the selected local interpreter
- TRIGGER: run the helper with an interpreter that does not have `pytest` installed
- EXPECT: the failure is handled cleanly without an unhandled Python exception report from the host
- VERIFY: if the host reports an unhandled exception for `get_pytest_options.py`, the bug still reproduces
- RECOVER: install `pytest` or recreate the venv before rerunning

This workspace reproduces the `get_pytest_options.py` crash path when the selected interpreter does not have `pytest` installed.

## Python version

The original report reproduced this on Python `3.12.4`. No stricter Python-version requirement has been established for this workspace; the important condition is that the selected interpreter does not have `pytest` installed.

## Setup

1. Create a fresh virtual environment in this folder.
2. Select that local `.venv` interpreter.
3. Do not install `pytest` into the environment.
4. Run the bundled Pylance helper script with that interpreter:

```powershell
.\.venv\Scripts\python.exe <path-to-ms-python.vscode-pylance>\dist\bundled\files\get_pytest_options.py
```

## Expected result

The script raises `ModuleNotFoundError: No module named '_pytest'` and exits with code `1`.
