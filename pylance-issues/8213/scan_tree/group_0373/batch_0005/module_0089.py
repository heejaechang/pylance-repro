"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0373.module_0089'
OFFSET = 373089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
