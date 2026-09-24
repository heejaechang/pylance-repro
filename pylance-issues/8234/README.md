Issue: https://github.com/microsoft/pylance-release/issues/8234

Related public report: https://github.com/microsoft/pylance-release/issues/8209

## Reproduction steps
1. Create `.vscode/settings.json` with `python.analysis.enablePytestSupport` set to `true`.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Open `test_move_symbol_pytest_8209.py` and place the cursor on `TypeToMove`.
4. Run `Move symbol to...` from the code actions menu.
5. Select `move_symbol_destination_8209.py` as the destination file.

Saved entry file: `test_move_symbol_pytest_8209.py`.

## Expected behavior
`move_symbol_destination_8209.py` contains `class TypeToMove` and `label = "move me"`.
The source file retains `import sys` and `unrelated_function`, but no longer contains `class TypeToMove:`.

## Actual behavior
The destination file remains empty after selecting it.
The source file still contains `class TypeToMove:`.

## Environment
- Target version: 2026.3.105
- Public availability at report preparation: This version is published on Visual Studio Marketplace (checked 2026-09-24 09:31 UTC).
- Observed Pylance version: 2026.3.105
- Build availability: Published on Visual Studio Marketplace at verification time.
- VS Code version: unknown (not recorded)
- Python version: unknown (not recorded)
- Operating system: unknown (not recorded)

## Evidence and limitations
This report uses saved verifier results and a public copy of the retained repro. Verification was not rerun. Any privacy or portability changes to the public copy are listed below.

The public repro was prepared from saved verification evidence and was not freshly tested.
The saved verification enabled `python.analysis.enablePytestSupport: true`.
Private source annotations were removed without changing executable code.
Recorded manifest settings were included in the portable copy; reporting did not rerun them.
Private source comments were removed without changing executable code.
requirements.txt was adjusted for public sharing; the original saved file was not changed or rerun.
test_move_symbol_pytest_8209.py was adjusted for public sharing; the original saved file was not changed or rerun.
Saved screenshot 2 was omitted because useful public-safe pixels could not be established.
Saved screenshot 3 was omitted because useful public-safe pixels could not be established.
