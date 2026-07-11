# SCENARIO: a file under `src` that shadows a stdlib module should surface the shadowed-import diagnostic in the shadowing file itself
# TARGET: open `codeactions.py` in this folder first, then return to this `mailbox.py` file and inspect diagnostics for this file
# TRIGGER: Problems / diagnostics refresh
# EXPECT: diagnostics are available for this file after the support file has been opened
# VERIFY: this file shows a `reportShadowedImports` warning indicating that local `mailbox.py` shadows the stdlib `mailbox` module
# RECOVER: no recovery needed

LOCAL_MAILBOX = 1