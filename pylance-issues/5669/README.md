# Issue 5669 — Repro workspace
# https://github.com/microsoft/pylance-release/issues/5669
#
# Title: A local variable is being treated as type 'Never' in an except handler
#
# Scenario: scenarios/issue_5669_never_in_except.py
#
# Verified: 2026-05-28 via pylanceLanguageInfo
# Status: STILL REPRODUCES
#
# Root cause: When an async method has no return type annotation, assigning its
# awaited result to a variable with an explicit `T | None` annotation inside a
# try block causes the type evaluator to collapse the variable to `Never` after
# an `is not None` narrowing guard in the except handler. The issue does NOT
# reproduce when the async method has an explicit return type annotation.
#
# Subsystem: Pyright core — control-flow / type narrowing on try/except paths
# when the assigned value has an implicit (Unknown) return type.
