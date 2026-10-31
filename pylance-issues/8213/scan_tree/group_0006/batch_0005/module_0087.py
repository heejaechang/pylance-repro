"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0006.module_0087'
OFFSET = 6087

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
