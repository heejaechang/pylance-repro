# Repro for https://github.com/microsoft/pylance-release/issues/7972
# Title: variable type inlay hints seem to be truncated to 32 characters, regardless of the editor inline hint length setting
# See README.md in this workspace for the full reporter context.

from collections.abc import Iterable
from types import MappingProxyType

def t():
    d : dict[str, Iterable[int]] = {}
    return MappingProxyType(d)

v = t()
