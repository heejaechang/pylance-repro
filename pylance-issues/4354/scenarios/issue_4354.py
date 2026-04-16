 # SCENARIO: pressing Enter at the end of a return line should not leave trailing whitespace
 # TARGET: the end of `return 'bar'`
 # TRIGGER: put the cursor at the end of the return line and press Enter a couple of times
 # EXPECT: each inserted line is blank without trailing spaces
 # VERIFY: if the first new line contains trailing whitespace, the bug still reproduces
 # RECOVER: no recovery needed

class Foo:
    def bar(self):
        return 'bar'