"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0426.module_0025'
OFFSET = 426025

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
