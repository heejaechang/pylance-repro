 # SCENARIO: type hierarchy should include indirect subtypes even when overrides use `@override`
 # TARGET: `method` in classes `A`, `B`, and `C`
 # TRIGGER: show the type hierarchy for `A.method` and expand subtypes
 # EXPECT: `C.method` appears as a subtype under `B.method`
 # VERIFY: if the hierarchy stops at `B.method`, the bug still reproduces
 # RECOVER: no recovery needed

from abc import ABC, abstractmethod
from typing import override


class A(ABC):
    @abstractmethod
    def method(self):
        pass


class B(A):
    @override
    def method(self):
        pass


class C(B):
    @override
    def method(self):
        pass