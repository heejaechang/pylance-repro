"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0303.module_0016'
OFFSET = 303016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
