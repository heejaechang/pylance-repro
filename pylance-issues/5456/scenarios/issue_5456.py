# SCENARIO: continuing a function call on a new line with tab indentation should use one nesting tab plus spaces for alignment, not extra tabs
# TARGET: the end of the `incorrect_indentation(a, b, c,` line below
# TRIGGER: Press Enter, then type `d, e, f)` on the new line
# EXPECT: the new line is inserted as a continuation line under the existing call
# VERIFY: the resulting continuation line text is `\t                      d, e, f)` with one leading tab for nesting and only spaces for the alignment before `d`
# RECOVER: revert the file to its original contents after the check

def foo():
	incorrect_indentation(a, b, c,