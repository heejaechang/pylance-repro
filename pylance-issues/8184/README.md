# Issue #8184: `enableEditableInstalls` breaks relative imports in editable package

- Source: https://github.com/microsoft/pylance-release/issues/8184
- State: open
- Created: 2026-09-02T11:09:15+00:00
- Updated: 2026-09-02T11:09:15+00:00

## Reporter context

## Environment

* Pylance pre-release: `2026.3.101`
* Pyright: `1.1.413`
* Python extension: `2026.4.0`
* Python: `3.13.5`
* OS: Ubuntu 24.04.4 LTS

## Description

With Pylance `2026.3.101`, enabling editable-install support causes valid relative imports inside an editable package to be reported as unresolved.

For example:

```python
from .hey import hey
```

is reported as:

```text
Import ".hey" could not be resolved
```

The package is a regular Python package with `__init__.py` files present.

Setting:

```json
"python.analysis.enableEditableInstalls": false
```

immediately fixes the issue.

Stable Pylance `2026.3.1` also resolves the same import correctly.

## Reproduction repository

https://github.com/antontkv/pylance-relative-import-issue

The repository contains a minimal reproducible setup and trace logs for the working and failing configurations.

## Steps to reproduce

1. Install repository as `pip install -e .`.
2. Use Pylance pre-release `2026.3.101`.
3. Ensure:

```json
"python.analysis.enableEditableInstalls": true
```

4. Open the `hey_import/you.py`.

5. Pylance reports:

```text
Import ".hey" could not be resolved
```

6. Change the setting to:

```json
"python.analysis.enableEditableInstalls": false
```

7. Restart/reload Pylance.

The relative import now resolves correctly.

## Expected behavior

Relative imports within the package should resolve normally when `python.analysis.enableEditableInstalls` is enabled.

## Actual behavior

With `enableEditableInstalls=true`, Pylance dynamically resolves the editable package but subsequently fails to resolve a sibling relative import.

The trace log contains:

```text
[Editable Installs] Resolved packages: ...
```

followed by:

```text
Could not import '.hey'
```

With `enableEditableInstalls=false`, the same module is resolved correctly.

## Regression

The same project works with stable Pylance `2026.3.1`.

The difference appears to be related to the dynamic editable-install resolution path used by Pylance `2026.3.101` / Pyright `1.1.413`.

## Logs

Trace logs produced with:

```json
"python.analysis.logLevel": "Trace"
```

are included in the reproduction repository.
