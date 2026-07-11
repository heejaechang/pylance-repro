 # SCENARIO: extract method should not turn referenced functions into new parameters
 # TARGET: the `for` loop in the `if __name__ == '__main__'` block
 # TRIGGER: select the loop and run "Extract method"
 # EXPECT: the extracted method takes only `d`, not `add`
 # VERIFY: if the new method signature includes `add`, the bug still reproduces
 # RECOVER: undo the refactoring or reload the file

def add(a, b):
    return a + b


def new_func(add, d):
    for i in range(10):
        add(i, d)

if __name__ == '__main__':
    d = 5
    new_func(add, d)