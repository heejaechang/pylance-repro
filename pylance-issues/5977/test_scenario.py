def foo(key1: str = 'r', key2: str = 'z') -> None:
    pass

foo(key1='hello')
foo(key1=f"hello {key2} world")
