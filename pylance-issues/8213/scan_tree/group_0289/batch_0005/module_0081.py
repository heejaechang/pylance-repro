"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0289.module_0081'
OFFSET = 289081

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
