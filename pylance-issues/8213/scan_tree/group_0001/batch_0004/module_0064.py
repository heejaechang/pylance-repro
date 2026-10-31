"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0001.module_0064'
OFFSET = 1064

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
