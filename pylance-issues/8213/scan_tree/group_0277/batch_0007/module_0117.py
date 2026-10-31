"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0277.module_0117'
OFFSET = 277117

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
