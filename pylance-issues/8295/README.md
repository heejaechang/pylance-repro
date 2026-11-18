# Pylance + Pyrefly: semantic-token failures in PEP 723 scripts

Original issue: https://github.com/microsoft/pylance-release/issues/8295

Related issue: https://github.com/microsoft/pylance-release/issues/8293
(a common cause has not been established).
Linked implementation work:
https://github.com/microsoft/pyrx/pull/10069 and
https://github.com/microsoft/pyrx/pull/10077.
These references and the fix label do not verify the reporter's scenario.

Labels in the saved November 18 issue: `bug`, `tsp-pyrefly`,
`fixed in next version (main)`, `repro workspace`.

## Reporter context

The reporter uses browser-based VS Code in Ona on Ubuntu 24.04.5, Pylance
2026.4.1, Pyrefly 1.4.1, CPython 3.11.18, uv-managed PEP 723 scripts, and an
editable local package. Imported symbols lose semantic coloring with
`python.analysis.diagnosticsSource = "Pylance + Pyrefly"`. Basic syntax colors
remain. The abbreviated logs show `textDocument/semanticTokens/full` errors
with code `-32603`, reading undefined `typeParams` or `parameters`. Switching
to `Pylance` and reloading with the same interpreter restores coloring.
Ordinary project files retain coloring. Disabling uv-auto-venv and manually
selecting the interpreter did not resolve the problem.

No original source, exact inline metadata, editable-package contents, uv
commands, complete settings, VS Code/Ona version, or full failing trace were
supplied. This is a **concrete partial investigation fixture**, not reporter
code, a proven reduction, or a faithful reproduction of the full scenario.

## Files and dependency contract

- `scenarios/issue_8295.py`: synthetic PEP 723 script with imported functions,
  a generic class, enum, and bound `TypedDict.get`.
- `scenarios/regular_project_control.py`: same executable imports and expressions
  without inline metadata.
- `editable-package/`: synthetic local dependency; aliased overloads and generic
  shapes are investigation probes, not recovered reporter types.
- `requirements.txt`: editable package and reporter-mentioned Pyrefly 1.4.1.
- `.vscode/settings.json`: safe initial Pylance source and compact tracing.
- `fixlist-manifest.json`, `verification-plan.md`, and `procedures/`: explicit
  caller-owned checks and editor open/navigation inputs, not run results.

The intended reusable environment is `.venv`; dependency source is
`requirements.txt`. Verify its interpreter and dependencies before reuse.

## Reproduction steps

1. Prepare or reuse an issue-local CPython 3.11 environment for this partial
   fixture. Prefer reporter version 3.11.18 if available. Install
   `requirements.txt` from this workspace root using the approved package feed
   in the actual extension host. Record commands, versions, interpreter and
   Pyrefly executable. This is fixture setup, not the unknown reporter uv flow.
2. With the exact interpreter, verify `import issue8295_editable` resolves to
   `editable-package/src/`, its installation is editable, and the selected
   Pyrefly executable reports version 1.4.1.
3. Open this workspace in the caller's VS Code session, with compact server
   tracing and native trace logging. Verify actual workbench dimensions of at
   least 1920x1080 and record the loaded Pylance build. Select and verify the
   exact interpreter in the live editor.
4. Set `python.analysis.pyreflyVersion` to the verified absolute executable path,
   then set `python.analysis.diagnosticsSource` to `Pylance + Pyrefly` and reload.
   Establish actual external-server/TSP readiness, not just setting readback.
5. Establish an incremental editor-LSP trace baseline, then open
   `scenarios/issue_8295.py` through `procedures/pep723.json`. The tested trigger
   is opening/focusing the script after the backend switch and reload.
6. Observe editor-originated semantic-token full/range/delta requests for that
   URI and inspect rendered coloring of `Box`, `Domain`, `convert`, `identity`
   and `metadata_get`. Retain request IDs, errors/stacks and screenshots.
   Do not substitute syntax coloring or a direct provider call.
7. With the same interpreter and backend, open
   `scenarios/regular_project_control.py` through
   `procedures/ordinary-control.json`; repeat the token and rendered checks.
8. Change only diagnostics source to `Pylance`, reload, verify the interpreter
   is unchanged, and repeat `scenarios/issue_8295.py`.

## Evidence and limitations

- **Issue-wide result: inconclusive.** A November 18 Windows desktop check of
  this partial fixture used Pylance 2026.4.101, Pyrefly 1.4.1 and CPython
  3.11.15. Opening and focusing both scenario files produced successful
  semantic-token full and delta responses and visible imported-name coloring.
  The PEP 723 script also retained coloring with the same interpreter after
  switching to Pylance. No reported token error was observed in those checks.
  This does not establish behavior in the reporter's original environment.
- Retained November 17 Windows receipts for this fixture report successful
  semantic-token full requests in `scenarios/issue_8295.py` with Pyrefly and
  Pylance, and in `scenarios/regular_project_control.py` with Pyrefly. That run
  used Pylance 2026.4.101, Python 3.11.15 and Pyrefly 1.4.1, not the reporter's
  complete environment. Separate hover errors in both files are not the
  reported semantic-token failure and do not establish its cause.
- A later historical attempt was blocked during Marketplace startup, before
  product checks. That is not evidence that current setup will fail or that the
  product symptom was reproduced.
- `dependencies = []` and a separately installed editable package are explicit
  fixture assumptions. They do **not** reconstruct the reporter's per-script
  uv environment. Executing the script with automatic uv isolation is not a
  substitute for the declared editor checks.
- Browser/Ona hosting, Ubuntu, exact metadata/package types, interpreter
  resolution, original uv commands and complete trace remain unconfirmed.
  Windows desktop observations are lower-fidelity supporting evidence only.
- No save action/settings, theme override, search path, or semantic-highlighting
  override is invented. Settings here are test instrumentation, not a complete
  reporter configuration. Apply machine-specific executable paths at runtime.
- A pass on this partial fixture does **not** justify closure or establish
  `not_reproduced` for the reporter. A matching failure needs its full trace
  and producer evidence before assigning a root cause.
- If partial checks pass, request a shareable affected script, exact PEP 723
  metadata, editable package example, uv commands/interpreter path, VS Code/Ona
  version and full failing Pylance trace.

## Public export boundary

This workspace contains only synthetic fixture code, portable settings and
instructions. Keep environments, bytecode, egg metadata, setup receipts,
screenshots and native logs outside public export. A non-git exporter must
explicitly exclude runtime files even though `.gitignore` lists them.
