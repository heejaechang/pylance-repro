"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0261.module_0048'
OFFSET = 261048

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
