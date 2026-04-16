class Foo:
    def __init__(self, x: int) -> None:
        self.x = x


class Bar:
    def __init__(self, foo_a: Foo, x) -> None:
        self.foo_a = foo_a
        self.x = x


foo_a = Foo(1)
