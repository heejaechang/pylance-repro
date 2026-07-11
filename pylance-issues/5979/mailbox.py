 # SCENARIO: control case for `reportShadowedImports` stdlib shadowing diagnostics
 # TARGET: this file name with `reportShadowedImports = "error"`
 # TRIGGER: open the workspace with the setting enabled
 # EXPECT: this file is flagged for shadowing stdlib `mailbox`
 # VERIFY: this control case helps compare against the missing `sys.py` diagnostic
 # RECOVER: no recovery needed

value = 'mailbox-shadow'