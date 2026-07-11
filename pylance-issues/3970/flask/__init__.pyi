from typing import Callable, TypeVar

_F = TypeVar('_F', bound=Callable[..., object])


class Flask:
    def __init__(self, import_name: str) -> None: ...
    def route(self, rule: str) -> Callable[[_F], _F]: ...