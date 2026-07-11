from prettypretty.color.style import Style
from prettypretty.color.termco import Rgb
from prettypretty.color.theme import Theme, VGA_COLORS


def use_symbols() -> tuple[type[Style], type[Rgb], type[Theme], object]:
    return Style, Rgb, Theme, VGA_COLORS