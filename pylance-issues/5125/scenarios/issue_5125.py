def test():
    a = 5
    b = 6
    # mark this and the next line, choose refactor -> nothing
    c = a * b
    return a + b, c


def leading_comment_case():
    a = 5
    b = 6
    # mark this comment line and the next line, choose refactor -> nothing
    c = a * b
    return a + b, c


def control_case():
    a = 5
    b = 6
    # leave this comment unselected
    c = a * b
    return a + b, c


def trailing_comment_case():
    a = 5
    b = 6
    c = a * b
    # mark the statement above plus this trailing comment line, choose refactor -> nothing
    return a + b, c
