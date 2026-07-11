# SCENARIO: quoted generic type annotations should color their brackets consistently with unquoted generic annotations
# TARGET: the `[` and `]` inside `'Box[T]'`
# TRIGGER: inspect semantic token coloring in the editor
# EXPECT: quoted generic brackets are not left behind as plain string punctuation when compared with the unquoted `Box[T]` line below
# VERIFY: the brackets in the quoted annotation do not remain string-colored while the unquoted generic brackets receive semantic/punctuation coloring
# RECOVER: no recovery needed

from typing import Generic, TypeVar

T = TypeVar('T')


class Box(Generic[T]):
    pass


def quoted(value: 'Box[T]') -> None:
    pass


def unquoted(value: Box[T]) -> None:
    pass