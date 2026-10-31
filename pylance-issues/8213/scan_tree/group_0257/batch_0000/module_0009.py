"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0257.module_0009'
OFFSET = 257009

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
