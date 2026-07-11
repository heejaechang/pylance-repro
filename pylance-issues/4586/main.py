 # SCENARIO: extract method availability should not disappear when the selection starts with a comment
 # TARGET: select from the start of the comment through the assignment line
 # TRIGGER: open the refactor menu for the selection
 # EXPECT: Extract Method is available
 # VERIFY: if the menu reports no refactorings available, the bug still reproduces
 # RECOVER: clear the selection

def main():
    # here is a comment
    foo = 'bar'