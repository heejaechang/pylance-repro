# Issue #5031 — Installed stubs don't take precedence over bundled stubs

- Issue: https://github.com/microsoft/pylance-release/issues/5031
- Type: bug (stub-resolution precedence)
- Reporter: @rchiodo (maintainer-filed); maintainer-revalidated 2026-04-18 by @heejaechang.

## Verbatim repro (from the issue body)

The issue body lists these exact steps:

> 1. Install django-stubs into your environment
> 2. Set typechecking mode to basic
> 3. Add the following code to a file
>
> ```python
> from django.db import models
>
> class MyModel(models.Model):
>     nullable = models.IntegerField(null=True)
>
> def foo():
>     m = MyModel.objects.get()
>
>     def accepts_only_int(x: int):
>         pass
>
>     accepts_only_int(m.nullable)
> ```
>
> 4. If we actually used the django-stubs, passing m.nullable to accepts_only_int shouldn't show an error.
> 5. If you goto declaration on models.IntegerField it will still jump into our bundled stubs.

The code block above is copied byte-for-byte into `main.py`.

## Files in this workspace

- `main.py` — the issue's code block verbatim. (The issue says "add the following code to a file"
  but does not name the file; `main.py` is a neutral choice.)
- `requirements.txt` — `Django==4.2.6` + `django-stubs==4.2.6`, matching the maintainer's
  2026-04-18 revalidation environment. The issue's step 1 requires django-stubs to be installed.
- `.vscode/settings.json` — `python.analysis.typeCheckingMode = basic`, required by the issue's step 2.

## Verification checklist (run in real VS Code with the Pylance extension)

1. Create a venv and `pip install -r requirements.txt`. Select that interpreter in VS Code.
2. Confirm Pylance is the prerelease build whose `dist/bundled/stubs/django-stubs` is present
   (the bundled stubs are what this issue is about).
3. Open `main.py`. Wait for analysis.
4. **Expected (per issue step 4):** NO error on `accepts_only_int(m.nullable)` — if the installed
   django-stubs were used, `m.nullable` would be typed `int`.
5. **Actual (reported / maintainer-revalidated):** an `int | None` → `int` argument-type error is
   reported on `accepts_only_int(m.nullable)`, because the bundled django-stubs take precedence and
   type `nullable` as `int | None`.
6. **Expected (per issue step 5):** "Go to declaration" on `models.IntegerField` lands in the
   **installed** `site-packages/django-stubs`.
   **Actual:** it lands in Pylance's **bundled** `dist/bundled/stubs/django-stubs`.

The bug reproduces when steps 4/5 show the "Actual" behavior.

## Root cause (verified by code structure)

- `packages/pylance-internal/src/pylanceImportResolver.ts` → `resolveImportEx` (lines 150-184)
  looks up the bundled stub via `getBundledTypeStubsPath(...)` and, if found, returns it
  **unconditionally** tagged `ImportType.ThirdParty`.
- `packages/pyright/packages/pyright-internal/src/analyzer/importResolver.ts`
  `_resolveBestAbsoluteImport` computes the installed site-packages stub into `bestResultSoFar`
  (lines 1610-1646), then only short-circuits before the `resolveImportEx` hook when the installed
  package is fully `py.typed` (lines 1651-1658: `if (bestResultSoFar?.pyTypedInfo && !isPartlyResolved) return`).
- For an installed stub-only package **without** a `py.typed` marker (django-stubs historically
  lacked one — see typeddjango/django-stubs#2089), the py.typed early-out does not fire, so
  execution reaches `resolveImportEx`, which returns the bundled stub and overrides the installed one.

Also reported for Matplotlib (comment by @dstansby), confirming it is not Django-specific.
