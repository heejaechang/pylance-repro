 # SCENARIO: incomplete code should degrade to diagnostics instead of crashing analysis
 # TARGET: the incomplete `for item in ra` statement
 # TRIGGER: open the file and let Pylance analyze it
 # EXPECT: Pylance reports normal syntax or name diagnostics without crashing
 # VERIFY: if analysis fails with an internal error or stops responding, the bug still reproduces
 # RECOVER: no recovery needed

for item in ra