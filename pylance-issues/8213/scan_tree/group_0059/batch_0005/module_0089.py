"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0059.module_0089'
OFFSET = 59089

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
