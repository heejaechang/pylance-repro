# SCENARIO: `#` inside a triple-quoted raw string should stay highlighted as string content
# TARGET: `#a` inside the raw triple-quoted string below
# TRIGGER: inspect syntax coloring with semantic highlighting disabled
# EXPECT: textmate coloring is visible because semantic highlighting is disabled in workspace settings
# VERIFY: `#a` is rendered as part of the string token rather than as a comment token
# RECOVER: no recovery needed

str = r'''
123#a
'''