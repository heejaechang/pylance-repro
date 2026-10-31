"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0033.module_0121'
OFFSET = 33121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
