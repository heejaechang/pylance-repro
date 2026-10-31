"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0223.module_0034'
OFFSET = 223034

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
