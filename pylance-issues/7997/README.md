# Issue #7997: Incorrect syntax highlighting for method calls in subclassing parameters

- Source: https://github.com/microsoft/pylance-release/issues/7997
- State: open
- Created: 2026-04-23T10:43:20+00:00
- Updated: 2026-05-14T07:46:26+00:00
- Labels: textmate bug, ai-triage-responded

## Reporter context

## Environment data

-   Pylance version: 2026.2.100
-   OS and version: Microsoft Windows Version 25H2 (OS Build 26200.846)
-   Python version: Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03)

## Code Snippet

```python
from typing import Any
class B:
    def __init_subclass__(cls, *, foo, bar): print(f'foo: {foo}, bar: {bar}', file=bar) # a base class with custom __init_subclass__ taking some keyword parameters
def f(x) -> Any: return x # strip away type information
reveal_type(f(1)) # revealed type is 'Any'
class A(B, foo=f('').lower, bar='bar.txt'): ...
```

## Expected behavior

Below is from the perspective of dark mode.

`lower`, a method of strings, correctly shows as the same colour (yellow) as methods and functions in other contexts when the function `f` is not applied. However, after the type is cast to `Any`, `lower` is no longer an attribute of known type. Therefore, it should not be highlighted (white), or in the worst case highlighted with the colour for attributes on objects (light blue).

## Actual behavior

`lower` is highlighted as green, the colour for classes. It was probably treated as a base class due to its location. This should be special-cased.
