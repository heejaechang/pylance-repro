"""mylib — library that should be importable via sitecustomize.py adding ./lib to sys.path."""

MY_CONSTANT: str = "hello"


def greet(name: str) -> str:
    return f"Hello, {name}!"
