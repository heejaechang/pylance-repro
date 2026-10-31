"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0321.module_0032'
OFFSET = 321032

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
