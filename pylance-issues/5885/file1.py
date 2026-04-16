from math import cos, radians


def make_dot_string(x):
    """
    creates a string of spaces followed by a dot.
    @param x: the number of spaces before the dot.
    @return: a string with x spaces, then a dot.
    """
    rad = radians(x)
    c = abs(round(cos(rad), 2))
    if c == 0:
        return 0

    numspaces = int((9 * 1 / c - 9))
    return numspaces