class A:
    def __init__(self, a):
        self.a = a

    def get_base(self):
        return self.a


class B(A):
    def __init__(self, a):
        self.a = a

    def get_sub(self):
        return self.a


value = B(1)
print(value.get_base(), value.get_sub())