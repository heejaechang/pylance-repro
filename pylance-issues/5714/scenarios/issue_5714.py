# SCENARIO: aliased imported types should show the same alias in visible inlay hints and inserted edits
# TARGET: the variable-type inlay hint for `z = a` below, and the return-type inlay hint for `foo` if it is also visible
# TRIGGER: apply the visible inlay hint without changing imports manually
# EXPECT: the visible inlay hint label uses the alias-aware name `MyClassAlias`
# VERIFY: applying the hint inserts `MyClassAlias`, and the inserted text matches the label that was shown instead of displaying `MyClass` and inserting `MyClassAlias`
# RECOVER: revert the file to its original text after the check

from MyClass import MyClass as MyClassAlias


def foo(a: MyClassAlias):
    z = a
    return z