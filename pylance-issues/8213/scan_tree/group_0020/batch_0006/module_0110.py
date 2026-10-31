"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0020.module_0110'
OFFSET = 20110

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
