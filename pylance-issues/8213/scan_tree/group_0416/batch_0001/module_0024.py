"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0416.module_0024'
OFFSET = 416024

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
