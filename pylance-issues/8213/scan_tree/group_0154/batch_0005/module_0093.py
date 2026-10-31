"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0154.module_0093'
OFFSET = 154093

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
