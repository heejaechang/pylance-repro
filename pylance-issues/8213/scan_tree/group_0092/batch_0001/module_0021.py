"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0092.module_0021'
OFFSET = 92021

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
