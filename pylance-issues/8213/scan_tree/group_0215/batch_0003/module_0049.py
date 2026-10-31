"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0215.module_0049'
OFFSET = 215049

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
