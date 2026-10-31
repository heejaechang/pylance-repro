"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0319.module_0031'
OFFSET = 319031

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
