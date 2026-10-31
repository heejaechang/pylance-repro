"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0360.module_0014'
OFFSET = 360014

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
