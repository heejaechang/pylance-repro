"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0036.module_0002'
OFFSET = 36002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
