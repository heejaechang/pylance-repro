"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0212.module_0054'
OFFSET = 212054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
