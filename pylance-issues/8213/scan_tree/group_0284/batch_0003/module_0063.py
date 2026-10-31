"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0284.module_0063'
OFFSET = 284063

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
