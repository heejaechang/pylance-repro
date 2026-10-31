"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0074.module_0076'
OFFSET = 74076

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
