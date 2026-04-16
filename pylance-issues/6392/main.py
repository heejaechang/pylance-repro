class Foo:
    class Descriptor:
        def __get__(self, obj, objtype=None):
            return self

    a = b = c = Descriptor()
    'this docstring is only visible for Foo.c'


Foo.a
Foo.b
Foo.c