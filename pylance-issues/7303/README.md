# Issue 7303: Overloaded __init__ docstring prefers base class over sibling overload

**Issue**: https://github.com/microsoft/pylance-release/issues/7303  
**Status**: Reproduced  
**Type**: Enhancement  

## Problem

When hovering over a constructor call for a derived class (`Line`) that has overloaded `__init__`
with a docstring on only one overload (the `*args` catch-all), Pylance shows the docstring from 
the base class (`Curve`) instead of the docstring from the sibling overload.

## Reproduction

1. Open `main.py` in VS Code with Pylance
2. Hover over `Line()` on line 4

### Expected (from issue body)
> The hover tooltip should show the Line class docstring:
> "The AcDbLine class represents the line entity in AutoCAD..."

### Actual (from issue body)
> "I get the docstring for Curve" — the base class docstring is shown instead.

Verified actual output:
```
class Line()
---
Curve base class constructor.
```

## Files

- `stubs.pyi` — Class hierarchy with overloaded `__init__` (verbatim from issue)
- `main.py` — Usage file that triggers hover

## Root Cause

In `packages/pyright/packages/pyright-internal/src/analyzer/typeDocStringUtils.ts`:

The `getOverloadedDocStringsInherited()` function (line 139) calls `getOverloadedDocStrings()` 
which correctly finds the docstring on the `*args` overload. However, the per-overload hover path
uses `getFunctionDocStringInheritedInfo()` (line 88) which:

1. Checks the specific matched overload's `shared.docString` (empty for the no-arg overload)
2. Falls through to MRO walk  
3. Finds `Curve.__init__` docstring

The fix: before walking the MRO, check sibling overloads in the same class for a docstring.
