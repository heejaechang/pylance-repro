"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0210.module_0012'
OFFSET = 210012

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
