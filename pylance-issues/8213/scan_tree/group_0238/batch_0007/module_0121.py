"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0238.module_0121'
OFFSET = 238121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
