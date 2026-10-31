"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0302.module_0101'
OFFSET = 302101

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
