"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0236.module_0116'
OFFSET = 236116

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
