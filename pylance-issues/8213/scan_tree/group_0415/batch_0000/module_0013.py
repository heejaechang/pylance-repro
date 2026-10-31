"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0415.module_0013'
OFFSET = 415013

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
