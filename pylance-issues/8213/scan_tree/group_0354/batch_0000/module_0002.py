"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0354.module_0002'
OFFSET = 354002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
