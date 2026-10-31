"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0104.module_0020'
OFFSET = 104020

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
