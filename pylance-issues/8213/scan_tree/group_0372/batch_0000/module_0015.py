"""Original synthetic input for a workspace traversal/shutdown check."""

MODULE_NAME = 'group_0372.module_0015'
OFFSET = 372015

def make_record(value: int) -> dict[str, int | str]:
    return {'name': MODULE_NAME, 'value': value + OFFSET}
