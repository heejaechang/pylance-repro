"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0454.module_0101'
OFFSET = 454101

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
