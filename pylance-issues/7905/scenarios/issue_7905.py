# SCENARIO: positional-only optional parameters should not show call-argument-name inlay hints
# TARGET: the call `do_something("Hello")`
# TRIGGER: inspect visible call-argument-name inlay hints
# EXPECT: no `value=` inlay hint appears before the argument because `value` is positional-only
# VERIFY: the call site does not display a misleading parameter-name inlay hint for the positional-only argument
# RECOVER: no recovery needed

def do_something(value: str | None = None, /) -> None:
    ...


do_something('Hello')