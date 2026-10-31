"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0213.module_0052'
OFFSET = 213052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
