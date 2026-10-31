"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0417.module_0081'
OFFSET = 417081

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
