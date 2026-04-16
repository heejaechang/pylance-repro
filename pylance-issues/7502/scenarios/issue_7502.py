# SCENARIO: decorator highlighting should stay consistent when the decorator comes from a parameter attribute
# TARGET: compare `@MethodDecorator(\">>>\")` with `@my_param_decorator.decorate`
# TRIGGER: inspect editor token classes with semantic highlighting enabled
# EXPECT: the decorator expression should not fall back to parameter/member coloring for `my_param_decorator.decorate`
# VERIFY: the parameter part of the decorator should not be semantically colored as a plain parameter while the sibling decorator stays decorator-colored
# RECOVER: no recovery needed

class MethodDecorator:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        return func

    def decorate(self, func):
        return self(func)


def main(my_param_decorator: MethodDecorator):
    @MethodDecorator('>>>')
    def hail(name):
        print(f'Hail, {name}!')

    @my_param_decorator.decorate
    def greet(name):
        print(f'Hello, {name}!')

    greet('Alice')
    hail('Bob')


main(MethodDecorator('>>>'))