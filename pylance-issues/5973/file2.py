 # SCENARIO: moving a symbol into a file that already has `from ... import ...` should carry over needed imports
 # TARGET: move `myfunc` into `file2.py`
 # TRIGGER: run "Move symbol to..." on `myfunc` and pick `file2.py`
 # EXPECT: `import os` is added to the destination file
 # VERIFY: if `myfunc` lands here without adding `import os`, the bug still reproduces
 # RECOVER: undo the move or restore both files

from sys import version


print(version)


def myfunc():
    return os.path.abspath(__file__)