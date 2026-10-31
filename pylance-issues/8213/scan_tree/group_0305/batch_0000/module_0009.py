"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0305.module_0009'
OFFSET = 305009

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
