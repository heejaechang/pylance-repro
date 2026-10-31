"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0114.module_0031'
OFFSET = 114031

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
