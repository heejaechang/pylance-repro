"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0415.module_0007'
OFFSET = 415007

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
