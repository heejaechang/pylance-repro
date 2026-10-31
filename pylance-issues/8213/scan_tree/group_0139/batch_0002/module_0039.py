"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0139.module_0039'
OFFSET = 139039

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
