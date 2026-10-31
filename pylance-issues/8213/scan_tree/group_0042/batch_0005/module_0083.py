"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0042.module_0083'
OFFSET = 42083

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
