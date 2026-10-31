"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0049.module_0102'
OFFSET = 49102

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
