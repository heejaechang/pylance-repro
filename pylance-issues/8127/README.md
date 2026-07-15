# pylance-release issue #8127 — repro workspace

- **Issue:** [[TSP] Goto implementation doesn't work for Pyrefly](https://github.com/microsoft/pylance-release/issues/8127)
- **Author:** rchiodo (Pylance maintainer)
- **Labels:** `team needs to reproduce`
- **Classification:** bug — TSP / Pyrefly parity gap
- **Subsystem:** Language service — Go To / Find All Implementations over an
  external type server (Pyrefly) via TSP.
  `AsyncImplementationProvider` → `AsyncTypeHierarchyProvider.onSubtypes`.

## Summary

When Pylance is configured to use **Pyrefly as the diagnostics source**
(external type server over TSP), invoking **Go To Implementations** /
**Find All Implementations** on a base-class method returns **only the clicked
symbol** instead of all overrides. With the native Pylance type server the same
action returns every override.

## Repro steps

1. Configure Pylance so Pyrefly is the diagnostics source (force Pyrefly as the
   external type server over TSP).
2. Open `scenarios/issue_8127.py`.
3. Right-click `BaseWithConcreteMethod.method` and choose
   `Go To Implementations` (or `Find All Implementations`).

### Expected

All overrides are listed:

- `BaseWithConcreteMethod.method`
- `Intermediate.method`
- `Derived2.method`

### Actual (bug)

Only the clicked symbol (`BaseWithConcreteMethod.method`) is returned.

## Root cause (from code tracing)

`handleImplementation` routes every backend (including the external Pyrefly TSP
snapshot) through `AsyncImplementationProvider.getImplementations()`
(`packages/pylance-internal/src/server/languageServices/asynchronousFeatures.ts`).
That provider returns the self location plus whatever
`AsyncTypeHierarchyProvider.onSubtypes()` yields
(`packages/pylance-internal/src/languageService/asyncImplementationProvider.ts`).

`onSubtypes` / `_handleMethodSubtypes` / `_handleClassSubtypes` depend on
**Pylance-native evaluator operations** —
`getTypeOfClass`, `lookUpClassMembers`, `assignClassToProtocol`,
`getInferredTypeOfDeclaration`
(`packages/pylance-internal/src/languageService/asyncTypeHierarchyProvider.ts`).
When Pyrefly is the external type server these class-typing operations do not
produce results over TSP, so the subtype walk yields an empty set and only the
self location survives — matching the reported symptom.

This is a `[TSP]` parity tracking bug, not a regression in the native path.
