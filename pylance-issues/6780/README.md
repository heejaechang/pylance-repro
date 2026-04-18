# Issue 6780

This workspace reproduces the case where bundled `sklearn` stubs shadow the installed `scikit-learn==1.6.0` export of `Tags`.

## Python version

This repro was revalidated on Python `3.13.12` with a local `.venv` interpreter in this folder.

## Setup

1. Create a Python `3.13` virtual environment in this folder.
2. Install the packages from `requirements.txt` into that environment.
3. Open this folder in VS Code and select the local `.venv` interpreter.
4. Open `scenarios/issue_6780.py` and wait for diagnostics to settle.

The workspace already sets `python.analysis.typeCheckingMode` to `basic` and `python.analysis.diagnosticMode` to `workspace`.

## Expected result

Pylance reports `"Tags" is unknown import symbol` on `from sklearn.utils import Tags` instead of resolving `Tags` from the installed `scikit-learn` package.