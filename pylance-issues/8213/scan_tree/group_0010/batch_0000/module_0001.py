"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0010.module_0001'
OFFSET = 10001

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
