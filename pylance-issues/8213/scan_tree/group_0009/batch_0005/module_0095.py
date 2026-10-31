"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0009.module_0095'
OFFSET = 9095

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
