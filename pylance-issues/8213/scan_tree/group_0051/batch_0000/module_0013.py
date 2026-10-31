"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0051.module_0013'
OFFSET = 51013

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
