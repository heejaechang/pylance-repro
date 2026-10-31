"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0429.module_0002'
OFFSET = 429002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
