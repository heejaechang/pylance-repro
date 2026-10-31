"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0110.module_0002'
OFFSET = 110002

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
