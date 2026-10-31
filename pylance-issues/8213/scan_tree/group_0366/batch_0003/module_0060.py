"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0366.module_0060'
OFFSET = 366060

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
