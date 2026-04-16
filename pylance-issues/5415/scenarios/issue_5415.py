# SCENARIO: after manually unindenting inside a triple-quoted argument, pressing Enter should preserve the previous line's indentation rather than re-aligning to the open parenthesis
# TARGET: the end of the `select * from mytable` line below
# TRIGGER: Press Enter on that line while still inside the triple-quoted argument
# EXPECT: a new line is inserted inside the triple-quoted string
# VERIFY: the new line starts with four spaces, matching the previous SQL line's indentation, rather than a deep open-paren alignment
# RECOVER: revert the file to its original contents after the check

def foo(cursor):
    cursor.execute("""
    select * from mytable