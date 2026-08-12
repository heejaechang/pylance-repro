"""Minimal Pylance/Pyright hover reproducer for a converter-aware field."""

from typing import Any, Callable, TypeVar, Union, dataclass_transform

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


def field(*, default: Any) -> Any:
    """A regular field specifier used as the working control case."""
    return default


def converted_field(*, converter: Callable[[InputT], OutputT], default: Any) -> Any:
    """A field specifier whose converter determines the accepted write type."""
    del converter
    return default


@dataclass_transform(kw_only_default=True, field_specifiers=(field, converted_field))
class ModelBase:
    """Teach Pyright about both field specifiers."""

    def __init__(self, **values: Any) -> None:
        self.__dict__.update(values)


def to_float(value: Union[float, str]) -> float:
    """Convert the field's wider input type to its stored type."""
    return float(value)


class Model(ModelBase):
    plain: float = field(default=0.0)
    """This documentation appears when hovering over ``model.plain``."""

    converted: float = converted_field(default=0.0, converter=to_float)
    """This documentation is missing when hovering over ``model.converted``."""


model = Model(converted="1.5")

model.plain
model.converted
