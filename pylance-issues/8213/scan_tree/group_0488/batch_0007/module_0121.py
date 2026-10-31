"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0488.module_0121'
OFFSET = 488121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
