# SCENARIO: relative auto-imports should group together below existing absolute local imports when importFormat is relative
# TARGET: the two blank assignment values at the bottom of `issue_5550.py`, where `Mapping3` should be completed first and `Mapping1` second
# TRIGGER: Completion on the right-hand side of `mapping3 =` and `mapping1 =`, commit `Mapping3`, then commit `Mapping1`
# EXPECT: committing both completions inserts relative imports for `test3` and `test1`
# VERIFY: the final import block keeps the existing absolute import `from test2 import Mapping2` above both relative imports, with the relative imports grouped together below it
# RECOVER: revert the file to its original text after the check

from test2 import Mapping2

mapping3 = 
mapping1 = 
