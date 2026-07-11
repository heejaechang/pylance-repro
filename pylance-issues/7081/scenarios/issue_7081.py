# SCENARIO: Go to Definition should work when invoked on call parentheses and operators
# TARGET: the `(` in `callable_thing(1)` and the `+` in `add_left + add_right`
# TRIGGER: invoke Go to Definition with the cursor on the punctuation token
# EXPECT: navigation should resolve to `__call__` and `__add__`
# VERIFY: if navigation stays in place or fails to reach the dunder definitions, the issue remains valid
# RECOVER: no recovery needed


class CallableThing:
    def __call__(self, value: int) -> int:
        return value


class Addable:
    def __add__(self, other: 'Addable') -> 'Addable':
        return self


callable_thing = CallableThing()
add_left = Addable()
add_right = Addable()

call_result = callable_thing(1)
sum_result = add_left + add_right