"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0133.module_0107'
OFFSET = 133107

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
