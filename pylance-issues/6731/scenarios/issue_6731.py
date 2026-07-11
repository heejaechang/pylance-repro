# SCENARIO: renaming a class property should also update structural pattern matching uses
# TARGET: rename `prop` to `my_prop`
# TRIGGER: invoke Rename Symbol on the class property
# EXPECT: both `case Foo(prop=1)` and `case Foo(prop=prop)` update to use `my_prop`
# VERIFY: if the pattern-matching cases remain on `prop`, the rename bug still reproduces
# RECOVER: revert the file after the check

class Foo:
    prop: int


def process(f: Foo):
    match f:
        case Foo(prop=1):
            print('one')
        case Foo(prop=prop):
            print(f'other: {prop}')
        case _:
            print('default')


if __name__ == '__main__':
    f = Foo()
    f.prop = 1
    process(f)