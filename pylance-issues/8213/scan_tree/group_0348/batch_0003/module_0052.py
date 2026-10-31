"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0348.module_0052'
OFFSET = 348052

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
