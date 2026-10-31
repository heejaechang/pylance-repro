"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0487.module_0114'
OFFSET = 487114

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
