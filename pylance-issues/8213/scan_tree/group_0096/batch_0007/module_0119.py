"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0096.module_0119'
OFFSET = 96119

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
