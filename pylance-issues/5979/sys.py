 # SCENARIO: `reportShadowedImports` should also report stdlib shadowing for `sys.py`
 # TARGET: this file name with `reportShadowedImports = "error"`
 # TRIGGER: open the workspace with the setting enabled
 # EXPECT: this file is flagged just like `mailbox.py`
 # VERIFY: if only `mailbox.py` gets a diagnostic, the bug still reproduces
 # RECOVER: no recovery needed

value = 'sys-shadow'