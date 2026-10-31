"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0137.module_0054'
OFFSET = 137054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
