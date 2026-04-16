# SCENARIO: negative numeric literals should tokenize as literals rather than splitting the minus into a separate operator color
# TARGET: the leading `-` in `-1.0` and `-1e-4`
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: the minus sign on negative literals is colored with the numeric literal rather than as a standalone arithmetic operator
# VERIFY: `-1.0` and `-1e-4` keep a unified numeric token style, while `-x` style operator behavior is not the target here
# RECOVER: no recovery needed

a = 1.0
b = -1.0
c = 1e4
d = 1e-4
e = -1e-4
f = -(3**2)
g = -a