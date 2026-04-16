# SCENARIO: bytes-literal arguments constrained by Literal overloads should offer the available bytes values in completion
# TARGET: the gap between the quotes in `example(b"")` below
# TRIGGER: Completion
# EXPECT: completion opens while the cursor stays inside the bytes literal argument
# VERIFY: the suggestion list includes all three literal payloads `int`, `bool`, and `str` for the bytes-literal argument rather than offering no Literal completions
# RECOVER: no recovery needed

from typing import Literal, overload


@overload
def example(parameter: Literal[b'int']) -> int: ...


@overload
def example(parameter: Literal[b'bool']) -> bool: ...


@overload
def example(parameter: Literal[b'str']) -> str: ...


def example(parameter):
    return parameter


example(b"")