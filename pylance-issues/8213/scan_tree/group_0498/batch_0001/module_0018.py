"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0498.module_0018'
OFFSET = 498018

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
