"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0263.module_0091'
OFFSET = 263091

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
