# SCENARIO: async override completion should unwrap a sync base method's `Awaitable[T]` return type when generating an async derived override
# TARGET: the partial `async def ya` line inside class `Derived` below; keep the cursor at the end of the partial method name token before triggering completion
# TRIGGER: Completion commit
# EXPECT: override completion offers the inherited `yadda` method from class `Base`
# VERIFY: after committing the selected override completion, the generated method signature is `async def yadda(self) -> Awaitable[int]:` instead of the correct `async def yadda(self) -> int:`
# RECOVER: revert the file after the check

from typing import Awaitable


class Base:
    def yadda(self) -> Awaitable[int]:
        ...


class Derived(Base):
    async def ya