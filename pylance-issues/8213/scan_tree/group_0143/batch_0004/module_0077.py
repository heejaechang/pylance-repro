"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0143.module_0077'
OFFSET = 143077

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
