# Issue 6751

This retained repro captures the multi-root hidden-directory interpreter mismatch from `microsoft/pylance-release#6751`.

## Why this workspace matters

The discriminating detail is not the file contents alone. All four Python files are intentionally the same. The bug shows up only when:

- the folder is opened as a multi-root workspace
- `ws1` and `ws2` use different interpreters
- the compared file is inside a hidden directory such as `.hidden_folder`

In the original thread, the reporter also confirmed that running or debugging the hidden file uses the correct environment. The bug is in analysis/workspace binding rather than in terminal/debug execution.

## Setup

1. Open `issue6751.code-workspace` in VS Code.
2. Create a local virtual environment in each root:
   - `ws1/.venv`
   - `ws2/.venv`
3. Install the packages from each root's `requirements.txt` into that root's `.venv`.
4. Select the `ws1/.venv` interpreter for workspace folder `ws1` and the `ws2/.venv` interpreter for workspace folder `ws2`.
5. Open all four files:
   - `ws1/ws1.py`
   - `ws1/.hidden_folder/ws1_hidden.py`
   - `ws2/ws2.py`
   - `ws2/.hidden_folder/ws2_hidden.py`

## Expected repro

- `ws1.py` and `ws1_hidden.py` should behave like `ws1` and resolve `jwt` but not `pydantic`.
- `ws2.py` should behave like `ws2` and resolve `pydantic` but not `jwt`.
- `ws2_hidden.py` incorrectly behaves like `ws1`, resolving against the wrong interpreter.

## Notes

- This retained repro is based on a faithful current-bits rerun from the sweep, not just on the issue text.
- The rerun matched the maintainer root-cause note that hidden dotted-path files fall back to the default workspace instead of binding to their containing workspace folder.
- The portable repro intentionally excludes the original machine-local `.venv` directories; recreate them locally using the included requirements files.
