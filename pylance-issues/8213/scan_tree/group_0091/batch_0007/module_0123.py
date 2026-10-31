"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0091.module_0123'
OFFSET = 91123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
