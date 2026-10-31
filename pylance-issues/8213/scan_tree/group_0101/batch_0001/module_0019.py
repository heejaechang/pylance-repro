"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0101.module_0019'
OFFSET = 101019

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
