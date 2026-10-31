"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0248.module_0052'
OFFSET = 248052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
