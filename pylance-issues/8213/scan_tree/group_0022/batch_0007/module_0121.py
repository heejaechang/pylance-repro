"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0022.module_0121'
OFFSET = 22121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
