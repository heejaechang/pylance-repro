"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0475.module_0031'
OFFSET = 475031

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
