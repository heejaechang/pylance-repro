"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0378.module_0032'
OFFSET = 378032

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
