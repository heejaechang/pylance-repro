"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0156.module_0010'
OFFSET = 156010

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
