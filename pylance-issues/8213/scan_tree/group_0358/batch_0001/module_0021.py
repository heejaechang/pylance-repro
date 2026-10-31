"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0358.module_0021'
OFFSET = 358021

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
