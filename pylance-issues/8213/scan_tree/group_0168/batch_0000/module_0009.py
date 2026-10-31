"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0168.module_0009'
OFFSET = 168009

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
