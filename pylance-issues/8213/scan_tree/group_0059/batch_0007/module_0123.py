"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0059.module_0123'
OFFSET = 59123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
