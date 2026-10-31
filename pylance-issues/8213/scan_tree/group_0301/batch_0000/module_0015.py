"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0301.module_0015'
OFFSET = 301015

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
