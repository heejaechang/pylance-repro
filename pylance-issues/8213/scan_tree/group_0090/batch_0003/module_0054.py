"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0090.module_0054'
OFFSET = 90054

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
