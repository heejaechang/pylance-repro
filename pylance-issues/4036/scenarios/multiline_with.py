# Issue #4036 repro: multi-line with statement folding
# After Black formatting, the with statement spans multiple lines.
# Expected: the with-suite body should be foldable.
# Actual: only the open(...) call gets a fold arrow; the body does not.

with open(
    "path/to/extremely/long/file/path"
) as extremely_long_variable_name_probably_too_long:
    print("hello")
    print("world")
    print("this is the body")
    print("it should be foldable")
    print("but currently it is not")
    x = 1
    y = 2
    z = x + y
