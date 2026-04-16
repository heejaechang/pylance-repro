# SCENARIO: matching variable names should optionally suppress redundant call-argument-name inlay hints
# TARGET: the call `datetime(year, october, 27)`
# TRIGGER: inspect visible call-argument-name inlay hints
# EXPECT: a matching variable like `year` would be omitted while `month=` and `day=` remain visible
# VERIFY: if `year=` still renders before the `year` variable, the enhancement is still absent
# RECOVER: no recovery needed

from datetime import datetime


year = 2019
october = 10

moment = datetime(year, october, 27)