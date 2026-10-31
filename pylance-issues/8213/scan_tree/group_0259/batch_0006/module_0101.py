"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0259.module_0101'
OFFSET = 259101

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
