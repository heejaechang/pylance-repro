"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0196.module_0005'
OFFSET = 196005

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
