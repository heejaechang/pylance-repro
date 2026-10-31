"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0061.module_0116'
OFFSET = 61116

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
