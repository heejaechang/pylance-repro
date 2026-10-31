"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0049.module_0110'
OFFSET = 49110

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
