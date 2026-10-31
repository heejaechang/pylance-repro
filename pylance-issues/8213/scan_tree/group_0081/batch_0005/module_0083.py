"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0081.module_0083'
OFFSET = 81083

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
