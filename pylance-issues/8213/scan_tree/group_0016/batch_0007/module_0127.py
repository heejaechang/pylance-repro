"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0016.module_0127'
OFFSET = 16127

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
