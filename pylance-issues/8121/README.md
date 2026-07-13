# Repro workspace — pylance-release#8121

**Issue:** [\[TSP\] When using Pyrefly as a diagnostics source, there are no import code actions](https://github.com/microsoft/pylance-release/issues/8121)

**Author:** rchiodo
**Labels:** (none)

## Summary

When Pyrefly is configured as the diagnostics source over TSP
(`python.analysis.diagnosticsSource = "Pylance + Pyrefly"`), an unresolved
name/import such as `os` (used without `import os`) surfaces a diagnostic, but
the quick fixes / code actions offered are **only** the "ignore type error"
fixes. The expected **"Add `import os`"** code action is missing.

Root cause (confirmed in code): `MultiplexingDiagnosticCodeMapper.onUpdateSettings`
only installs a diagnostic-code mapper (`TyDiagnosticCodeMapper`) when the type
server executable filename `startsWith('tsp-ty')`. Pyrefly's executable is named
`pyrefly`/`pyrefly.exe`, so no mapper is installed and Pyrefly's diagnostic codes
never translate to Pyright `reportXxx` rules — so add-import quick fixes are
never offered.

- `packages/pylance-internal/src/common/diagnosticCodeMapper.ts` — `_isTyTypeServer`, `MultiplexingDiagnosticCodeMapper`
- `packages/pylance-internal/src/common/addImports.ts`
- `packages/pylance-internal/src/languageService/importResolveCodeActions.ts`
- `packages/pylance-internal/src/languageService/codeActionDiagnostics.ts`

## Steps to reproduce

1. Open this workspace in VS Code with Pyrefly configured as the diagnostics
   source over TSP.
2. Open `scenarios/issue_8121.py`.
3. Observe the diagnostic on the unresolved `os` reference.
4. Invoke Quick Fix (Ctrl+.) on `os`.

### Expected

Quick fixes include **"Add `import os`"**.

### Actual (bug)

Quick fixes contain only "ignore type error" style fixes; no add-import action.
