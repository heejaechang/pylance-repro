"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0157.module_0034'
OFFSET = 157034

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
