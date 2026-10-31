"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0370.module_0007'
OFFSET = 370007

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
