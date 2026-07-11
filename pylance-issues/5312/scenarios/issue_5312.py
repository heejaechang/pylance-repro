# SCENARIO: hover over the return annotation should surface return documentation
# TARGET: the `->` token in `def add(a: int, b: int) -> int:` below
# TRIGGER: Hover
# EXPECT: hover opens on the return annotation target
# VERIFY: hover content includes `The sum of the numbers.` from the Returns section of the docstring
# RECOVER: no recovery needed


def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the numbers.
    """
    return a + b