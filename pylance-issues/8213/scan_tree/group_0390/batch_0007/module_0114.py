"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0390.module_0114'
OFFSET = 390114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
