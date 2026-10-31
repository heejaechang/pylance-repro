"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0297.module_0114'
OFFSET = 297114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
