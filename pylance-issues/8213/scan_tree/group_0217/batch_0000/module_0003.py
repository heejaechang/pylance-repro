"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0217.module_0003'
OFFSET = 217003

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
