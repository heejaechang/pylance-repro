 # SCENARIO: descriptor docstrings should stay attached when one descriptor is aliased across attributes
 # TARGET: hover over `Foo.a`, `Foo.b`, and `Foo.c`
 # TRIGGER: inspect the hover text for each alias
 # EXPECT: the descriptor hover stays consistent across all three aliases
 # VERIFY: if the docstring or hover content only appears for one alias, the bug still reproduces
 # RECOVER: no recovery needed

class Foo:
    class Descriptor:
        def __get__(self, obj, objtype=None):
            return self

    a = b = c = Descriptor()
    'this docstring is only visible for Foo.c'


Foo.a
Foo.b
Foo.c