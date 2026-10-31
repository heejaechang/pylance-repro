"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0467.module_0079'
OFFSET = 467079

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
