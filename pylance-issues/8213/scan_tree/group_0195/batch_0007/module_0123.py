"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0195.module_0123'
OFFSET = 195123

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
