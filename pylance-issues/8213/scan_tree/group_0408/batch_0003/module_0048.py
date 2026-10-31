"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0408.module_0048'
OFFSET = 408048

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
