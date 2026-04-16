# SCENARIO: typing `[` where no specific suggestions are available should not automatically open a generic completion popup
# TARGET: the end of `value` in `value` below
# TRIGGER: Type `[`
# EXPECT: there is no specific index-key or literal suggestion context for `value`
# VERIFY: no autocomplete popup appears automatically after typing `[`
# RECOVER: revert the file to its original text

value = object()
value