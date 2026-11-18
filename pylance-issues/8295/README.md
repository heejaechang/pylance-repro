# Pylance + Pyrefly semantic-token failures in PEP 723 scripts

Original issue: https://github.com/microsoft/pylance-release/issues/8295

Reporter-mentioned related issue:
https://github.com/microsoft/pylance-release/issues/8293.
The reporter has not confirmed a common cause.

Labels observed during investigation: `bug`, `tsp-pyrefly`, and
`fixed in next version (main)`.

## Reported behavior

The reporter uses browser-based VS Code in Ona on Ubuntu 24.04.5, Pylance
2026.4.1, Pyrefly 1.4.1, CPython 3.11.18, a uv-managed interpreter, a PEP 723
script, and an editable local package.

With `python.analysis.diagnosticsSource` set to `Pylance + Pyrefly`, imported
symbols lose semantic coloring. Pylance logs show failed
`textDocument/semanticTokens/full` requests with `-32603` and exceptions reading
undefined `typeParams` or `parameters`. Selecting `Pylance` with the same
interpreter restores coloring. Ordinary project files retain coloring with
Pyrefly.

The issue contains no affected source, package layout, full trace, screenshot,
or attachment. This workspace is therefore a concrete partial reproduction,
not a transcription of reporter code.

## Workspace contents

- `scenarios/issue_8295.py` is the PEP 723 script under test.
- `scenarios/regular_project_control.py` repeats the same imports and expressions
  without PEP 723 metadata.
- `editable-package/` is installed editable into the selected environment.
- `editable-package/src/issue8295_editable/types.py` contains synthetic
  imported-symbol probes: aliased overloads, a generic
  function/class, an enum member, and a `TypedDict.get` value.
- `requirements.txt` pins Pyrefly 1.4.1 and declares the editable package.
- `fixlist-manifest.json` records the reusable environment and visual checks.
- `verification-plan.md` records the pending real-editor and log checks.
- `procedures/pep723.json` and `procedures/ordinary-control.json` declare
  editor-originated open/navigation steps; neither invokes a provider directly.

These probes are not the reporter's code or a proven reduction of the failure.
They retain useful imported function/class shapes without any product source.
In particular, `dependencies = []` in the script and the separately installed
editable dependency are fixture choices, not recovered reporter metadata.
This workspace does not reconstruct a uv per-script cache environment or prove
that inline metadata causes the issue.

## Reproduction steps

1. Reuse an existing compatible `.venv` when available. For a fresh public
   checkout only, prepare it with CPython 3.11 and install `requirements.txt`
   from this workspace root using uv or the issue-workspace setup flow.
   Record the actual version if exact CPython 3.11.18 is unavailable.
2. Verify both commands with the selected environment:
   - `<venv-python> -c "import issue8295_editable; print(issue8295_editable.__file__)"`
   - `<venv-pyrefly> --version` must report Pyrefly 1.4.1.
3. Open this directory in a fresh VS Code session at a workbench size of at
   least 1920x1080. Select the exact `.venv` interpreter and verify the status
   bar selection.
4. Set `python.analysis.pyreflyVersion` to the absolute path of the verified
   `.venv` Pyrefly executable. Then set
   `python.analysis.diagnosticsSource` to `Pylance + Pyrefly` and reload.
5. Establish that Pyrefly started and served the workspace through the Type
   Server Protocol. The setting alone is not readiness evidence.
6. Open `scenarios/issue_8295.py`. Trigger normal editor semantic-token
   requests and inspect the imported names `Box`, `Domain`, `convert`,
   `identity`, and `metadata_get`. `procedures/pep723.json` supplies the
   open/navigation steps after setup and reload.
7. Confirm that `textDocument/semanticTokens/full` completes and semantic
   coloring remains visible. Capture any `-32603` error or stack mentioning
   `typeParams`, `parameters`, `getName`, or `findIndex`.
8. Open `scenarios/regular_project_control.py`, using
   `procedures/ordinary-control.json`, and repeat the same checks as the
   reporter's ordinary-project-file control.
9. Change only `python.analysis.diagnosticsSource` to `Pylance`, reload, keep
   the same interpreter, and repeat the PEP 723 script check as the reporter's
   same-interpreter control.

## Evidence and limitations

- Existing Windows desktop observations from 2026-11-17 used Pylance
  2026.4.101, CPython 3.11.15 and Pyrefly 1.4.1 at 1920x1080.
  `scenarios/issue_8295.py` and `scenarios/regular_project_control.py` both
  received successful semantic-token full responses with Pyrefly, and the
  same-interpreter Pylance script control also succeeded. Saved screenshots
  show retained imported-name coloring.
- A separate editor hover on `convert` failed with undefined `parameters`
  under Pyrefly in both files, while the Pylance hover succeeded. This is not
  the reported semantic-token crash, and it does not establish a shared root
  cause or a PEP-723-specific trigger.
- Current issue-level verdict: **unknown**. These are historical partial
  observations; the caller owns the next real-editor check. No local fix was
  applied or accepted.
- The exact PEP 723 metadata, package contents, uv command, interpreter path,
  Ona/VS Code version, and full failing trace are unavailable. The metadata and
  local package here preserve the reported topology but cannot prove equivalence
  to the missing source.
- The host is not Ona on Ubuntu. A Windows desktop run is useful supporting
  evidence but cannot establish browser-host or Linux fidelity.
- `.vscode/settings.json` seeds a safe Pylance starting state and compact
  tracing for verification, not the reporter's complete settings. Interpreter
  selection and the verified absolute Pyrefly executable path must be applied
  by the runner in its own host namespace before enabling Pyrefly. No theme,
  semantic-highlighting override, search path, or unknown reporter setting is
  invented here.
- Do not infer semantic coloring from an LSP success alone. Retain both the
  semantic-token request result and rendered editor evidence.
- A pass on this workspace does not justify closing the issue. It shows only
  that the current build handles this issue-grounded partial topology.
- A remaining crash is actionable. Preserve the complete request stack and, if
  possible, the Type Server Protocol payload or reconstructed type immediately
  before the failing consumer.

## Public export boundary

Export the fixture source, requirements, portable settings, manifest,
procedures, README and verification plan only. Do not copy `.venv`,
`__pycache__`, `*.egg-info`, machine-local setup metadata, native logs, or
editor receipts into the public repro. `.gitignore` excludes runtime files,
but a non-git exporter must honor these exclusions explicitly. Keep local
evidence outside this workspace.

