"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0124.module_0009'
OFFSET = 124009

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
