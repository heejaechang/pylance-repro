"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0038.module_0018'
OFFSET = 38018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
