"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0505.module_0070'
OFFSET = 505070

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
