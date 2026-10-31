"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0280.module_0104'
OFFSET = 280104

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
