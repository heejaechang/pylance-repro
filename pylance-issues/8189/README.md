# Pylance issue 8189 reproduction

Original issue: https://github.com/microsoft/pylance-release/issues/8189

This workspace checks whether **Add Type Annotation** inserts an annotation after the target of a
`with ... as` statement and thereby produces invalid Python syntax.

## Reproduction steps

1. Open `scenarios/issue_8189.py` in VS Code with Pylance enabled.
2. Explicitly run **Pylance: Add Type Annotation** for the file.
3. Inspect the `with open(...) as cmdfile:` statement and the Problems panel.
4. Check whether Pylance changes the statement to the invalid form
   `with open(...) as cmdfile: TextIOWrapper:`.

## Evidence and limitations

The scenario in `scenarios/issue_8189.py` transcribes the issue-grounded `with open(..., mode="r")
as cmdfile:` pattern. A command-level Pylance harness repro observed Add Type Annotation inserting
`: TextIOWrapper` immediately after `cmdfile`, and syntax analysis rejects that transformed form.

This verification tests the explicit **Add Type Annotation** trigger. The reporter's exact
`editor.codeActionsOnSave` and `python.analysis.fixAll` settings are not known, and the report does
not establish that accepting a type-checking recommendation enabled annotation-on-save. A result
for this explicit trigger therefore does not confirm or disprove every part of the reporter's
save-time experience.
