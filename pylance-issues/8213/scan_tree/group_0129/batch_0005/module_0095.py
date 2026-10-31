"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0129.module_0095'
OFFSET = 129095

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
