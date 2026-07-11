# Issue #7390 - Type hints of member variables of a class which explicitly implements protocols

## Issue URL
https://github.com/microsoft/pylance-release/issues/7390

## Problem
"Find All References" and "Rename Symbol" fail to link member variables across Protocol base classes and implementing classes. Variables with type annotations in subclasses are treated as new declarations rather than overrides of the Protocol-defined variables.

## Repro Steps (from issue body verbatim)

1. Open `test.py` containing the code from the issue
2. Use "Find All References" on `self.a` in class `A` → shows only `P.a` and `self.a` in `A` (missing `Q.a`, `B.a`)
3. Use "Find All References" on `self.b` in class `A` → shows no other variable as the same one (missing `P.b`, `Q.b`, `B.b`)
4. Use "Find All References" on `B.a` or `B.b` → shows no other variable as the same one

## Expected (from issue)
> All of the `a` and `b` in `P`, `Q`, `A` and `B` should be the same variable, respectively.

## Actual (from issue)
> - For `self.a` in class `A`, Pylance shows only `P.a` and `self.a` in `A` are the same variable
> - For each of `self.b` in class `A`, `B.a` and `B.b`, Pylance shows no other variable as the same one

## Verification Checklist
- [ ] "Find All References" on `P.a` should include `Q.a`, `A.a` (self.a), and `B.a`
- [ ] "Find All References" on `P.b` should include `Q.b`, `A.b` (self.b), and `B.b`
- [ ] "Find All References" on `self.a` in `A` should include `P.a`, `Q.a`, and `B.a`
- [ ] "Find All References" on `self.b` in `A` should include `P.b`, `Q.b`, and `B.b`
- [ ] "Find All References" on `B.a` should include `P.a`, `Q.a`, and `A.a`
- [ ] "Find All References" on `B.b` should include `P.b`, `Q.b`, and `A.b`
- [ ] "Rename Symbol" on any of the above should rename all linked occurrences
