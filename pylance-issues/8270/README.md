# Pytest fixture support: Unknown member hover, missing signature help and definition, and skipped pytester annotations

- Issue: https://github.com/microsoft/pylance-release/issues/8270
- Public reporter workspace: https://github.com/heejaechang/pylance-repro/tree/main/pylance-issues/8270
- Pinned reporter artifact: https://github.com/heejaechang/pylance-repro/tree/8a23f80c33561a9ba226b01d779c7d463ed04c1e/pylance-issues/8270
- Issue created: 2026-10-17.
- Issue state and labels read on 2026-10-28: open; `fixed in next version (main)`.

The report records four editor failures with inferred pytest fixture types:
Unknown hover on `capfdbinary.close`, no signature help on `pytester.genitems()`,
no definition for `doctest_namespace.clear()`, and omitted pytester annotations
and import after the file-wide fixture annotation action. These are concrete
checks worth verifying; their product attribution is not established by this
workspace preparation.

## Files and provenance

- `tests/pytest_test.py`: authoritative entry file, retaining the complete
  public scenario, comments, unannotated parameters, and unfinished expression.
- `tests/conftest.py`: public `Fruit`/`FruitSalad`, `fruit_bowl`, and `sample_bowl`
  definitions. No optional pytester plugin is activated.
- `tests/__init__.py`: empty, as supplied.
- `scenarios/issue_8270.py`: full source mirror for the canonical scenario-file
  contract, NOT the editor entry file. It is an added export artifact, not part
  of the reporter topology. Use `tests/pytest_test.py` for all checks; do not
  substitute the mirror, which has no adjacent conftest.py. No reference-count
  or whole-workspace rename assertion is requested against this added mirror.
- `requirements.txt`: public unpinned `pytest` dependency.
- `.vscode/settings.json` and `pyrightconfig.json`: retained portable public
  configuration, including `extraPaths: ["."]` and execution root `"."`.
- `screenshots/screenshot-1.png` through `screenshot-5.png`: retained historical
  reporter screenshots, NOT current verification results.

Only public reporter code/configuration and these instructions are included.
No local interpreter path, credentials, or internal product source is needed.

## Reproduction steps

1. Open THIS workspace root in VS Code with Python and Pylance enabled. Use a
   headless workbench of at least 1920x1080 for automation; measure the actual
   workbench dimensions before UI checks.
2. Prepare/select a Python environment, preferably Python 3.12.10 as recorded.
   Install `python -m pip install -r requirements.txt` using that interpreter.
   Record its exact executable/version and the installed pytest version. Probe
   `import pytest` using that same interpreter and confirm its live selection
   in VS Code. No pytest version was recorded by the reporter.
3. Keep the supplied settings, especially `python.analysis.enablePytestSupport`,
   `python.analysis.enablePytestExtra`, and
   `python.analysis.inlayHints.pytestParameters`, all true. Wait for language
   analysis to settle. Do not add annotations, repair syntax, activate pytester,
   or invent format/save actions before the original-setup checks.
4. Open `tests/pytest_test.py`. Leave `test_fixture_completion`'s unfinished
   `capfdbinary.` expression at line 33 unchanged.
5. **Member hover:** hover `close` in `test_fixture_hover` at line 37. Inspect
   the full visible tooltip and documentation for up to 15 seconds. Expected:
   usable CaptureFixture.close signature/documentation. Record the exact text;
   distinguish a real annotation from the CaptureFixture[bytes] inlay hint.
6. **Signature help:** place the cursor between the parentheses of
   `pytester.genitems()` in `test_fixture_signatureHelp` at line 42. Explicitly
   invoke **Trigger Parameter Hints** (Ctrl+Shift+Space); do not merely hover or
   wait for auto-trigger. Observe for 15 seconds. Record popup presence and full
   text, and any pytester fixture-availability limitation separately.
7. **Go to Definition:** place the cursor on `clear` in
   `test_fixture_gotodef` at line 46 and explicitly invoke **Go to Definition**
   (F12). Observe for 15 seconds. Record the destination or exact notification;
   do not infer success from the doctest_namespace type/inlay hint alone.
