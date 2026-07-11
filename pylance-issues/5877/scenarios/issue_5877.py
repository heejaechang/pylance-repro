# SCENARIO: repeated f-string format specifiers should all tokenize consistently, including the last one
# TARGET: the final `{d:%d}` segment in the f-string below
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: all three `{d:%d}` segments have matching tokenization for the braces and format specifier text
# VERIFY: the final format-specifier segment does not use different token classes/colors from the first two segments
# RECOVER: no recovery needed

import datetime

d = datetime.date.today()
f'{d:%d} {d:%d} {d:%d}'