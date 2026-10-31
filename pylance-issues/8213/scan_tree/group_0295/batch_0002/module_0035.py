"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0295.module_0035'
OFFSET = 295035

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
