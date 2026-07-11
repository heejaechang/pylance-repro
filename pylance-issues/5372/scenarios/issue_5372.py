# SCENARIO: renaming a variable inside parentheses should prefill the rename prompt with the bare symbol name
# TARGET: `A` inside `if (A):` below
# TRIGGER: Rename Symbol
# EXPECT: the rename UI opens for the selected symbol
# VERIFY: the rename input is prefilled with `A` rather than `(A)`
# RECOVER: cancel the rename UI without applying any edit

A = True
if (A):
    pass