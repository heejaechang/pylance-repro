# SCENARIO: renaming parameters should update keyword arguments passed through functools.partial
# TARGET: rename parameter `a` to `number`
# TRIGGER: invoke Rename Symbol on `a` in `def foo(a: int, b: str)`
# EXPECT: both the direct call and `partial(foo, a=1)` update to `number=`
# VERIFY: if the partial call keeps `a=1`, the rename bug still reproduces
# RECOVER: revert the file after the check

from functools import partial


def foo(a: int, b: str):
    print(a, b)


def main():
    foo(a=1, b='hello')
    partial_foo = partial(foo, a=1)
    partial_foo(b='world')


if __name__ == '__main__':
    main()