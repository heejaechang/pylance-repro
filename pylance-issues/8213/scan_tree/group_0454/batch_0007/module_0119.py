"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0454.module_0119'
OFFSET = 454119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
