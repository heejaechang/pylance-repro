"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0364.module_0114'
OFFSET = 364114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
