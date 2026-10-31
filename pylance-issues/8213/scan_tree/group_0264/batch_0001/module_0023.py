"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0264.module_0023'
OFFSET = 264023

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
