# Caller-owned current-behavior checks for issue 8295

Issue: https://github.com/microsoft/pylance-release/issues/8295

This is repro/current-behavior mode, not local-fix acceptance. The investigation
prepares only the partial fixture. The caller owns all environment preparation,
VS Code lifecycle, backend readiness and UI observations.

## Environment metadata

- `venvPath`: `.venv` (intended, currently not prepared)
- `dependencySource`: `requirements.txt`
- Python: reporter CPython 3.11.18; record any substitution.
- Pyrefly: reporter 1.4.1, pinned in requirements.
- Local fixture: editable `./editable-package`.
- Product: caller-selected current Pylance build; prefer latest prerelease when
  no build is prescribed and record exact loaded version/artifact.
- Reporter host: browser VS Code in Ona / Ubuntu 24.04.5. Local Windows checks
  remain partial; no claim that host differences are causal.
- Historical environment: Windows CPython 3.11.15 / Pyrefly 1.4.1. It is not
  present at the canonical workspace now; historical paths are not readiness.

Reuse a declared compatible environment or valid issue-workspace setup receipt
if the caller has one. Otherwise use the controller's issue-monitor setup
contract, preserving its original source interpreter, `--issue-number 8295`,
the canonical workspace and exact supplied `EVIDENCE_ROOT`. No receipt or
environment was created by this investigation. Install dependencies through
the approved feed, verify the editable import and Pyrefly executable, and retain
any setup failure separately from the product result.

## Preconditions and lifecycle (not procedure steps)

1. Use a fresh caller-owned headless session unless otherwise requested. Set
   `python.trace.server: "compact"` before launch and native `logLevel: "trace"`.
   Record loaded extension identity; do not silently substitute another build.
2. Verify `window.innerWidth >= 1920` and `window.innerHeight >= 1080` before
   UI checks. Save dimensions in the exact caller evidence directory.
3. Select the intended exact interpreter and verify the status-bar selection.
   With that interpreter, verify package origin and editable installation.
4. Verify the actual Pyrefly executable/version, write its absolute path to
   `python.analysis.pyreflyVersion`, then enable `Pylance + Pyrefly` at workspace
   scope and reload.
5. Retain `getDiagnosticsBackendState` for the exact workspace-folder URI.
   Its explicit inconclusive state is not external-server readiness. Correlate
   native initialization and a served TSP operation with this owned session.
6. Call `observeEditorLsp` before editor actions to establish an owned-session
   baseline. Do not mix direct provider calls or a hover into the acceptance
   sequence. Perform any separate readiness probe before this baseline.

## editorRunProcedure

Prepared schema-version-1 JSON inputs:

- `procedures/pep723.json`: open/focus `scenarios/issue_8295.py`.
- `procedures/ordinary-control.json`: open/focus the ordinary-file control.

Use the shared `editorRunProcedure` action with the owning live `sessionId`,
exact absolute `params.workspacePath`, and absolute `params.procedurePath`
under this workspace. Set `includeServiceTimings: true` and a fresh
`params.resultPath` under the exact supplied evidence directory for each call.
Input hashes guard saved scenario bytes. Successful procedure completion proves
actions only, not a semantic-coloring verdict.

Lifecycle, source switches, reloads, readiness, screenshots and incremental LSP
observations remain separate caller actions. Do not write an empirical
acceptance record for these unexecuted inputs.

## Checks and observations

1. **REPRO / Pyrefly script:** run `procedures/pep723.json`; capture actual
   editor-originated semantic-token full/range/delta responses for
   `scenarios/issue_8295.py`, with request ID, URI, duration, error and full
   stack. Check imported-name coloring in the rendered editor. Expected:
   semantic highlighting, no `-32603` token error. Actual: pending.
2. **GEN / ordinary-file control:** run `procedures/ordinary-control.json`
   without changing the environment/backend. Repeat token and rendered checks.
   This is a file outside PEP 723, not an inline-metadata causality proof.
   Actual: pending.
3. **GEN / Pylance control:** change only diagnostics source to `Pylance`,
   reload, verify the exact same interpreter, and rerun `procedures/pep723.json`.
   Repeat the same token and rendered checks. Actual: pending.

Retain a fresh `observeEditorLsp` result after each check; observations consume
a cursor. Preserve pending records and follow up without replaying mutations.
Missing trace events do not prove absence/success. Remote transports need
native host logs where the local observer is unsupported. Inspect request
methods: a hover failure is not a semantic-token failure. The reported stack
mentions `typeParams`/`parameters`; preserve any complete stack before tracing
type producers. Syntax colors alone are not semantic-coloring evidence.

After capture, restore the original workspace source and stop only the
caller's owned session. Never use historical session IDs as cleanup authority.

## Fidelity and disposition

The script has empty PEP 723 dependencies and uses a separately installed
synthetic editable package. Exact reporter source, per-script uv environment,
settings and host remain missing. No unknown save setting or action is assumed.
If these partial checks pass, preserve the observations but keep issue-wide
behavior unresolved and request the missing reporter materials. Do not close
the issue on that basis. A matching failure is actionable symptom evidence;
producer RCA still needs a linked failing boundary payload and runtime proof.
