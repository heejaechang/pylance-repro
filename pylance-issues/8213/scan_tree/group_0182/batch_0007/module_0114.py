"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0182.module_0114'
OFFSET = 182114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
