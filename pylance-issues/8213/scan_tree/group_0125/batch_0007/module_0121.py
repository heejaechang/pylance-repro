"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0125.module_0121'
OFFSET = 125121

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
