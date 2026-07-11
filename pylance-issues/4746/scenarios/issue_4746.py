# SCENARIO: raw f-strings should keep raw-string coloring for escape text like `\\n`
# TARGET: the `\\n` segment in `raw_f_string` and `raw_f_string2`
# TRIGGER: inspect tokenization with semantic highlighting disabled
# EXPECT: the raw-f-string escape text tokenizes like the raw string `r"raw_string\\n"`
# VERIFY: the `\\n` text in the `rf` and `fr` strings uses the same string-token styling as the raw string case rather than plain regular-string styling
# RECOVER: no recovery needed

string = 'string'
raw_string = r'raw_string\n'
f_string = f'f-{string}'
raw_f_string = rf'f-{raw_string}\n'
raw_f_string2 = fr'f-{raw_string}\n'