"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0061.module_0126'
OFFSET = 61126

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
