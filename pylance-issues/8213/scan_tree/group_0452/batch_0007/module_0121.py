"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0452.module_0121'
OFFSET = 452121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
