"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0427.module_0051'
OFFSET = 427051

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
