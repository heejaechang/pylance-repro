# Comparison: multi-line for statement folding (works correctly per issue report)

extremely_long_variable_name_probably_too_long_iterable = [1, 2, 3, 4]
for (
    extremely_long_variable_name_probably_too_long
) in extremely_long_variable_name_probably_too_long_iterable:
    print("hello")
    print("world")
    print("this body IS foldable")
    print("the fold arrow appears on the last line of the for statement")
    x = 1
    y = 2
    z = x + y
