"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0270.module_0025'
OFFSET = 270025

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
