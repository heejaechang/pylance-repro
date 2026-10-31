"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0097.module_0015'
OFFSET = 97015

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
