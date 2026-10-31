"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0364.module_0018'
OFFSET = 364018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
