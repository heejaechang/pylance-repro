"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0009.module_0077'
OFFSET = 9077

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
