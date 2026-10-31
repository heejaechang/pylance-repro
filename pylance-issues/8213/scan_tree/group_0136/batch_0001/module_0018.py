"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0136.module_0018'
OFFSET = 136018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
