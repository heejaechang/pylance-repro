"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0144.module_0121'
OFFSET = 144121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
