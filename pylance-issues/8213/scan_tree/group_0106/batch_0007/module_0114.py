"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0106.module_0114'
OFFSET = 106114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
