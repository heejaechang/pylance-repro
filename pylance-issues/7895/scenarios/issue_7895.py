# SCENARIO: local parameter completions should outrank self-member completions when names collide
# TARGET: the partial identifier `upd` inside `some_method`
# TRIGGER: trigger completion at the end of `upd` and accept the top suggestion
# EXPECT: the top suggestion resolves to the local parameter `update_trees`
# VERIFY: if accepting the top suggestion inserts `self.update_trees`, the bug still reproduces
# RECOVER: no recovery needed


class SomeClass:
    def update_trees(self) -> None:
        ...

    def some_method(self, update_trees: bool) -> None:
        if upd:
            self.update_trees()