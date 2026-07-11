# Issue #8035 Verification Workspace

**Issue**: https://github.com/microsoft/pylance-release/issues/8035
**Title**: 'Go to Definition' should be special-cased for `typing` aliases for `collections.abc` ABCs

## Repro Steps (from issue body)

1. Open `test_file.py` which contains `from collections.abc import Iterable`
2. Place cursor on `Iterable`
3. Invoke "Go to Definition" (F12 / Ctrl+Click)

## Expected Behavior (quoted from issue)

> "Go to Definition" should navigate to the actual class definition in `collections/abc.py` (or the stub `typing.pyi`), not the alias assignment in `typing.py`.

## Actual Behavior (quoted from issue)

> "Go to Definition" navigates to the alias assignment line in `typing.py` (e.g. `Iterable = _collections_abc.Iterable`) which is "useless".

## Verification Checklist

- [ ] "Go to Definition" on `Iterable` in `test_file.py` — confirm where it navigates
- [ ] Check if it lands on `typing.py` alias assignment (confirms bug)
- [ ] Check if "Go to Declaration" (different command) goes to `typing.pyi` (expected per commenter @Enegg)
- [ ] Test with `from typing import Iterable` as well (same expected behavior)

## Notes

- The issue is about source mapping: the stub `typing.pyi` defines `Iterable` as a class, but the source mapper maps to `typing.py` where it's just an alias `Iterable = _collections_abc.Iterable`
- The user wants "Go to Definition" to follow through to `collections/abc.py` where the actual class is defined
- This is an enhancement request (current behavior is technically correct alias resolution)
- Requires a real Python interpreter to verify (source mapping depends on installed Python's `.py` files)
