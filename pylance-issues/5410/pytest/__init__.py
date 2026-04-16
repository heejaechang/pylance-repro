from typing import Any, Callable, Iterable, Literal, Optional, Sequence, TypeVar, Union

FixtureFunction = TypeVar('FixtureFunction', bound=Callable[..., object])
_ScopeName = Literal['session', 'package', 'module', 'class', 'function']


class FixtureFunctionMarker:
    def __call__(self, function: FixtureFunction) -> FixtureFunction:
        return function


def fixture(
    fixture_function: Optional[FixtureFunction] = None,
    *,
    scope: Union[_ScopeName, Callable[[str], _ScopeName]] = 'function',
    params: Optional[Iterable[object]] = None,
    autouse: bool = False,
    ids: Optional[Union[Sequence[Optional[object]], Callable[[Any], Optional[object]]]] = None,
    name: Optional[str] = None,
) -> Union[FixtureFunctionMarker, FixtureFunction]:
    fm = FixtureFunctionMarker()
    return fm