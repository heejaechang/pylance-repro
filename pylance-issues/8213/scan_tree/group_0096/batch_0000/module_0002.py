"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0096.module_0002'
OFFSET = 96002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
