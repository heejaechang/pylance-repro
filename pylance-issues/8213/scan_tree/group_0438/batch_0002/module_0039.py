"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0438.module_0039'
OFFSET = 438039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
