"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0468.module_0025'
OFFSET = 468025

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
