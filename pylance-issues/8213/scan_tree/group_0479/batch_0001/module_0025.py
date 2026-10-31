"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0479.module_0025'
OFFSET = 479025

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
