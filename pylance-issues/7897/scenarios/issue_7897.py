# SCENARIO: f-string triple quotes should auto-close the same way normal triple quotes do
# TARGET: the trailing `f` on the final line below
# TRIGGER: type `"""` after the `f`
# EXPECT: the editor auto-inserts the closing triple quotes
# VERIFY: if the line remains `value = f"""` without a closing pair, the bug still reproduces

value = f