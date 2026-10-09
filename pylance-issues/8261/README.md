Issue: https://github.com/microsoft/pylance-release/issues/8261

Related public report: https://github.com/microsoft/pylance-release/issues/8189

## Reproduction steps
1. Create a workspace containing the attached `.vscode/settings.json` and `with_item_annotations_8189.py` files.
2. Open the workspace in VS Code with Pylance 2026.4.100 and select a Python interpreter.
3. Set `editor.inlayHints.enabled` to `on`, then open `with_item_annotations_8189.py` and wait for analysis to finish.
4. Inspect the `source_file` target in the first `with open(...)` statement while the editor text remains `as source_file,`.

Saved entry file: `with_item_annotations_8189.py`.

## Expected behavior
A variable type inlay hint showing `TextIOWrapper` is rendered for `source_file` without changing the source text.

## Actual behavior
No `TextIOWrapper` variable type inlay hint was rendered for `source_file` after bounded observations, although variable type inlay hints were enabled.

## Environment
- Target version: 2026.4.100
- Public availability at report preparation: This version is published on Visual Studio Marketplace (checked 2026-10-09 22:50 UTC).
- Observed Pylance version: 2026.4.100
- Build availability: Published on Visual Studio Marketplace (checked 2026-10-09 22:50 UTC).
- VS Code version: unknown (not recorded)
- Python version: 3.14.6 (selected .venv shown in the recorded screenshot)
- Operating system: unknown (not recorded)

## Evidence and limitations
This report uses saved verifier results and a public copy of the retained repro. Verification was not rerun. Any privacy or portability changes to the public copy are listed below.

The saved verification did not save the file or invoke Fix All because the required inlay-hint precondition was not met; it does not establish the Fix All annotation result.
`editor.inlayHints.enabled` was explicitly set to `on` during the recorded verification.
The portable settings include the recorded Fix All-on-save setting, but this report was prepared from saved evidence and was not freshly tested.
Private verification annotations were removed from the public repro file.
Local-only or unrelated editor settings were omitted from the portable copy.
Recorded manifest settings were included in the portable copy; reporting did not rerun them.
Private source comments were removed without changing executable code.
.vscode/settings.json was adjusted for public sharing; the original saved file was not changed or rerun.
with_item_annotations_8189.py was adjusted for public sharing; the original saved file was not changed or rerun.
