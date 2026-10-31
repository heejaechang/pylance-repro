"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0210.module_0005'
OFFSET = 210005

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
