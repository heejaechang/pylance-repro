# SCENARIO: extract method should return every value that still flows out of the selected if-branch block
# TARGET: select exactly the three marked lines inside the `if a > 0:` block below, from `print("HELLO")` through `b = 7`
# TRIGGER: Quick Fix
# EXPECT: the refactor menu contains `Extract method`
# VERIFY: after applying the refactor, the caller captures both `e` and `b` from the extracted function, for example with `e, b =` or `b, e =`, rather than returning only `b`
# RECOVER: revert the file to its original contents after the check

def example(a: int):
    if a > 0:
        print("HELLO")
        e = 1
        b = 7

        print(b)
    else:
        e = 2

    print(e)