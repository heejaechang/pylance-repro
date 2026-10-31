"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0121.module_0114'
OFFSET = 121114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
