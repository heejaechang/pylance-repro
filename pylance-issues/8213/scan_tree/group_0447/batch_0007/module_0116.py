"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0447.module_0116'
OFFSET = 447116

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
