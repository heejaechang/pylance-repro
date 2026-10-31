"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0122.module_0117'
OFFSET = 122117

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
