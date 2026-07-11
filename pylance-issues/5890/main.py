 # SCENARIO: superclass and subclass assignments to the same member should stay linked for navigation and rename
 # TARGET: `self.a` in both `A.__init__` and `B.__init__`
 # TRIGGER: run find references or rename on `self.a`
 # EXPECT: both assignments are treated as the same member variable
 # VERIFY: if navigation or rename treats them as separate variables, the bug still reproduces
 # RECOVER: undo the rename or reload the file

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