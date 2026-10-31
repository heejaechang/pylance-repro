"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0238.module_0107'
OFFSET = 238107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
