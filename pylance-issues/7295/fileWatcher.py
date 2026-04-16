 # SCENARIO: external file changes should trigger reanalysis for imported symbols
 # TARGET: `TypeChangedExternally()` on the final line
 # TRIGGER: change the imported type in `lib/changeExternally.py` while this file is open
 # EXPECT: diagnostics and type information update after the external change
 # VERIFY: if Pylance keeps stale results after the edit, the bug still reproduces
 # RECOVER: revert the external change or reload the workspace

from lib.changeExternally import TypeChangedExternally

TypeChangedExternally()
