# SCENARIO: parameter hover should not concatenate doc blocks with raw `---`
# TARGET: the parameter `item` in `def foo(item: type[Post]) -> None:`
# TRIGGER: hover the parameter name in the function signature
# EXPECT: the parameter doc and the referenced type doc should not collapse into one line containing `---`
# VERIFY: if the hover still contains the raw concatenated text `item: Docstring-for-item--- Docstring-for-Post`, the issue remains valid
# RECOVER: no recovery needed


class Post:
    """Docstring-for-Post"""


def foo(item: type[Post]) -> None:
    """Args:
        item: Docstring-for-item"""
    ...