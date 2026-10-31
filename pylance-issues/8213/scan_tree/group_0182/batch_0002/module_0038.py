"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0182.module_0038'
OFFSET = 182038

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
