# SCENARIO: hover on a dataclass constructor keyword argument should show the full optional type and default value
# TARGET: `bar` in `Foo(bar="asf")` below
# TRIGGER: Hover
# EXPECT: hover opens on the keyword argument label
# VERIFY: the hover content includes the full parameter shape `bar: str | None = None` rather than showing only the default value without the union type
# RECOVER: no recovery needed

from dataclasses import dataclass


@dataclass
class Foo:
    bar: str | None = None


a = Foo(bar="asf")