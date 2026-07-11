 # SCENARIO: completion ranking should keep the closest `function1...` matches near the top
 # TARGET: the trailing `f` on the final line
 # TRIGGER: trigger completion at the cursor after `f`
 # EXPECT: the `function1...` candidates stay grouped near the top of the list
 # VERIFY: if lower-similarity results outrank the closer `function1...` matches, the bug still reproduces
 # RECOVER: no recovery needed

def function1():
    pass


def function2():
    pass


def function3():
    pass


def function1_with_extra_bit():
    pass


def function1_with_extra_bit_and_another_bit():
    pass


def function1_with_extra_bit_and_something_else():
    pass


f