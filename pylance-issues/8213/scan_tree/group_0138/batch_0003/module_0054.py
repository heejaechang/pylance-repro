"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0138.module_0054'
OFFSET = 138054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
