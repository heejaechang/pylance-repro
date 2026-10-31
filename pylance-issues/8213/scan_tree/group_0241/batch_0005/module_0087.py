"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0241.module_0087'
OFFSET = 241087

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
