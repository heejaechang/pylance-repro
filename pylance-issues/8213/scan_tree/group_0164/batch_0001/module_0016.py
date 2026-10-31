"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0164.module_0016'
OFFSET = 164016

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
