"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0040.module_0012'
OFFSET = 40012

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
