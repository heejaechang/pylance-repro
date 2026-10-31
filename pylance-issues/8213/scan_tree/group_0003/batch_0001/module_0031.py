"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0003.module_0031'
OFFSET = 3031

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
