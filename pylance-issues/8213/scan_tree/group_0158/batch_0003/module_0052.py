"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0158.module_0052'
OFFSET = 158052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
