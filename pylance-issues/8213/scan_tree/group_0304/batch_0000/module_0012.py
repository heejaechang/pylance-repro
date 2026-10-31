"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0304.module_0012'
OFFSET = 304012

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
