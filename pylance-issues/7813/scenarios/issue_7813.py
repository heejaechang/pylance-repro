# SCENARIO: hash symbols inside triple-quoted raw strings should not tokenize as comments
# TARGET: `# comment here` inside the first two triple-quoted raw strings
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: the hash fragment remains part of the string token in both triple-quoted raw strings
# VERIFY: the text after `#` inside the multiline raw strings does not share the comment token class/color
# RECOVER: no recovery needed

s = r"""
this should not be presented as comment: # comment here
"""
s2 = r'''
this should not be presented as comment: # comment here
'''
s_nonraw = """
this should not be presented as comment: # comment here
"""
ss_raw = r'this should not be presented as comment: # comment here'