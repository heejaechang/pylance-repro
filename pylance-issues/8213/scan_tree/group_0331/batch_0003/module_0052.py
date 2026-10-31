"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0331.module_0052'
OFFSET = 331052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
