# Issue 8191: Experimental Django support misses reverse ForeignKey with an app-label string target

- Issue: https://github.com/microsoft/pylance-release/issues/8191
- Labels: `team needs to reproduce`
- Classification: `bug`
- Importance: `med`
- Difficulty: `M`
- Fixable now: `yes`
- Allow auto-close: `false`
- Requires public linkback: `true`

## Reporter environment

- VS Code: 1.136.1
- Pylance: 2026.3.1
- OS: Linux x86_64
- Python: 3.13.5
- Django: 5.1
- django-stubs: not installed
- Type checking mode: `basic`

## Summary

With experimental Django support enabled, Pylance generates Django stubs but
does not recognize a reverse `ForeignKey` relation when the target uses a
Django `"app_label.ModelName"` string and the application is nested in a
Python package.

This workspace preserves the reported distinction:

- Python application path: `sample.groups`
- Django application label: `groups`
- Relation target: `"groups.Group"`
- Reverse relation: `Group.networks`

At runtime Django resolves the relation and creates `Group.networks`. Pylance
reports `reportAttributeAccessIssue` for `self.networks` in
`sample/groups/models.py`.

## Workspace layout

```text
.
├── .vscode/
│   └── settings.json
├── example/
│   ├── __init__.py
│   └── settings.py
├── sample/
│   ├── __init__.py
│   ├── groups/
│   │   ├── __init__.py
│   │   └── models.py
│   └── networks/
│       ├── __init__.py
│       └── models.py
├── scenarios/
│   └── issue_8191.py
├── manage.py
└── requirements.txt
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On Linux/macOS, use `.venv/bin/python` instead.

Open this directory in VS Code and select the environment containing
Django 5.1. The checked-in workspace settings enable experimental Django
support and basic type checking.

## Reproduction

1. Reload the VS Code window after selecting the interpreter.
2. Open `sample/groups/models.py`.
3. Inspect `self.networks` in `Group.get_networks`.
4. Check Problems for `reportAttributeAccessIssue`.
5. Optionally hover over `self.networks`.

## Expected

Pylance recognizes `Group.networks` as the reverse relation generated from
`Network.group`, with a type equivalent to `models.Manager[Network]` (or
Pylance's internal Django reverse-related manager type). No
`reportAttributeAccessIssue` is emitted.

## Reported actual behavior

Pylance reports:

```text
Cannot access attribute "networks" for class "Group"
  Attribute "networks" is unknown
```

## Runtime sanity check

The scenario confirms that Django itself resolves the relation:

```powershell
python scenarios/issue_8191.py
```

It prints the reverse accessor name and verifies that `Group` has a
`networks` descriptor.

## Candidate reproduction with complete expressions

The self-contained [complete-expressions](complete-expressions) workspace
records the same reverse-relation diagnostic and three related completion
failures on the Pylance 2026.3.103 candidate, with VS Code 1.137.0,
Python 3.14.4, Django 5.1.15, and Windows 11.

Open that subdirectory itself as the VS Code workspace and follow its
**Reproduction steps**. Its model files remain syntactically complete;
downstream member expressions live in a separate file. Its README records
the observed behavior, environment, and build-availability limitation.
