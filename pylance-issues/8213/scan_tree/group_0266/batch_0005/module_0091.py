"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0266.module_0091'
OFFSET = 266091

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
