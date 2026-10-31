"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0317.module_0023'
OFFSET = 317023

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
