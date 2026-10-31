"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0385.module_0080'
OFFSET = 385080

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