8. **File-wide fixture annotation:** return to `tests/pytest_test.py`, put the
   cursor on `pytester` in `test_fixture_codeAction` at line 50, and invoke
   **Quick Fix** (Ctrl+.). Allow up to 30 seconds for the menu. Select
   **Add type annotations for all fixture references in this file**. Inspect
   the applied source edits/imports, specifically BOTH pytester parameters in
   `test_fixture_signatureHelp` and `test_fixture_codeAction`, and whether a
   Pytester import appears. Record changes to other fixtures as controls.
   An offered menu item alone is not successful annotation.
9. Undo the annotation action and confirm original source/imports are restored.
   Record whether a save/reload was actually used; neither is an established
   missing reporter prerequisite.
10. Optional follow-up ONLY AFTER recording the original setup: explicitly
    activate pytester using a standard pytest plugin declaration and repeat
    the two pytester checks. Record the exact declaration, interpreter/plugin
    availability, and results as a **changed-setup variant**, not as evidence
    that pytester was activated in the report. Restore the original conftest.py.

## Evidence and limitations

### Historical observations (not rerun here)

The issue body and public README record these tested triggers and results:

| Trigger in `tests/pytest_test.py` | Historical reported result | Retained image |
| --- | --- | --- |
| Hover `capfdbinary.close` | `(function) close: Unknown`, despite parameter inlay hint | `screenshots/screenshot-1.png` |
| Explicit parameter hints inside `pytester.genitems()` | No popup in 15 seconds | `screenshots/screenshot-2.png` |
| Go to Definition on `doctest_namespace.clear()` | `No definition found for 'clear'` | `screenshots/screenshot-3.png` |
| Apply file-wide annotation from the pytester parameter | Action offered; other fixtures annotated, both pytester parameters/import skipped | `screenshots/screenshot-4.png`, `screenshots/screenshot-5.png` |

The current preparation inspected these five images, read the live issue and
retained public source/configuration, and materialized the workspace. It did
NOT rerun hover, parameter hints, definition, or annotation in VS Code.
All four fresh editor observations remain pending the next verifier.
No current `reproduced`, `not_reproduced`, or `fixed` finding is asserted.
Static validation matched all six retained source/configuration files to the
pinned public artifact above (normalizing line endings and terminal newlines),
matched all five screenshots byte-for-byte, checked the exact trigger lines,
and confirmed the empty package marker and unchanged optional-plugin setup.
The canonical scenario mirror was checked byte-for-byte against the entry file.

- Reported host: Windows, Python 3.12.10, observed Pylance 2026.3.105. Exact
  target build, VS Code version, pytest version, and public availability of
  that observed Pylance build were not recorded. Do not silently claim an
  exact historical environment or identify a development version by name alone.
- The optional pytester plugin is NOT activated in the supplied files.
  Missing pytester help/annotations may reflect fixture unavailability.
  This does not invalidate the other concrete fixture checks or justify
  discarding the partial scenario.
- The unfinished `capfdbinary.` is intentional reporter input. Running pytest
  collection would encounter syntax errors and is not an editor verdict.
  Do not remove it without preserving and first testing the unchanged case.
- Screenshot type labels are inlay hints; the authoritative source parameters
  are unannotated. Do not transcribe those visual hints into annotations.
- The original saved accessibility snapshots mentioned by the report were not
  recovered here; image/body descriptions are historical evidence only.
- The public copy already changed a named-workspace extraPaths value to `"."`,
  made pyrightconfig.json valid with root `"."`, removed unrelated dependencies,
  and omitted local-only editor settings. Those portability changes were not
  freshly verified. Unknown original settings are not silently reconstructed.
- A fixed-in-next-version label or related merged change is context, not
  empirical confirmation for any of the four fresh checks.
- Later verification must record actual product/build provenance and the
  resulting editor behavior. Keep fresh screenshots/results outside this
  public workspace, under the investigation evidence directory.
- This is a useful partial editor repro even if exact historical package/build
  matching is unavailable. Report limitations per check rather than skipping
  the entire issue, and do not auto-close based on this preparation.
