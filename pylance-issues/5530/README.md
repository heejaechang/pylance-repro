# Repro workspace — pylance-release#5530

Issue: https://github.com/microsoft/pylance-release/issues/5530
Title: Support `missing module import` diagnostic in `change spelling`
Type: enhancement (maintainer-filed feature request)

## Issue body (verbatim repro)

> currently, `change spelling` quick fix only response to `unknown identifier`
> diagnostic. make it to response to `missing import module` diagnostic as well
> so it can offer `quick fix` in this situation as well.
>
> ```
> import pandos
>
> ```
>
> expected behavior:
> show `change spelling to 'pandas'`
>
> actual behavior:
> no `change spelling` code action
>
> ...
>
> it should only offer the quick fix if it can find real module whose name is
> closer to the what is written.

## Files

- `test.py` — contains the issue's verbatim repro: `import pandos`
- `.vscode/settings.json` — ensures Pylance is the language server (implied scaffolding)

## Verification checklist (in issue order)

1. Open `test.py`. Pylance reports a missing-import diagnostic (`reportMissingImports`)
   on `pandos`.
2. Place the cursor on `pandos` and invoke Quick Fix (Ctrl+.).
3. Expected (per issue): a `change spelling to 'pandas'` quick fix is offered,
   because `pandas` is a real module name close to the typed text.
4. Actual (current bits): **no** `change spelling` code action is offered. This
   confirms the enhancement gap — change-spelling only fires on
   `reportUnboundVariable` / `reportUndefinedVariable`, not on missing-import
   diagnostics.
5. Negative gate (per issue's final note): for text with no close real module
   (e.g. `import zzqqxx`), no change-spelling action should be offered even after
   the enhancement lands.

## Notes

This is a feature request, not a bug. The "reproduced" state here is the *current
absence* of the change-spelling quick fix on missing-import diagnostics, which
matches the maintainer's described actual behavior.
