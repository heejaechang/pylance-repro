from dataclasses import dataclass

class RegularClass:
    def __init__(self, foo: str, bar: str = None):
        self.foo = foo
        self.bar = bar

@dataclass
class Dataclass:
    foo: str
    bar: str = None
          
def my_function(foo_arg: str, bar_kwarg: str = None):
    rc = RegularClass(
        foo_arg,
        bar=bar_kwarg,
    )

    dc = Dataclass(
        foo_arg,
        bar=bar_kwarg,
    )
