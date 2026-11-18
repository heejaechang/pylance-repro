# Pending real-editor checks

Use the workspace root containing this file. The caller owns execution.

## Environment declaration

- `venvPath`: `.venv`
- `dependencySource`: `requirements.txt`
- Requested Python: CPython 3.11, matching 3.11.18 when available
- Requested Pyrefly: 1.4.1
- Editable dependency: `./editable-package`
- Product input: caller-selected current Pylance build, with its exact loaded
  version and artifact identity recorded. This is a current-behavior check,
  not paired baseline/fix acceptance.
- Reported host: browser-based VS Code in Ona on Ubuntu 24.04.5
- Available local-host result must be labeled lower-fidelity if it does not use
  that host and operating system

## Preconditions

1. Reuse the declared environment if present; do not reinstall or recreate a
   working environment. A Windows environment cannot serve a Linux host.
2. Verify the editable import and Pyrefly executable with the exact interpreter.
3. Start a fresh VS Code session at 1920x1080 or larger and record
   `window.innerWidth` and `window.innerHeight`.
4. Select and verify the declared interpreter.
5. Set `python.analysis.pyreflyVersion` to the verified absolute executable path,
   then set `python.analysis.diagnosticsSource` to `Pylance + Pyrefly`.
6. Reload and establish external Type Server Protocol readiness.
7. Start incremental LSP observation before opening the scenario.

The existing local environment was rechecked on 2026-11-18: CPython 3.11.15,
Pyrefly 1.4.1, and an editable import resolving inside `editable-package/src/`.
No new environment was prepared. Portable settings intentionally omit the
previous runner's absolute interpreter and Pyrefly paths; apply them explicitly
in the next live session. No setup-helper receipt is bundled here.

## editorRunProcedure

After the preconditions, use the shared `editorRunProcedure` action with the
owning live `sessionId`, the exact absolute `params.workspacePath`, and
`params.procedurePath` pointing to `procedures/pep723.json` under this workspace.
Use `procedures/ordinary-control.json` for the ordinary-file check. Reuse
`procedures/pep723.json` after the source-only Pylance switch and awaited reload.
Both procedure files are persisted, schema-version-1 JSON with source hashes.

Choose a fresh `params.resultPath` under the controller evidence root for each
invocation and set `includeServiceTimings: true`. These files are procedure
inputs, not execution receipts or verdicts. Setup, reload, backend readiness,
rendered observation, screenshots and incremental LSP collection remain
separate caller-owned actions; the procedures do not assert success.

Use compact tracing plus native trace logging. Call `observeEditorLsp` before
editor actions to establish an owned-session baseline, then after each check
with a fresh result path. Retain all receipts because observation advances the
cursor. Distinguish full, range and delta requests by method, ID and scenario
URI. Keep unresolved records pending; missing records do not prove success or
absence of a request. For hosts unsupported by this observer, retain native
host logs rather than treating missing local logs as a product result.

After each source change, retain `getDiagnosticsBackendState` for the exact
workspace-folder URI, but do not treat its explicitly inconclusive backend
state as readiness. Correlate actual external-server initialization/operation
with the scenario. Verify the selected interpreter in the live status bar.
Record actual renderer dimensions of at least 1920x1080 before UI checks.

## Checks

### Pyrefly PEP 723 check

Open `scenarios/issue_8295.py`.

- Confirm a `textDocument/semanticTokens/full` request is issued for this URI.
- Confirm the request completes without `-32603`.
- Inspect rendered tokens for imported `Box`, `Domain`, `convert`, `identity`,
  and `metadata_get`; retain a screenshot or Inspect Editor Tokens evidence.
- Retain the post-action incremental LSP observation and Pylance trace.
- Search the trace for `typeParams`, `parameters`, `getName`, and `findIndex`.
- Judge imported-symbol coloring, not the continued presence of syntax colors.
- Do not add a hover call to this target sequence. If checking the previously
  observed hover anomaly, do it afterward in a separately labeled observation.

### Pyrefly ordinary-file control

Open `scenarios/regular_project_control.py` without changing the interpreter or
Pyrefly settings.

- Repeat the semantic-token request and rendered-color checks.
- Record whether behavior differs from the PEP 723 script.

### Same-interpreter Pylance control

Change only `python.analysis.diagnosticsSource` to `Pylance`, reload, and reopen
`scenarios/issue_8295.py`.

- Verify the selected interpreter did not change.
- Repeat the semantic-token request and rendered-color checks.

## Existing observations, not a new verdict

The 2026-11-17 Windows run used Pylance 2026.4.101, CPython 3.11.15 and
Pyrefly 1.4.1. Semantic-token full requests succeeded for the Pyrefly script
(request 11, 1719 ms), Pyrefly ordinary control (29, 184 ms), and Pylance
script control (9, 955 ms). Saved editor screenshots retain coloring.
Separate Pyrefly hover requests 20 and 33 failed with undefined `parameters`
in both files; Pylance hover 14 succeeded. No corresponding semantic-token
failure or producer diagnosis was established.

The new procedures deliberately omit hover and do not replace or reinterpret
those original receipts. No new editor session has been launched by this
investigation.

## Interpretation

- A Pyrefly-only crash after readiness reproduces the product symptom on this
  partial topology. Preserve the full stack and external type payload before
  attributing a producer.
- Success for all checks is supporting evidence only. The reporter's exact
  script, package, uv topology, Ona host, and Ubuntu environment remain missing,
  so it is not an unable-to-reproduce or closure result.
- If only real-editor execution can decide the checks, the investigation
  execution verdict remains `unknown` until the caller completes them.
- Ask for the affected script plus a shareable editable-package example,
  exact uv setup/interpreter resolution and full trace if the partial fixture
  still passes. The absence of that material does not make the partial
  workspace ineligible.
- Stop only the caller's owned session after saving evidence; do not adopt or
  terminate a historical session based on its ID in old notes.
