# SCENARIO: a loose long string split with a trailing backslash should keep the same string coloring after the line break
# TARGET: the continuation line of the loose split string literal
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: the continuation text in the loose split literal is tokenized like the assigned and call-argument control strings below
# VERIFY: the continuation text in the loose split literal does not lose string token styling compared with the assigned and call-argument controls
# RECOVER: no recovery needed

'sdfsdfsddsssdadsadsadsadasdasdsadsadasdasdasdasdasdasdasdasdadasdasdasdasadasdasdasdasdasdasdasdsadasdas\
     dasdsdsaadsad'

foo = 'sdfsdfsddsssdadsadsadsadasdasdsadsadasdasdasdasdasdasdasdasdadasdasdasdasadasdasdasdasdasdasdasdsadasdas\
     dasdsdsaadsad'

print('sdfsdfsddsssdadsadsadsadasdasdsadsadasdasdasdasdasdasdasdasdadasdasdasdasadasdasdasdasdasdasdasdsadasdas\
     dasdsdsaadsad')