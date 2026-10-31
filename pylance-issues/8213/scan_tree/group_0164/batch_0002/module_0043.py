"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0164.module_0043'
OFFSET = 164043

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
