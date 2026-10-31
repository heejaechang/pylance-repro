"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0452.module_0001'
OFFSET = 452001

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
