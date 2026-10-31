"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0127.module_0108'
OFFSET = 127108

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
