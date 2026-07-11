# Repro for https://github.com/microsoft/pylance-release/issues/7997
# Title: Incorrect syntax highlighting for method calls in subclassing parameters
# See README.md in this workspace for the full reporter context.

from typing import Any
class B:
    def __init_subclass__(cls, *, foo, bar): print(f'foo: {foo}, bar: {bar}', file=bar) # a base class with custom __init_subclass__ taking some keyword parameters
def f(x) -> Any: return x # strip away type information
reveal_type(f(1)) # revealed type is 'Any'
class A(B, foo=f('').lower, bar='bar.txt'): ...
