"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0330.module_0117'
OFFSET = 330117

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
