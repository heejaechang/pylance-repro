"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0238.module_0039'
OFFSET = 238039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
