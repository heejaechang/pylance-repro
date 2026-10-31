"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0014.module_0038'
OFFSET = 14038

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
