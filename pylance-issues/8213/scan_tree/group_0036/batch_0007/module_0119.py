"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0036.module_0119'
OFFSET = 36119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
