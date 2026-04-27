# SCENARIO: autoFormatStrings should not add an f-prefix for unicode-name escapes
# TARGET: the string literal below, with the cursor immediately after `\N`
# TRIGGER: type `{` so the escape becomes `\N{BLACK CAT}`
# EXPECT: the string should remain a normal string literal, not an f-string
# VERIFY: if Pylance rewrites the literal to start with `f"`, issue #5185 still reproduces
# RECOVER: remove the inserted `f` prefix and `{` character, or reset the file

emoji = "\NBLACK CAT}"