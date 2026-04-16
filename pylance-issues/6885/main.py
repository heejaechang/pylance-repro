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