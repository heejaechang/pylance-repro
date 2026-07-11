# Issue 5031

This workspace reproduces the case where Pylance bundled Django stubs still shadow the installed `django-stubs==4.2.6` package.

## Python version

This repro was revalidated on Python `3.12.13` with a local `.venv` interpreter in this folder.

## Setup

1. Create a Python `3.12` virtual environment in this folder.
2. Install the packages from `requirements.txt` into that environment.
3. Open this folder in VS Code and select the local `.venv` interpreter.
4. Open `scenarios/issue_5031.py` and wait for diagnostics to settle.

The workspace already sets `python.analysis.typeCheckingMode` to `basic` and `python.analysis.diagnosticMode` to `workspace`.

## Expected result

Pylance reports that `int | None` cannot be assigned to `int` for `accepts_only_int(m.nullable)`, which indicates the bundled Django stub surface is still winning over the installed `django-stubs` package for this scenario.
