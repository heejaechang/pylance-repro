# Issue #8288: Workspace symbol search (#) fails for closed files when using Pylance + Pyrefly (TSP launched with --indexing-mode none)

- Source: https://github.com/microsoft/pylance-release/issues/8288
- State: open
- Created: 2026-11-02T12:15:14+00:00
- Updated: 2026-11-02T12:15:14+00:00

## Reporter context

**Environment data**
- Pylance version: 2026.4.1
- Python extension version: 2026.10.0
- VS Code version: (please fill in)
- OS: Windows
- Python version: 3.15.2 (from .venv)
- Diagnostics source: Pylance + Pyrefly

**Behaviour**
When the diagnostics source is set to Pylance + Pyrefly, workspace symbol search (Quick Open with #) only finds symbols from currently open files. Symbols defined in closed files are not found, even though Pylance’s own indexing reports that it finished successfully. 

With the defining file open, searching # string_to_enum correctly returns the symbol.

With the file closed, the same search returns “No matching workspace symbols”.This works as expected when the diagnostics source is set back to plain Pylance.

**Steps to reproduce**

1. Configure Pylance to use Pylance + Pyrefly as the diagnostics source.
2. Ensure indexing is enabled (python.analysis.indexing: true, higher userFileIndexingLimit if needed).
3. Open a Python file that defines a top-level function/class (e.g. def string_to_enum(...)).
4. In Quick Open, type # string_to_enum → the symbol is found.
5. Close the file.
6. Repeat the same # string_to_enum search → “No matching workspace symbols”.

**Expected behaviour**
Workspace symbol search should find symbols from closed files in the workspace once indexing has completed, the same way it does with the default Pylance diagnostics source.

**Actual behaviour**
Symbols from closed files are invisible to workspace symbol search while Pyrefly is the diagnostics source.

Relevant log excerpts

```
Client: Pylance shadow experiment not started: primaryUsesPyrefly.
...
TS: Launched server 29340 using runtime ...\.venv\Scripts\pyrefly.exe with args: tsp --indexing-mode none
...
FG(...): Found 326 source files
...
IDX(...): Indexing(4) started
IDX(...): scanned(4) 1406 files over 1 exec env
IDX(...): indexed(4) 1406 files over 1 exec env
IDX(...): Indexing finished(4).

```
Note the --indexing-mode none argument passed to the Pyrefly TSP process. Pylance’s own indexer still reports that it finished, but the workspace-symbol results do not include closed files.

**Additional context**

- The problem is isolated to the Pylance + Pyrefly integration. Switching the diagnostics source back to plain Pylance restores normal closed-file workspace symbol search.
- Indexing settings (python.analysis.indexing, userFileIndexingLimit, clearing persisted indices, restarting the language server) were already tried and do not resolve the issue while Pyrefly is selected.

## Reproduction steps

Open `scenarios/issue_8288.py` in this workspace and follow the reporter steps quoted above.

## Evidence and limitations

This is extracted investigation material, not a verifier-confirmed reproduction. Only the first code block is extracted; other files, settings, dependencies and triggers may still be missing. Consult the reporter context before drawing conclusions.
