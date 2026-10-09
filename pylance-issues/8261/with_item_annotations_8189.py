# BUG: Fix All on save must not add type annotations to ``with ... as`` targets when variable inlay hints are enabled.
# Issue: https://github.com/microsoft/pylance-release/issues/8189
# SETTINGS: editor.codeActionsOnSave.source.fixAll="explicit"; python.analysis.fixAll=["addTypeAnnotation"].
# SETTINGS: python.analysis.inlayHints.variableTypes=true. These settings must be active before saving.
# CONTEXT: This reproducer first expects a visible variable type inlay hint for source_file.


def get_value() -> int:
    return 42

# CHECK: 8189 with-item inlay-hint precondition
# EXPECTED: visible type hint for "source_file" is TextIOWrapper while the real editor text remains "as source_file,"
with open("input.txt", encoding="utf-8") as source_file, open("output.txt", "w", encoding="utf-8") as destination_file:
    destination_file.write(source_file.read())

# CHECK: 8189 fix-all-on-save skips with-item targets
# EXPECTED: contains "line_count: int = get_value()"
# EXPECTED: not-contains "as source_file: TextIOWrapper"
# EXPECTED: not-contains "as destination_file: TextIOWrapper"
# DIRTY SAVE: append one space to this comment before saving. This edit only makes the file dirty; do not type annotations.
line_count = get_value()

# CHECK: 8189 direct with-item action is unavailable
# EXPECTED: not-contains "Add type annotation"
with open("audit.txt", encoding="utf-8") as audit_file:
    audit_file.read()
