 # SCENARIO: extract method should stay available when a selection begins with a comment
 # TARGET: select from the start of the comment through the assignment line
 # TRIGGER: press the refactor shortcut for the selection
 # EXPECT: Extract Method appears in the refactor menu
 # VERIFY: if Extract Method disappears for this selection, the bug still reproduces
 # RECOVER: clear the selection

def main():
    # here is a comment
    foo = 'bar'