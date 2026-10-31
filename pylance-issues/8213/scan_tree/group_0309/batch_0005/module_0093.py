"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0309.module_0093'
OFFSET = 309093

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
