"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0079.module_0031'
OFFSET = 79031

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
