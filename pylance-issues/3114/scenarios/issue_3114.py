 # SCENARIO: assignment from an IPython shell command should work without a parse error
 # TARGET: `stdout = !echo {num}`
 # TRIGGER: open the cell or script with IPython magic support enabled
 # EXPECT: the command output can be assigned to `stdout` without `Expected expression`
 # VERIFY: if the assignment line is flagged as a syntax error, the bug still reproduces
 # RECOVER: no recovery needed

# %%
num = 42
stdout = !echo {num}
print(stdout)