"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0286.module_0007'
OFFSET = 286007

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
