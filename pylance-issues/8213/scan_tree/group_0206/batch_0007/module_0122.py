"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0206.module_0122'
OFFSET = 206122

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
