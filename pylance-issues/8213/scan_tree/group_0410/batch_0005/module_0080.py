"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0410.module_0080'
OFFSET = 410080

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
