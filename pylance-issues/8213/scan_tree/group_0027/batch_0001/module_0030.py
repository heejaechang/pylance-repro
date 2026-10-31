"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0027.module_0030'
OFFSET = 27030

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
