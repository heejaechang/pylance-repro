# Issue 6029

This workspace reproduces the stale Django-stubs problem for `RemovedInDjango51Warning`.

## Python version

The original report reproduced this on Python `3.12.2`, and the original repro steps explicitly used a Python `3.12` virtual environment.

## Setup

1. Create a Python `3.12` virtual environment in this folder.
2. Install the packages from `requirements.txt` into that environment.
3. Open this folder in VS Code and select the local `.venv` interpreter.
4. Open `manage.py`.

The workspace already sets `python.analysis.typeCheckingMode` to `standard`.

## Expected result

Pylance reports `RemovedInDjango51Warning` as an unknown import symbol on the import line even though the Django runtime exports it.
