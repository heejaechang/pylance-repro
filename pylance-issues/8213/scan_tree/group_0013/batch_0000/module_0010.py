"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0013.module_0010'
OFFSET = 13010

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
