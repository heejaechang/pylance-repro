"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0054.module_0108'
OFFSET = 54108

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
