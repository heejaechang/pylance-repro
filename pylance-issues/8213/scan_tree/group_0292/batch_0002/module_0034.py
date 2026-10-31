"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0292.module_0034'
OFFSET = 292034

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
