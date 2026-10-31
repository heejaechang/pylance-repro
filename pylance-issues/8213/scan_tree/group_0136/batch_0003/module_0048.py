"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0136.module_0048'
OFFSET = 136048

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
