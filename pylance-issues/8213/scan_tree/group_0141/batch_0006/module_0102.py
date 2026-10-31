"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0141.module_0102'
OFFSET = 141102

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
