"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0107.module_0022'
OFFSET = 107022

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
