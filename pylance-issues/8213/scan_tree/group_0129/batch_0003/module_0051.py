"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0129.module_0051'
OFFSET = 129051

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
