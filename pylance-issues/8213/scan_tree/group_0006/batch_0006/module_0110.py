"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0006.module_0110'
OFFSET = 6110

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
