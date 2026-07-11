# SCENARIO: syntax highlighting should stay consistent when an f-string is line-broken at the opening `{`
# TARGET: the second line of the broken f-string, especially `name}, nice to meet you!`
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: the line-broken f-string tokenizes like the single-line control f-string above
# VERIFY: the text after the line break inside the f-string does not lose its normal f-string token styling
# RECOVER: no recovery needed

name = 'John'
print(f'My name is {name}, nice to meet you!')

print(f'My name is {
    name}, nice to meet you!')