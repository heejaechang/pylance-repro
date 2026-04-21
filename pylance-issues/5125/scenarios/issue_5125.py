# SCENARIO: Extract Method refactoring disappears when the selected block starts or ends with a comment line
# TARGET: the marked line pairs inside `leading_comment_case` and `trailing_comment_case`; use `control_case` as the no-comment control
# TRIGGER: Select the indicated lines, then invoke Refactor... / Extract Method
# EXPECT: current bug: Extract Method is missing when the first or last selected line is a comment; the control selection without a comment still offers Extract Method
# VERIFY: `leading_comment_case` and `trailing_comment_case` omit the Extract Method action, while `control_case` still offers it
# RECOVER: no file edits need to be applied; clear the selection or undo any accidental refactor preview


def leading_comment_case():
    a = 5
    b = 6
    # Select this line and the next line, then invoke Refactor...
    c = a * b
    return a + b, c


def trailing_comment_case():
    a = 5
    b = 6
    c = a * b
    # Select the previous line and this line, then invoke Refactor...
    return a + b, c


def control_case():
    a = 5
    b = 6
    c = a * b
    d = a + b
    return c, d