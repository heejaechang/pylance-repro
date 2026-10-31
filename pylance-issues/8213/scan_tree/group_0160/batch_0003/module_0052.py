"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0160.module_0052'
OFFSET = 160052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
