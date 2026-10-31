"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0024.module_0079'
OFFSET = 24079

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
