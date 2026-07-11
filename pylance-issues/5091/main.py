# SCENARIO: block comment inside an indented Python block should preserve the surrounding structure
# TARGET: select the `print(i / 10)` and `x.append(i)` lines inside the `for` loop below
# TRIGGER: run Block Comment on that two-line selection
# EXPECT: the selection stays inside the `for` block and the block comment action is available
# VERIFY: after execution, the inserted triple-quoted block remains indented under the `for` loop and does not break the Python block structure
# RECOVER: undo until the file matches its original text

x = []
for i in range(100):
    print(i)
    print(i / 10)
    x.append(i)
    if i == 10:
        print('yes')
print('end')