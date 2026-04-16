# Issue 5410

Use this folder to check hover on a pytest fixture parameter. The key file is `hover_fixture.py`.

## Steps

1. Open `hover_fixture.py`.
2. Hover over the `fixt_1` parameter use inside `test_some_test(fixt_1)`.

## Expected Result

- Hover opens successfully on the parameter use.
- The hover should include the fixture docstring `Fixture one description for hover verification.`.
- If the hover only shows parameter typing such as `(parameter) fixt_1: Any` and omits the fixture docstring, the issue still reproduces.
