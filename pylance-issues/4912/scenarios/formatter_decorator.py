from typing import Callable


class Formatter:
    def decorator(self, main_function: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print("Inside the decorator")
            return main_function(*args, **kwargs)
        return wrapper


@Formatter().decorator
def second_foo():
    print("Inside the second_foo function")


if __name__ == "__main__":
    second_foo()
