"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0084.module_0093'
OFFSET = 84093

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
