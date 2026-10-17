Issue: https://github.com/microsoft/pylance-release/issues/8271

## Saved failed scenarios
- commit override completion in notebook context
- rename a shadowing module from a notebook quick fix
- highlight a repeated variable name in notebook context
- format on type after a `match` statement
- rename a notebook-visible type reference
- rename a method reference on `m`
- verify notebook analysis in restricted workspace mode

## Reproduction steps
1. Keep the complete supplied directory tree, including the supporting Python modules, .vscode/settings.json, pyrightconfig.json, and requirements.txt. Open its root folder in VS Code with the Python, Pylance, and Jupyter extensions enabled.
2. For a portable Windows environment, create a workspace-local virtual environment and install the supplied public dependencies from the workspace root:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
```
The recorded Python version was 3.12.10; dependency versions were not recorded.
3. Select .venv\Scripts\python.exe as both the Python interpreter and the notebook kernel. Open src\notebook.ipynb and retain the supplied analysis settings, including basic type checking and reportShadowedImports set to information.
4. The cell indices below are zero-based. These are editor/analysis scenarios, not a Run All workflow: the notebook and supporting files deliberately contain incomplete Python. Preserve those inputs, particularly the unresolved MyType import. Dismiss menus between scenarios and restore original text if an action makes an edit.
5. Override completion, cell 2: locate class Derived(MyType) and put the caret immediately after me in the incomplete declaration def me. Invoke Trigger Suggestion and inspect the rendered completion entries. The recorded scenario attempts to commit the method override only if that entry is offered.
6. Shadowing-module quick fix, cell 3: retain src\mailbox.py, locate import mailbox, and place the caret inside mailbox. Open Quick Fix and look for the entry that renames mailbox to mailbox_x. Do not substitute an unused-import action for the requested rename.
7. Document highlighting, cell 8: place the caret inside variable in variable = "Hello" and invoke Document Highlight once. Inspect the assignment, print(variable), for ch in variable, and the visible comment occurrences of variable. The saved observation allowed 10 seconds.
8. Enter after match, cell 10: put the caret immediately after the colon in match ch:, with the cell editor focused. Press Enter once and inspect both the source text and caret position. The saved observation allowed 10 seconds.
9. Type rename, cell 17: place the caret on MyType in m = MyType(). Invoke Rename Symbol and attempt to supply MyType2. Inspect whether a rename input opens and whether notebook-visible references change. Keep the existing from completion import MyDict, MyType statement in cell 2 unchanged.
10. Method rename, cell 17: place the caret on method in m.method(v=zipPath("path")). Invoke Rename Symbol and attempt to supply method2. Keep the existing zipPath import in cell 16 and the unresolved MyType context unchanged.
11. Workspace Trust baseline, cell 22: begin with the repro folder trusted. In c = pytest.Cache(Path("path"), pytest.Config(pytest.PytestPluginManager())), inspect Cache and Path. The recorded trusted baseline resolved Cache as class Cache.
12. Run Workspaces: Manage Workspace Trust and switch this repro folder to Restricted Mode. Return to the same cell and inspect Cache and Path. The saved observation showed Cache becoming Unknown while Path remained class Path.
13. Switch the same folder back to trusted mode without reloading the window. Return to the exact Cache target in cell 22 and inspect whether hover analysis resumes automatically. The saved hover attempt timed out after approximately 60 seconds; a second read-only hover also timed out, and the notebook showed Loading.
14. For recovery only, run Reload Window once and return to the same cell. The saved recovery restored Cache and Path class hovers. This recovery does not replace the preceding failure to refresh automatically after trust was restored.

Saved entry file: `src/notebook.ipynb`.

## Expected behavior
Override completion: the completion list includes method; committing it inserts an override method skeleton and any required imports into notebook-visible text.
Shadowing-module quick fix: Quick Fix on import mailbox offers the rename entry for mailbox to mailbox_x, allowing the requested rename to be initiated.
Document highlighting: the recorded scenario explicitly expects variable matches in comments as well as the assignment and code references.
Enter after match: pressing Enter after match ch: inserts a new line with the caret indented for the match body.
Type rename: Rename accepts MyType2 and updates the affected notebook-visible MyType references.
Method rename: Rename accepts method2 and updates the affected notebook-visible method references.
Workspace Trust: third-party symbols stop resolving in Restricted Mode while bundled symbols remain inspectable; restoring trusted mode automatically restores usable analysis without requiring Reload Window.

## Actual behavior
Override completion, cell 2: the rendered completion list contained only memoryview, not method. The required override could not be committed, and no edit occurred. Diagnostics reported MyType as an unknown import symbol in from completion import MyDict, MyType.
Shadowing-module quick fix, cell 3: the menu offered Remove unused import, Remove all unused imports, and a Copilot action, but no mailbox-to-mailbox_x rename entry. No file rename occurred. The active diagnostic was an unused-import hint, not a shadowed-import diagnostic.
Document highlighting, cell 8: exactly three code occurrences were decorated—the assignment, print(variable), and for ch in variable. The visible comment occurrences were not highlighted. Code-symbol highlighting itself worked.
Enter after match, cell 10: after one Enter, the cell text was unchanged and the caret remained at line 19, column 10 rather than moving to a new indented line. The editor input retained focus, and no picker was visible.
Type rename, cell 17: VS Code displayed "The element can't be renamed." No rename input opened, and MyType remained unchanged. Hover identified the imported MyType as Unknown.
Method rename, cell 17: VS Code displayed "The element can't be renamed." No rename input opened, and method remained unchanged. The instance m came from the unresolved MyType context.
Workspace Trust, cell 22: the initial transition to Restricted Mode changed Cache to Unknown while Path remained class Path. After returning to trusted mode, Cache hover timed out twice and the notebook showed Loading. Reload Window restored Cache and Path class hovers, but automatic trusted-return recovery had failed.

## Environment
- Target version: 2026.3.105
- Public availability at report preparation: This version is published on Visual Studio Marketplace (checked 2026-10-17 02:59 UTC).
- Observed Pylance version: 2026.3.105
- Build availability: 2026.3.105 was published on Visual Studio Marketplace according to the supplied publication lookup, checked 2026-10-17 02:59 UTC.
- VS Code version: unknown (not recorded)
- Python version: 3.12.10
- Operating system: Windows

## Evidence and limitations
This report uses saved test results and a public copy of the retained repro. Verification was not rerun. Any privacy or portability changes to the public copy are listed below.

This report preserves seven recorded failed checks. It does not establish that all seven observations are Pylance defects or regressions.
The override-completion and two rename failures share an unresolved MyType fixture context. The supplied completion module does not provide the imported MyType. That input is intentionally preserved rather than repaired or replaced.
The mailbox action was absent without a shadowed-import diagnostic. The recorded expectation did not match the available action context; the cause was not established as a Pylance defect.
The highlight failure concerns the explicit comment-match expectation. All three code references were highlighted; the notes qualify the difference as host behavior rather than a demonstrated Pylance defect.
The Enter observation is a keyboard/editor-input failure, not specifically attributed to Pylance. Focus remained in the editor, but the responsible layer was not established.
The trusted-return failure is retained despite successful recovery after Reload Window. The saved evidence establishes hover timeouts and Loading, not whether Pylance, VS Code, or the interaction controller caused them.
The public copy was prepared from saved evidence only. No tests or editor scenarios were rerun, and no new reproduction or verification result is claimed.
Private annotations, unrelated local settings, notebook outputs, and notebook metadata were removed during preparation. The portable settings use relative paths, and dependencies use public package names. Supporting files and incomplete analysis inputs are retained.
src/docstrings.py is supplied as a complete replacement with public EXAMPLE_ configuration names and harmless literal 'test' credential placeholders. Its existing rendering examples, markup, directives, and executable statements are retained.
requirements.txt includes pandas and lxml. Follow that file for installation; the notebook retains historical dependency comments saying pandas was absent. Package versions were not recorded or pinned, so a fresh installation may differ from the saved environment.
All reported failures come from failed_checks. Other completed checks supplied environment context only and are not presented as additional failures.
Six screenshots are included. Their crops exclude account imagery and surrounding workspace UI. Some editor text and the quick-fix menu were already clipped in the captured window; the detailed observations also rely on the saved notes. No screenshot of the Workspace Trust failure is attached.
Additional screenshots were omitted because the report image limit was reached.
Local-only or unrelated editor settings were omitted from the portable copy.
Private source comments were removed without changing executable code.
Notebook outputs and metadata were stripped; code cells were not fixed or rerun.
.vscode/settings.json was adjusted for public sharing; the original saved file was not changed or rerun.
pyrightconfig.json was adjusted for public sharing; the original saved file was not changed or rerun.
requirements.txt was adjusted for public sharing; the original saved file was not changed or rerun.
src/docstrings.py was adjusted for public sharing; the original saved file was not changed or rerun.
src/docstrings.py was excluded because its private content could not be removed from the public copy.
