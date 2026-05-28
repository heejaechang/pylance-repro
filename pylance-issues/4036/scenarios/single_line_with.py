# Comparison: single-line with statement folding (works correctly per issue report)

with open("path/to/extremely/long/file/path") as extremely_long_variable_name:
    print("hello")
    print("world")
    print("this body IS foldable when with is on a single line")
    x = 1
    y = 2
    z = x + y
