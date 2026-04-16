# SCENARIO: the add-import quick fix for an unresolved symbol should insert the import above the first usage rather than after it
# TARGET: `environ` on the first line below
# TRIGGER: Quick Fix
# EXPECT: the quick-fix menu contains `Add "from os import environ"`
# VERIFY: after executing the fix, the file begins with `from os import environ` and the unresolved usage is no longer left above the inserted import
# RECOVER: revert the file to its original contents after the check

environ

from os import path

path