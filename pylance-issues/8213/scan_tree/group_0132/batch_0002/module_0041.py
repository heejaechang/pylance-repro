"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0132.module_0041'
OFFSET = 132041

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
