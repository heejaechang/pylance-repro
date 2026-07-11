# Issue 7443

This retained repro captures the current `microsoft/pylance-release#7443` gap where Pylance does not use the nested Python Environments project interpreter in a single-root workspace, even though running the nested file uses that interpreter.

## Why this workspace matters

The discriminating detail is the difference between these two project-marking mechanisms:

- `python-envs-scenario` uses the Python Environments project marker shape from the issue.
- `nearest-config-control` uses Pylance's nested `pyrightconfig.json` / nearest-configuration path as a control.

The sweep's faithful current-prerelease rerun found that the Python Environments shape still reports `nested_only_pkg` as unresolved in `nested/main.py`, while the nearest-config control resolves the same package cleanly.

## Setup

Use the same package setup for both `python-envs-scenario` and `nearest-config-control`.

1. Open one scenario folder in VS Code.
2. Create a root environment named `.venv-root` in the scenario folder.
3. Create a nested environment named `.venv` under the scenario's `nested` folder.
4. From the `nested` folder, install the local package into `nested/.venv`:
   - Windows: `.venv\Scripts\python -m pip install -r requirements.txt`
   - macOS/Linux: `.venv/bin/python -m pip install -r requirements.txt`
5. Select the root `.venv-root` interpreter for the opened workspace folder.
6. Open `nested/main.py`.

## Expected current behavior

In `python-envs-scenario`:

- Running `nested/main.py` should use the nested environment and print `nested environment`.
- Pylance currently reports `Import "nested_only_pkg" could not be resolved` in `nested/main.py`.

In `nearest-config-control`:

- Pylance should resolve the same `nested_only_pkg` import cleanly.

## Notes

- This retained repro intentionally excludes the original machine-local `.venv*` directories. Recreate them locally using the setup steps above.
- The failing scenario requires the Python Environments extension/project support to be enabled.
- The control is included to show that nested interpreter routing can work when the nested project is represented through Pylance's nearest-configuration path.