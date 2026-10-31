"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0329.module_0123'
OFFSET = 329123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
