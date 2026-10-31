"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0075.module_0009'
OFFSET = 75009

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
