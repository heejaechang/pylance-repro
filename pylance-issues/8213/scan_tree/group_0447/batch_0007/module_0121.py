"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0447.module_0121'
OFFSET = 447121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
