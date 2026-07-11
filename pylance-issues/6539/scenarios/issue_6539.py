# SCENARIO: override completion with type checking mode off should still generate inherited parameter and return type annotations
# TARGET: the partial `def f` line inside class `B` below; keep the cursor at the end of the partial method name token before triggering completion
# TRIGGER: Completion commit
# EXPECT: override completion offers the inherited `f` method from class `A`
# VERIFY: after committing the selected override completion, the generated method signature is `def f(self, a: int, b: str) -> None:` rather than an unannotated `def f(self, a, b):`
# RECOVER: revert the file after the check

class A:
    def f(self, a: int, b: str) -> None:
        pass


class B(A):
    def f