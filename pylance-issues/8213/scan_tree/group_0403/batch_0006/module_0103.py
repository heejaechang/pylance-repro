"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0403.module_0103'
OFFSET = 403103

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
