"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0048.module_0064'
OFFSET = 48064

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
