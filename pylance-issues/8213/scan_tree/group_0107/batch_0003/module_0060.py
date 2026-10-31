"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0107.module_0060'
OFFSET = 107060

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
