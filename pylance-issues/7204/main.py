import functools


def my_func():
    """Simple function that uses functools."""
    return functools.lru_cache(maxsize=128)
