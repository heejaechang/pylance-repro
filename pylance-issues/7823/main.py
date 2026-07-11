 # SCENARIO: assigning a function object should preserve its callable type information
 # TARGET: `value = foo`
 # TRIGGER: hover over `value`
 # EXPECT: hover shows the same callable signature as `foo`
 # VERIFY: if the signature is lost or widened incorrectly, the bug still reproduces
 # RECOVER: no recovery needed

def foo() -> None:
    pass


foo()
foo()
value = foo