# SCENARIO: go to definition on `print` should prefer the real print declaration over `object.__str__`
# TARGET: the builtin `print`
# TRIGGER: invoke Go to Definition on `print`
# EXPECT: the opened definition surface lands on a `def print(` declaration
# VERIFY: if the primary target still lands on `def __str__(self) -> str`, the bug still reproduces
# RECOVER: no recovery needed

print('foo')