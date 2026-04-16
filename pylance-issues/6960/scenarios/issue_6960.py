# SCENARIO: Quick Fix should suggest a spelling replacement for a misspelled API name
# TARGET: `findAll`
# TRIGGER: open Quick Fix on `re.findAll`
# EXPECT: the Quick Fix menu includes a spelling fix such as `Change spelling to "findall"`
# VERIFY: if the menu still lacks a direct spelling correction for `findAll`, the enhancement request remains valid
# RECOVER: no recovery needed

import re


result = re.findAll('x', 'xyz')
print(result)