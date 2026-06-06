# Verification workspace — pylance-release #5364: "Globs in extra paths"

Issue: https://github.com/microsoft/pylance-release/issues/5364

## What the issue requests (enhancement)

Users with Bazel (`rules_python`) monorepos must list every pip dependency
directory individually in `python.analysis.extraPaths`. They ask for
glob/wildcard support so the list does not need manual syncing as the
dependency tree changes. The concrete glob example from the thread is:

> `external/rules_python~~pip~pip_310_*/site-packages`

This is NOT a bug report — it is a request for a capability Pylance does not
currently have. This workspace demonstrates the current behavior gap: a glob
pattern in `extraPaths` is treated as a literal path and is never expanded.

## Workspace layout

```
5364/
  main.py                                                  # import mypkg
  .vscode/settings.json                                    # glob extraPath
  external/rules_python~~pip~pip_310_abc123/site-packages/
      mypkg/__init__.py                                    # def hello() -> str
```

`.vscode/settings.json` mirrors the issue's glob verbatim:

```json
{ "python.analysis.extraPaths": ["external/rules_python~~pip~pip_310_*/site-packages"] }
```

The real dependency directory uses a concrete suffix (`pip_310_abc123`) that the
glob is meant to match — exactly the Bazel `external/...~~pip~pip_310_<hash>`
layout the reporter described.

## Verification checklist

1. Open this folder in VS Code with Pylance active.
2. Open `main.py`.
3. Observe `import mypkg` reports **`reportMissingImports`** ("Import "mypkg"
   could not be resolved"), even though `mypkg` exists under the directory the
   glob is intended to match. This confirms the glob is not expanded.
4. Confirmation that only the glob is the problem: temporarily replace the
   `extraPaths` entry with the **literal** matching path
   `external/rules_python~~pip~pip_310_abc123/site-packages`. The import now
   resolves and `mypkg.hello()` type-checks. This proves the directory and
   package are correct; the gap is solely the missing glob expansion.

## Root cause (code evidence)

`packages/pyright/packages/pyright-internal/src/common/configOptions.ts`
resolves each `extraPaths` entry as a literal path:

- default config (~line 1319): `configExtraPaths.push(configDirUri.resolvePaths(path))`
- per-`executionEnvironment` (~line 1705): `newExecEnv.extraPaths.push(configDirUri.resolvePaths(path))`

`Uri.resolvePaths` (baseUri.ts) only joins and normalizes `..`/`.`; `*` is a
literal path character. There is no glob expansion anywhere in the parse path.

## Design tension (from the thread, for the product decision)

`extraPaths` is order-dependent (it affects import resolution order), while
globs are order-independent. A glob implementation must pick a deterministic
expansion order (alphabetical was proposed) and document the resolution-order
implications. An alternative is direct Bazel output-tree support.
