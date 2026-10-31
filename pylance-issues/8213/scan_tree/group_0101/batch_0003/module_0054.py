"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0101.module_0054'
OFFSET = 101054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
