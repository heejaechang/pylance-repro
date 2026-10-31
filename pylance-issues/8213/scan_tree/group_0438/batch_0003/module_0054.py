"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0438.module_0054'
OFFSET = 438054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
