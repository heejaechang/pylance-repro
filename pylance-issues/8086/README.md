# Issue #8086 verification workspace

Issue: https://github.com/microsoft/pylance-release/issues/8086
Title: **[TSP] Pyrefly as a TSP server is not returning the correct MRO list for a unittest.TestCase**

## Reporter's steps (verbatim from the issue body)

1. Clone django
2. Setup a venv with the requirements
3. Change Pylance to use pyrefly as the diagnostics source
4. Open `tests\basic\tests.py` and try to goto def on a `self.assertEqual` function for a test case.

**Expected result:**
> It finds the assertEqual on unittest.testcase

**Actual result:**
> No definition found

## What this workspace contains

The issue title isolates the root cause to the MRO of a `unittest.TestCase`
subclass (`self.assertEqual` is inherited from `unittest.TestCase`). The
reporter's Django `tests/basic/tests.py` is just a vehicle: its test classes
ultimately derive from `unittest.TestCase`.

This workspace uses a faithful, isolated repro instead of a full Django clone:

- `tests.py` — a direct `unittest.TestCase` subclass with `self.assertEqual(1, 1)`.
- `.vscode/settings.json` — sets `python.analysis.diagnosticsSource` to
  `"Pylance + Pyrefly"` (the setting that routes Pylance's diagnostics/type
  source to the Pyrefly external TSP server).

A harness-level run with the **real pinned pyrefly binary** confirmed the
direct-subclass repro produces the identical failure (see "Evidence" below), so
cloning Django adds no diagnostic value.

## Verification checklist (real VS Code)

1. Open this folder in VS Code with the Pylance/pylance-dev extension that has
   Pyrefly-as-TSP support.
2. Confirm `python.analysis.diagnosticsSource` is `"Pylance + Pyrefly"` (already
   set in `.vscode/settings.json`). Pyrefly will be auto-resolved/downloaded.
3. Open `tests.py`.
4. Place the cursor on `assertEqual` in `self.assertEqual(1, 1)` and invoke
   **Go to Definition** (F12).
5. **Expected:** lands on `TestCase.assertEqual` in the unittest stub
   (`unittest/case.pyi`).
6. **Bug (current):** "No definition found".

To contrast, temporarily set `python.analysis.diagnosticsSource` back to
`"Pylance"` (native Pyright). Go to Definition then resolves correctly — proving
the gap is in the Pyrefly TSP path, not Pylance's definition logic.

## Evidence (harness-level, real pyrefly binary)

Temp repro test:
`packages/pylance-internal/src/tests/pyreflyTsp/fast/issue8086.repro.test.ts`
(investigation-only; delete after use). Run output:

- Pyrefly TSP path: `[pyrefly] assertEqual definitions: undefined` → reproduces "No definition found".
- Native pyright control: `[native] assertEqual definitions: [/typeshed-fallback/stdlib/unittest/case.pyi@99:8]` → resolves correctly.

## Root-cause pointers (pyrx side)

- TSP `ClassType` carries no MRO/base classes over the wire
  (`packages/type-server/src/protocol/typeServerProtocol.ts` — must NOT be modified).
- Pylance reconstructs the class (and MRO) from pyrefly's synthesized stub /
  declaration in `packages/pylance-internal/src/common/typeProvider.ts`
  (`Synthesized` case ~558-696; `buildSyntheticClass` fallback ~818-844 collapses
  MRO to `[Subclass, object]` when bases can't be recovered).
- MRO is walked for the member declaration via `lookUpClassMember` in
  `packages/pylance-internal/src/languageService/asyncDefinitionProvider.ts`.

The fix is likely external (Pyrefly's TSP response for the TestCase subclass) or
a Pylance reconstruction-tolerance change; precedent issues #8016/#8075 were a
mix of pyrefly-side and Pylance-side fixes. The TSP wire protocol must not change.
