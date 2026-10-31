"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0188.module_0064'
OFFSET = 188064

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
