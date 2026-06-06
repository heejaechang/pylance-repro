# Verification workspace — pylance-release #5365

Issue: https://github.com/microsoft/pylance-release/issues/5365
Title: Providing `__builtins__.pyi` causes lots of "Could not resolve source for '__builtins__'" trace log output

## What this workspace reproduces

Per the issue body (verbatim repro steps):

> 1. In new folder, create two empty files: `typing\__builtins__.pyi` and `test.py`. See [the pyright docs](https://microsoft.github.io/pyright/#/builtins) for info on `__builtins__.pyi`.
> 2. Set `"python.analysis.logLevel": "Trace"`
> 3. Open folder in VS Code
> 4. Open "Python Language Server" log in Output pane

> ## Actual behavior
>
> The following is logged once per `.py` file in the workspace. And then each time a file is opened for the first time, it gets logged again twice (once by FG and once by BG):
>
> (the issue's fenced log block — a `Could not resolve source for '__builtins__'` line followed by ~25 search-path lines — was pruned from the fetched body; see saved manifest)

## Files in this workspace

- `typings/__builtins__.pyi` — empty user-provided builtins stub.
- `test.py` — empty project source file (a non-stub `.py` that implicitly imports `__builtins__`).
- `.vscode/settings.json` — sets `python.analysis.logLevel: "Trace"` (from the repro) and `python.analysis.stubPath: "typings"`.

## Fidelity note: `typing` vs `typings`

The issue text writes the stub at `typing\__builtins__.pyi`. The default Pylance/Pyright stub path is **`typings`** (with an `s`) — see `packages/pyright/packages/pyright-internal/src/common/pathConsts.ts` (`defaultStubsDirectory = 'typings'`). A `__builtins__.pyi` is only picked up when it sits on the stub search path, so the reported log spam (which requires the stub to actually resolve) implies the stub lived in the real stub path. The issue's `typing` is therefore treated as a typo for the default `typings`. To remove ambiguity this workspace:

- places the stub at `typings/__builtins__.pyi` (the default stub path described by the linked pyright builtins docs), and
- sets `python.analysis.stubPath: "typings"` explicitly (redundant with the default, but unambiguous).

If a verifier prefers the byte-literal path, rename the folder to `typing` and set `python.analysis.stubPath: "typing"` — the behavior is identical because both make `__builtins__.pyi` resolvable on the stub path.

## Verification checklist (real VS Code, current bits)

1. Open this folder in VS Code with Pylance.
2. Confirm `.vscode/settings.json` has `"python.analysis.logLevel": "Trace"`.
3. Open the "Python Language Server" output channel.
4. Expected (bug present): a `Could not resolve source for '__builtins__' in file '.../test.py'` block (followed by ~25 search-path lines) is emitted once per `.py` file, and again (FG + BG) when a file is first opened.
5. Expected (bug fixed): no `Could not resolve source for '__builtins__'` block for the implicit builtins stub import.

## Root-cause anchors (for reference)

- `packages/pyright/packages/pyright-internal/src/analyzer/sourceFile.ts:1492-1493` — non-stub project files implicitly import `__builtins__` first.
- `packages/pyright/packages/pyright-internal/src/analyzer/importResolver.ts:960` — when `__builtins__` resolves to a stub, `nonStubImportResult` is computed; with no `__builtins__.py` source it is `isImportFound === false`.
- `packages/pyright/packages/pyright-internal/src/analyzer/program.ts:1492-1510` — emits the "Could not resolve source" verbose log. The suppression guard at line 1496 only skips stub-file importers and stdlib typeshed stubs, so a user `__builtins__` stub imported from a non-stub `.py` is not suppressed.
