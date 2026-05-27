# Issue #8054 - Support Sphinx target resolution in ReST cross-references

**Issue URL**: https://github.com/microsoft/pylance-release/issues/8054

## Repro Steps

1. Open `test_crossref.py`
2. Hover over `connect_client` to see its docstring
3. Verify that `:meth:`Client.connect`` renders as a clickable link (currently renders as inline code)
4. Hover over `disconnect` to see its docstring
5. Verify that `:meth:`connect`` renders as a clickable link (this works - same class reference)

## Expected Behavior (from issue)

> Pylance should implement Sphinx's target resolution logic:
> "Names in these roles are searched first without any further qualification, then with the current module name prepended, then with the current module and class name (if any) prepended."

Specifically, `:meth:`Client.connect`` in `connect_client`'s docstring should resolve to a clickable link pointing to `Client.connect`.

## Actual Behavior

`:meth:`Client.connect`` in `connect_client`'s docstring renders as inline code (`` `Client.connect` ``) instead of a clickable link.

## Files

- `test_crossref.py` — verbatim from issue body
