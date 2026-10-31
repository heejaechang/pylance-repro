"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0316.module_0038'
OFFSET = 316038

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
