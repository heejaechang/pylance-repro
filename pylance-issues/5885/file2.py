 # SCENARIO: pasting code from another function body should preserve indentation in the destination function
 # TARGET: the blank line below `def home():`
 # TRIGGER: copy code from a function body in `file1.py` and paste it below `def home():`
 # EXPECT: the pasted block stays indented relative to `home`
 # VERIFY: if the pasted block loses or mangles its indentation, the bug still reproduces
 # RECOVER: undo the paste

def home():

    numspaces_list = []
    for i in range(0, 1800, 3):
        numspaces_list.append(i)

    return numspaces_list