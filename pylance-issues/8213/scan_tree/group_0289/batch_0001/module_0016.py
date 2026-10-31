"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0289.module_0016'
OFFSET = 289016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
