# SCENARIO: the extract refactor title outside a class should be named `Extract function` rather than `Extract method`
# TARGET: select the entire `x = 1` statement below
# TRIGGER: Quick Fix
# EXPECT: the quick-fix / refactor menu opens for the selected statement
# VERIFY: the available extract refactor title is `Extract function` and not `Extract method`
# RECOVER: cancel the refactor UI without applying any edit

x = 1