# Issue #6088: No docstring shown for `np.zeros` in numpy 2.0

**Issue URL**: https://github.com/microsoft/pylance-release/issues/6088

## Repro Steps (from issue body)

1. Install the requirements.txt (including numpy 2.0)
2. Open the `docstrings.py` file
3. Hover over `zeros` in the `np.zeros` call.

## Expected behavior

> Docstring for `zeros` is shown. It is shown if you use numpy 1.x instead (I tried 1.26.4)

## Actual behavior

> No docstring.

## Verification Checklist

- [ ] numpy >= 2.0 is installed in the workspace interpreter
- [ ] Hover over `zeros` in `np.zeros(5)` on line 3 of `docstrings.py`
- [ ] Verify whether a docstring appears in the hover popup
- [ ] If no docstring: issue **reproduced**
- [ ] If docstring shown: issue **not reproduced** (fixed on current bits)

## Supporting files

- `requirements.txt` — ensures numpy 2.0+ is installed (the reporter explicitly used numpy 2.0)
- `docstrings.py` — mirrors the reporter's repro file (hovering over `np.zeros`)

## Root Cause (from investigation)

Pylance's bundled native stubs at `packages/pylance-internal/bundled/native-stubs/numpy/core/_multiarray_umath.pyi`
were generated against numpy 1.20.2. In numpy 2.0, the internal C extension moved from
`numpy.core._multiarray_umath` to `numpy._core._multiarray_umath`. The import resolver's
`_findNativeStub` method looks for the stub based on the runtime module path, so with numpy 2.0
it looks for `numpy/_core/_multiarray_umath.pyi` which doesn't exist.
