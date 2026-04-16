 # SCENARIO: Add Import quick fix should still work when the current file sits in an ignored directory
 # TARGET: `os` in `os.path`
 # TRIGGER: with `excluded/` listed in `pyrightconfig.json`, open quick fix on `os`
 # EXPECT: `Add 'import os'` is still offered
 # VERIFY: if no Add Import quick fix appears until the folder is removed from ignore, the bug still reproduces
 # RECOVER: restore `pyrightconfig.json` or reload analysis

os.path