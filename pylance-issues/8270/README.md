Issue: https://github.com/microsoft/pylance-release/issues/8270

## Saved failed scenarios
- hover close provides fixture method tooltip
- genitems signature help popup
- go to definition on doctest_namespace.clear
- pytester type annotation code action adds correct imports

## Reproduction steps
1. Use the attached workspace, retaining tests/pytest_test.py, tests/conftest.py, and the empty tests/__init__.py. Open the workspace root in VS Code with the Python and Pylance extensions enabled.
2. Prepare a Python environment and install the public dependency with `python -m pip install -r requirements.txt`. Select that environment using Python: Select Interpreter. The recorded interpreter was Python 3.12.10; the installed pytest version was not recorded.
3. Retain the supplied workspace settings, particularly python.analysis.enablePytestSupport=true, python.analysis.enablePytestExtra=true, and python.analysis.inlayHints.pytestParameters=true. Leave the fixture parameters unannotated and retain the original unfinished `capfdbinary.` expression.
4. Hover failure: in tests/pytest_test.py, find test_fixture_hover and hover over `close` in `capfdbinary.close` at line 37. Inspect the method signature and documentation in the tooltip. The recorded observation window was 15 seconds.
5. Signature-help failure: find test_fixture_signatureHelp, place the cursor between the parentheses in `pytester.genitems()` at line 42, and invoke Trigger Parameter Hints. Inspect whether a signature-help popup appears. The recorded observation window was 15 seconds.
6. Definition failure: find test_fixture_gotodef, place the cursor on `clear` in `doctest_namespace.clear()` at line 46, and invoke Go to Definition. Inspect the notification and whether a definition target opens. The recorded observation window was 15 seconds.
7. Annotation failure: find test_fixture_codeAction, place the cursor on its `pytester` parameter at line 50, and invoke Quick Fix. Select the offered action `Add type annotations for all fixture references in this file`.
8. Inspect the resulting imports and both test_fixture_codeAction(pytester) and test_fixture_signatureHelp(pytester). Compare these parameters with the other fixtures annotated by the same action. The recorded Quick Fix menu observation budget was 30 seconds.
9. Undo the annotation action to restore the original imports and unannotated functions. This restoration was also performed in the saved check.

Saved entry file: `tests/pytest_test.py`.

## Expected behavior
Hovering over `capfdbinary.close` provides the CaptureFixture.close method signature and documentation, rather than an Unknown member type.
Trigger Parameter Hints inside `pytester.genitems()` displays signature help.
Go to Definition on `doctest_namespace.clear()` opens a usable definition target for clear.
The file-wide fixture annotation action annotates the pytester parameters in both functions and adds the corresponding Pytester import.

## Actual behavior
The close tooltip displayed only `(function) close: Unknown`, without the expected method signature or documentation. The screenshot also showed a CaptureFixture[bytes] parameter inlay hint. The saved accessibility snapshot independently recorded the Unknown tooltip.
Trigger Parameter Hints completed at `pytester.genitems(|)`, but no signature-help popup appeared within 15 seconds. The saved screenshot and accessibility snapshot showed an unobstructed editor without a parameter-hints widget.
Go to Definition displayed `No definition found for 'clear'` and remained in tests/pytest_test.py. No definition target opened within 15 seconds. The screenshot showed a dict[str, Any] inlay hint for doctest_namespace.
The file-wide annotation action was offered and executed. It added imports for typing.Any and conftest.Fruit and annotated other fixtures, but both pytester parameters remained unannotated and no Pytester import was added. Undo restored the original file.

## Environment
- Target version: unknown (not recorded)
- Public availability at report preparation: The exact target version was not recorded; Marketplace availability was not inferred.
- Observed Pylance version: 2026.3.105
- Build availability: unknown (not recorded)
- VS Code version: unknown (not recorded)
- Python version: 3.12.10
- Operating system: Windows

## Evidence and limitations
This report uses saved test results and a public copy of the retained repro. Verification was not rerun. Any privacy or portability changes to the public copy are listed below.

These are recorded failed editor checks, not confirmed product defects. Root cause and attribution were not established.
The supplied conftest.py defines user fixtures but contains no pytester plugin declaration. The public copy preserves this setup; no plugin or replacement provider was added. This fixture-availability limitation applies to the pytester signature-help and annotation observations.
The source intentionally contains the unfinished `capfdbinary.` expression and other editor scenarios. It is an editor reproduction, not a runnable pytest suite. The unfinished expression was retained rather than repaired.
The installed pytest version was not recorded. requirements.txt remains unpinned, so a new installation may differ from the recorded environment.
Pylance 2026.3.105 is the observed build. The exact target version was not recorded, and Marketplace availability was not established. No publicly available release of that build is asserted.
The hover observation initially matched two hover elements, one hidden. The saved screenshot and read-only accessibility snapshot resolved that selector ambiguity without repeating the hover action.
The definition failure included an explicit no-definition message; it was not merely a mismatch against a particular expected destination.
The annotation action changed other recognized fixtures before Undo. The reported failure is specifically its omission of the pytester annotations and import.
For portability, the named-workspace extraPaths value was replaced with a relative workspace path. pyrightconfig.json now uses the supplied workspace root instead of an absent src directory and is valid JSON. Unrelated dependencies were removed; pytest and all supplied supporting Python files were retained.
The public copy was prepared from saved evidence only. No tests or editor actions were rerun, and the portability adjustments have not been freshly verified.
Local-only or unrelated editor settings were omitted from the portable copy.
.vscode/settings.json was adjusted for public sharing; the original saved file was not changed or rerun.
pyrightconfig.json was adjusted for public sharing; the original saved file was not changed or rerun.
requirements.txt was adjusted for public sharing; the original saved file was not changed or rerun.
