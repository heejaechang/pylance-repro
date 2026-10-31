"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0247.module_0018'
OFFSET = 247018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
