"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0339.module_0121'
OFFSET = 339121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
