# SCENARIO: imports guarded by `try`/`except ImportError` still report missing-import diagnostics
# TARGET: the guarded imports inside the `try` block
# TRIGGER: open the file and let diagnostics settle
# EXPECT: if the requested ignore behavior is not available, the guarded imports still show `reportMissingImports`
# VERIFY: if the missing-import diagnostics still appear on the guarded imports, the enhancement request remains valid
# RECOVER: no recovery needed

try:
    from definitely_missing_qt6 import QEvent
except ImportError:
    from definitely_missing_qt2 import QEvent


print(QEvent)