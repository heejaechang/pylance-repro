"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0339.module_0023'
OFFSET = 339023

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
