# SCENARIO: signature help should not pop while wrapping an existing triple-quoted string in a function call
# TARGET: the opening triple quotes in `"""payload"""` below
# TRIGGER: type `demo(` immediately before the opening triple quotes so the existing string becomes the first argument of the call
# EXPECT: after inserting `demo(`, the cursor remains inside the existing string literal instead of a call-site position that needs signature help
# VERIFY: no signature-help popup for `demo(first, second)` appears while the cursor is still editing inside the triple-quoted string literal
# RECOVER: revert the file to its original text after the check

def demo(first, second):
    return first, second


"""payload"""