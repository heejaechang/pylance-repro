# SCENARIO: replacing an existing named argument with a completed named-argument suggestion should not leave a double equals token
# TARGET: the existing `bar` token inside `foo(bar="")` below; select only `bar`, type `cool` to start the replacement, then complete `cool_param=`
# TRIGGER: Completion commit with Tab
# EXPECT: after typing `cool` over the selected token, the suggestion list contains `cool_param=`
# VERIFY: after committing the completion, the line becomes `foo(cool_param="")` with a single `=` and not `foo(cool_param=="")`
# RECOVER: revert the file to its original contents after the check

def foo(bar: str | None = None, cool_param: str | None = None) -> None:
    ...


foo(bar="")