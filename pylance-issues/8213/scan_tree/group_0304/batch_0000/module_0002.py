"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0304.module_0002'
OFFSET = 304002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
